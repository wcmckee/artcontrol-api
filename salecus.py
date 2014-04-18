# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Challenge Description:
# 
# Our marketing department has just negotiated a deal with several local merchants that will allow us to offer exclusive discounts on various products to our top customers every day. The catch is that we can only offer each product to one customer and we may only offer one product to each customer.
# 
# Each day we will get the list of products that are eligible for these special discounts. We then have to decide which products to offer to which of our customers. Fortunately, our team of highly skilled statisticians has developed an amazing mathematical model for determining how likely a given customer is to buy an offered product by calculating what we call the "suitability score" (SS). The top-secret algorithm to calculate the SS between a customer and a product is this:
# 
# 1. If the number of letters in the product's name is even then the SS is the number of vowels (a, e, i, o, u, y) in the customer's name multiplied by 1.5.
# 2. If the number of letters in the product's name is odd then the SS is the number of consonants in the customer's name.
# 3. If the number of letters in the product's name shares any common factors (besides 1) with the number of letters in the customer's name then the SS is multiplied by 1.5.
# 
# Your task is to implement a program that assigns each customer a product to be offered in a way that maximizes the combined total SS across all of the chosen offers. Note that there may be a different number of products and customers. You may include code from external libraries as long as you cite the source.
# Input sample:
# 
# Your program should accept as its only argument a path to a file. Each line in this file is one test case. Each test case will be a comma delimited set of customer names followed by a semicolon and then a comma delimited set of product names. Assume the input file is ASCII encoded. For example (NOTE: The example below has 3 test cases):
# 
# Jack Abraham,John Evans,Ted Dziuba;iPad 2 - 4-pack,Girl Scouts Thin Mints,Nerf Crossbow
# 
# Jeffery Lebowski,Walter Sobchak,Theodore Donald Kerabatsos,Peter Gibbons,Michael Bolton,Samir Nagheenanajar;Half & Half,Colt M1911A1,16lb bowling ball,Red Swingline Stapler,Printer paper,Vibe Magazine Subscriptions - 40 pack
# 
# Jareau Wade,Rob Eroh,Mahmoud Abdelkader,Wenyi Cai,Justin Van Winkle,Gabriel Sinkin,Aaron Adelson;Batman No. 1,Football - Official Size,Bass Amplifying Headphones,Elephant food - 1024 lbs,Three Wolf One Moon T-shirt,Dom Perignon 2000 Vintage
# 
# Output sample:
# 
# For each line of input, print out the maximum total score to two decimal places. For the example input above, the output should look like this:
# 
# 21.00
# 83.50
# 71.25

# <codecell>



import math
import random

# <codecell>

nlist = []
maslist = []

# <codecell>

lowra = random.randint(0,5)
highra = random.randint(10,20)
maslist.append(lowra)
maslist.append(highra)
nlist.append(lowra)

# <codecell>

maslist

# <codecell>

def fib(n):
    a,b = lowra, highra
    while b < n:
        print b, 
        sab = a, b = b, a+b
        print sab
        nlist.append(sab)
        

# <codecell>

chfib = fib(lowra)

# <codecell>

print nlist

# <codecell>

snlist = nlist.count(')')

for sn in enumerate(nlist):
    print sn
    maslist.append(sn)

# <codecell>

print len(nlist)
maslist.append(len(nlist))

# <codecell>

print len('blahblahlbah')

# <codecell>

print maslist

# <codecell>

print snlist
print nlist

# <codecell>

for blehz in nlist:
    print blehz

# <codecell>


# <codecell>

fib(50)

# <codecell>

def fib2(n):
    result= []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b

# <codecell>

thefib = fib2(20000)

# <codecell>

pi = math.pi

# <codecell>

import sys
import os
import socket

# <codecell>

thehost = socket.gethostname()

# <codecell>

maslist.append(thehost)

# <codecell>

thehost

# <codecell>

import getpass

# <codecell>

maslist.append(theuser)

# <codecell>

theuser = getpass.getuser()

# <codecell>

print theuser

# <codecell>

upass = theuser + '@' + thehost

# <codecell>

print upass

# <codecell>

os.defpath

# <codecell>

maslist.append(upass)

# <codecell>

maslist.append(os.getresuid())

# <codecell>

os.curdir

# <codecell>

maslist.append(os.getppid())

# <codecell>

maslist.append(os.listdir('/home'))

# <codecell>

maslist.append(os.times())

# <codecell>

os.ctermid()

# <codecell>

from github import Github

# <codecell>

g = Github()

# <codecell>

gitlist = []

# <codecell>

def gitusrz(gitn):
    for repo in g.get_user(gitn).get_repos():
        print repo.name
        gitlist.append(repo.name)

# <codecell>

gitusrz('wcmckee')

# <codecell>

import random
import git

# <codecell>

gitlstint = len(gitlist)

# <codecell>

print gitlstint

# <codecell>

gitrepoz = random.randint(0, gitlstint)

# <codecell>

fgitrepoz = gitlist[gitrepoz]

# <codecell>


print fgitrepoz

# <codecell>

gitlist

# <codecell>

os.chdir('/home/drhealsgood/wcmckee/')

# <codecell>

for gitre in gitlist:
    print gitre

# <codecell>

git.Git().clone("https://github.com/wcmckee/" + takn)

# <codecell>

lisdir = os.listdir('/home/drhealsgood/wcmckee/')

# <codecell>

ls

# <codecell>

set(lisdir) & set(gitlist)

# <codecell>

takegit =(set(lisdir).intersection(gitlist))

# <codecell>

for takn in takegit:
    print takn
    #git.Git().clone("https://github.com/wcmckee/" + takn)

# <codecell>

for listd in lisdir:
    print listd

# <codecell>

os.environ

# <codecell>

def printinfo(name, timel):
   "This prints a passed info into this function"
   print "hostname: ", name;
   print "time left ", timel;
   return;

# <codecell>

def f(x):
    return x**pi

# <codecell>

print f(24)

# <codecell>

g = lambda x: x**pi

# <codecell>

blehg =  g(80)

# <codecell>

print blehg

# <codecell>

def makn(n): 
    return lambda x: x + n

# <codecell>

f = makn(4)
g = makn(20)

# <codecell>

print f(2)
print g(7)

# <codecell>

printinfo('william', 34)

# <codecell>


# <codecell>

import collections

# <codecell>

newfile = open('config', 'w')

# <codecell>

#cusname1 = 'figlet holley'

# <codecell>

datlist = []

# <codecell>

cusname = fgitrepoz
datlist.append(cusname)

# <codecell>

productname1 = 'figlufets food yu'

# <codecell>

productname = 'debian linux'
datlist.append(productname)

# <codecell>

set(datlist)

# <codecell>

cunum = 0
salelist = []

# <codecell>

chrinpro = len(productname)
datlist.append(chrinpro)

# <codecell>

#print chrinpro

# <codecell>

def chrinpa(letra):
    if (chrinpro % 2 == 0):
        print 'true'
    else:
        print 'false'

# <codecell>

chrinpa('blayyliuuiteylhertet')

# <codecell>

if (chrinpro % 2 == 0):
    #print 'true'
    letiname = ['a', 'e', 'i', 'o', 'u', 'y']
    multi = 1
else:
    #print 'false'
    letiname = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    multi = 1.5

# <codecell>

#print multi

# <codecell>

lempan = f(chrinpro), g(chrinpro)

# <codecell>

lempan

# <codecell>


# <codecell>

for extension in letiname:
    if extension in cusname:
        #print(extension, cunum +1)
        #salelist.append(extension)
        salelist.append(cunum +1)
        datlist.append(extension)
        #print saledict

# <codecell>

print datlist

# <codecell>

cusa = sum(salelist)
datlist.append(cusa)

# <codecell>

fincus = cusa * multi
datlist.append(fincus)

# <codecell>

#print fincus

# <codecell>

thenum = 0 

# <codecell>

#print salelist

# <codecell>

#for num in salelist:
#    print num

# <codecell>

litpro = list(productname)

# <codecell>

listcus = list(cusname)

# <codecell>

#set(litpro) & set(listcus)

# <codecell>

def numz(checkn):
    [i for i, j in zip(litpro, listcus) if i == j]
    return i + j
    

# <codecell>

numz('gbdgggr')

# <codecell>

numbsli = [i for i, j in zip(litpro, listcus) if i == j]

# <codecell>

datlist.append(numbsli)

# <codecell>

#numbsli

# <codecell>

chset = set(litpro).intersection(listcus)

# <codecell>

print chset

# <codecell>

for n in chset:
    print n
    datlist.append(n)

# <codecell>

print datlist

# <codecell>

procol = collections.Counter(litpro)

# <codecell>

cuscol = collections.Counter(listcus)

# <codecell>

#print procol
datlist.append(procol)
#print cuscol
datlist.append(cuscol)

# <codecell>

doctpro = dict(procol)

# <codecell>

dictcol = dict(cuscol)

# <codecell>

available = set(doctpro.items())
satchel = set(dictcol.items())


findif = available.difference(satchel)
datlist.append(findif)

# <codecell>

#print findif

# <codecell>

finval = dictcol.values()

# <codecell>

#print finval
datlist.append(finval)

# <codecell>

fint1 = [x for x in finval if x != 1]
#print fint1
datlist.append(fint1)

# <codecell>

if fint1:
    #print 'list has elements'
    fincus = fincus * 1.5
else:
    fincus = fincus
    

# <codecell>

finalcus = "%.2f" % fincus

# <codecell>

datlist.append(finalcus)

# <codecell>

print ('The score is:', finalcus)

# <codecell>

print finalcus

# <codecell>

print datlist[0]

# <codecell>

nums = finalcus
for i in range(2, 8):
    nums = filter(lambda x: x == i or x % i, nums)

# <codecell>


