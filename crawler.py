import urllib
import urllib2
from bs4 import BeautifulSoup

def to_file(content,filename):
    with open(filename,'wb') as output:
      output.write(content.read())

url = "https://ilearn.ucr.edu/"
req = urllib2.Request(url)
res = urllib2.urlopen(req)

data = res.read()
soup = BeautifulSoup(data, 'html.parser')

links = []
for link in soup.find_all('a'):
    print "--------------"
    href = link.get('href')
    try:
        if(href[0] == "/"):
            href = url + href[1:]
    except TypeError:
        print "None"

    print(href)
    links.append(href)

list(set(links))

