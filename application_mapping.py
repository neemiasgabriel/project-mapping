"""
acad_cluster = 'vsacadprdback:5052'
ctas_cluster = 'bcopmswrkctn01:8642'

1. Buscar as integrações do sistema no bootstrap
  1.1. Se houver, procurar o nome das variáveis no feign ou, no application-hml.properties
  1.2. Se houver acad-integration, procurar nomes de variável dentro do application-hml.properties (buscar nome da variável) e
    procurar por outras variáveis no application-prd.properties
2. Caso não tenha bootstrap, procurar variáveis no application-prd.properties
"""

import re
import json
from resources import (
  application_properties_files,
  application_properties_regex,
  feign_folder_regex,
  feign_url_regex,
  bootstrap_regex,
  ignored_files,
  fernanda_acronyns,
  other_projects_acronym
)


acad_cluster = 'vsacadprdback:5052'
ctas_cluster = 'bcopmswrkctn01:8642'

def add_dictionary_entry(dictionary_mapping, integration, acronym, project):
  if dictionary_mapping.get(integration) is None:
    dictionary_mapping[integration] = {}

  if dictionary_mapping[integration].get(acronym) is None:
    dictionary_mapping[integration][acronym] = {}

  if dictionary_mapping[integration][acronym].get(project) is None:
    dictionary_mapping[integration][acronym][project] = []

def delete_dictionary_entry(dictionary_mapping, integration, acronym, project):
  if len(dictionary_mapping[integration][acronym][project]) == 0:
    del dictionary_mapping[integration][acronym][project]

  if len(dictionary_mapping[integration][acronym]) == 0:
    del dictionary_mapping[integration][acronym]

  if len(dictionary_mapping[integration]) == 0:
    del dictionary_mapping[integration]

def load_file(file_path):
  with open(file_path, 'r') as f:
    try:
      return json.load(f)
    except json.decoder.JSONDecodeError:
      return None

def save_acronym_dictionary(projects_dict, file_name):
  with open(f'files/{file_name}.json', 'w') as f:
    try:
      json.dump(projects_dict, f)
    except json.decoder.JSONDecodeError:
      print(projects_dict)

def main():
  other_projects_dict = load_file('files/other_projects_dictionary.json')
  fwms_dictionary = load_file('files/fwms_dictionary.json')
  project_mapping_dictionary = {}

  if other_projects_dict is None:
    print("Não foi possível carregar o dicionário")
    return None

  for acronym in other_projects_dict.keys():
    for project in other_projects_dict[acronym].keys():
      bootstrap = other_projects_dict[acronym][project].get('bootstrap')
      valid_integrations = []

      add_dictionary_entry(project_mapping_dictionary, "acad", acronym, project)
      add_dictionary_entry(project_mapping_dictionary, "ctas", acronym, project)

      if len(bootstrap) != 0:
        integrations = bootstrap[0].get('integrations')
        integrations = integrations.split(';')

        for integration in integrations:
          integration = integration.strip().replace('-integration', '')

          if integration in fernanda_acronyns:
            valid_integrations.append(integration)
            add_dictionary_entry(project_mapping_dictionary, integration, acronym, project)

        feign = other_projects_dict[acronym][project].get('feign')

        if len(feign) != 0:
          for integration in valid_integrations:
            for file in feign:
              if file.get('url').startswith(integration):
                project_mapping_dictionary[integration][acronym][project].append(file.get('url'))

            if project_mapping_dictionary.get(integration) is not None:
              delete_dictionary_entry(project_mapping_dictionary, integration, acronym, project)

      if other_projects_dict[acronym][project]["application"] is None:
        continue

      application_prd = other_projects_dict[acronym][project]["application"].get("application-prd.properties")

      if application_prd is not None and len(application_prd) != 0:
        for prd in application_prd:
          if prd.get('url_text').startswith(acad_cluster):
            project_mapping_dictionary["acad"][acronym][project].append(prd.get('url_text'))
          if prd.get('url_text').startswith(f'{ctas_cluster}/ctas'):
            project_mapping_dictionary["ctas"][acronym][project].append(prd.get('url_text'))

      application = other_projects_dict[acronym][project]["application"].get("application.properties")

      if application is not None and len(application) != 0:
        for prd in application:
          if prd.get('url_text').startswith(acad_cluster):
            project_mapping_dictionary["acad"][acronym][project].append(prd.get('url_text'))
          if prd.get('url_text').startswith(f'{ctas_cluster}/ctas'):
            project_mapping_dictionary["ctas"][acronym][project].append(prd.get('url_text'))

      delete_dictionary_entry(project_mapping_dictionary, "acad", acronym, project)
      delete_dictionary_entry(project_mapping_dictionary, "ctas", acronym, project)

  save_acronym_dictionary(project_mapping_dictionary, 'project_mapping_dictionary')


if __name__ == '__main__':
  main()