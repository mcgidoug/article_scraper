import requests
from bs4 import BeautifulSoup
from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse, urljoin

url = "https://example.com"  # Replace with your target URL

# Step 1: Parse robots.txt
parsed_url = urlparse(url)
robots_url = urljoin(f"{parsed_url.scheme}://{parsed_url.netloc}", "/robots.txt")

rp = RobotFileParser()
rp.set_url(robots_url)
rp.read()

# Step 2: Check if scraping is allowed for our user-agent
user_agent = "*"
if rp.can_fetch(user_agent, url):
    print("Scraping is allowed. Proceeding...\n")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    for p in soup.find_all("p"):
        print(p.text.strip())
else:
    print(f"Scraping is disallowed by {robots_url}")

