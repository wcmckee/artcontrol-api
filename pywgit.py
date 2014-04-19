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

# <codecell>

g = Github()

# <codecell>

gitlist = []

# <codecell>

for repo in g.get_user(theuser).get_repos():
    gitlist.append(repo.name)

# <codecell>

#gitlist

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

#print dlrepo

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


