from pointwise import GlyphClient
from pointwise.glyphapi import *

#to test
def zoomToFit(pw,animate=0):
    ###    This action changes the zoom level and pans to center the display around all currently visible entities.
    ###    animate:	This option specifies that the view transition should be animated over the specified number of seconds.
    
    if animate != 0:  
        pw.Display.zoomToFit('-animate',animate)
    else:
        pw.Display.zoomToFit()

#to test
def zoomToEntities(pw,ents,animate=0):  
    ###    This action changes the zoom level and pans to center the display around the list of given entities.
    ###    animate:	This option specifies that the view transition should be animated over the specified number of seconds.
    ###    ents:	This parameter is a list of entities, database boundaries, or connector end spacings.  The display will be panned and zoomed to fit these entities.

    pw.Display.zoomToFit('-animate',animate,ents)
    
#to test
def saveView(pw,slot,view,name='Saved View'):
    ###This action saves a view into a slot.
    ###slot:	This parameter is the saved view integer slot with the range [1, 6].
    ###view:	This parameter is the view to save which includes the list of three vectors (center, translation, and rotation axis) and two floats (rotation angle and zoom).
    ###name:	This parameter is the new view name string.
    pw.Display.saveView(slot,view)
    pw.Display.setViewName(slot,name)

#to test
def recallView(pw,view):
    ###view: Either view/slot number or view name as string 
    pw.Display.recallView(view)

#to test
def clearView(pw,view):
    ###Clears specified view
    ###view: Either view/slot number or view name as string 
    pw.Display.clearView(view)

#to test
def isSavedView(pw,view):
    ###This action checks to see if a view is saved in a slot or has the given name.
    ###view	This parameter is the saved view integer slot with the range [1, 6] or the saved view name string.
    return pw.Display.isSavedView(view)
    
#to test
def resetView(pw,view):
    #view: '-X' '+X' '-Y' '+Y' '-Z' '+Z'
    pw.Display.resetView(view)
    
#to test
def setCurrentView(pw,view,animate=0):
# This action updates the display to the current view.
# -animate	This specifies that the view transition should be animated over the specified number of seconds.
# view	This parameter is the view to save which includes the list of three vectors (center, translation, and rotation axis) and 
    if animate!=0:
        pw.Display.setCurrentView(view,'-animate',animate)
    else:   
        pw.Display.setCurrentView(view)

def showNodes(pw):
    pw.Display.setShowNodes(1)

def hideNodes(pw):
    pw.Display.setShowNodes(0)

#to test
def showCons(pw):
    pw.Display.setShowConnectors(1)
#to test
def hideCons(pw):
    pw.Display.setShowConnectors(0)

#to test
def showDoms(pw):
    pw.Display.setShowDomains(1)
#to test
def hideDoms(pw):
    pw.Display.setShowDomains(0)

#to test
def showOverset(pw):
    pw.Display.setShowOverset(1)
#to test
def hideOverset(pw):
    pw.Display.setShowOverset(0)

#to test
def showDisabled(pw):
    pw.Display.setShowDisabledEntities(1)
#to test
def hideDisabled(pw):
    pw.Display.setShowDisabledEntities(0)

#to test
def showDrawingGuide(pw):
    pw.Display.setShowDrawingGuide(1)
#to test
def hideDrawingGuide(pw):
    pw.Display.setShowDrawingGuide(0)

def showViewManipulator(pw):
    pw.Display.setShowViewManipulator(1)

def hideViewManipulator(pw):
    pw.Display.setShowViewManipulator(0)

#to test
def isolateLayer(pw,layer):
    ###This action isolates the given layer by hiding all other layers, showing this layer and setting it as the current layer.
    pw.Display.isolateLayer(layer)

#to test
def showLayer(pw,layer):
    ###This action sets the given layers to be shown in the current display.
    ###layer:   accepts integer or list of integers
    pw.Display.showLayer(layer)

def hideLayer(pw,layer):
    ###This action sets the given layers to be hidden in the current display.
    ###layer:   accepts integer or list of integers
    pw.Display.hideLayer(layer)

#to test
def showAllLayers(pw):
    ###This action sets all of the layers to be shown in the current display.
    pw.Display.showAllLayers()

#to test
def hideAllLayers(pw):
    ###This action sets all of the layers to be hidden in the current display.
    pw.Display.hideAllLayers()

#to test
def toggleLayer(pw,layer):
    ###This action toggles the visibility of the given layers in the current display.
    ###layer: accepts either integer or list of integers
    pw.Display.toggleLayer(layer)

#to test
def toggleAllLayers(pw):
    ###This action toggles all of the layers in the current display.
    pw.Display.toggleAllLayers()

#to test
def toggleEnabled(pw,ent,parent=0):
    ###This action toggles the Enabled attribute of the entity.
    ###parent:	This optional parameter specifies that if this entity is a pw::Model or pw::Block, then the entity’s parents will have their Enabled attribute toggled as well.
    if parent !=0:
        entity.toggleEnabled(parent)
    else:
        entity.toggleEnabled()

#to test
def transparency(pw,ent,value=0):
    ###This attribute is the transparency of the entity.
    ###value: This value represents the transparency as float value with a range of [0,1].  A value of 0 (the default for most entities) indicates no transparency, while a value of 1 represents full transparency.
    ###Default is 0.0 (except for sources, which have a default value of 0.5)
    ent.setTransparency(value)

#to test
def setLayer(pw,ents,layer,parent=0):
    ###Sets layer that the entity is in
    ###This optional parameter specifies that if this entity is a pw::Model or pw::Block, then the entity’s parents will have their Layer attribute set as well.  It is only available when using setLayer.
    if len(ents) == 1:
        ents = [ents]
    for ent in ents:
        if parent == 1:
            ent.setLayer(layer,'-parents',1)    
        else:
            ent.setLayer(layer)
    

#to test
def saveImage(pw,filename,fgOption='Color',bgOption='Color',dpi=72,size=0,format='PNG'):
    ###This action saves an image of the current display to a file.  This automatically causes an update of the display first to make sure the display is current.
    ###fgOption:	This option takes a string value representing the foreground color option.  The available options are: Color, Grayscale, White, and Black.  This controls how the color of all non-background objects are treated.  The default Color option preserves the existing colors.  The Grayscale option converts the colors to the corresponding gray values.  The White option converts all colors to white, and the Black option converts all colors to Black.
    ###bgOption:	The option takes a string value representing the background color option.  The available options are: Color, Grayscale, White, Black, and Transparent.  This controls how the background is represented in the image.  The default Color option preserves the existing background colors.  The Grayscale option converts the background colors to gray values.  The White option converts the background to white (an error is raised if this is selected and the foreground option is also set to White).  The Black option converts the background to black (an error is raised if the foreground is also set to Black).  The Transparent option saves the image with a transparent background if the graphics hardware supports it and the PNG format is specified (either explicitly or implicitly through the filename’s extension).  Otherwise the Color option is used.
    ###dpi:	        This option expects a positive non-zero integer value representing the dots-per-inch value saved in the image.  The default value is 72.
    ###size:    	This option specifies the image size in inches.  It is represented as a list of 2 real numbers denoting the width and height of the image.  This value, along with the dots-per-inch setting are used to determine the pixel size of the image.  If not specified, the image size in pixels will be the same as the current display.
    ###format:      String value of the form PNG, BMP, or TIFF. 
    ###filename:	This string value should contain the name of a writable file to which the image will be saved.  If the format is not specified with the -format option, the format will be determined from the filename extension if possible.  Recognized extensions are “.bmp”, “.png”, “.tif”, and “.tiff”.  The format should be explicitly declared if a different extension is specified.
    if size !=0:
        pw.Display.saveImage('-foreground',fgOption,'-background',bgOption,'-dpi',dpi,'-size',size,'-format',format,filename)
    else:
        pw.Display.saveImage('-foreground',fgOption,'-background',bgOption,'-dpi',dpi,'-format',format,filename)

#to test   
def saveState(pw,name=0):
    ###This action saves the layer visibility state of the curent display.  
    ###name:	This optional parameter is the string name to give this state for referring to it in other actions; if no name is given, a unique name will be generated.
    if name != 0:
        pw.Layer.saveState(name)
    else:
        pw.Layer.saveState()

#to test   
def restoreState(pw,name):
    ###This action restores the layer visibility state to the curent display.
    ###name:This parameter is the string name of the state to restore.
    pw.Layer.restoreState(name)

#to test   
def removeState(pw,name):
    ###This action removes the save state from the list of saved states.
    ###name:This parameter is the string name of the state to remove.
    pw.Layer.removeState(name)

#to test   
def renameState(pw,oldname,newname):
    ###This action removes the save state from the list of saved states.
    pw.Layer.renameState(oldname,newname)

#to test
def setFillMode(pw,ent,mode):
    ###mode: 'None' 'Flat' 'Shaded' 'HiddenLine'
    if type(ent) == list:
        for obj in ent:
            obj.setRenderAttribute('FillMode',mode)
    else:
        ent.setRenderAttribute('FillMode',mode)

#to test
def setLineMode(pw,ent,mode):
    ###mode: 'None' 'All'
    ent.setRenderAttribute('LineMode',mode)
    
def updateDisplay(pw):
    pw.Display.update()
    
