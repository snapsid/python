import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


url= urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_432338.xml').read()

stuff = ET.fromstring(url)
lst = stuff.findall('comments/comment')
print('User count:', len(lst))

count=0
for item in lst:
    count=count+int(item.find('count').text)
print('Sum:', count)
