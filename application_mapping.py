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

      if len(bootstrap) != 0:
        integrations = bootstrap[0].get('integrations')
        integrations = integrations.split(';')

        for integration in integrations:
          integration = integration.strip().replace('-integration', '')

          if integration in fernanda_acronyns:
            valid_integrations.append(integration)
            if project_mapping_dictionary.get(integration) is None:
              project_mapping_dictionary[integration] = {}

            if project_mapping_dictionary[integration].get(acronym) is None:
              project_mapping_dictionary[integration][acronym] = {}

            if project_mapping_dictionary[integration][acronym].get(project) is None:
              project_mapping_dictionary[integration][acronym][project] = []

        feign = other_projects_dict[acronym][project].get('feign')

        if len(feign) != 0:
          for integration in valid_integrations:
            for file in feign:
              if file.get('url').startswith(integration):
                project_mapping_dictionary[integration][acronym][project].append(file.get('url'))

          print(project_mapping_dictionary)

  save_acronym_dictionary(project_mapping_dictionary, 'project_mapping_dictionary')



if __name__ == '__main__':
  main()