import requests
import json
res = requests.get('https://wtvehiclesapi.duckdns.org/docs/')
response = json.load(res.text)