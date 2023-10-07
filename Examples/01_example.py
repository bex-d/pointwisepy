# Import python library
from pointwisepy_test import * 

# Connect to Pointwise license
# from pointwise import GlyphClient
# from pointwise.glyphapi import *
pw,glf = connectPort(2807)

# Reset settings
reset(pw)

# Define coordinates for geometry creation
coords = [[[0,0,0],[0,10,0]],[[0,10,0],[1,10,0]],[[1,0,0],[0,0,0]],[[1,10,0],[1,6,0]],[[1,0,0],[1,5,0]],[[1,5,0],[2,5,0]],[[1,6,0],[2,6,0]],
[[2,10,0],[2,6,0]],[[2,0,0],[2,5,0]],[[2,0,0],[3,0,0]],[[2,10,0],[3,10,0]],[[3,00,0],[3,10,0]],
[[4,0,0],[4,7,0]],[[4,7,0],[5,7,0]],[[5,7,0],[5,0,0]],[[5,0,0],[4,0,0]],
[[4,8,0],[4,10,0]],[[4,10,0],[5,10,0]],[[5,8,0],[5,10,0]],[[5,8,0],[4,8,0]],
[[6,0,0],[6,2,0]],[[6,2,0],[7,2,0]],[[7,2,0],[7,0,0]],[[7,0,0],[6,0,0]],
[[6,3,0],[6,10,0]],[[6,10,0],[7,10,0]],[[7,3,0],[7,10,0]],[[7,3,0],[6,3,0]]]

# Create straight database curves & and append to list of curves
curves = []
for coord in coords:
    curves.append(createCurve(pw,coord))

#create curved database curves and store objects
curve1 = createCurve(pw,points=[[13,8,0],[12.5,8,0]],seg="circle",slope=0,shoulder=0,center=0,plane=(0,0,1),endAngle=360,angle=0)
curve2 = createCurve(pw,points=[[16,8,0],[15.5,8,0]],seg="circle",slope=0,shoulder=0,center=0,plane=(0,0,1),endAngle=360,angle=0)
curve3 = createCurve(pw,points=[[11,5,0],[17,5,0]],seg="circle",slope=0,shoulder=[14,2,0],center=0,plane=(0,0,1),endAngle=0,angle=0)

# Get coordinates from either end of the last connector
coords = [getXYZ(pw,curve3,'-arc',0),getXYZ(pw,curve3,'-arc',1)]

# Create another connector
curve4 = createCurve(pw,coords)

# Update display and pause to view progress in GUI
zoomToFit(pw)
updateDisplay(pw)
input("Press Enter to continue...") 

# Interpolate curves into surfaces database
surf1 = interpolate(pw,curves[1],curves[2])
surf2 = interpolate(pw,curves[5],curves[6])
surf3 = interpolate(pw,curves[9],curves[10])

surf4 = interpolate(pw,curves[17],curves[19])
surf5 = interpolate(pw,curves[13],curves[15])
surf6 = interpolate(pw,curves[21],curves[23])
surf7 = interpolate(pw,curves[24],curves[26])

surf8 = interpolate(pw,curve3,curve4)

# Create surfaces from circular curves
patch(pw,curve1)
patch(pw,curve2)

# Delete old curves
delete(pw,getByType(pw,'Curve'))

# Set fill mode for all database entities
setFillMode(pw,getByType(pw,'Database'),'Shaded') 

# Pause & update display
updateDisplay(pw)
input("Press Enter to continue...") 

# Set connector spacing defaults
setCalculateDimensionMethod(pw,'Spacing')
setCalculateDimensionSpacing(pw,0.2)

# Mesh surfaces
domains = createDom(pw,getByType(pw,'Database'))

# Delete extra domains
delete(pw,['dom-10','dom-11'])
delete(pw,['con-32','con-33','con-34','con-35','con-37','con-38','con-39','con-40'])

# Merge domains
dom1 = getByName(pw,'dom-1')
dom2 = getByName(pw,'dom-2')
dom3 = getByName(pw,'dom-3')
dom8 = getByName(pw,'dom-8')
dom9 = getByName(pw,'dom-9')
join(pw,[dom1,dom2,dom3])
join(pw,[dom9,dom8])

# Move databse surfaces to new layer and hide
setLayer(pw,getByType(pw,'Database'),1)
hideLayer(pw,1)

# Pause & update display
updateDisplay(pw)
input("Press Enter to continue...") 

# Update all connector spacings
setConnectorSpacings(pw,getByType(pw,'Connector'),0.4)
updateDisplay(pw)
        
# Refine selected connectors
setConnectorSpacings(pw,['con-1','con-2'],0.1)
setConnectorSpacings(pw,['con-43','con-11'],0.3)
updateDisplay(pw)

# Set spacing distribution       
setConnectorSpacings(pw,['con-5','con-11'],0.1,mode='e')
setConnectorSpacings(pw,['con-12','con-43'],0.1,mode='b')

# Pause & update display
updateDisplay(pw)
input("Press Enter to continue...") 

# Create farfield
createFarfield(pw,ents=[getByType(pw,'Domain')],size=100)   
farfieldCons = getByType(pw,'Connector')[-12:]
setConnectorSpacings(pw,farfieldCons,25)
zoomToFit(pw)

# Export Nastran file & save project (update to local directory)
filename = 'C:/../Example_01.pw'
nasfile = filename[:-3]+'.nas'

if filename != 'C:/../Example_01.pw':
    save(pw,filename)
    domains = getByType(pw,'Domain')
    exportGrid(pw,domains,nasfile)
else:
    print('Update file directory on line 118 to save and export project')