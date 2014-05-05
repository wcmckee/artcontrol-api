# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# ArtControl.me Python Development

# <codecell>

import requests
import json

# <codecell>

webArt = ('http://artcontrol.me/?wpapi=search&dev=1&keyword=post&count=2&page=1&content=1')

# <codecell>

dawArt = requests.get(webArt)

# <codecell>

jawArt = json.loads(dawArt.text)
print jawArt

# <codecell>

lodArt = jawArt['posts']

# <codecell>

print lodArt[1]

# <codecell>


# <codecell>


# <codecell>

print lodArt[1]

# <codecell>

#print lodArt[0]

behArt = lodArt[1]

areArt = behArt['content']
print areArt

# <codecell>

from bs4 import BeautifulSoup

# <codecell>

postData = BeautifulSoup(areArt)
#print postData

linkData = postData.find_all('a')
print linkData[0]

# <codecell>

for link in postData.find_all('a'):
    print(link.get('href'))

# <codecell>

txtzData = (postData.get_text())

print imgzData


# <codecell>

tlahArt = getArt['title']
print tlahArt

# <codecell>

dictData = {'imgz': linkData, 'text': txtzData}

print dictData

# <codecell>

getArt = requests.get('http://artcontrol.me/?wpapi=get_posts&dev=0')
jsnArt = json.loads(getArt.text)
print jsnArt

# <codecell>

jsnArt.keys()

# <codecell>

jsnArt

# <codecell>

titArt = jsnArt['posts']
titArt =  titArt[0]
print titArt

# <codecell>

yaeArt = len(titArt)
print yaeArt

# <codecell>

arlis = []

# <codecell>

adres = []

# <codecell>

for tiar in titArt:
    #print titArt[tiar]
    print tiar
    print titArt[tiar]
    adres.append(titArt['url'])
    arlis.append(titArt[tiar])

# <markdowncell>

# How can I get these 16 results in a list?

# <codecell>

arlis

# <markdowncell>

# After some thought I just made a list manually. This needs to be fixed to auto collect
# these items

# <codecell>

adres

# <codecell>

arlis[

# <codecell>

lipArt = ('name','parent','title','url','author','excerpt','slug','comment_count','tag',
          'date','type','page','id','comment_status')

# <codecell>

print lipArt

# <codecell>

contArt = len(lipArt)

# <codecell>

print contArt

# <codecell>

randArt = random.randint(0,14)

# <codecell>

jerArt = lipArt[randArt]
print jerArt

# <codecell>

repArt = titArt[jerArt]
print repArt

# <codecell>

titleArt = titArt['title']
print titleArt

# <codecell>

extrArt = titArt['excerpt']
print extrArt

# <codecell>

dateArt = titArt['date']
print dateArt

# <codecell>


# <codecell>


# <codecell>


# <codecell>


