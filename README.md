artcontrol-api
==============

artcontrol-api: a collection of ipython notebooks.

Focus is on web data. Code is Python. 
requests, beautifulsoup, subprocess, along with a bunch of 
other modules used.  

**Artcontrol**
The artcontrol notebook focuses on requests and json.
Downloading a JSON object and converting it to a python 
dict. 
The notebook is a mess and I need to clean it out to extract
useful information (and save it?). 

**AklMCam**
Convert xml file to json object. I'm using it here to get 
Auckland Web Cam data. Need to do more with json object. 

**dh**
dh notebook is an attempt to get dhcp.leases from a network
and analyze them. Feeds some example data but needs lots of 
work.

**pyssh**
This notebook focuses on digitalocean - linux servers 
(or droplet as do like to call them)!
It returns the users (login?) droplets.
Makes list with server name, ip, image id, and region id.
Saves as json object. File needs a cleanup.
Turns off all servers, make snapshot, turn back on. 
Create new server. 

**pywgit**
git and github modules are used to lookup user on github and
clone all repos. Need to add more features - started exploring 
organise on github.

**redTube**
uses redtube json object to get video/actor info.
Uses feed parser to get rss feed from pornhub.
Two lots of data. 
warning: this notebook is not safe for work.

**tpb**
quick look at the piratebay python module

**tlc**
The Learning Connexion.
beautifulsoup4 downloading and sorting of html elements.

