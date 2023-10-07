from naca import naca4 #From https://github.com/dgorissen/naca
from pointwisepy import *
import os

#get current working directory
fileDir = os.getcwd()

#connect to Pointwise license (batch mode)
pw,glf = connectPort(0)

print('Enter NACA number:')
NACA = input()

print('Enter filename to save to (no extension):')
filename = input()

nasFile = append(fileDir,projectFile,'.nas')
projectFile = append(fileDir,projectFile,'.pw')

#get coordinates for NACA aerofoil
points = naca4(str(NACA),100)

#plot aerofoil
for i = 0:length(points)-1:
    createCon(pw,points[i],points[i+1])
createCon(pw,points[0],points[end])

# create farfield
createCon(pw,seg="circle",center=(0,0,0),plane=(0,0,1),setAngle=360)

#get all grid entities and export .nas file
exportGrid(pw,getByType(pw,'g'),nasFile)

save(pw,projectFile)