# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import os
import json
import digitalocean

# <codecell>

os.chdir('/home/wcmckee/password')

# <codecell>

opdig = open('dig', 'r')

# <codecell>

opdig.read()

# <codecell>

list(opdig)

# <codecell>

digcli = ('a24a5636402aaf75d07b774d98591ea3')

# <codecell>

print digcli

# <codecell>

apikey = ('3e5eb096244fd5e791283d372be9da9f')

# <codecell>

print apikey

# <codecell>

manager = digitalocean.Manager(client_id = digcli, api_key = apikey)

# <codecell>

mydrop = manager.get_all_droplets()

# <codecell>


# <codecell>

print mydrop

# <codecell>

dropo = mydrop[0]

# <codecell>

print dropo

# <codecell>

events = dropo.get_events()

# <codecell>

for event in events:
    event.load()
    print event.percentage

# <codecell>

dropo.ip_address

# <codecell>

dropo.name

# <codecell>

dropo

# <codecell>

for dr in mydrop:
    print dr.ip_address
    print dr.status
    print dr.region_id

# <codecell>

dropo.api_key

# <codecell>

dropo.call_reponse

# <codecell>

dropo.image_id

# <codecell>

dropo.size_id

# <codecell>

dropo.events

# <codecell>

dropo.size_id

# <codecell>

domain = manager.get_all_domains

# <codecell>

print domain

# <codecell>

domain.im_self

# <codecell>

gimg = manager.get_global_images

# <codecell>

gimg

# <codecell>

list(gimg)

# <codecell>


