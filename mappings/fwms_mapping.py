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
  header = ["Sigla", "Nome da Variavel","URL"]
  csv_matrix.append(header)

  regex = r"(?P<name>.*?)\s*=\s*(https?://)(?P<url_text>.*)"
  gl = gitlab_api()

  for acronym in acronym_list:
    fwms_regex = f"{acronym}-integration.properties"

    projects_list = gl.projects.list(search="fwms", all=True)

    for project in projects_list:
      if not project.name.endswith('-java'):
        continue

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

        if file_name.endswith('.gitignore') or not file_name.endswith('-corp.properties'):
          continue

        file_acronym = file_name.replace('-integration.properties', '')

        if file_acronym in (fernanda_project_acronym):
          continue

        # if file_name in relevant_files or re.match(feign_regex, file.get('path')):

        if re.match(fwms_regex, file.get('path')):
          file_info = {'name': file_name, 'path': file.get('path')}
          file_filter.append(file_info)

      if len(file_filter) == 0:
        continue

      for filtered_file in file_filter:
        path = filtered_file.get('path')
        file_content = project.files.get(ref='master', file_path=path)
        file_data = base64.b64decode(file_content.content).decode("utf-8").replace('\\n', '\n')

        for line in file_data.splitlines():
          match = re.search(regex, line)

          if match:
            variable_name = match.group("name")
            url_text = match.group("url_text")
            csv_matrix.append([acronym, variable_name, url_text])
            print(f"Acronym: {acronym} | Nome da Variável: {variable_name} | URL: {url_text}\n")
  return csv_matrix

def main():
  csv_matrix = search_project_files(fernanda_project_acronym)
  generate_csv('fernanda_fwms_variables', csv_matrix)

if __name__ == '__main__':
  main()