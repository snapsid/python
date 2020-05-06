import urllib
from bs4 import BeautifulSoup


url = input('Enter URL:')
count = int(input('Enter count:'))
position = int(input('Enter position:'))-1
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html,"html.parser")
p = soup('a')


for i in range(count):
    link = p[position].get('href', None)
    print (p[position].contents[0])
    html = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(html,"html.parser")
    p = soup('a')
