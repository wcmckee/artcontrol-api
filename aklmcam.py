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

datadict = xmltodict.parse(data)

# <codecell>

#savxml = open('/home/will/Desktop/brobeur-static/feeds/aklmcam.json', 'w')
#savxml.write(data)
#savxml.close()

# <codecell>

import json
jsononjz = json.dumps(datadict)
#read the data back in
#newDictionary = json.load(datadict)

# <codecell>

savcdat = open('/home/will/Desktop/brobeur-static/feeds/aklmcam.json', 'w')
savcdat.write(str(jsononjz))
savcdat.close()

# <codecell>


