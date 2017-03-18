import requests
from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

urls = ['https://en.wikipedia.org/wiki/Cabinet_of_President_Goodluck_Jonathan'];
file = open("senators.txt", "w")

def getUrl(urls):
  for url in urls:
    response = BeautifulSoup(urlopen(url).read())
    tables = response.findAll('table')
    links = response.findAll('a')
    for link in links:
      name = link.getText()
      print(name)
    file.close()

getUrl(urls)

