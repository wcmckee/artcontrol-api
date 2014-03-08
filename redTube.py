# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# RedTube json Python

# <markdowncell>

# '''
# copyright 2013 WCMCKEE
# will@artcontrol.me
# '''

# <codecell>

import requests
import json
import random

# <codecell>

redhtp = ('http://api.redtube.com/?data=redtube.')
redtagz = ('tags.getTagList')
redcat = ('Categories.getCategoriesList')
redstar = ('Stars.getStarList') 
redvid = ('Videos.searchVideos&page=1')
redj = ('&output=json')

# <markdowncell>

# need to choose a random between tagz cat and star

# <codecell>

endlist = [redtagz, redcat, redstar]

# <codecell>

ranclist = random.choice(endlist)

# <codecell>

print endlist

# <codecell>

fullurlz = redhtp + ranclist + redj

# <codecell>

fulur = redhtp + redvid + redj

# <codecell>

print fullurlz

# <codecell>

fuz = str(fullurlz)

# <codecell>

print fulur

# <markdowncell>

# Requests and json are the two main modules used for this. Random can also be handy

# <codecell>

getfullurl = requests.get(fullurlz)
loazfullurl = json.loads(fullurlz)

# <codecell>

getPrn = requests.get(fulur)

# <markdowncell>

# Simple requests command to get the json object. This could be any json object - not just RedTube

# <codecell>

loaPrn = json.loads(getPrn.text)
print loaPrn

# <markdowncell>

# Convert it into readable text that you can work with

# <codecell>

for feed in loaPrn[u'videos']:
    print feed
    #for entry in feed[u'video']:
        #print entry

# <codecell>

titlost = []

# <codecell>

for nums in range(20):
    naoPrn = loaPrn[u'videos'][nums]
    #print naoPrn
    
    ngePrn = naoPrn[u'video']
    #print ngePrn
    urlPrn = ngePrn[u'title']
    titlost.append(urlPrn)
    print urlPrn

# <codecell>

print titlost

# <codecell>


# <codecell>

naoPrn = loaPrn[u'videos'][5]
print naoPrn

# <markdowncell>

# Compress down - look at first element of json object. You could cycle through older elements
# by increasing the int

# <codecell>

ngePrn = naoPrn[u'video']
print ngePrn

# <markdowncell>

# Compress down again - this time video. It's always a bit of a trial and error to figure out
# navagating json objects, IPython is perfect for this. 

# <headingcell level=2>

# Individual Data!

# <markdowncell>

# This could be imporoved by turning the following unicode into a list and get the program
# to cycle though - saving off each element. Maybe save to a list?

# <codecell>

ratPrn = ngePrn[u'title']

# <codecell>

for k in naoPrn:
    print k

# <codecell>

from PIL import Image

# <codecell>

im = Image.open('ratPrn')

# <codecell>

thumPrn = ratPrn[u'thumb']

# <codecell>

print thumPrn

# <codecell>

ratPrn = ngePrn[u'ratings']
print ratPrn

# <codecell>

urlPrn = ngePrn[u'url']
print urlPrn

# <codecell>

viwPrn = ngePrn[u'views']
print viwPrn

# <codecell>

idPrn = ngePrn[u'video_id']
print idPrn

# <codecell>

pdaPrn = ngePrn[u'publish_date']
print pdaPrn

# <codecell>

timPrn = ngePrn[u'duration']
print timPrn

# <codecell>

titPrn = ngePrn[u'title']
print titPrn

# <codecell>

tagPrn = ngePrn[u'tags']
print tagPrn

# <codecell>

derbPrn = (tagPrn, 'tag_name')
print derbPrn

# <codecell>

thNum = 0
taTrn = tagPrn[thNum]
print taTrn
thNum + 1

# <markdowncell>

# TODO: Cycle the list and print all tags

# <codecell>

naTrn = taTrn['tag_name']
print naTrn

# <codecell>

demHub = (titlHub, titPrn, naTrn, urlPrn, pdaPrn, thumPrn, imgHub, linHub)

# <codecell>

print demHub

# <headingcell level=2>

# Saving Data

# <markdowncell>


# <codecell>

savPrn = open('savPrn','w')
savPrn.write('<h3 style="text-align: center;"><a href="' + urlPrn + '">')
savPrn.write(titPrn + '</a></h3>')
savPrn.write('<p style="text-align: right;">' + pdaPrn)
savPrn.write('</a></h3><img class="aligncenter" alt="null" src="' + thumPrn)
savPrn.write('" />')
savPrn.close()

# <codecell>

savTub

# <codecell>

ls

# <codecell>

opPrn = open('savPrn','r')
for op in opPrn:
    print op

# <codecell>


# <headingcell level=1>

# PornHub

# <codecell>

import feedparser

# <codecell>

urlHub = feedparser.parse('http://www.pornhub.com/video/webmasterss')

# <codecell>

urlHub['feed']['title']

# <codecell>

tlinHub = urlHub['feed']['link']

# <codecell>

pubHub = urlHub['feed']['published']

# <codecell>

linHub = urlHub.entries[0].link

# <codecell>

titlHub = urlHub.entries[0].title

# <codecell>

imgHub = urlHub.entries[0].thumb_large

# <codecell>

urlHub.entries[0]

# <codecell>


# <codecell>

for daHub, da in enumerate([titlHub, linHub, pubHub, imgHub]):
    titlost.append(titHub)
    print daHub, da

# <codecell>


# <codecell>


# <codecell>


