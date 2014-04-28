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

for us in usergen:
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

data= opcon.read()

# <codecell>

import xmltodict

# <codecell>

thexml = ('<?xml version=\'1.0\' encoding=\'UTF-8\'?><tns:getCamerasResponse xmlns:rem="http://remote.service.callcenter.nzta.govt.nz" xmlns:tns="https://infoconnect.highwayinfo.govt.nz/schemas/camera" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><tns:camera><tns:id>130</tns:id><tns:name>SH16 1 Bond St</tns:name><tns:description>Bond St looking east</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/130.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/130</tns:viewUrl><tns:mapx>142</tns:mapx><tns:mapy>229</tns:mapy><tns:congestionLocation><tns:name>St Lukes Rd - Newton Rd</tns:name><tns:direction>Eastbound</tns:direction><tns:congestion>Free Flow</tns:congestion></tns:congestionLocation><tns:congestionLocation><tns:name>Newton Rd - St Lukes Rd</tns:name><tns:direction>Westbound</tns:direction><tns:congestion>Free Flow</tns:congestion></tns:congestionLocation></tns:camera><tns:camera><tns:id>140</tns:id><tns:name>SH16 2 Gt North Rd</tns:name><tns:description>Gt North Road looking west</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/140.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/140</tns:viewUrl><tns:mapx>113</tns:mapx><tns:mapy>232</tns:mapy><tns:congestionLocation><tns:name>Rosebank Rd - Great Nth Rd Waterview</tns:name><tns:direction>Eastbound</tns:direction><tns:congestion>Free Flow</tns:congestion></tns:congestionLocation><tns:congestionLocation><tns:name>Great Nth Rd Waterview - Rosebank Rd</tns:name><tns:direction>Westbound</tns:direction><tns:congestion>Free Flow</tns:congestion></tns:congestionLocation></tns:camera><tns:camera><tns:id>150</tns:id><tns:name>SH16 3 Te Atatu Rd</tns:name><tns:description>Te Atatu Road looking east</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/150.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/150</tns:viewUrl><tns:mapx>70</tns:mapx><tns:mapy>216</tns:mapy><tns:congestionLocation><tns:name>Te Atatu Rd - Rosebank Rd</tns:name><tns:direction>Eastbound</tns:direction><tns:congestion>Free Flow</tns:congestion></tns:congestionLocation><tns:congestionLocation><tns:name>Rosebank Rd - Te Atatu Rd</tns:name><tns:direction>Westbound</tns:direction><tns:congestion>Free Flow</tns:congestion></tns:congestionLocation></tns:camera><tns:camera><tns:id>160</tns:id><tns:name>SH16 4 Lincoln Rd E</tns:name><tns:description>Lincoln Rd  looking west</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/160.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/160</tns:viewUrl><tns:mapx>52</tns:mapx><tns:mapy>207</tns:mapy><tns:congestionLocation><tns:name>Te Atatu Rd - Lincoln Rd</tns:name><tns:direction>Westbound</tns:direction><tns:congestion>Free Flow</tns:congestion></tns:congestionLocation><tns:congestionLocation><tns:name>Lincoln Rd - Te Atatu Rd</tns:name><tns:direction>Eastbound</tns:direction><tns:congestion>Free Flow</tns:congestion></tns:congestionLocation></tns:camera><tns:camera><tns:id>170</tns:id><tns:name>SH16 5 Lincoln Rd W</tns:name><tns:description>Lincoln Rd looking east</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/170.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/170</tns:viewUrl><tns:mapx>35</tns:mapx><tns:mapy>207</tns:mapy><tns:congestionLocation><tns:name>Lincoln Rd - Royal Rd</tns:name><tns:direction>Westbound</tns:direction><tns:congestion>Free Flow</tns:congestion></tns:congestionLocation><tns:congestionLocation><tns:name>Royal Rd - Lincoln Rd</tns:name><tns:direction>Eastbound</tns:direction><tns:congestion>Free Flow</tns:congestion></tns:congestionLocation></tns:camera><tns:camera><tns:id>270</tns:id><tns:name>SH16 6 Hobsonville W</tns:name><tns:description>Hobsonville looking West towards Kumeu</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/270.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/270</tns:viewUrl><tns:mapx>0</tns:mapx><tns:mapy>0</tns:mapy></tns:camera><tns:camera><tns:id>271</tns:id><tns:name>SH16 7 Hobsonville E</tns:name><tns:description>Hobsonville Road looking East</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/271.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/271</tns:viewUrl><tns:mapx>0</tns:mapx><tns:mapy>0</tns:mapy></tns:camera><tns:camera><tns:id>221</tns:id><tns:name>SH18 Trig Rd</tns:name><tns:description>Trig Rd looking west</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/221.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/221</tns:viewUrl><tns:mapx>0</tns:mapx><tns:mapy>0</tns:mapy></tns:camera><tns:camera><tns:id>222</tns:id><tns:name>SH18 Waiahora Creek</tns:name><tns:description>Upper harbour motorway looking west</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/222.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/222</tns:viewUrl><tns:mapx>0</tns:mapx><tns:mapy>0</tns:mapy></tns:camera><tns:camera><tns:id>223</tns:id><tns:name>SH18 Brigham Creek</tns:name><tns:description>Upper harbour motorway looking East</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/223.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/223</tns:viewUrl><tns:mapx>0</tns:mapx><tns:mapy>0</tns:mapy></tns:camera><tns:camera><tns:id>224</tns:id><tns:name>SH18 Sinton Rd</tns:name><tns:description>Upper harbour motorway looking west</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/224.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/224</tns:viewUrl><tns:mapx>0</tns:mapx><tns:mapy>0</tns:mapy></tns:camera><tns:camera><tns:id>225</tns:id><tns:name>SH18 Squadron Dr</tns:name><tns:description>Upper harbour motorway looking east</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/225.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/225</tns:viewUrl><tns:mapx>0</tns:mapx><tns:mapy>0</tns:mapy></tns:camera><tns:camera><tns:id>171</tns:id><tns:name>SH18 6 Tauhinu BRG</tns:name><tns:description>Tauhinu bridge looking east</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/171.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/171</tns:viewUrl><tns:mapx>60</tns:mapx><tns:mapy>207</tns:mapy></tns:camera><tns:camera><tns:id>172</tns:id><tns:name>SH18 7 Albany HWY</tns:name><tns:description>Albany Highway Looking East</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/172.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/172</tns:viewUrl><tns:mapx>35</tns:mapx><tns:mapy>207</tns:mapy></tns:camera><tns:camera><tns:id>173</tns:id><tns:name>SH18 8 Tauhinu East</tns:name><tns:description>Tauhinu East Looking East</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/173.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/173</tns:viewUrl><tns:mapx>35</tns:mapx><tns:mapy>207</tns:mapy></tns:camera><tns:camera><tns:id>174</tns:id><tns:name>SH18 9 Paul Matthews</tns:name><tns:description>Paul matthews looking east</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/174.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/174</tns:viewUrl><tns:mapx>35</tns:mapx><tns:mapy>207</tns:mapy></tns:camera><tns:camera><tns:id>175</tns:id><tns:name>SH18 10 Greenhithe</tns:name><tns:description>Greenhithe Rd looking east</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/175.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/175</tns:viewUrl><tns:mapx>35</tns:mapx><tns:mapy>207</tns:mapy></tns:camera><tns:camera><tns:id>176</tns:id><tns:name>SH18 11 George Deane</tns:name><tns:description>George deane looking east</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/176.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/176</tns:viewUrl><tns:mapx>35</tns:mapx><tns:mapy>207</tns:mapy></tns:camera><tns:camera><tns:id>177</tns:id><tns:name>SH18 12 Upper Hbr CW</tns:name><tns:description>Upper harbour looking east</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/177.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/177</tns:viewUrl><tns:mapx>35</tns:mapx><tns:mapy>207</tns:mapy></tns:camera><tns:camera><tns:id>178</tns:id><tns:name>SH18 13 Wicklam Lane</tns:name><tns:description>Wicklam Lane looking west</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/178.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/178</tns:viewUrl><tns:mapx>35</tns:mapx><tns:mapy>207</tns:mapy></tns:camera><tns:camera><tns:id>10</tns:id><tns:name>SH1 1 Greville Rd</tns:name><tns:description>Greville road looking south</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/10.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/10</tns:viewUrl><tns:mapx>125</tns:mapx><tns:mapy>71</tns:mapy><tns:congestionLocation><tns:name>Upper Harb Hwy - Oteha Valley Rd</tns:name><tns:direction>Northbound</tns:direction><tns:congestion>Free Flow</tns:congestion></tns:congestionLocation><tns:congestionLocation><tns:name>Oteha Valley Rd - Upper Harb Hwy</tns:name><tns:direction>Southbound</tns:direction><tns:congestion>Free Flow</tns:congestion></tns:congestionLocation></tns:camera><tns:camera><tns:id>20</tns:id><tns:name>SH1 2 Tristram Ave</tns:name><tns:description>Tristram Avenue looking south</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/20.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/20</tns:viewUrl><tns:mapx>148</tns:mapx><tns:mapy>118</tns:mapy><tns:congestionLocation><tns:name>Tristram Ave - Esmonde Rd</tns:name><tns:direction>Southbound</tns:direction><tns:congestion>Free Flow</tns:congestion></tns:congestionLocation><tns:congestionLocation><tns:name>Esmonde Rd - Tristram Ave</tns:name><tns:direction>Northbound</tns:direction><tns:congestion>Free Flow</tns:congestion></tns:congestionLocation></tns:camera><tns:camera><tns:id>30</tns:id><tns:name>SH1 3 Northcote Rd</tns:name><tns:description>Northcote Rd looking north</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/30.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/30</tns:viewUrl><tns:mapx>156</tns:mapx><tns:mapy>141</tns:mapy><tns:congestionLocation><tns:name>Tristram Ave - Esmonde Rd</tns:name><tns:direction>Southbound</tns:direction><tns:congestion>Free Flow</tns:congestion></tns:congestionLocation><tns:congestionLocation><tns:name>Esmonde Rd - Tristram Ave</tns:name><tns:direction>Northbound</tns:direction><tns:congestion>Free Flow</tns:congestion></tns:congestionLocation></tns:camera><tns:camera><tns:id>40</tns:id><tns:name>SH1 4 Esmonde Rd</tns:name><tns:description>Esmonde Rd looking south</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/40.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/40</tns:viewUrl><tns:mapx>178</tns:mapx><tns:mapy>146</tns:mapy><tns:congestionLocation><tns:name>Esmonde Rd - Onewa</tns:name><tns:direction>Southbound</tns:direction><tns:congestion>Free Flow</tns:congestion></tns:congestionLocation><tns:congestionLocation><tns:name>Stafford Rd - Esmonde Rd</tns:name><tns:direction>Northbound</tns:direction><tns:congestion>Free Flow</tns:congestion></tns:congestionLocation></tns:camera><tns:camera><tns:id>50</tns:id><tns:name>SH1 5 Onewa Rd</tns:name><tns:description>Onewa Rd looking south</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/50.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/50</tns:viewUrl><tns:mapx>157</tns:mapx><tns:mapy>162</tns:mapy><tns:congestionLocation><tns:name>Harbour Bridge</tns:name><tns:direction>Southbound</tns:direction><tns:congestion>Free Flow</tns:congestion></tns:congestionLocation><tns:congestionLocation><tns:name>Stafford Rd - Esmonde Rd</tns:name><tns:direction>Northbound</tns:direction><tns:congestion>Free Flow</tns:congestion></tns:congestionLocation></tns:camera><tns:camera><tns:id>215</tns:id><tns:name>SH1 Alpurt Web cam</tns:name><tns:description>Johnstone hill tunnels looking south</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/215.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/215</tns:viewUrl><tns:mapx>0</tns:mapx><tns:mapy>0</tns:mapy></tns:camera><tns:camera><tns:id>212</tns:id><tns:name>SH1 17 Goodwood</tns:name><tns:description>Goodwood heights looking south</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/212.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/212</tns:viewUrl><tns:mapx>0</tns:mapx><tns:mapy>0</tns:mapy></tns:camera><tns:camera><tns:id>214</tns:id><tns:name>SH1 18 Rainbows End</tns:name><tns:description>Rainbows End looking north at SH1 and SH20 link</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/214.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/214</tns:viewUrl><tns:mapx>0</tns:mapx><tns:mapy>0</tns:mapy></tns:camera><tns:camera><tns:id>60</tns:id><tns:name>SH1 1 CMJ</tns:name><tns:description>Central motorway junction looking south at the link between state highways 1 and 16</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/60.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/60</tns:viewUrl><tns:mapx>162</tns:mapx><tns:mapy>217</tns:mapy><tns:congestionLocation><tns:name>Nelson St - Gillies Ave</tns:name><tns:direction>Southbound</tns:direction><tns:congestion>Free Flow</tns:congestion></tns:congestionLocation></tns:camera><tns:camera><tns:id>70</tns:id><tns:name>SH1 2 Market Rd</tns:name><tns:description>Southern motorway at newmarket looking south towards the Market  Rd overbridge</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/70.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/70</tns:viewUrl><tns:mapx>183</tns:mapx><tns:mapy>241</tns:mapy><tns:congestionLocation><tns:name>Gillies Ave - Greenlane</tns:name><tns:direction>Southbound</tns:direction><tns:congestion>Free Flow</tns:congestion></tns:congestionLocation><tns:congestionLocation><tns:name>Greenlane - Gillies Ave</tns:name><tns:direction>Northbound</tns:direction><tns:congestion>Free Flow</tns:congestion></tns:congestionLocation></tns:camera><tns:camera><tns:id>80</tns:id><tns:name>SH1 3 Greenlane Rd</tns:name><tns:description>Greenlane Rd looking north</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/80.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/80</tns:viewUrl><tns:mapx>198</tns:mapx><tns:mapy>262</tns:mapy><tns:congestionLocation><tns:name>Gillies Ave - Greenlane</tns:name><tns:direction>Southbound</tns:direction><tns:congestion>Free Flow</tns:congestion></tns:congestionLocation><tns:congestionLocation><tns:name>Greenlane - Gillies Ave</tns:name><tns:direction>Northbound</tns:direction><tns:congestion>Free Flow</tns:congestion></tns:congestionLocation></tns:camera><tns:camera><tns:id>90</tns:id><tns:name>SH1 4 SE Highway</tns:name><tns:description>South eastern highway looking south</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/90.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/90</tns:viewUrl><tns:mapx>219</tns:mapx><tns:mapy>278</tns:mapy><tns:congestionLocation><tns:name>Mt Wellington Hway - SE Highway</tns:name><tns:direction>Northbound</tns:direction><tns:congestion>Free Flow</tns:congestion></tns:congestionLocation><tns:congestionLocation><tns:name>SE Highway - Mt Wellington Hway</tns:name><tns:direction>Southbound</tns:direction><tns:congestion>Moderate</tns:congestion></tns:congestionLocation></tns:camera><tns:camera><tns:id>100</tns:id><tns:name>SH1 5 Redoubt Rd</tns:name><tns:description>Redoubt Rd looking north</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/100.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/100</tns:viewUrl><tns:mapx>254</tns:mapx><tns:mapy>341</tns:mapy><tns:congestionLocation><tns:name>Redoubt Rd - Hill Rd</tns:name><tns:direction>Southbound</tns:direction><tns:congestion>Free Flow</tns:congestion></tns:congestionLocation><tns:congestionLocation><tns:name>Hill Rd - Redoubt Rd</tns:name><tns:direction>Northbound</tns:direction><tns:congestion>Free Flow</tns:congestion></tns:congestionLocation></tns:camera><tns:camera><tns:id>110</tns:id><tns:name>SH1 6 Bairds Rd</tns:name><tns:description>Bairds Rd looking north</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/110.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/110</tns:viewUrl><tns:mapx>275</tns:mapx><tns:mapy>383</tns:mapy><tns:congestionLocation><tns:name>East Tamaki Rd - Princes St</tns:name><tns:direction>Northbound</tns:direction><tns:congestion>Free Flow</tns:congestion></tns:congestionLocation><tns:congestionLocation><tns:name>Princes St - East Tamaki Rd</tns:name><tns:direction>Southbound</tns:direction><tns:congestion>Free Flow</tns:congestion></tns:congestionLocation></tns:camera><tns:camera><tns:id>120</tns:id><tns:name>SH1 7 Alfriston Rd</tns:name><tns:description>Alfriston Rd looking north</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/120.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/120</tns:viewUrl><tns:mapx>291</tns:mapx><tns:mapy>411</tns:mapy><tns:congestionLocation><tns:name>Takanini - Hill Rd</tns:name><tns:direction>Northbound</tns:direction><tns:congestion>Free Flow</tns:congestion></tns:congestionLocation><tns:congestionLocation><tns:name>Hill Rd - Takanini</tns:name><tns:direction>Southbound</tns:direction><tns:congestion>Free Flow</tns:congestion></tns:congestionLocation></tns:camera><tns:camera><tns:id>121</tns:id><tns:name>SH1 8 Takanini</tns:name><tns:description>Takanini looking south</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/121.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/121</tns:viewUrl><tns:mapx>290</tns:mapx><tns:mapy>380</tns:mapy></tns:camera><tns:camera><tns:id>122</tns:id><tns:name>SH1 9 Walter Streven</tns:name><tns:description>Walter-Strevens Drive looking south</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/122.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/122</tns:viewUrl><tns:mapx>285</tns:mapx><tns:mapy>400</tns:mapy></tns:camera><tns:camera><tns:id>123</tns:id><tns:name>SH1 10 Pahurehure</tns:name><tns:description>Pahurehure looking south</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/123.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/123</tns:viewUrl><tns:mapx>265</tns:mapx><tns:mapy>410</tns:mapy></tns:camera><tns:camera><tns:id>124</tns:id><tns:name>SH1 11 Rushgreen Ave</tns:name><tns:description>Rushgreen Ave looking south</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/124.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/124</tns:viewUrl><tns:mapx>285</tns:mapx><tns:mapy>420</tns:mapy></tns:camera><tns:camera><tns:id>125</tns:id><tns:name>SH1 12 Park Estate</tns:name><tns:description>Park estate looking south</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/125.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/125</tns:viewUrl><tns:mapx>300</tns:mapx><tns:mapy>430</tns:mapy></tns:camera><tns:camera><tns:id>126</tns:id><tns:name>SH1 13 Slippery Crk</tns:name><tns:description>Slippery Creek looking  south</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/126.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/126</tns:viewUrl><tns:mapx>286</tns:mapx><tns:mapy>445</tns:mapy></tns:camera><tns:camera><tns:id>274</tns:id><tns:name>SH20A Montgomerie Rd</tns:name><tns:description>Montgomerie Rd looking east</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/274.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/274</tns:viewUrl><tns:mapx>0</tns:mapx><tns:mapy>0</tns:mapy></tns:camera><tns:camera><tns:id>275</tns:id><tns:name>SH20A Kirkbride Road</tns:name><tns:description>Kirkbride Rd looking east</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/275.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/275</tns:viewUrl><tns:mapx>0</tns:mapx><tns:mapy>0</tns:mapy></tns:camera><tns:camera><tns:id>276</tns:id><tns:name>SH20A Bader Drive</tns:name><tns:description>Bader Drive looking east</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/276.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/276</tns:viewUrl><tns:mapx>0</tns:mapx><tns:mapy>0</tns:mapy></tns:camera><tns:camera><tns:id>272</tns:id><tns:name>SH20B Prices Road</tns:name><tns:description>Prices Rd looking east</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/272.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/272</tns:viewUrl><tns:mapx>0</tns:mapx><tns:mapy>0</tns:mapy></tns:camera><tns:camera><tns:id>273</tns:id><tns:name>SH20B Waokauri Creek</tns:name><tns:description>Waokauri Creek looking west</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/273.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/273</tns:viewUrl><tns:mapx>0</tns:mapx><tns:mapy>0</tns:mapy></tns:camera><tns:camera><tns:id>190</tns:id><tns:name>SH20 1 Queenstown Rd</tns:name><tns:description>Queenstown Rd looking south</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/190.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/190</tns:viewUrl><tns:mapx>35</tns:mapx><tns:mapy>207</tns:mapy></tns:camera><tns:camera><tns:id>191</tns:id><tns:name>SH20 2 Hillsborough</tns:name><tns:description>Hillsborough Rd looking south</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/191.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/191</tns:viewUrl><tns:mapx>35</tns:mapx><tns:mapy>207</tns:mapy></tns:camera><tns:camera><tns:id>192</tns:id><tns:name>SH20 3 Melrose</tns:name><tns:description>Melrose looking south</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/192.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/192</tns:viewUrl><tns:mapx>35</tns:mapx><tns:mapy>207</tns:mapy></tns:camera><tns:camera><tns:id>193</tns:id><tns:name>SH20 4 Dominion Rd</tns:name><tns:description>Dominion Rd looking south</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/193.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/193</tns:viewUrl><tns:mapx>35</tns:mapx><tns:mapy>207</tns:mapy></tns:camera><tns:camera><tns:id>194</tns:id><tns:name>SH20 5 Sandringham</tns:name><tns:description>Sandringham looking South</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/194.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/194</tns:viewUrl><tns:mapx>35</tns:mapx><tns:mapy>207</tns:mapy></tns:camera><tns:camera><tns:id>201</tns:id><tns:name>SH20 6 Gloucester Pk</tns:name><tns:description>Gloucester Park looking north</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/201.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/201</tns:viewUrl><tns:mapx>0</tns:mapx><tns:mapy>0</tns:mapy></tns:camera><tns:camera><tns:id>202</tns:id><tns:name>SH20 7 Onehunga</tns:name><tns:description>Onehunga wharf looking north</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/202.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/202</tns:viewUrl><tns:mapx>0</tns:mapx><tns:mapy>0</tns:mapy></tns:camera><tns:camera><tns:id>203</tns:id><tns:name>SH20 8 Rimu Rd</tns:name><tns:description>Rimu Rd looking north</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/203.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/203</tns:viewUrl><tns:mapx>0</tns:mapx><tns:mapy>0</tns:mapy></tns:camera><tns:camera><tns:id>204</tns:id><tns:name>SH20 9 Crawford Ave</tns:name><tns:description>Crawford Ave looking north</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/204.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/204</tns:viewUrl><tns:mapx>0</tns:mapx><tns:mapy>0</tns:mapy></tns:camera><tns:camera><tns:id>205</tns:id><tns:name>SH20 Coronation Rd</tns:name><tns:description>Coronation Rd looking east</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/205.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/205</tns:viewUrl><tns:mapx>0</tns:mapx><tns:mapy>0</tns:mapy></tns:camera><tns:camera><tns:id>206</tns:id><tns:name>SH20 11 Puhinui Rd</tns:name><tns:description>Puhinui road interchange looking south</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/206.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/206</tns:viewUrl><tns:mapx>0</tns:mapx><tns:mapy>0</tns:mapy></tns:camera><tns:camera><tns:id>207</tns:id><tns:name>SH20 12 Nesdale Road</tns:name><tns:description>Nesdale Rd looking east</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/207.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/207</tns:viewUrl><tns:mapx>0</tns:mapx><tns:mapy>0</tns:mapy></tns:camera><tns:camera><tns:id>208</tns:id><tns:name>SH20 13 Plunket Ave</tns:name><tns:description>Plunket Ave looking south</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/208.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/208</tns:viewUrl><tns:mapx>0</tns:mapx><tns:mapy>0</tns:mapy></tns:camera><tns:camera><tns:id>209</tns:id><tns:name>SH20 14 Lambie Drive</tns:name><tns:description>Lambie Drive looking south</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/209.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/209</tns:viewUrl><tns:mapx>0</tns:mapx><tns:mapy>0</tns:mapy></tns:camera><tns:camera><tns:id>210</tns:id><tns:name>SH20 15 Barrowcliffe</tns:name><tns:description>Barrowcliffe Place looking west</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/210.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/210</tns:viewUrl><tns:mapx>0</tns:mapx><tns:mapy>0</tns:mapy></tns:camera><tns:camera><tns:id>211</tns:id><tns:name>SH20 16 Great South</tns:name><tns:description>Great South Rd Looking westbound</tns:description><tns:offline>false</tns:offline><tns:underMaintenance>false</tns:underMaintenance><tns:imageUrl>http://www.trafficnz.info/camera/211.jpg</tns:imageUrl><tns:viewUrl>http://www.trafficnz.info/camera/view/211</tns:viewUrl><tns:mapx>0</tns:mapx><tns:mapy>0</tns:mapy></tns:camera></tns:getCamerasResponse>')

# <codecell>

datadict = xmltodict.parse(thexml)

# <codecell>

dakey = datadict.keys

# <codecell>

dalist = []

# <codecell>

dalist

# <codecell>

import json

#write the dictionary to a file
outfile = open('linkz', 'w')
json.dump(datadict, outfile)

#read the data back in
with open('linkz') as infile:
    newDictionary = json.load(infile)

# <codecell>

print key

# <codecell>

import json

# <codecell>

dicttojson = json.dumps(newDictionary)

# <codecell>

newDictionary

# <codecell>

newdicli = []

# <codecell>

newDictionary.items

# <codecell>

len(newDictionary)

# <codecell>

althere = newDictionary[u'tns:getCamerasResponse']

# <codecell>

len(althere)

# <codecell>

print 'hello world'

# <codecell>

althere.keys()

# <codecell>

bthere = althere[u'tns:camera']

# <codecell>

print len(bthere)

# <codecell>

bthere.

# <codecell>

print bthere

# <codecell>

nthere = blthere[1]

# <codecell>

print blthere

# <codecell>

blthere.keys()

# <codecell>

for nth in nthere:
    print nthere[nth]

# <codecell>

nthere[u'tns:id']

# <codecell>

althere = campos[u'tns:camera']

# <codecell>

print althere()

# <codecell>

campos = newDictionary[u'tns:getCamerasResponse']

# <codecell>

campos.items

# <codecell>

print 'hello world'

# <codecell>

for key, items in newDictionary.iteritems():
    print key, items
    newdicli.append(items)

# <codecell>

newDictionary.values()

# <codecell>

for value in datadict.itervalues():
    print value
    dalist.append(value)
    

# <codecell>

dakey.im_self

# <codecell>

#opcon.read()

# <codecell>

print hamxml

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


