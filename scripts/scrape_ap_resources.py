import requests
from bs4 import BeautifulSoup

def get_ap_topics():

    url = "https://www.khanacademy.org/humanities/ap-us-history"

    r = requests.get(url)

    soup = BeautifulSoup(r.text,"html.parser")

    topics = []

    for link in soup.find_all("a"):

        text = link.text.strip()

        if "Unit" in text:
            topics.append(text)

    return topics


print(get_ap_topics())
