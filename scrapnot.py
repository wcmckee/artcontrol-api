# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# This is a scrapbook for exploring some python ideas and modules that i plan to take into other notebooks.

# <codecell>

import markdown

# <codecell>

import requests
import json
import xmltodict

# <codecell>

hcpux = requests.get('http://feeds.feedburner.com/HamiltonComputerClub?format=xml')

# <codecell>

cerz = hcpux.text

# <codecell>

hamx = xmltodict.parse(cerz)

# <codecell>

for ha in hamx['rss']['channel']:
    print ha

# <codecell>

staz = hamx['rss']['channel']

# <codecell>

opd = json.dumps(hamx)

# <codecell>

savopd = open('cpuclu.json', 'w')

# <codecell>

savopd.write(opd)

# <codecell>

savopd.close()

# <codecell>

zopa = open('cpuclu.json', 'r')

# <codecell>


# <codecell>

myjson = zopa.read()

# <codecell>

sjson = json.dumps(hamx)

# <codecell>

print sjson

# <codecell>

cerz

# <codecell>

markdown.to_html_string('*testing one two three*')

# <codecell>

html = markdown.markdown('testing123!')

# <codecell>

print html

# <codecell>

import os

# <codecell>

posfol = ("~/home/wcmckee/hamiiltoncomputerclub.org.nz/static/posts")
blotil = ("wcmckee")

# <codecell>

os.makedirs(posfol)

# <codecell>

os.chdir(posfol)

# <codecell>

ls

# <codecell>

rstz = open((blotil + '.rst'), 'w')

# <codecell>

rstz.write('

# <codecell>


# <codecell>

conv = markdown.markdownFromFile

