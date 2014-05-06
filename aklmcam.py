# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import subprocess

# <codecell>

subprocess.call('curl -k -H "username: williammckee" -H "password: J3e6t8q5y2" -o linkz https://infoconnect1.highwayinfo.govt.nz/ic/jbi/TrafficCameras/REST/FeedService/', shell=True)

# <codecell>

opcon = open('linkz', 'r')

# <codecell>

data = opcon.read()

# <codecell>

import xmltodict

# <codecell>

#savxml = open('/home/will/Desktop/brobeur-static/feeds/aklmcam.json', 'w')
#savxml.write(data)
#savxml.close()

# <codecell>

datadict = xmltodict.parse(data)

# <codecell>

import json

#write the dictionary to a file
outfile = open('linkz', 'w')
json.dump(datadict, outfile)

#read the data back in
with open('linkz') as infile:
    newDictionary = json.load(infile)

# <codecell>

savcdat = open('/home/will/Desktop/brobeur-static/feeds/aklmcam.json', 'w')
savcdat.write(str(newDictionary))
savcdat.close()

# <codecell>


