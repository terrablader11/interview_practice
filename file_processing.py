import requests
import random
import json

guides = ["CLO", "Corporate Finance", "Credit", "Economics", "Equity Derivatives", "FX", "MBS", "Money Market", "Muni", "Rates", "Regulation", "Behavioral", "Markets", "Pitch"]
selected = ["CLO", "Corporate Finance", "Credit", "Economics", "Equity Derivatives", "FX", "MBS", "Money Market", "Muni", "Rates", "Regulation"]
files = []
file_names = []

def process_file(url):
  page = requests.get(url)
  return page.text.split('\r\n\r\n')

technical = []
markets = []
behavioral = []
pitch = []
id_counter = 1

for guide in guides:
  url = "https://raw.githubusercontent.com/terrablader11/interview_practice/refs/heads/main/text/" + guide.replace(' ', '%20') + "%20Q%26A.txt"
  processed_file = process_file(url)

  for x in range(len(processed_file)):
    if x%2 == 0:
      d = {}
      d['id'] = id_counter
      d['category'] = guide
      d['question'] = processed_file[x]
      d['answer'] = processed_file[x+1]
      if guide == "Behavioral":
        behavioral.append(d)
      elif guide == "Markets":
        markets.append(d)
      elif guide == "Pitch":
        pitch.append(d)
      else:
        technical.append(d)
      id_counter += 1

counter = 0
names = ["technical", "markets", "behavioral", "pitch"]
for result in [technical, markets, behavioral, pitch]:
  json_dump = json.dumps(result, indent=2, ensure_ascii=False)
  with open(names[counter] + ".json", "w") as outfile:
      outfile.write(json_dump)
  counter += 1
