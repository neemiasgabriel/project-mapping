import re
import pandas as pd

df_others = pd.read_csv("files/others-projects.csv")

dictionary = {}
regex = r"java.*"

for index, row in df_others.iterrows():
  sigla_pod = row['Sigla_Pod']
  pods = row['PODs']

  if dictionary.get(sigla_pod) is None:
    dictionary[sigla_pod] = set()

  result = re.sub(regex, "", pods)
  dictionary[sigla_pod].add(f"{result}java")

for key in dictionary:
  values = list(dictionary.get(key))
  dictionary[key] = values

print(dictionary)