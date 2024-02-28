import os
import base64
import requests
import gitlab
from dotenv import load_dotenv

load_dotenv()

class GitlabApi:
  def __init__(self):
    session = requests.Session()
    self.gl = gitlab.Gitlab('https://git.original.com.br', private_token=os.getenv('GITLAB_TOKEN'), session=session)
    self.forbidden_projects = []

  def get_forbidden_projects(self):
    return self.forbidden_projects

  def get_project(self, acronym, project_name):
    try:
      project = self.gl.projects.get(f'{acronym}/{project_name}')
      return project
    except gitlab.exceptions.GitlabGetError as e:
      if e.error_message == '404 Project Not Found':
        self.forbidden_projects.append(project_name)

      return None
