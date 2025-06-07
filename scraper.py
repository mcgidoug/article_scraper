import requests
from bs4 import BeautifulSoup

url = ""
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

for p in soup.find_all("p"):
    print(p.text.strip())
