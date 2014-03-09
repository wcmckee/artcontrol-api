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

cusname = 'williamcliffordmckeewww'

# <codecell>

productname = 'wwwalter whites: ble meth'

# <codecell>

chrinpro = len(productname)

# <codecell>

print chrinpro

# <codecell>

if (chrinpro % 2 == 0):
    print 'true'
else:
    print 'false'

# <codecell>

letiname = ['a', 'e', 'i', 'o', 'u', 'y']

# <codecell>

consoltlist = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

# <codecell>

print consoltlist

# <codecell>

print letiname

# <codecell>

import string

# <codecell>


string.lowercase

# <codecell>

thenum = 0 

# <codecell>

cunum = 0
salelist = []

# <codecell>

for extension in consoltlist:
    if extension in cusname:
        print(extension, cunum +1)
        #salelist.append(extension)
        salelist.append(cunum +1)
        #print saledict

# <codecell>

print salelist

# <codecell>

cusa = sum(salelist)

# <codecell>

fincus = cusa * 1.5

# <codecell>

print fincus

# <codecell>

for num in salelist:
    print num

# <codecell>

litpro = list(productname)

# <codecell>

listcus = list(cusname)

# <codecell>

set(litpro) & set(listcus)

# <codecell>

numbsli = [i for i, j in zip(litpro, listcus) if i == j]

# <codecell>

numbsli

# <codecell>

set(litpro).intersection(listcus)

# <codecell>

import collections

# <codecell>

procol = collections.Counter(litpro)

# <codecell>

cuscol = collections.Counter(listcus)

# <codecell>

print procol
print cuscol

# <codecell>

diff = set(procol.keys()) - set(cuscol.keys())

# <codecell>

print diff

# <codecell>

numkey = 0

# <codecell>

for key in cuscol.keys():
    if not key in procol:
        print (key, numkey + 1)

# <codecell>


# <codecell>

if chrinpro is even:
    print 'even'
else:
    print 'odd'

# <codecell>

dict((y, x) for x, y in t)
#{'a': 1, 'b': 2}

# <codecell>

{}

# <codecell>

if "x" in cusname:
    print "Yes!"
else:
    print 'no'

# <codecell>

for n in letiname:
    print n
    if n in cusname:
        print n
        print thenum + 1
        print cusname
    

# <codecell>


if "x" in dog:
    print "Yes!"

# <codecell>


