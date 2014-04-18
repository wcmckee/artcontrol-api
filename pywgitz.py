# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 11:24:16 2014

@author: wcmckee
"""

from github import Github
import sys
import os
import socket
import getpass
import random
import git


g = Github()

gitlist = []

def gitusrz(gitn):
    for repo in g.get_user(gitn).get_repos():
        print repo.name
        gitlist.append(repo.name)


thehost = socket.gethostname()

theuser = getpass.getuser()

print theuser

upass = theuser + '@' + thehost

print upass

os.defpath

os.curdir

alusr = os.listdir("/home")


g = Github()

g = Github()

gitlist = []

def gitusrz(gitn):
    for repo in g.get_user(gitn).get_repos():
        #print repo.name
        gitlist.append(repo.name)


locu = len(alusr)
#print locu
thus = random.randint(0,locu)
#print thus
fusr = alusr[thus]
#print fusr
gitusrz(fusr)
gitlstint = len(gitlist)

#print gitlstint

gitrepoz = random.randint(0, gitlstint)

fgitrepoz = gitlist[gitrepoz]

#print fgitrepoz

#gitlist

urdir = '/home/' + theuser + '/github/'
#print urdir
#for gitre in gitlist:
#    print gitre
os.chdir(urdir)

for gi in gitlist:
    print gi
    git.Git().clone("https://github.com/wcmckee/" + gi)
giturl = ('https://github.com/' + 'wcmckee' + '/Documents/')
#print giturl
lisdir = os.listdir(urdir)
#print lisdir
tesgit = set(lisdir) & set(gitlist)

#print tesgit

takegit =(set(lisdir).intersection(gitlist))
#print takegit
#for takn in takegit:
   # print takn
    #git.Git().clone("https://github.com/wcmckee/" + takn)

def gitclone(repoa):
    git.Git().clone("https://github.com/wcmckee/" + repoa)
#for listd in 
    
