import requests
import base64
import re
import gitlab
from dotenv import load_dotenv

load_dotenv()

session = requests.Session()

gl = gitlab.Gitlab('https://git.original.com.br', private_token='b-GBompfzdj2jdZ_ydS-', session=session)

fernanda_dictionary = {
  'ctas': ['ctas-cmm-rest-java', 'ctas-consulta-bloqueio-transacional-java', 'ctas-consulta-lancamentos-java']
}

dictionary = {
  'atad': ['atad-esqueci-minha-senha-java', 'atad-liveness-servicos-java']
}

for key in dictionary:
  # groups = gl.groups.get(key)
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

