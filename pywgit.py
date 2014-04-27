# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# pywgit

# <markdowncell>

# This is a python script to download repos from github
# It takes the login name (wcmckee in my case) and downloads the repos of github user (the system login name). It downloads it to the home dir. 
# The program checks if you have local folders that are also on github. It will skip them from downloading from github. 

# <codecell>

from github import Github
import os
import getpass
import git

# <codecell>

theuser = getpass.getuser()

# <markdowncell>

# muliti support for user names - cycle through a list, user input, and get username from login. 

# <codecell>

usergen = ['ipython', 'wcmckee', 'drhealsgood', 'hamipy']

# <codecell>

userinput = raw_input('github username: ')

# <codecell>

for us in usergen:d
    print us

# <codecell>

g = Github()

# <codecell>

import requests

# <codecell>

highgit = requests.get('https://infoconnect1.highwayinfo.govt.nz/ic/jbi/TrafficCameras/REST/FeedService/', auth=('williammckee', 'J3e6t8q5y2'))

# <codecell>

from requests.auth import HTTPBasicAuth

theres = requests.get('https://infoconnect1.highwayinfo.govt.nz/ic/jbi/TrafficCameras/REST/FeedService/', auth=HTTPBasicAuth('williammckee', 'J3e6t8q5y2'))

# <codecell>

from requests.auth import HTTPDigestAuth
url = 'https://infoconnect1.highwayinfo.govt.nz/ic/jbi/TrafficCameras/REST/FeedService/'
workt = requests.get(url, auth=HTTPDigestAuth('williammckee', 'J3e6t8q5y2'))

# <codecell>

workt.text

# <codecell>

theres.text

# <codecell>

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }
headers = { 'User-Agent' : user_agent }

# <codecell>

highgit.text

# <codecell>

%%bash 
curl -u wcmckee:J3e6t8q5y2 https://infoconnect1.highwayinfo.govt.nz/ic/jbi/TrafficCameras/REST/FeedService/

# <codecell>

%%bash
curl -k -H "username: williammckee" -H "password: J3e6t8q5y2" -o linkz https://infoconnect1.highwayinfo.govt.nz/ic/jbi/TrafficCameras/REST/FeedService/


# <codecell>

opcon = open('linkz', 'r')

# <codecell>

opcon.read()

# <codecell>

gitlist = []

# <codecell>

searchpy = g.search_repositories(theuser)

# <codecell>

typy = g.search_users(theuser)

# <codecell>

blehgit = g.search_repositories('reddit')

# <rawcell>

# oh man, what have i got happening here. This started with a way of downloading repos in bulk from a user and ive started to bring in more github module. Here I am searching repositories on github for reddit. 
# What things could i get it to search for?
# - list
# - search your repos on global to find similar named ones.
# - 

# <codecell>

repolis = []

# <codecell>

print repolis

# <codecell>

for bleh in blehgit:
    repolis.append(bleh)
    #print bleh.full_name

# <markdowncell>

# I'm having a problem with auth! Need to get myself loged in here. 
# Needs better security for logging in. - SSH Key? - hash the password 

# <markdowncell>

# What to do with all the output i am geting from searching. appending it into a list. maybe turn to dict? Make a rest feed? 

# <codecell>

for blzgit in blehgit:
    print blzgit.name

# <codecell>

print blehgit.totalCount

# <codecell>

print typy.totalCount

# <codecell>

print typy

# <codecell>

gepy = g.get_organization('brobeur')

# <codecell>

gepy.email

# <codecell>

gepy.blog

# <codecell>

gepy.url

# <codecell>

gepy.created_at

# <codecell>

brorepo.totalCount()

# <codecell>

gepy.public_repos

# <codecell>

gepic = gepy.avatar_url

# <codecell>

gepic

# <codecell>

gepy.type

# <codecell>

from IPython.core.display import Image 
Image(filename='test.png') 

# <codecell>

gepy.raw_data

# <codecell>

print alrepo

# <codecell>

brorepo = gepy.get_repo('linux')

# <codecell>

brorepo.size

# <codecell>

gepy.get_public_members()

# <codecell>


# <codecell>

gepy.location

# <codecell>

searchbleh = g.get_api_status()

# <codecell>

print searchbleh.status
print searchbleh.last_modified

# <codecell>

searchpy.totalCount

# <codecell>

import geopy

# <codecell>

koapi = ('d2b321e45a2041f19551a3f3b223fce0')

# <codecell>

geoloc = geopy.geocoders.GoogleV3()

# <codecell>

address = geoloc.geocode('8 Margaret Street Levin')

# <codecell>

print address

# <codecell>

address.point

# <codecell>

for se in searchpy:
    print se.url

# <codecell>

for repo in g.get_user(theuser).get_repos():
    gitlist.append(repo.name)

# <codecell>

os.mkdir('/home/wcmckee/github')

# <codecell>

os.chdir('/home/' + theuser + '/github')

# <codecell>

lisdir = os.listdir('/home/wcmckee/github')
curlist = []
for ls in lisdir:
    #print ls
    curlist.append(ls)

# <codecell>

dlrepo = list(set(gitlist) - set(curlist))

# <codecell>

print dlrepo

# <codecell>


# <codecell>

'''
for gi in gitlist:
    #print gi
    #git.Git().clone("https://github.com/" + theuser + "/" + dlrepo)
    print ("Downloading: " + theuser + "/" + dlrepo)



'''

# <codecell>

from clint.textui import colored

# <codecell>

for gitbl in dlrepo:
        #print ('Downloading - ' + theuser + " - "  + gitbl)
        print (colored.red('Downloading - ' + theuser + " - "  + gitbl))
        git.Git().clone("https://github.com/" + theuser + "/" + gitbl)

# <codecell>


