import gitlab

from gitlab_api import GitlabApi
from projects_resources import fernanda_project_acronym

gl_api = GitlabApi()

forbidden_projects = []
file_list = ['application.properties', 'application-hml.properties', 'application-dev.properties', 'bootstrap.yml']

for key in fernanda_dictionary:
  project_names = fernanda_dictionary.get(key)

  try:
    gl = gl_api.gl
    projects_list = gl.projects.list(search=key, all=True)

    project_name = ''
    for project in projects_list:
      print(project)
      project_name = project.name
      project_files = project.repository_tree(ref='master', recursive=True, all=True)

  except gitlab.exceptions.GitlabGetError as e:
    if e.error_message == '404 Project Not Found':
      print(f"Project {project_name} not found in project {key}")
      forbidden_projects.append(project_name)

print('\n'.join(gl_api.forbidden_projects))