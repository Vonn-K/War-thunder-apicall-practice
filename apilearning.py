import requests

url = "https://wtvehiclesapi.duckdns.org/api/vehicles/stats?version=2.53.0.7"

response = requests.get(url)

print(response.status_code)
print(response.headers["Content-Type"])
print(response.text)