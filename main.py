import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

soup = BeautifulSoup(indeed_result.text, 'html.parser')

print(soup)


