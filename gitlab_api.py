import os
import gitlab
import requests
from dotenv import load_dotenv

load_dotenv()

class GitlabApi:
  def __init__(self):
    session = requests.Session()
    self.gl = gitlab.Gitlab('https://git.original.com.br', private_token=os.getenv('GITLAB_TOKEN_COLLINS'), session=session)
    self.forbidden_projects = []

  def get_project(self, acronym, project_name):
    try:
      return self.gl.projects.get(f'{acronym}/{project_name}')
    except gitlab.exceptions.GitlabGetError as e:
      if e.error_message == '404 Project Not Found':
        self.forbidden_projects.append(project_name)

      return None
