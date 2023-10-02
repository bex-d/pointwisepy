#Pointwise connect
from pointwise import GlyphClient
from pointwise.glyphapi import *

def startPW(port=0):    
    
    glf = GlyphClient(port=port)
    pw = glf.get_glyphapi()
    
    print('Connected to Pointwise, port {}'.format(port))