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

def feign_mapping_data(acronym, project, filtered_list):
  for filtered_file in filtered_list:
    file_data = get_file_data(project, filtered_file.get('path'))
    match = re.search(feign_url_regex, file_data)

    if match:
      url_text = match.group("url_text")
      url_text = url_text.replace('"${', '').replace('}"', '')
      print(f"Acronym: {acronym} | Project Name: {project.name} | File Name: {filtered_file.get('name')} | URL: {url_text}\n")

def application_properties_data(acronym, project, filtered_list):
  for filtered_file in filtered_list:
    file_data = get_file_data(project, filtered_file.get('path'))

    for line in file_data.splitlines():
      match = re.search(application_properties_regex, line)

      if match:
        variable_name = match.group("name")
        url_text = match.group("url_text")
        # csv_matrix.append([acronym, project.name, filtered_file.get('name'), variable_name, url_text])
        print(
          f"Acronym: {acronym} | Project Name: {project.name} | File Name: {filtered_file.get('name')} | Nome da Variável: {variable_name} | URL: {url_text}\n")

def bootstrap_data(acronym, project, filtered_list):
  for filtered_file in filtered_list:
    file_data = get_file_data(project, filtered_file.get('path'))
    match = re.search(bootstrap_regex, file_data, flags=re.DOTALL)

    # acronym_dictionary[acronym][project.name] = []

    if match:
      integrations = match.group("integrations")
      integrations = integrations.replace(',', ';')
      # url_text = url_text.replace('"${', '').replace('}"', '')
      # acronym_dictionary[acronym][project.name].append({'file': filtered_file.get('name'), 'path': path, 'url': url_text})
      # csv_matrix.append([acronym, project.name, integrations])
      print(f"Acronym: {acronym} | Project Name: {project.name} | Integrations: {integrations}\n")

def build_representation(api, acronym):
  project_list = api.projects.list(search=acronym, all=True)

  for project in project_list:
    repo_files = get_repo_files(project)

    if repo_files is None:
      return None

    properties_files = filter_files_by_list(repo_files, application_properties_files)
    bootstrap_files = filter_files_by_list(repo_files, ['bootstrap.yml'])
    feign_files = filter_files_by_regex(repo_files, feign_folder_regex)

def main():
  gl = gitlab_api()
  build_representation(gl, "cdps")
