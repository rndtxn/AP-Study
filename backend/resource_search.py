import requests
from bs4 import BeautifulSoup

def search_resources(query):

    url = f"https://www.google.com/search?q={query}"

    headers = {"User-Agent":"Mozilla/5.0"}

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text,"html.parser")

    links = []

    for a in soup.find_all("a"):
        href = a.get("href")

        if "http" in str(href):
            links.append(href)

    return links[:10]
