import json
from resources import (
  fernanda_acronyns,
  other_projects_acronym
)

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
  # fwms_dictionary = load_file('files/fwms_dictionary.json')

  # original_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
  # subset_keys = ["a", "c"]
  # subset_dict = {key: original_dict[key] for key in subset_keys if key in original_dict}

  # fernanda_projects_dict = {key: fwms_dictionary[key] for key in fernanda_acronyns if key in fwms_dictionary}
  # save_acronym_dictionary(fernanda_projects_dict, 'fernanda_projects_dictionary')
  #
  # other_projects_dict = {key: fwms_dictionary[key] for key in other_projects_acronym if key in fwms_dictionary}
  # save_acronym_dictionary(other_projects_dict, 'other_projects_dictionary')

  acronym_dict = load_file('files/acronym_dictionary.json')
  other_projects_list = {key: acronym_dict[key] for key in other_projects_acronym if key in acronym_dict}
  save_acronym_dictionary(other_projects_list, 'other_projects_list')

if __name__ == '__main__':
  main()
