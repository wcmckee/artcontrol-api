# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# <h1>Auckland Motor Camera</h1>
# A project by [wcmckee](http://wcmckee.com/). 
# 
# This script I run as a cronjob every minute in order to keep the json file updated. 
# It logs into the infoconnect highway cameras. This is a xml file. I am not a big fan of working with xml files. I can do it, but I'd rather json. This gives me access to my 

# <markdowncell>

# [artcontrol.me](http://artcontrol.me/)
# 
# [freshfigure: photography](http://freshfigure.com/art)
# 
# [brobeur](http://brobeur.com)

# <markdowncell>

# **TODO** Add more useful data to the json feed. 

# <codecell>

ou need this number to board:
14692305 -
14N1 - HLZAKL

Please report at least

Bus - 5 minutes

before departure time

5:50pm 	
Hamilton (Central)

# <codecell>

import subprocess

# <markdowncell>

# [nzta](https://infoconnect1.highwayinfo.govt.nz/ "nzta")

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

savcdat = open('/home/wcmckee/brobeur-static/feeds/aklmcam.json', 'w')
savcdat.write(str(jsononjz))
savcdat.close()
print('done uploading feed!')

# <codecell>


