# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

# Taking off from where I had left off! Lists and Tuples

# <codecell>

# First list

# <codecell>

values = ['python', 'c' , 'java']

values = values[-3]
print(values.title())

# <codecell>

values = ['python' , 'c' , 'java']
values = values[-1]
print(values.title())

# <codecell>

values = ['python' , 'c' , 'java']
values = values[-2]
print(values.title())

# <codecell>

values =['python' , 'c' , 'java']
values = values[-3]
print(values.title())

# <codecell>

#Creating an empty list - and then using it!

# <codecell>

usernames = []

# then adding some users
usernames.append( 'peter')
usernames.append('mary')
usernames.append('roderick')
usernames.append('claire')
usernames.append('paul')

#Greet all of our users
for username in usernames:
    print("Welcome, " + username.title()+ '!')

# <codecell>


