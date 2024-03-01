import os
import re
import base64
import gitlab
import requests
from dotenv import load_dotenv
from projects_resources import fernanda_project_acronym, other_projects_acronym, relevant_files

load_dotenv()

def generate_csv(file_name, csv_matrix):
  rows = ["{},{},{}".format(i, j, k) for i, j, k in csv_matrix]
  text = "\n".join(rows)

  with open(f'files/{file_name}.csv', 'w') as f:
    f.write(text)

def gitlab_api():
  session = requests.Session()
  return gitlab.Gitlab('https://git.original.com.br', private_token=os.getenv('GITLAB_TOKEN_COLLINS'), session=session)

def search_project_files(acronym_list):
  csv_matrix = []
  header = ["Sigla", "Projeto", "Integrations"]
  csv_matrix.append(header)

  regex = r"name\s*:\s*(?P<integrations>.*)"
  gl = gitlab_api()
  acronym_dictionary = {}

  for acronym in acronym_list:
    acronym_dictionary[acronym] = {}
    projects_list = gl.projects.list(search=acronym, all=True)

    for project in projects_list:
      try:
        repo_files = project.repository_tree(ref='master', recursive=True, all=True)
      except gitlab.exceptions.GitlabGetError as e:
        if e.error_message == '404 Tree Not Found':
          print(f"Project {project.name} has no folder structure")
          repo_files = None

      file_filter = []

      if repo_files is None:
        continue

      for file in repo_files:
        file_name = file.get('name')

        if file_name == "bootstrap.yml":
          file_info = {'name': file_name, 'path': file.get('path')}
          file_filter.append(file_info)

      if len(file_filter) == 0:
        continue

      for filtered_file in file_filter:
        path = filtered_file.get('path')
        file_content = project.files.get(ref='master', file_path=path)
        file_data = base64.b64decode(file_content.content).decode("utf-8").replace('\\n', '\n')
        match = re.search(regex, file_data, flags=re.DOTALL)

        # acronym_dictionary[acronym][project.name] = []

        if match:
          integrations = match.group("integrations")
          integrations = integrations.replace(',',';')
          # url_text = url_text.replace('"${', '').replace('}"', '')
          # acronym_dictionary[acronym][project.name].append({'file': filtered_file.get('name'), 'path': path, 'url': url_text})
          csv_matrix.append([acronym, project.name, integrations])
          print(f"Acronym: {acronym} | Project Name: {project.name} | Integrations: {integrations}\n")
  return acronym_dictionary, csv_matrix

def main():
  dictionary, csv_matrix = search_project_files(fernanda_project_acronym)
  print(dictionary)
  generate_csv('fernanda_bootstrap_projects_integration', csv_matrix)

if __name__ == '__main__':
  main()