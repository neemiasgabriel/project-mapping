import base64
import re
import gitlab

from gitlab_api import GitlabApi
from project_map import get_dictionaries

gl_api = GitlabApi()

fernanda_dictionary , dictionary = get_dictionaries()

forbidden_projects = []

for key in dictionary:
  project_names = dictionary.get(key)

  try:
    for name in project_names:
      project_repo = gl_api.get_project(acronym=key, project_name=name)

      if project_repo is None:
        continue

      files_repo = project_repo.repository_tree(ref='master', recursive=True, all=True)

      file_filter = []
      pattern = r"application-.*\.properties"

      print(f'Project Name: {name}\n')

      for file in files_repo:
        if re.match(pattern, file.get('name')) or file.get('name') == 'application.properties' or file.get('name') == 'bootstrap.yml':
          file_path = {'name': file.get('name'), 'path': file.get('path')}
          file_filter.append(file_path)
          print(f"name: {file_path.get('name')}, path: {file_path.get('path')}")

        for filtered_file in file_filter:
          path = filtered_file.get('path')
          file_content = project_repo.files.get(ref='master', file_path=file_path)
          file_data = base64.b64decode(file_content.content).decode("utf-8").replace('\\n', '\n')
          print(file_data)
  except gitlab.exceptions.GitlabGetError as e:
    if e.error_message == '404 Project Not Found':
      forbidden_projects.append(name)
      print(f"Project {name} not found in project {key}")

print(gl_api.forbidden_projects)