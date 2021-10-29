from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import string

# Python program to crawl a web page and get most frequent words
# crawl GlassDoor to find Most job title

url = "https://www.glassdoor.com/Job/sweden-spotify-jobs-SRCH_IL.0,6_IN223_KO7,14.htm?clickSource=searchBox"
wordlist = []


def Scrap(url):

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')

    for each_text in soup.find_all('a', {'class': 'jobLink'}):
        res = re.split(', | -', each_text.text)
        word = str(res[0])
        if(word != 'Spotify' and word != ''):
            wordlist.append(word)

    print(wordlist)


Scrap(url)
