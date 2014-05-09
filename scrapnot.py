# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# This is a scrapbook for exploring some python ideas and modules that i plan to take into other notebooks.

# <codecell>

import markdown

# <codecell>

import requests

# <codecell>

hcpux = requests.get('http://feeds.feedburner.com/HamiltonComputerClub?format=xml')

# <codecell>

hcpux.

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

