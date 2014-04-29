# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# pydigdrop

# <markdowncell>

# This Python script uses digitalocean services.  It gets the users server list - from the vps hosting company Digital Ocean. Their plans start as little as $5.00 and are charged by the hour. 

# <codecell>

import os
import json
import digitalocean

# <codecell>

digcli = ('a24a5636402aaf75d07b774d98591ea3')

# <codecell>

print digcli

# <codecell>

apikey = ('9898216d345df5b70ab943c5005c05df')

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

for meip in mydrop:
    print meip.ip_address
    print meip.status
    print meip.image_id

# <codecell>

dropo.ip_address

# <codecell>

dropo.name

# <codecell>

dropo

# <codecell>

droplis = []

# <codecell>

iplis = []

# <codecell>

dropdict = dict{}

# <codecell>

drstr = []

# <codecell>

for dr in mydrop:
    print dr.ip_address
    droplis.append(dr.name)
    droplis.append(dr.ip_address)
    iplis.append(dr.ip_address)
    droplis.append(dr.status)
    print dr.status
    droplis.append(dr.region_id)
    print dr.region_id
    droplis.append(dr.ssh_key_ids)
    droplis.append(dr.id)
    droplis.append(dr)
    print dr.name
    print dr.ssh_key_ids
    print dr.id
    print dr.image_id
    print dr
    drstr.append(dr)

# <codecell>

print droplis

# <codecell>

print drstr

# <codecell>

print iplis

# <codecell>

#!/usr/bin/python
 
# All SSH libraries for Python are junk (2011-10-13).
# Too low-level (libssh2), too buggy (paramiko), too complicated
# (both), too poor in features (no use of the agent, for instance)
 
# Here is the right solution today:
 
import subprocess
import sys
 
HOST= '74.50.51.32'
# Ports are handled in ~/.ssh/config since we use OpenSSH
COMMAND="uname -a"
 
ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
shell=False,
stdout=subprocess.PIPE,
stderr=subprocess.PIPE)
result = ssh.stdout.readlines()
if result == []:
    error = ssh.stderr.readlines()
    print >>sys.stderr, "ERROR: %s" % error
else:
    print result

# <codecell>

from crontab import CronTab

system_cron   = CronTab()
system_cron.new

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
    droplet.power_off()

# <codecell>

for droplet in my_droplets:
    print droplet
    droplet.power_on()

# <codecell>

for droplet in my_droplets:
    print droplet
    print droplet.name

# <codecell>

dropo.power_off()

# <codecell>

dropo.take_snapshot('deb')

# <codecell>

dropo.rebuild()

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

