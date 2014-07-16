# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# ArtControl.me Python Development

# <markdowncell>

# This is a script to get the latest posts and data from artcontrol.me blog and post it into the static html site.

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


# <codecell>

pwd

# <codecell>

print lodArt[0]

# <codecell>

#print lodArt[0]

behArt = lodArt[1]

areArt = behArt['content']
print areArt

# <codecell>

savart = open('latepost', 'w')
savart.write(str(areArt))
savart.close

opart = open('latepost', 'r')
opart.read()

# <codecell>

pwd

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

#print imgzData


# <codecell>

#tlahArt = getArt['title']
#print tlahArt

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

for ite in titArt.keys():
    print ite
    for blehz in titArt:
        print blehz

# <codecell>

for tiar in titArt:
    #print titArt[tiar]
    #print tiar
    #print titArt[tiar]
    adres.append(titArt[ite])
    #arlis.append(titArt[tiar])

# <markdowncell>

# How can I get these 16 results in a list?

# <codecell>


# <codecell>

adres

<<<<<<< HEAD
# <codecell>

arlis

# <markdowncell>

# After some thought I just made a list manually. This needs to be fixed to auto collect
# these items

=======
>>>>>>> b659041c2a37da8db8236833152b4cecc67c63bd
