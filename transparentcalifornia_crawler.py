import urllib
import urllib2
from bs4 import BeautifulSoup

def to_file(content,filename):
    with open(filename,'wb') as output:
      output.write(content.read())

url = "http://transparentcalifornia.com/agencies/salaries/#counties"
req = urllib2.Request(url)
res = urllib2.urlopen(req)
data = res.read()
soup = BeautifulSoup(data, 'html.parser')
rows = soup.find("table", class_="agency-list").find_all('tr')
#http://transparentcalifornia.com/export/agoura-hills-2015.csv
pre = "http://transparentcalifornia.com/export/"
for row in rows:
    name = row.find("a").get_text().lower().replace(" ","-")
    for year in range(1,5):
        y = str(year)
        try:
            to_file(urllib2.urlopen(pre + name + "-201" + y + ".csv"), name + "-201" + y + ".csv")
        except:
            print "HTTP Error 404: Not Found URL('" + pre + name + "-201" + y + ".csv')"

