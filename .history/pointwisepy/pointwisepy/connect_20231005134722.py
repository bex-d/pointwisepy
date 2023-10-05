from pointwise import GlyphClient
from pointwise.glyphapi import *
import sys
import time
from .get import *

def connectPort(port=0,result=None):   
    """
    Connects to a Pointwise license. 
    For GUI: Script > Glyph Server > Active & port=2807

    Arguments:
    port: 0 for batch mode, 2807 for GUI
    result: None  - Will keep pinging server until license found
            False - Only look for license once
            
    Returns:
    pw,glf
    """
    print('Looking for license...')
    LINE_UP = '\033[1A'
    LINE_CLEAR = '\x1b[2K'
    
    while result is None:
        try:
            glf = GlyphClient(port=port)
            pw = glf.get_glyphapi()
            print('\nConnected to Pointwise, port {}'.format(port))
            return pw,glf
        
        except:
            if port==2807:  
                print(' Cannot connect to Pointwise (port 2807). Ensure Glyph server is active. Close function panels and end Glyph journalling')
                #clears command line output for retry countdown
                sys.stdout.write("\r")
                sys.stdout.flush()
            else:
                print(' No Pointwise license (port 0)')
                
        #wait ten seconds to retry for license, rewrites output to same line
        for i in range(10,0,-1):
            sys.stdout.write('\rWaiting to retry in... '+str(i)+' \r')
            sys.stdout.flush()
            time.sleep(1)
            if i == 1:
                print(LINE_UP,LINE_UP)
            
def disconnectPW():
    """
    Disconnects from a Pointwise license. No arguments or return. 
    """
    pw = 0
    glf = 0
    print('Disconnected from Pointwise License')

def reset(pw):
    """
    Reset application settings.
    """
    pw.Application.reset()
    
def clearModified(pw):
    """
    Resets the flag to track modifications.
    """
    pw.Application.clearModified()
 
def setUndoMaximumLevels(pw,levels=5):
    """
    Set number of undo actions to record. Irrelevant unless used with GUI.
    """
    pw.Application.setUndoMaximumLevels(levels)
          
def delete(pw,ents):
    """
    Deletes pointwise entities.

    Arguments:
    pw: Must be connected to Pointwise instance
    ents: Entities to delete. Accepts defined pointwise entities and entity names as strings. May have to be a list? 
            
    Examples:
    delete(pw,getByType(pw,'Connector'))
    delete(pw,[ent1,ent2])
    delete(pw,['curve-1','surface-2])
    """
    try:
        for ent in ents:
            if type(ent) == str:
                try: 
                    ent = getByName(pw,ent)
                except:
                    print("No entity by name: {}".format(ent))
            ent.delete()
    except:
        ent = ents
        if type(ent) == str:
            try: 
                ent = getByName(pw,ent)
            except:
                print("No entity by name: {}".format(ent))
            ent.delete()
        
def deleteSpecial(pw,ents):
    pw.Entity.checkDelete('-freed',ents)
    pw.Entity.delete(ents)
    pw.Application.markUndoLevel('Delete Special')

def save(pw,fileloc,env=0):
    #C:/location/filename.pw
    if env == 1:
        pw.Application.save('-environment',fileloc)
    else:
        pw.Application.save(fileloc)
        
def projectLoader(pw,fileloc,defer=0,append=False):
    with pw.Application.begin('ProjectLoader') as loader:
        loader.initialize(fileloc)
        loader.setRepairMode('Defer')
        loader.setAppendMode(append)
        loader.load() 
    pw.Application.markUndoLevel('Append')

def undo(pw):
    pw.Application.undo()

def save(pw,filename):
    pw.Application.save(filename)    