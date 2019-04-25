#This is a test script for retrieving files from forgery.motive.com. This isn't really intended for use on other websites
from lxml import html
import requests

print 'Hello, World!'
url="http://forgery.motive.com/staging/Patches/5.1.3-HDM/dbscripts/"
thign = requests.get(url)
tree = html.fromstring(thign.content)
titles = tree.xpath('//a/@href')
print titles
print len(titles)
print '/staging/Patches/5.1.3-HDM/' in titles


# print the list
for i in titles:
    if ( titles.index(i) >4 ):
        print i

i = 0

# remove the uneccessary first 5 elements in the list
while (len(titles) != 46):
    print titles[i]
    titles.pop(i)
files = []
# get the actual file content in text form from the url
for title in titles:
    files.append(requests.get(url+title))
    #print files

# actually writes the the content from the reponses to real files in the OS
for file in files:
    print file.url
    try:
        f= open(titles[files.index(file)],"w")
        f.write(file.content)
        f.close()
        print titles[files.index(file)]+" went fine"
    except:
        print "CAUSED AN ERROR"
        print titles[files.index(file)]
# f= open("9gclistorm","w")
# f.write("lingbatbatling")
# f.close()
exit()