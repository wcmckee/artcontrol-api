# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=2>

# pywsshx

# <markdowncell>

# this is a python script to expand features on Digital Ocean.
# since i have been busy with github clone repo python script i have became interested in deployment of servers. I hope some of the code here is useful for you.

# <markdowncell>

# TODO: 
#     - sort out login. 
#     - make functions/test
#     - merge with other scripts. eg github.
#     - make dict better
# - config file. - specify
# - terminal -commands
# - 

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


# <codecell>

print apikey

# <codecell>

manager = digitalocean.Manager(client_id = digcli, api_key = apikey)

# <codecell>

mydrop = manager.get_all_droplets()

# <codecell>

myserv = manager.get_all_images()

# <codecell>

mybleh = manager.get_all_regions()

# <codecell>

mybez = manager.get_global_images()

# <codecell>

myhez = manager.get_all_sizes()

# <codecell>

hezdict = {}

# <codecell>

print hezdict

# <codecell>

for hez in myhez:
    print hez.name
    hezdict.update({'size': hez.name, 'cost hour': hez.cost_per_hour,
                    'cost month': hez.cost_per_month, 'cpu': hez.cpu})
    print hez.cost_per_hour
    print hez.cost_per_month
    print hez.cpu
    print hez.disk
    print hez.id
    print hez.memory

# <codecell>

for ekk in mybez:
    print ekk.name

# <codecell>

for bleh in mybleh:
    print bleh.name
    print bleh.id

# <codecell>

for imgz in myserv:
    print imgz.name
    print imgz.id
    print imgz.distribution

# <codecell>

myserv

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

import subprocess

# <codecell>

conser = subprocess.check_output('ls')

# <codecell>

process = subprocess.Popen("ssh wcmckee@" + ipz + " ls", shell=True,
    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output,stderr = process.communicate()
status = process.poll()
print output

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

from dop.client import Client

client = Client(digcli, apikey)

# Print regions.
regions = client.regions()
for region in regions:
    print(region.to_json())

# Print sizes.
sizes = client.sizes()
for size in sizes:
    print(size.to_json())

# Print public global images.
images = client.images()
for image in images:
    print(image.to_json())

# Print your private images.
#images = client.images(filter='my_images')
#for image in images:
#    print(image.to_json())

# Create a droplet
conf = {
    'name': 'test',
    'size': {'size_slug': '512MB'},
    'image': {'image_slug': 'ubuntu-13-04-x64'},
    'region': {'region_slug': 'nyc1'},
}

# <codecell>


