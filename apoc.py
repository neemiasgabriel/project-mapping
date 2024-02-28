import os
import re
import base64
import gitlab
import requests

from dotenv import load_dotenv
from project_map import get_dictionaries

load_dotenv()

session = requests.Session()

gl = gitlab.Gitlab('https://git.original.com.br', private_token=os.getenv('GITLAB_TOKEN'), session=session)

fernanda_dictionary , dictionary = get_dictionaries()

forbidden_projects = []

for key in dictionary:
  project_names = dictionary.get(key)

  for name in project_names:
    project_repo = gl.projects.get(f"{key}/{name}")
    files_repo = project_repo.repository_tree(ref='master', recursive=True, all=True)

    file_filter = []
    pattern = r"application-.*\.properties"

    for file in files_repo:
      if re.match(pattern, file.get('name')) or file.get('name') == 'application.properties' or file.get('name') == 'bootstrap.yml':
        file_path = {'name': file.get('name'), 'path': file.get('path')}
        file_filter.append(file_path)
        print(f"name: {file_path.get('name')}, path: {file_path.get('path')}")

    try:
      for file in file_filter:
        path = file.get('path')
        file_content = project_repo.files.get(ref='master', file_path=path)
        file_data = base64.b64decode(file_content.content).decode("utf-8")

        print(f"File: {file.get('name')}\n\n")
        print(file_data.replace('\\n', '\n'))

    except gitlab.exceptions.GitlabGetError as e:
      print(f"File 'application.properties' not found in project {project_repo.name}")

