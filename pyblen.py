# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 16:10:05 2014

@author: wcmckee
"""

import IPython
#IPython.start_ipython(argv=[])

print IPython.__version__
'''
from IPython import embed

#embed()
embed()
IPython.embed_kernel()
'''
'''
from IPython import embedCancer123now!

a = 10
b = 20
embed('First time')
c = 30
d = 40
embed
print (a, b, c, d)
'''

import cocos
class HelloWorld(cocos.layer.Layer):
    def __init__(self):
        super( HelloWorld, self ).__init__()
        
        
label = cocos.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=32,
                          anchor_x='center', anchor_y='center')
                          
                          
label.position = 320,240


self.add( label )

cocos.director.director.init()

hello_layer = HelloWorld ()

main_scene = cocos.scene.Scene (hello_layer)

cocos.director.director.run (main_scene)