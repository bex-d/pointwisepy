from pointwise import GlyphClient
from pointwise.glyphapi import *
import sys
import time
from .get import *

def connectPort(port=0,reset=1,result=None,):   
    """
    Connects to a Pointwise license. 
    For GUI: Script > Glyph Server > Active & port=2807

    Arguments:
    port: 0 for batch mode, 2807 for GUI
    reset: 0 - append to existing project. 1 - Clear project (default). 
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
            if reset == 1:
                pw.Application.reset()
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
    Arguments: 
        pw: Requires Pointwise license
    """
    pw.Application.reset()
    
def clearModified(pw):
    """
    Resets the flag to track modifications.
    Arguments: 
        pw: Requires Pointwise license
    """
    pw.Application.clearModified()
 
def setUndoMaximumLevels(pw,levels=5):
    """
    Set number of undo actions to record. Irrelevant unless used with GUI.
    Arguments: 
        pw: Requires Pointwise license
        levels: Optional. Number of undo levels. Default is 5. 
    """
    pw.Application.setUndoMaximumLevels(levels)
          
def delete(pw,ents,dependents=0):
    """
    Deletes pointwise entities.

    Arguments:
    pw: Must be connected to Pointwise instance
    ents: Entity or list of entities to delete. Accepts defined pointwise entities and entity names as strings.
    dependents: 0 (false, default) or 1 (true). If entity is not removed from project with delete(), try deleting dependents 
            
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
            if dependents == 1:
                ent.delete('-dependents')
            else:
                ent.delete()
    except:
        ent = ents
        if type(ent) == str:
            try: 
                ent = getByName(pw,ent)
            except:
                print("No entity by name: {}".format(ent))
            if dependents == 1:
                ent.delete('-dependents')
            else:
                ent.delete()

def deleteSpecial(pw,ents):
    """
    Untested, could be developed to delete dependent entities. 
    Check Glyph function here: 
    https://pointwise.com/doc/glyph2/files/Glyph/cxx/GlyphEntity-cxx.html#pw.Entity.checkDelete
    """
    pw.Entity.checkDelete('-freed',ents)
    pw.Entity.delete(ents)
    pw.Application.markUndoLevel('Delete Special')

def save(pw,filedir,env=0):
    """
    Saves project file. 
    
    Arguments: 
    pw: Requires Pointwise license.
    filedir: location and file name of project in format "C:/location/filename.pw". If spaces in string, try raw string literal r"C:/drive name/filename.pw" 
    env: Optional, set to 1 to save project environment. 
    """
    try:
        if env == 1:
            pw.Application.save('-environment',filedir)
            print("Saved project file and/or environment to {}".format(filedir))
        else:
            pw.Application.save(filedir)
            print("Saved project file and/or environment to {}".format(filedir))
    except:
        print("Unable to save to project to {}".format(filedir))
        
def projectLoader(pw,filedir,repair=0,append=False):
    """
    Loads project file. 
    
    Arguments: 
    pw: Requires Pointwise license.
    filedir: location and file name of project in format "C:/location/filename.pw". If spaces in string, try raw string literal r"C:/drive name/filename.pw" 
    repair: Repair mode for out of sync grid points. Default is defer. Options explained here: https://pointwise.com/doc/glyph2/files/Glyph/cxx/GlyphProjectLoader-cxx.html#pw.ProjectLoader.RepairMode
    append: Append to existing project. Default option is to clear any existing project and overwrite with loaded project.
    """
    with pw.Application.begin('ProjectLoader') as loader:
        loader.initialize(filedir)
        if repair == 0:
            loader.setRepairMode('Defer')
        elif repair ==  'KeepGridPoints':
            loader.setRepairMode('KeepGridPoints')
        elif repair ==  'KeepDistributions':
            loader.setRepairMode('KeepDistributions')
        else: 
            raise Exception("Incorrect defer mode in project loader: {}".format(repair)) 
            
        loader.setAppendMode(append)
        loader.load() 
    pw.Application.markUndoLevel('Append')

def undo(pw):
    pw.Application.undo()
