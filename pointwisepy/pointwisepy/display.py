from pointwise import GlyphClient
from pointwise.glyphapi import *

#to test
def zoomToFit(pw,animate=0):
    """
    Zooms to fit all visible entities to screen
    
    Arguments:
        pw: Requires Pointwise license
        animate: 0 - no animation upon zoom, 1+ - length of animation (seconds).     
    """
    if animate != 0:  
        pw.Display.zoomToFit('-animate',animate)
    else:
        pw.Display.zoomToFit()

#to test
def zoomToEntities(pw,ents,animate=0):  
    """
    Zooms to fit all selected entities to screen
    
    Arguments:
        pw: Requires Pointwise license
        ents: entities to zoom to fit.
        animate: 0 - no animation upon zoom, 1+ - length of animation (seconds).     
    """
    pw.Display.zoomToFit('-animate',animate,ents)
    
#to test
def saveView(pw,slot,view,name='Saved View'):  
    """
    Zooms to fit all selected entities to screen. To find view vectors record glyph script. 
    
    Arguments:
        pw: Requires Pointwise license
        slot: 1-6, slot number in which to store view
        view: View to save. List of three vectors (center, translation, and rotation axis) and two floats (rotation angle and zoom). 
        name: View name as string
    """
    pw.Display.saveView(slot,view)
    pw.Display.setViewName(slot,name)

#to test
def recallView(pw,view):    
    """
    Recall view from slot number or view name (string)
    """
    pw.Display.recallView(view)

#to test
def clearView(pw,view):
    """
    Clear view from slot number or view name (string)
    """
    pw.Display.clearView(view)

#to test
def isSavedView(pw,view):
    """
    Checks if view saved under slot number or view name (string). Returns true/false
    """
    return pw.Display.isSavedView(view)
    
#to test
def resetView(pw,view):
    """
    Set view to '-X' '+X' '-Y' '+Y' '-Z' '+Z'
    """
    pw.Display.resetView(view)
    
#to test
def setCurrentView(pw,view,animate=0):
    """
    Set to new view from vectors.
    
    Arguments:
        pw: Requires Pointwise license
        view: List of three vectors (center, translation, and rotation axis) and two floats (rotation angle and zoom). 
        animate: 0 - no animation upon zoom, 1+ - length of animation (seconds).     
    """
    if animate!=0:
        pw.Display.setCurrentView(view,'-animate',animate)
    else:   
        pw.Display.setCurrentView(view)

def showNodes(pw):
    """
    Show all node entities.
    """
    pw.Display.setShowNodes(1)

def hideNodes(pw):
    """
    Hide all node entities.
    """
    pw.Display.setShowNodes(0)

#to test
def showCons(pw):
    """
    Show all connector entities.
    """
    pw.Display.setShowConnectors(1)
#to test
def hideCons(pw):
    """
    Hide all connector entities.
    """
    pw.Display.setShowConnectors(0)

#to test
def showDoms(pw):
    """
    Show all domain entities.
    """
    pw.Display.setShowDomains(1)
#to test
def hideDoms(pw):
    """
    Hide all domain entities.
    """
    pw.Display.setShowDomains(0)

#to test
def showOverset(pw):
    """
    Show overset data.
    """
    pw.Display.setShowOverset(1)
#to test
def hideOverset(pw):
    """
    Hide overset data.
    """
    pw.Display.setShowOverset(0)

#to test
def showDisabled(pw):
    """
    Show all disabled entities.
    """
    pw.Display.setShowDisabledEntities(1)
#to test
def hideDisabled(pw):
    """
    Hide all disabled entities.
    """
    pw.Display.setShowDisabledEntities(0)

#to test
def showDrawingGuide(pw):
    """
    Show drawing guide.
    """
    pw.Display.setShowDrawingGuide(1)
#to test
def hideDrawingGuide(pw):
    """
    Hide drawing guide.
    """
    pw.Display.setShowDrawingGuide(0)

def showViewManipulator(pw):
    """
    Show view manipulator.
    """
    pw.Display.setShowViewManipulator(1)

def hideViewManipulator(pw):
    """
    Hide view manipulator.
    """
    pw.Display.setShowViewManipulator(0)

#to test
def isolateLayer(pw,layer):
    """
    Isolate layer. 
    Arguments:
        pw: Requires Pointwise license
        layer: Number of layer to isolate
    """
    pw.Display.isolateLayer(layer)

#to test
def showLayer(pw,layer):
    """
    Show layer. 
    Arguments:
        pw: Requires Pointwise license
        layer: Number of layer to show
    """
    pw.Display.showLayer(layer)

def hideLayer(pw,layer):
    """
    Hide layer. 
    Arguments:
        pw: Requires Pointwise license
        layer: Number of layer to hide
    """
    pw.Display.hideLayer(layer)

#to test
def showAllLayers(pw):
    """
    Show all layers. 
    Arguments:
        pw: Requires Pointwise license
    """
    pw.Display.showAllLayers()

#to test
def hideAllLayers(pw):
    """
    Hides all layers. 
    Arguments:
        pw: Requires Pointwise license
    """
    pw.Display.hideAllLayers()

#to test
def toggleLayer(pw,layer):
    """
    Toggle layer visbility. 
    Arguments:
        pw: Requires Pointwise license
        layer: Number of layer
    """
    pw.Display.toggleLayer(layer)

#to test
def toggleAllLayers(pw):
    """
    Toggle visbility of all layers. 
    Arguments:
        pw: Requires Pointwise license
    """
    pw.Display.toggleAllLayers()

#to test
def toggleEnabled(pw,ent,parent=0):
    """
    Toggle whether entity enabled. 
    Arguments:
        pw: Requires Pointwise license
        ent: Entity to toggle
        parent: If entity is a model or block, entity parent toggled too.
    """
    if parent !=0:
        entity.toggleEnabled(parent)
    else:
        entity.toggleEnabled()

#to test
def transparency(pw,ent,value=0):
    """
    Set entity transparency. 
    Arguments:
        pw: Requires Pointwise license
        ent: Entity to adjust
        value: float value between 0 (opaque) and 1 (transparent).
    """
    ent.setTransparency(value)

#to test
def setLayer(pw,ents,layer,parent=0):
    """
    Set entity layer. 
    Arguments:
        pw: Requires Pointwise license
        ents: Entities to move
        layer: layer number to move entities to
        parent: if 1 move parent entities too
    """
    if len(ents) == 1:
        ents = [ents]
    for ent in ents:
        if parent == 1:
            ent.setLayer(layer,'-parents',1)    
        else:
            ent.setLayer(layer)

#to test
def saveImage(pw,filename,fgOption='Color',bgOption='Color',dpi=72,size=0,format='PNG'):
    """
    Exports image of display.
     
    Arguments:
        pw: Requires Pointwise license
        filename: Directory and filename of image
        fgOption: Optional. Foreground colour option. 'Color' 'Grayscale' 'White' 'Black'. Default is 'Color'.
        bgOption: Optional. Background colour option. 'Color' 'Grayscale' 'White' 'Black' 'Transparent'. Default is 'Color'.
        dpi: Optional. Dots per inch of image to save. Default is 72.
        size: Optional. Size of image in inches [width,height]. Default is display size. 
        format: Optional. "PNG" "BMP" "TIFF". Default is "PNG"
    """
    if size !=0:
        pw.Display.saveImage('-foreground',fgOption,'-background',bgOption,'-dpi',dpi,'-size',size,'-format',format,filename)
    else:
        pw.Display.saveImage('-foreground',fgOption,'-background',bgOption,'-dpi',dpi,'-format',format,filename)

#to test   
def saveState(pw,name=0):
    """
    Saves current layer visibility of display.
     
    Arguments:
        pw: Requires Pointwise license
        name: Optional. Chosen state name as string.
    """
    if name != 0:
        pw.Layer.saveState(name)
    else:
        pw.Layer.saveState()

#to test   
def restoreState(pw,name):
    """
    Restores saved layer visibility settings.
     
    Arguments:
        pw: Requires Pointwise license
        name: Saved state name as string.
    """
    pw.Layer.restoreState(name)

#to test   
def removeState(pw,name):
    """
    Removed saved layer visibility settings.
     
    Arguments:
        pw: Requires Pointwise license
        name: Saved state name as string.
    """
    pw.Layer.removeState(name)

#to test   
def renameState(pw,oldname,newname):
    """
    Renamed saved layer visibility.
     
    Arguments:
        pw: Requires Pointwise license
        oldname: Saved state name as string.
        newname: New state name as string.
    """
    pw.Layer.renameState(oldname,newname)

#to test
def setFillMode(pw,ent,mode):
    """
    Set entity fill mode. 
     
    Arguments:
        pw: Requires Pointwise license
        ent: Entities to set visibility for. 
        mode: 'None' 'Flat' 'Shaded' 'HiddenLine'
    """
    if type(ent) == list:
        for obj in ent:
            obj.setRenderAttribute('FillMode',mode)
    else:
        ent.setRenderAttribute('FillMode',mode)

#to test
def setLineMode(pw,ent,mode):
    """
    Set line mode to render interior/boundary lines. 
     
    Arguments:
        pw: Requires Pointwise license
        ent: Entities to set visibility for. 
        mode: "All","Boundary","None"
    """
    ent.setRenderAttribute('LineMode',mode)
    
def updateDisplay(pw):
    """
    Updates display. Useful for checking progress of script running on connected GUI instance.
    """
    pw.Display.update()
    
