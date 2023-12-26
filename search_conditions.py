import requests
import json
import os
import webbrowser

healthConditionID = None

data = json.load(open('conditions.json'))
print (data);

search = input ("What is your ailment?")

for i in range(0, len(data)-1):
  s = data[i]['description'].find(search)
  if s > -1:
    healthConditionID = data[i]['healthConditionID']


if healthConditionID is not None:
  webbrowser.open('https://www.amazon.com/s?k=zinc', new=2)

