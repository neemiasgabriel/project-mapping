def main():
  acronym_dictionary = load_file('files/acronym_dictionary.json')
  fwms_dictionary = load_file('files/fwms_dictionary.json')

  # original_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
  # subset_keys = ["a", "c"]
  # subset_dict = {key: original_dict[key] for key in subset_keys if key in original_dict}

  fernanda_projects_dict = {key: acronym_dictionary[key] for key in fernanda_acronyns if key in acronym_dictionary}

  save_acronym_dictionary(fernanda_projects_dict, 'fernanda_projects_dictionary')