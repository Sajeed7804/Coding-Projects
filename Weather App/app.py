import requests

url = "https://randomfox.ca/floof"

response = requests.get(url)

fox = response.json()

print(fox['image'])