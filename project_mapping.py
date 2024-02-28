import os
import base64
import gitlab
import requests
from dotenv import load_dotenv
from projects_resources import fernanda_project_acronym, other_projects_acronym, relevant_files

load_dotenv()

def gitlab_api():
  session = requests.Session()
  return gitlab.Gitlab('https://git.original.com.br', private_token=os.getenv('GITLAB_TOKEN_COLLINS'), session=session)

def search_project_files(acronym):
  gl = gitlab_api()

  if acronym in fernanda_project_acronym:
    projects_list = gl.projects.list(search=acronym, all=True)

    for project in projects_list:
      try:
        repo_files = project.repository_tree(ref='master', recursive=True, all=True)
      except gitlab.exceptions.GitlabGetError as e:
        if e.error_message == '404 Tree Not Found':
          print(f"Project {project.name} has any folder structure")
          repo_files = None

      file_filter = []

      if repo_files is None:
        continue

      for file in repo_files:
        file_name = file.get('name')

        if file_name in relevant_files:
          file_info = {'name': file_name, 'path': file.get('path')}
          file_filter.append(file_info)

      if len(file_filter) == 0:
        continue

      print(f'Project Name: {project.name}\n')

      for filtered_file in file_filter:
        print(f'File Name: {filtered_file.get("name")}\n')

        path = filtered_file.get('path')
        file_content = project.files.get(ref='master', file_path=path)
        file_data = base64.b64decode(file_content.content).decode("utf-8").replace('\\n', '\n')

        print(file_data)
        print('\n')

def main():
  search_project_files('apio')

if __name__ == '__main__':
  main()