
import json
import re
import urllib.request
import http.client
from xml.dom import minidom

# get XML RSS feed
response = urllib.request.urlopen("http://www.dhs.sg/rss/what%2527s-new%3F-19.xml")
xml = response.read().decode('utf-8')
# get all XML as a string
xml_data = minidom.parseString(xml).getElementsByTagName('channel')
# get all items
parts = xml_data[0].getElementsByTagName('item')
parts.length
jsonlist = []
titlelist = []
linklist = []
descriptionlist = []
# loop all items
for part in parts:
    # get title
    title = part.getElementsByTagName('title')[0].firstChild.nodeValue.strip()
    titlelist.append(title)
    # get link
    link = part.getElementsByTagName('link')[0].firstChild.nodeValue.strip()
    linklist.append(link)
    # get description
    description = part.getElementsByTagName('description')[0].firstChild.wholeText.strip()
    description = re.sub("<[^>]*>", "", description)
    description = description[:-10]
    descriptionlist.append(description)
    jsonconvertdict = { 'title' : title,
                        'link' : link,
                        'description' : description }
    jsonlist.append(jsonconvertdict)
# formatting dict for JSON
jsonconvertdict = { 'feeds' : jsonlist }
# Get JSON encoding
jsonencoded = json.dumps(jsonconvertdict, separators=(',', ':'))
print(jsonencoded)
