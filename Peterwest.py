# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

# First list

# <codecell>

# Taking off from where I had left off! Lists and Tuples

# <codecell>


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

# functions! Wow!

# <codecell>

# Defining a function
def function_name(argument_1, argument_2):
    
    def Thank_you(name!):
     #This function prints a two lined note of thanks 
        print("You are doing good work, %s!" %name)
        print("Thank you very much for your efforts at home!")
        
        "Thank_you( 'Mary')
        "Thank_you( 'Paul')
        "Thank_you( 'Claire')
        

