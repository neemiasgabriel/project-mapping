import base64
import gitlab

from gitlab_api import GitlabApi
from project_map import get_dictionaries

gl_api = GitlabApi()

fernanda_list = ['acad', 'apio', 'cdps', 'ctas', 'fepw', 'parc', 'rtto', 'tbgr', 'trfo', 'atmo', 'gcen', 'mcsv', 'ctasm']
fernanda_dictionary , dictionary = get_dictionaries()

forbidden_projects = []
file_list = ['application.properties', 'application-hml.properties', 'application-dev.properties', 'bootstrap.yml']

for key in fernanda_dictionary:
  project_names = fernanda_dictionary.get(key)

  try:
    for name in project_names:
      project_repo = gl_api.get_project(acronym=key, project_name=name)

      if project_repo is None:
        continue

      print(f'Project Name: {name}\n')

      # files_in_repo = project_repo.repository_tree(ref='master', recursive=True, all=True)
      #
      # file_filter = []
      #
      # for file in files_in_repo:
      #   file_name = file.get('name')
      #
      #   if file_name in file_list:
      #     file_info = {'name': file_name, 'path': file.get('path')}
      #     file_filter.append(file_info)
      #
      # for filtered_file in file_filter:
      #   print(f'Project Name: {name} | File Name: {filtered_file.get("name")}\n')
      #
      #   path = filtered_file.get('path')
      #   file_content = project_repo.files.get(ref='master', file_path=path)
      #   file_data = base64.b64decode(file_content.content).decode("utf-8").replace('\\n', '\n')
      #   print(file_data)
      #   print('\n')

  except gitlab.exceptions.GitlabGetError as e:
    if e.error_message == '404 Project Not Found':
      print(f"Project {name} not found in project {key}")

print('\n'.join(gl_api.forbidden_projects))