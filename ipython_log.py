# IPython log file

get_ipython().magic(u'logstart')
import os
rostersys = ('/home/wcmckee/artxapi')
rostersys
os.chdir(rostersys)
os.mkdir('/home/deb/rosys')
rossys = ('/home/deb/rosys')
rossys
os.chdir(rossys)
nameflat = ['reuben', 'ramandip', 'raj', 'jayosh', 'william', 'mukesh', 'group']
nameflat
for flatm in nameflat:
    print (flatm)
    
dayweek = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
dayweek
for days in dayweek:
    print days
    
import random
shufz = random.shuffle(dayweek)
shufz
help('random')
