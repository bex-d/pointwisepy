
def zoomToFit(pw):  
    pw.Display.zoomToFit('-animate', 1)
    
def saveView(pw,viewNo,view,name):
    pw.Display.saveView(viewNo,view)
    pw.Display.setViewName(name)

def resetView(pw,view):
    #view: '-X' '+X' '-Y' '+Y' '-Z' '+Z'
    pw.Display.resetView(view)
    
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

def showViewManipulator(pw):
    pw.Display.setShowViewManipulator(1)

def hideViewManipulator(pw):
    pw.Display.setShowViewManipulator(0)

def setProjection(pw,proj):
    #proj: 'Perspective' 'Orthonormal'   
    pw.Display.setProjection(0)