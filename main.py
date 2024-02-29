import os
import re
import base64
import gitlab
import requests
from dotenv import load_dotenv
from resources import application_properties_files, application_properties_regex, feign_folder_regex, feign_url_regex, bootstrap_regex

load_dotenv()

def gitlab_api():
  session = requests.Session()
  return gitlab.Gitlab('https://git.original.com.br', private_token=os.getenv('GITLAB_TOKEN_COLLINS'), session=session)

def generate_csv_bootstrap(file_name, csv_matrix):
  rows = ["{},{},{}".format(i, j, k) for i, j, k in csv_matrix]
  text = "\n".join(rows)

  with open(f'files/{file_name}.csv', 'w') as f:
    f.write(text)

def generate_csv_application(file_name, csv_matrix):
  rows = ["{},{},{},{},{}".format(i, j, k, l, m) for i, j, k, l, m in csv_matrix]
  text = "\n".join(rows)

  with open(f'files/{file_name}.csv', 'w') as f:
    f.write(text)

def filter_files_by_regex(repo_files, regex):
  file_filter = []

  for file in repo_files:
    file_name = file.get('name')

    if re.match(regex, file.get('path')):
      file_info = {'name': file_name, 'path': file.get('path')}
      file_filter.append(file_info)

  return file_filter

def filter_files_by_list(repo_files, relevant_files):
  file_filter = []

  for file in repo_files:
    file_name = file.get('name')

    if file_name in relevant_files:
      file_info = {'name': file_name, 'path': file.get('path')}
      file_filter.append(file_info)

  return file_filter

def get_repo_files(project):
  repo_files = None

  try:
    repo_files = project.repository_tree(ref='master', recursive=True, all=True)
  except gitlab.exceptions.GitlabGetError as e:
    if e.error_message == '404 Tree Not Found':
      print(f"Project {project.name} has no folder structure")
      repo_files = None

  return repo_files

def get_file_data(project, path):
  file_content = project.files.get(ref='master', file_path=path)
  return base64.b64decode(file_content.content).decode("utf-8").replace('\\n', '\n')

def feign_data_mapping(project, filtered_list):
  data = []

  for filtered_file in filtered_list:
    file_data = get_file_data(project, filtered_file.get('path'))
    match = re.search(feign_url_regex, file_data)

    if match:
      url_text = match.group("url_text")
      url_text = url_text.replace('"${', '').replace('}"', '')
      data.append({'file': filtered_file.get('name'), 'url': url_text})

  return data

def application_properties_data_mapping(project, filtered_list):
  file_dictionary = {}

  for filtered_file in filtered_list:
    file_name = filtered_file.get('name')
    file_dictionary[file_name] = []
    file_data = get_file_data(project, filtered_file.get('path'))

    for line in file_data.splitlines():
      match = re.search(application_properties_regex, line)

      if match:
        variable_name = match.group("name")
        url_text = match.group("url_text")
        file_dictionary[file_name].append({'variable_name': variable_name, 'url_text': url_text})

  return file_dictionary

def bootstrap_data_mapping(project, filtered_list):
  data = []

  for filtered_file in filtered_list:
    file_data = get_file_data(project, filtered_file.get('path'))
    match = re.search(bootstrap_regex, file_data, flags=re.DOTALL)

    if match:
      integrations = match.group("integrations")
      integrations = integrations.replace(',', ';')
      data.append({'integrations': integrations})

  return data

def build_representation(api, acronym):
  project_list = api.projects.list(search=acronym, all=True)
  acronym_dictionary = {}
  acronym_dictionary[acronym] = {}

  for project in project_list:
    repo_files = get_repo_files(project)

    if repo_files is None:
      continue

    acronym_dictionary[acronym][project.name] = {}

    feign_files = filter_files_by_regex(repo_files, feign_folder_regex)
    acronym_dictionary[acronym][project.name]['feign'] = feign_data_mapping(project, feign_files)

    bootstrap_files = filter_files_by_list(repo_files, ['bootstrap.yml'])
    acronym_dictionary[acronym][project.name]['bootstrap'] = bootstrap_data_mapping(project, bootstrap_files)

    properties_files = filter_files_by_list(repo_files, application_properties_files)
    acronym_dictionary[acronym][project.name]['application'] = application_properties_data_mapping(project, properties_files)

  return acronym_dictionary

def main():
  gl = gitlab_api()
  acronym_dictionary = build_representation(gl, 'conv')

  print(acronym_dictionary)

if __name__ == '__main__':
  main()