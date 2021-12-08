from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import string


url = (
    "http://localhost:9000/component_measures?id=docker-py&metric=complexity&view=list"
)


def Scrap(url):

    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, "html.parser")

    for each_text in soup.find_all("tr", {"class": "measure-details-component-row"}):
        print(each_text.text)


Scrap(url)
