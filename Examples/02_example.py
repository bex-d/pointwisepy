from naca import naca4 #From https://github.com/dgorissen/naca
from pointwisepy import *
import os

#get current working directory
fileDir = os.getcwd()

#connect to Pointwise license (batch mode)
pw,glf = connectPort(2807)

print('Enter 4 digit NACA number:')
NACA = input()

print('Enter filename to save to (no extension):')
filename = input()

nasFile = fileDir+'/'+filename+'.nas'
projectFile = fileDir+'/'+filename+'.pw'

#get coordinates for NACA aerofoil
points = naca4(str(NACA),100)
x = points[0]
y = points[1]

#set default connector spacings
setCalculateDimensionMethod(pw)
setCalculateDimensionSpacing(pw,0.1)

#plot aerofoil
for i in range (0,len(x)-1):
    createCon(pw,[[x[i],y[i],0],[x[i+1],y[i+1],0]])
createCon(pw,[[x[0],y[0],0],[x[-1],y[-1],0]])

# create farfield
setCalculateDimensionSpacing(pw,10)
createCon(pw,points=[[-50,0,0],(0.5,0,0)],seg="circle",plane=(0,0,1),endAngle=360)
zoomToFit(pw)
delete(pw,'con-201')

#get all grid entities and export .nas file
exportGrid(pw,getByType(pw,'g'),nasFile)

save(pw,projectFile)