from pointwise import GlyphClient
from pointwise.glyphapi import *

def createCon(pw,points=[[0,0,0]],seg="spline",slope='CatmullRom',shoulder=0,center=0,plane=(0,0,1),endAngle=0,setAngle=0,flipArc=0):
    """
    Creates connector
    
    Arguments:
    pw: requires Pointwise license
    points: list of coordinates. Accepts single coordinate for node creation. [[x1,y1,z1],[x2,y2,z2]]
    seg: Optional. Segment type. 'Spline', 'Conic', or 'Circle' 
    slope: Optional. Set slope. Default 'CatmullRom'. Options 'Linear','Akima',''CatmullRom','Free'. Record Glyph journal if unsure. 
    shoulder: Optional. Set shoulder point for Circle or Conic types. Format [x,y,z]
    center: Optional. Set centre point for Circle segment type. Format [x,y,z]
    plane: Optional. Set plane for Circle segment type. Format [x,y,z]
    endAngle: Optional. Set angle for end point of Circle segment type. Input angle in degrees.
    setAngle: Optional. Set angle for Circle segment type. Input angle in degrees.
    flipArc: Optional. Flip arc for Circle segment type. Set to 1 to flip.
    
    Returns:
        Connector entity
    """
    with pw.Application.begin("Create") as creator:
        if seg == "SegmentSpline" or seg=="Spline" or seg=="spline":
            seg = pw.SegmentSpline.create()
            for point in points:
                seg.addPoint(point)
            if slope != 0:
                seg.setSlope(slope)
            
        elif seg == "SegmentConic" or seg=="Conic" or seg=="conic":
            seg = pw.SegmentConic.create()
            for point in points:
                seg.addPoint(point)
            if slope != 0:
                seg.setSlope(slope)
            
        elif seg == "SegmentCircle" or seg=="Circle" or seg == "circle":
            seg = pw.SegmentCircle.create()
            for point in points:
                seg.addPoint(point)
            if shoulder!=0:
                seg.setShoulderPoint(shoulder)
            elif center!=0:
                seg.setCenterPoint(center,plane)
            elif setAngle!=0:
                seg.setAngle(setAngle)
            elif endAngle!=0:
                seg.setEndAngle(endAngle)

        else:
            print('Incorrect segment type: {}'.format(seg))
            
        if flipArc==1:
            seg.flipArc()

        con = pw.Connector.create()
        con.addSegment(seg)
        con.calculateDimension()
        return con
  
def createCurve(pw,points=[[0,0,0]],seg="spline",slope=0,shoulder=0,center=0,plane=(0,0,1),endAngle=0,angle=0):
    """
    Creates database curve
    
    Arguments:
    pw: requires Pointwise license
    points: list of coordinates. Accepts single coordinate for node creation. [[x1,y1,z1],[x2,y2,z2]]
    seg: Optional. Segment type. 'Spline', 'Conic', or 'Circle' 
    slope: Optional. Set slope. Options 'Linear','Akima',''CatmullRom','Free'. Record Glyph journal if unsure. 
    shoulder: Optional. Set shoulder point for Circle or Conic types. Format [x,y,z]
    center: Optional. Set centre point for Circle segment type. Format [x,y,z]
    plane: Optional. Set plane for Circle segment type. Format [x,y,z]
    endAngle: Optional. Set angle for end point of Circle segment type. Input angle in degrees.
    angle: Optional. Set angle for Circle segment type. enter angle in degrees or [angle,plane].
    
    Returns:
        Database entity
        
    """
    # angle: [angle,normal]
    with pw.Application.begin("Create") as creator:
        if seg == "SegmentSpline" or seg=="Spline" or seg=="spline":
            seg = pw.SegmentSpline.create()
            for point in points:
                seg.addPoint(point)
            if slope != 0:
                seg.setSlope(slope)
            
        elif seg == "SegmentConic" or seg=="Conic" or seg=="conic":
            seg = pw.SegmentConic.create()
            for point in points:
                seg.addPoint(point)
            if slope != 0:
                seg.setSlope(slope)
            
        elif seg == "SegmentCircle" or seg=="Circle" or seg == "circle":
            seg = pw.SegmentCircle.create()
            for point in points:
                seg.addPoint(point)
            if shoulder!=0:
                seg.setShoulderPoint(shoulder)
            elif center!=0:
                seg.setCenterPoint(center,plane)
            elif endAngle!=0:
                seg.setEndAngle(endAngle)
            elif angle!=0:
                if type(angle) == list:
                    seg.setAngle(angle[0],angle[1])
                else:
                    seg.setAngle(angle)
            if slope != 0:
                seg.setSlope(slope)

        else:
            print('Incorrect segment type: {}'.format(seg))

        db = pw.Curve.create()
        db.addSegment(seg)
        return db
       
def createSource(pw,points=[[0,0,0]],seg="spline",slope=0,shoulder=0,center=0,plane=(0,0,1),endAngle=0):
    """
    Creates source curve
    
    Arguments:
    pw: requires Pointwise license
    points: list of coordinates. Accepts single coordinate for node creation. [[x1,y1,z1],[x2,y2,z2]]
    seg: Optional. Segment type. 'Spline', 'Conic', or 'Circle' 
    slope: Optional. Set slope. Options 'Linear','Akima',''CatmullRom','Free'. Record Glyph journal if unsure. 
    shoulder: Optional. Set shoulder point for Circle or Conic types. Format [x,y,z]
    center: Optional. Set centre point for Circle segment type. Format [x,y,z]
    plane: Optional. Set plane for Circle segment type. Format [x,y,z]
    endAngle: Optional. Set angle for end point of Circle segment type. Input angle in degrees.
    angle: Optional. Set angle for Circle segment type. enter angle in degrees or [angle,plane].
    
    Returns:
        Database entity
        
    Examples:
        src1 = createSource(pw,points=[[0,0,0],[10,0,0]])
    
    """
    with pw.Application.begin("Create") as creator:
        if seg == "SegmentSpline" or seg=="Spline" or seg=="spline":
            seg = pw.SegmentSpline.create()
            for point in points:
                seg.addPoint(point)
            if slope != 0:
                seg.setSlope(slope)
            
        elif seg == "SegmentConic" or seg=="Conic" or seg=="conic":
            seg = pw.SegmentConic.create()
            for point in points:
                seg.addPoint(point)
            if slope != 0:
                seg.setSlope(slope)
            
        elif seg == "SegmentCircle" or seg=="Circle" or seg == "circle":
            seg = pw.SegmentCircle.create()
            for point in points:
                seg.addPoint(point)
            if shoulder!=0:
                seg.setShoulderPoint(shoulder)
            elif center!=0:
                seg.setCenterPoint(center,plane)
            elif endAngle!=0:
                seg.setEndAngle(endAngle)
            if slope != 0:
                seg.setSlope(slope)

        else:
            print('Incorrect segment type: {}'.format(seg))

        src = pw.SourceCurve.create()
        src.addSegment(seg)
        return src            
  
def createDom(pw,ents,gridtype='Unstructured'):
    """
    Create domains. 
    
    Arguments:
    pw: requires Pointwise license
    ents: list of entities from which to create domain. Either database entities or connectors. 
    gridtype: 'Structured', 'Unstructured'. Default is unstructured mesh.
    
    Returns:
    domains created
    """

    #find first entity in list so can check type to determine domain creation function.
    try:
        ent = ents[0]
        ent = ent[0]
    except:
        ent = ents[0]

    if 'con-' in ent.getName():
        if gridtype == 'Unstructured' or gridtype == 'uns' or gridtype == 'U' or gridtype == 'u':
            pw.Application.setGridPreference('Unstructured')
            doms = pw.DomainUnstructured.createFromConnectors(ents) 
        elif gridtype == 'Structured' or gridtype == 'struc' or gridtype == 'S' or gridtype == 's':
            pw.Application.setGridPreference('Structured')
            doms = pw.DomainStructured.createFromConnectors(ents) 
        else:
            print('Incorrect grid type: {}\nOptions are: "Structured", "Unstructured"'.format(gridtype))

    else:
        if gridtype == 'Unstructured' or gridtype == 'uns' or gridtype == 'U' or gridtype == 'u':
            pw.Application.setGridPreference('Unstructured')
            doms = pw.DomainUnstructured.createOnDatabase(ents) 
        elif gridtype == 'Structured' or gridtype == 'struc' or gridtype == 'S' or gridtype == 's':
            pw.Application.setGridPreference('Structured')
            doms = pw.DomainStructured.createOnDatabase(ents) 
        else:
            print('Incorrect grid type: {}\nOptions are: "Structured", "Unstructured"'.format(gridtype))
        
    return doms

def createConsOnDatabase(pw,ents,gridtype='Unstructured'):
    """
    Create connectors on database. 
    
    Arguments:
    pw: requires Pointwise license
    ents: list of database entities from which to create connectors. 
    gridtype: 'Structured', 'Unstructured'. Default is unstructured mesh.
    
    Returns:
    connectors created
    """
    if gridtype == 'Unstructured' or gridtype == 'uns' or gridtype == 'U' or gridtype == 'u':
        pw.Application.setGridPreference('Unstructured')
        cons = pw.Connector.createOnDatabase(ents) 
    elif gridtype == 'Structured' or gridtype == 'struc' or gridtype == 'S' or gridtype == 's':
        pw.Application.setGridPreference('Structured')
        cons = pw.Connector.createOnDatabase(ents) 
    else:
        print('Incorrect grid type: {}\nOptions are: "Structured", "Unstructured"'.format(gridtype))
        
    return cons      
    
def createFarfield(pw,ents,shape='Sphere',size=[],BCs=[]):    
    """
    Create farfield. Returns nothing.
    
    Arguments:
    pw: requires Pointwise license
    ents: list of database entities from which to create connectors. 
    shape: Shape of farfield. "Box","Cylinder","Sphere","None". Default is sphere. 
    size: Farfield radius
    BCs: Boundary conditions in format [['bcname2',[ents]],['bcname2',[ents]]]
    """
    with pw.Application.begin('VolumeMesher',ents) as mesher:
        mesher.setFarfieldShapeType(shape)
        mesher.setFarfieldRadius(size)
        for BC in BCs:
            mesher.addBoundaryConditionFilter()
            mesher.setBoundaryConditionFilterName('bcf-1',BC[0])
            mesher.setBoundaryConditionFilterAdaptation(BC[0],'Off')
            mesher.setBoundaryConditionFilterPatterns(BC[0],BC[1])
            
        mesher.createGridEntities()
        mesher.end()

def patch(pw,ent):
    """
    Creates surface from circular database curve. Returns surface entity.
    
    Arguments:
    pw: requires Pointwise license
    ent: circular curve to create surface from
    """
    with pw.Application.begin('SurfaceFit') as patcher:
        surface = patcher.createSurfacesFromCurves(ent)
        patcher.setBoundaryTolerance(pw.Database.getFitTolerance())
        patcher.setUseBoundaryTangency(False)
        
    return surface
