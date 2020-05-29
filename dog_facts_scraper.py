from urllib.request import urlopen
import json

url = 'https://cat-fact.herokuapp.com/facts?animal_type=dog'
json_obj = urlopen(url)

data = json.load(json_obj)

for element in data['all']:
    print(element['text'])