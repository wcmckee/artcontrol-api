# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import os
import json
import digitalocean

# <codecell>

digcli = ('a24a5636402aaf75d07b774d98591ea3')

# <codecell>

print digcli

# <codecell>

apikey = ('9d4a1822e4aaf3a11f73012e5648ebd4')

# <codecell>

print apikey

# <codecell>

manager = digitalocean.Manager(client_id = digcli, api_key = apikey)

# <codecell>

mydrop = manager.get_all_droplets()

# <codecell>

mydrop.sort

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

sshin = []

# <codecell>

for ipz in sshin:
    print('wcmckee@' + ipz)

# <codecell>

for meip in mydrop:
    print meip.ip_address
    sshin.append(meip.ip_address)
    print meip.status
    print meip.image_id
    print meip.name
    print meip.private_ip_address

# <codecell>

dropo.ip_address

# <codecell>

dropo.name

# <codecell>

dropo

# <codecell>

droplis = []

# <codecell>

for dr in mydrop:
    print dr.ip_address
    droplis.append(dr.ip_address)
    droplis.append(dr.status)
    print dr.status
    droplis.append(dr.region_id)
    print dr.region_id
    droplis.append(dr.ssh_key_ids)
    droplis.append(dr.id)
    print dr.ssh_key_ids
    print dr.id
    print dr.image_id

# <codecell>

print droplis

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

my_droplets = manager.get_all_droplets()
for droplet in my_droplets:
    print droplet

# <codecell>

droplet.client_id

# <codecell>

myderp = manager.get_all_regions()

# <codecell>

print myderp

# <codecell>

myderp

# <codecell>

for derp in myderp:
    print derp
    droplis.append(derp.name)
    droplis.append(derp.id)
    print derp.name
    print derp.id

# <codecell>

print droplis

# <codecell>

dropserv = digitalocean.Droplet(client_id=digcli, api_key=apikey, name = 'uburub', region_id=5, image_id=3137635, size_id=66, backup_active=False)
dropserv.create()

# <codecell>

for event in events:
    event.load()
    #Once it shows 100, droplet is up and running
    print event.percentage

# <codecell>


