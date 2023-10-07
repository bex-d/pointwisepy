from pointwise import GlyphClient
from pointwise.glyphapi import *

def rotation(pw,ents,axis=(0,0,0),angle=0,anchor=(0,0,0)):
    """
    Returns rotated entities.
    
    Arguments:
        pw: Requires Pointwise license
        ents: Pointwise object or list of objects
        axis: axis of rotation
        angle: angle of rotation about the axis
        anchor: point around which the objects are rotated
    """
    pw.Application.clearClipboard()
    pw.Application.setClipboard(ents)
    with pw.Application.begin("Paste") as paste:
        ents = paste.getEntities()
        with pw.Application.begin("Modify",ents) as modifier:
            return pw.Entity.transform(Transform.rotation(axis,angle,anchor),ents)

def rotate(pw,ents,matrix=0,axis=(0,0,0),angle=0,anchor=(0,0,0)):
    """
    Returns rotated entities.
    
    Arguments:
        pw: Requires Pointwise license
        ents: Pointwise object or list of objects
        matrix: transform matrix
        axis: axis of rotation
        angle: angle of rotation about the axis
        anchor: point around which the objects are rotated
    """
    pw.Application.clearClipboard()
    pw.Application.setClipboard(ents)
    with pw.Application.begin("Paste") as paste:
        ents = paste.getEntities()
        with pw.Application.begin("Modify",ents) as modifier:
            return pw.Entity.transform(Transform.rotation(anchor,matrix,axis,angle),ents)

def translation(pw,ents,offset,paste=1):
    """
    Returns translated entities.
    
    Arguments:
        pw: Requires Pointwise license
        ents: Pointwise object or list of objects
        offset: translation transform offset
        paste: 0 - delete original entities, 1 - copy and paste
    """
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
    """
    Returns translated entities.
    
    Arguments:
        pw: Requires Pointwise license
        ents: Pointwise object or list of objects
        matrix: transform matrix
        offset: translation transform offset
    """
    pw.Application.clearClipboard()
    pw.Application.setClipboard(ents)
    with pw.Application.begin("Paste") as paste:
        ents = paste.getEntities()
        return pw.Entity.transform(Transform.translation(matrix,offset),ents)

def mirror(pw,ents,matrix,normal,dist):
    """
    Returns mirrored entities.
    
    Arguments:
        pw: Requires Pointwise license
        ents: Pointwise object or list of objects
        matrix: transform matrix
        normal: normal of the mirroring plane
        dist: constant value of the plane
    """
    pw.Application.clearClipboard()
    pw.Application.setClipboard(ents)
    with pw.Application.begin("Paste") as paste:
        ents = paste.getEntities()
        return pw.Entity.transform(Transform.mirroring(normal,dist),ents)
    
def mirroring(pw,ents,normal,dist):  
    """
    Returns mirrored entities.
    
    Arguments:
        pw: Requires Pointwise license
        ents: Pointwise object or list of objects
        normal: normal of the mirroring plane
        dist: constant value of the plane
    """          
    pw.Application.clearClipboard()
    pw.Application.setClipboard(ents)
    with pw.Application.begin("Paste") as paste:
        ents = paste.getEntities()
        pw.Entity.transform(Transform.mirroring(normal,dist),ents)
        return ents

def mirrorPlane(pw,ents,plane):   
    """
    Returns mirrored entities.
    
    Arguments:
        pw: Requires Pointwise license
        ents: Pointwise object or list of objects
        plane: the mirroring plane
    """
    pw.Application.clearClipboard()
    pw.Application.setClipboard(ents)
    with pw.Application.begin("Paste") as paste:
        ents = paste.getEntities()
        return pw.Entity.transform(Transform.mirrorPlane(plane),ents)
        
def scaling(pw,ents,scale,anchor=0):
    """
    Returns scaled entities.
    
    Arguments:
        pw: Requires Pointwise license
        ents: Pointwise object or list of objects
        scale: scaling vector
        anchor: anchor point. Default is origin
    """
    pw.Application.clearClipboard()
    pw.Application.setClipboard(ents)
    with pw.Application.begin("Paste") as paste:
        ents = paste.getEntities()
        if anchor!=0:
            return pw.Entity.transform(Transform.scaling('-anchor',anchor,scale),ents)
        else:
            return pw.Entity.transform(Transform.scaling(scale),ents)

def scale(pw,ents,matrix,scale,anchor=0):
    """
    Returns scaled entities.
    
    Arguments:
        pw: Requires Pointwise license
        ents: Pointwise object or list of objects
        matrix: transform matrix
        scale: scaling vector
        anchor: anchor point. Default is origin
    """
    pw.Application.clearClipboard()
    pw.Application.setClipboard(ents)
    with pw.Application.begin("Paste") as paste:
        ents = paste.getEntities()
        if anchor!=0:
            return pw.Entity.transform(Transform.scale('-anchor',anchor,matrix,scale),ents)
        else:
            return pw.Entity.transform(Transform.scale(matrix,scale),ents)
            
def calculatedScaling(pw,ents,anchor,start,end,tol=0):
    """
    Returns transform matrix
    
    Arguments:
        pw: Requires Pointwise license
        ents: Pointwise object or list of objects
        anchor: anchor point
        start: starting location of scaled point
        end: final location of scaled point
        tol: Default is 0
    """
    pw.Application.clearClipboard()
    pw.Application.setClipboard(ents)
    with pw.Application.begin("Paste") as paste:
        ents = paste.getEntities()
        return pw.Entity.transform(Transform.calculatedScaling(anchor,start,end,tol),ents)

def ortho(pw,ents,left,right,bottom,top,near,far): 
    """
    Create orthonormal view transform matrix from a view frustum
    
    Arguments:      
        pw: Requires Pointwise license
        ents: Pointwise object or list of objects         
        left: left plane constant
        right: right plane constant
        bottom: bottom plane constant
        top: top plane constant
        near: near plane constant
        far: far plane constant
    """
    pw.Application.clearClipboard()
    pw.Application.setClipboard(ents)
    with pw.Application.begin("Paste") as paste:
        ents = paste.getEntities()
        return pw.Entity.transform(Transform.ortho(left,right,bottom,top,near,far),ents)

def perspective(pw,ents,left,right,bottom,top,near,far):
    """
    Create perspective view transform matrix from a view frustum
    
    Arguments:      
        pw: Requires Pointwise license
        ents: Pointwise object or list of objects         
        left: left plane constant
        right: right plane constant
        bottom: bottom plane constant
        top: top plane constant
        near: near plane constant
        far: far plane constant
    """
    pw.Application.clearClipboard()
    pw.Application.setClipboard(ents)
    with pw.Application.begin("Paste") as paste:
        ents = paste.getEntities()
        return pw.Entity.transform(Transform.perspective(left,right,bottom,top,near,far),ents)

def stretch(pw,ents,matrix,anchor,start,end):
    """
    Returns stretched entities
    
    Arguments:
        pw: Requires Pointwise license
        ents: Pointwise object or list of objects
        matrix: transform matrix
        anchor: anchor point
        start: starting location of scaled point
        end: final location of scaled point
    """           
    pw.Application.clearClipboard()
    pw.Application.setClipboard(ents)
    with pw.Application.begin("Paste") as paste:
        ents = paste.getEntities()
        return pw.Entity.transform(Transform.stretch(matrix,anchor,start,end),ents)

def stretching(pw,ents,anchor,start,end):   
    """
    Returns stretched entities
    
    Arguments:
        pw: Requires Pointwise license
        ents: Pointwise object or list of objects
        anchor: anchor point
        start: starting location of scaled point
        end: final location of scaled point
    """                        
    pw.Application.clearClipboard()
    pw.Application.setClipboard(ents)
    with pw.Application.begin("Paste") as paste:
        ents = paste.getEntities()
        return pw.Entity.transform(Transform.stretching(anchor,start,end),ents)

def revolve(pw,ent,params):  
    """
    Returns revolved database
    
    Arguments:
        pw: Requires Pointwise license
        ent: Pointwise object or list of objects
        params: [angle,rotationPoint,[x,y,z]]
    """
    with pw.Application.begin('Create') as create:
        db = pw.Surface.create()
        db.revolve('-angle',params[0],ent,params[1],params[2])
    return db
