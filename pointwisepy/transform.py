from pointwise import GlyphClient
from pointwise.glyphapi import *

def rotation(pw,ents,axis=(0,0,0),angle=0,anchor=(0,0,0),point=0):
    #pwu::Transform rotation ?-anchor anchor_pt? < quat | axis angle | right up >
    #Return a transform matrix that is a rotation of the given quaternion, axis angle pair, or pair of vectors representing the new X and Y directions.
    #anchor:	This is the point about which the matrix is rotated (default is the origin).
    #quat:	This argument represents the rotation quaternion.
    #axis:	This argument is the axis of rotation and is used in conjunction with the angle argument.
    #angle:	This argument is angle of rotation about the axis argument.
    #right:	This represents the direction to which the X axis is rotated by the rotation matrix.  The value is normalized before use.
    #up:	This represents the direction to which the Y axis is rotated by the rotation matrix.  Note that it normalized and made orthogonal to the right vector.  An error is reported if it is parallel to the right vector.
    pw.Application.clearClipboard()
    pw.Application.setClipboard(ents)
    with pw.Application.begin("Paste") as paste:
        ents = paste.getEntities()
        with pw.Application.begin("Modify",ents) as modifier:
            # if method=="rotate":
                # print(ents)
            return pw.Entity.transform(Transform.rotation(axis,angle,anchor),ents)
                # pw.Entity.transform(Transform.rotation(anchor=(pwpy.getXYZ(pw,con280[1])),axis=(0,0,1),angle=90),con280)

def rotate(pw,ents,matrix=0,axis=(0,0,0),angle=0,anchor=(0,0,0),point=0):
    #Multiply the given transform matrix by a rotation transform
    #anchor:	the point about which the matrix is rotated (default is the origin)
    #matrix:	the transform matrix
    #axis:	the rotation transform axis vector
    #angle:	the rotation transform angle
    pw.Application.clearClipboard()
    pw.Application.setClipboard(ents)
    with pw.Application.begin("Paste") as paste:
        ents = paste.getEntities()
        with pw.Application.begin("Modify",ents) as modifier:
            # if method=="rotate":
                # print(ents)
            return pw.Entity.transform(Transform.rotation(anchor,matrix,axis,angle),ents)
                # pw.Entity.transform(Transform.rotation(anchor=(pwpy.getXYZ(pw,con280[1])),axis=(0,0,1),angle=90),con280)

def translation(pw,ents,offset,paste=1):
    #Return a transform matrix that is a translation of the given offset
    #offset:	the translation transform offset
    if paste == 1:
        pw.Application.clearClipboard()
        pw.Application.setClipboard(ents)
        with pw.Application.begin("Paste") as paste:
            ents = paste.getEntities()
            with pw.Application.begin("Modify",ents) as modifier:
                return pw.Entity.transform(Transform.translation(offset),ents)
    else:
        with pw.Application.begin("Modify",ents) as modifier:
                return pw.Entity.transform(Transform.translation(offset),ents)

def translate(pw,ents,matrix,offset):
    #Multiply the given transform matrix by a translation transform
    #offset:	the translation transform offset
    #matrix:	the transform matrix
    pw.Application.clearClipboard()
    pw.Application.setClipboard(ents)
    with pw.Application.begin("Paste") as paste:
        ents = paste.getEntities()
        return pw.Entity.transform(Transform.translation(matrix,offset),ents)

def mirror(pw,ents,matrix,normal,dist):
    #Multiply the given transform matrix by a mirroring transform
    #matrix:	the transform matrix
    #normal:	the normal of the mirroring plane
    #dist:	the constant value of the plane
    pw.Application.clearClipboard()
    pw.Application.setClipboard(ents)
    with pw.Application.begin("Paste") as paste:
        ents = paste.getEntities()
        return pw.Entity.transform(Transform.mirroring(normal,dist),ents)
    
def mirroring(pw,ents,normal,dist):            
    #normal:	the normal of the mirroring plane
    #dist:	the constant value of the plane
    pw.Application.clearClipboard()
    pw.Application.setClipboard(ents)
    with pw.Application.begin("Paste") as paste:
        ents = paste.getEntities()
        pw.Entity.transform(Transform.mirroring(normal,dist),ents)
        return ents

def mirrorPlane(pw,ents,plane):                
    #plane:	The mirroring plane.
    #dist:	the constant value of the plane
    pw.Application.clearClipboard()
    pw.Application.setClipboard(ents)
    with pw.Application.begin("Paste") as paste:
        ents = paste.getEntities()
        return pw.Entity.transform(Transform.mirrorPlane(plane),ents)
        
def scaling(pw,ents,scale,anchor=0):
    #Return a transform matrix that is a scaling of the given vector
    #anchor:	the point about which the matrix is scaled (default is the origin)
    #scale:	the scaling vector
    pw.Application.clearClipboard()
    pw.Application.setClipboard(ents)
    with pw.Application.begin("Paste") as paste:
        ents = paste.getEntities()
        if anchor!=0:
            return pw.Entity.transform(Transform.scaling('-anchor',anchor,scale),ents)
        else:
            return pw.Entity.transform(Transform.scaling(scale),ents)

def scale(pw,ents,matrix,scale,anchor=0):
    #Multiply the given transform matrix by a scaling transform
    #anchor:	the point about which the matrix is scaled (default is the origin)
    #matrix:	the transform matrix
    #scale:	the scaling matrix vector
    pw.Application.clearClipboard()
    pw.Application.setClipboard(ents)
    with pw.Application.begin("Paste") as paste:
        ents = paste.getEntities()
        if anchor!=0:
            return pw.Entity.transform(Transform.scale('-anchor',anchor,matrix,scale),ents)
        else:
            return pw.Entity.transform(Transform.scale(matrix,scale),ents)
            
def calculatedScaling(pw,ents,plane,tol=0):
    #Return a transform matrix that scales a given point from one location to another anchored at a third point
    #anchor:	the anchor for the scaling (a point at this location will not be transformed by the matrix)
    #start:	a point value representing a location before transformation
    #end:	a point value representing the start value’s location after transformation
    #tol:	if a component of the vector difference between the anchor and start point is less than the specified tolerance, the scaling factor will be set to 1 for that component (default value is zero)
    pw.Application.clearClipboard()
    pw.Application.setClipboard(ents)
    with pw.Application.begin("Paste") as paste:
        ents = paste.getEntities()
        return pw.Entity.transform(Transform.calculatedScaling(anchor,start,end,tol),ents)

def ortho(pw,ents,left,right,bottom,top,near,far):                
    #Create an orthonormal view transform matrix from a view frustum
    #left:	the left plane constant
    #right:	the right plane constant
    #bottom:	the bottom plane constant
    #top:	the top plane constant
    #near:	the near plane constant
    #far:	the far plane constant
    pw.Application.clearClipboard()
    pw.Application.setClipboard(ents)
    with pw.Application.begin("Paste") as paste:
        ents = paste.getEntities()
        return pw.Entity.transform(Transform.ortho(left,right,bottom,top,near,far),ents)

def perspective(pw,ents,left,right,bottom,top,near,far):                
    #Create a perspective view transform matrix from a view frustum
    #left:	the left plane constant
    #right:	the right plane constant
    #bottom:	the bottom plane constant
    #top:	the top plane constant
    #near:	the near plane constant
    #far:	the far plane constant
    pw.Application.clearClipboard()
    pw.Application.setClipboard(ents)
    with pw.Application.begin("Paste") as paste:
        ents = paste.getEntities()
        return pw.Entity.transform(Transform.perspective(left,right,bottom,top,near,far),ents)

def stretch(pw,ents,plane):                
    #Multiply the given transform matrix by a stretching transform.  If the vector defined by the start and end points is orthogonal to the vector defined by the start and anchor points, the transform is undefined and the matrix will be set to the identity matrix.##
    #matrix:	the transform matrix
    #anchor:	the anchor for the stretching (a point at this location will not be transformed by the matrix)
    #start:	a point value representing a location before transformation
    #end:	a point value representing the start value’s location after transformation
    pw.Application.clearClipboard()
    pw.Application.setClipboard(ents)
    with pw.Application.begin("Paste") as paste:
        ents = paste.getEntities()
        return pw.Entity.transform(Transform.stretch(matrix,anchor,start,end),ents)

def stretching(pw,ents,plane):                
    #Return a transform matrix that is a stretching transform.  If the vector defined by the start and end points is orthogonal to the vector defined by the start and anchor points, the transform is undefined and the matrix will be set to the identity matrix.
    #anchor:	the anchor for the stretching (a point at this location will not be transformed by the matrix)
    #start:	a point value representing a location before transformation
    #end:	a point value representing the start value’s location after transformation
    pw.Application.clearClipboard()
    pw.Application.setClipboard(ents)
    with pw.Application.begin("Paste") as paste:
        ents = paste.getEntities()
        return pw.Entity.transform(Transform.stretching(anchor,start,end),ents)

def revolve(pw,ent,params):
    # for point and direction:  params=[angle,rotationPoint,[x,y,z]]
    
    with pw.Application.begin('Create') as create:
        db = pw.Surface.create()
        db.revolve('-angle',params[0],ent,params[1],params[2])
    return db
    
def copyPaste(pw,ents,method,axis=0,angle=0,anchor=0,point=0):  
    #method: 'rotate' 'scale'
    pw.Application.clearClipboard()
    pw.Application.setClipboard(ents)
    
    with pw.Application.begin("Paste") as paste:
        ents = paste.getEntities()
        with pw.Application.begin("Modify",ents) as modifier:
            if method=="rotate":
                print(ents)
                return pw.Entity.transform(Transform.rotation(anchor,axis,angle),ents)
                # pw.Entity.transform(Transform.rotation(anchor=(pwpy.getXYZ(pw,con280[1])),axis=(0,0,1),angle=90),con280)
            elif method=="scale":
                return pw.Entity.transform(Transform.scaling('-anchor',point,plane,ents))
            elif method=="translation":
                return pw.Entity.transform(Transform.translation(plane,ents))
            pw.Application.markUndoLevel('Translate')
