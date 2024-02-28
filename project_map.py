import re
import pandas as pd

def get_dictionaries():
  files = ["files/fernanda-projects.csv", "files/others-projects.csv"]
  fernanda_dictionary = {}
  others_dictionary = {}

  for file in files:
    df_others = pd.read_csv(file)

    dictionary = {}
    regex = r"java.*"

    for index, row in df_others.iterrows():
      sigla_pod = row['Sigla_Pod']
      pods = row['PODs']

      if dictionary.get(sigla_pod) is None:
        dictionary[sigla_pod] = set()

      result = re.sub(regex, "", pods)
      dictionary[sigla_pod].add(f"{result}java")

    if file == "files/fernanda-projects.csv":
      fernanda_dictionary = dictionary
    else:
      others_dictionary = dictionary

  return fernanda_dictionary, others_dictionary
