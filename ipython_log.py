# IPython log file

get_ipython().magic(u'logstart -t')
get_ipython().magic(u'pwd ')
get_ipython().system(u'ls -F --color ')
get_ipython().magic(u'cd Desktop/')
get_ipython().system(u'ls -F --color ')
get_ipython().magic(u'cd artcontrol-api/')
get_ipython().system(u'ls -F --color ')
get_ipython().magic(u'logstop')
get_ipython().magic(u'logstart -t')
# Fri, 18 Apr 2014 10:48:56
get_ipython().system(u'ls -F --color ')
# Fri, 18 Apr 2014 10:49:19
from github import Github

# Fri, 18 Apr 2014 10:49:23
g = Github()

# Fri, 18 Apr 2014 10:49:26
gitlist = []

# Fri, 18 Apr 2014 10:49:28
def gitusrz(gitn):
    for repo in g.get_user(gitn).get_repos():
        print repo.name
        gitlist.append(repo.name)


# Fri, 18 Apr 2014 10:49:49
import sys
import os
import socket

# Fri, 18 Apr 2014 10:50:19
thehost = socket.gethostname()

# Fri, 18 Apr 2014 10:50:20
maslist.append(thehost)

# Fri, 18 Apr 2014 10:50:30
thehost

# Fri, 18 Apr 2014 10:50:36
theuser = getpass.getuser()

# Fri, 18 Apr 2014 10:50:39
import getpass

# Fri, 18 Apr 2014 10:50:42
theuser = getpass.getuser()

# Fri, 18 Apr 2014 10:50:43
print theuser

# Fri, 18 Apr 2014 10:50:46
upass = theuser + '@' + thehost

# Fri, 18 Apr 2014 10:50:49
print upass

# Fri, 18 Apr 2014 10:50:53
os.defpath

# Fri, 18 Apr 2014 10:50:58
os.curdir

# Fri, 18 Apr 2014 10:51:02
maslist.append(os.listdir('/home'))

# Fri, 18 Apr 2014 10:51:46
alusr = os.listdir("/home")
# Fri, 18 Apr 2014 10:51:53
alusr
# Fri, 18 Apr 2014 10:52:23
from github import Github

# Fri, 18 Apr 2014 10:52:24
g = Github()

# Fri, 18 Apr 2014 10:52:27
g = Github()

# Fri, 18 Apr 2014 10:52:29
gitlist = []

# Fri, 18 Apr 2014 10:52:32
def gitusrz(gitn):
    for repo in g.get_user(gitn).get_repos():
        print repo.name
        gitlist.append(repo.name)


# Fri, 18 Apr 2014 10:52:45
import random
# Fri, 18 Apr 2014 10:53:16
locu = len(alusr)
# Fri, 18 Apr 2014 10:53:28
print locu
# Fri, 18 Apr 2014 10:54:10
thus = random.randint(0,locu)
# Fri, 18 Apr 2014 10:54:15
print thus
# Fri, 18 Apr 2014 10:54:47
fusr = alusr[thus]
# Fri, 18 Apr 2014 10:54:51
print fusr
# Fri, 18 Apr 2014 10:55:46
gitusrz(fusr)
# Fri, 18 Apr 2014 10:56:38
import git
# Fri, 18 Apr 2014 10:56:51
gitlstint = len(gitlist)

# Fri, 18 Apr 2014 10:56:54
print gitlstint

# Fri, 18 Apr 2014 10:56:57
gitrepoz = random.randint(0, gitlstint)

# Fri, 18 Apr 2014 10:57:01
fgitrepoz = gitlist[gitrepoz]

# Fri, 18 Apr 2014 10:57:04
print fgitrepoz

# Fri, 18 Apr 2014 10:57:13
gitlist

