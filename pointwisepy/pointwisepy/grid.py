def merge(pw,con1,con2,mode='auto'):
    """
    Merge two connectors. Returns new connector.
    
    Arguments:
        pw: Requires Pointwise license
        con1: Pointwise object or name as string 
        con2: Pointwise object or name as string 
        mode: 
            'auto': Default. Let Pointwise replace whichever is 'best'.
            'first': Replaces first with second.
    """
    if type(con1) == str:
        con1 = pw.GridEntity.getByName(con1)
    if type(con2) == str:
        con2 = pw.GridEntity.getByName(con2)
            
    with pw.Application.begin('Merge') as merger:
        if mode == 'auto':
            return merger.replace('-automatic',con1,con2)
        elif mode == 'first':
            return merger.replace(con1,con2)
        else:
            print('Incorrect merge mode: {}'.format(mode))
            
  
def setConnectorSpacings(pw,cons,spacing,mode='avg'):
    """
    Set connector spacings or end spacings.
    
    Arguments:
        pw: Requires Pointwise license
        cons: Pointwise object or name as string. Accepts list or individual connectors.
        spacing: Spacing value. Float or integer 
        mode: 
            'avg': Set average spacing on connector
            'begin': Set spacing at start of connector 
            'end': Set spacing at end of connector
            'number': Set number of points on connector
    """
    if mode == 'Average' or mode == 'average' or mode == 'avg' or mode == 'a':
        if type(cons) is list:
            for con in cons:
                if type(con) == str:
                    con = pw.GridEntity.getByName(con)
                con.setDimensionFromSpacing('-resetDistribution',spacing)
        else:
            if type(cons) == str:
                cons = pw.GridEntity.getByName(cons)
            cons.setDimensionFromSpacing('-resetDistribution',spacing)
    elif mode == 'Start' or mode == 'start' or mode == 's' or mode == 'S' or mode == 'Begin' or mode == 'begin' or mode == 'b' or mode == 'B':
        if type(cons) is list:
            for con in cons:
                if type(con) == str:
                    con = pw.GridEntity.getByName(con)
                    
                    with pw.Application.begin('Modify',con) as modifier:   
                        dist = con.getDistribution(1)
                        dist.setBeginSpacing(spacing)
        else:
            if type(cons) == str:
                cons = pw.GridEntity.getByName(cons)
            with pw.Application.begin('Modify',cons) as modifier:   
                dist = cons.getDistribution(1)
                dist.setBeginSpacing(spacing) 
    elif mode == 'End' or mode == 'end' or mode == 'e' or mode == 'E':
        if type(cons) is list:
            for con in cons:
                if type(con) == str:
                    con = pw.GridEntity.getByName(con)
                    
                    with pw.Application.begin('Modify',con) as modifier:   
                        dist = con.getDistribution(1)
                        dist.setEndSpacing(spacing)
        else:
            if type(cons) == str:
                cons = pw.GridEntity.getByName(cons)
            with pw.Application.begin('Modify',cons) as modifier:   
                dist = cons.getDistribution(1)
                dist.setEndSpacing(spacing)       
            
    elif mode == 'Number' or mode == 'number' or mode == 'num' or mode == 'n':
        if type(cons) is list:
            for con in cons:
                if type(con) == str:
                    con = pw.GridEntity.getByName(con)
                    
                    with pw.Application.begin('Modify',con) as modifier:   
                        # dist = con.getDistribution(1)
                        dist.setDimensionFromSpacing(spacing)
        else:
            if type(cons) == str:
                cons = pw.GridEntity.getByName(cons)
            with pw.Application.begin('Modify',cons) as modifier:   
                # dist = cons.getDistribution(1)
                dist.setDimension(spacing)       
            
    

    else: 
        print('Incorrect connector spacing mode: {}, options are ["Average","Begin","End","Number"]'.format(mode))
        

def join(pw,ents):
    """
    Join two entities.
    
    Arguments:
        pw: Requires Pointwise license
        ents: List of Pointwise objects.
    """
    
    try:
        joinedEnts = pw.BlockStructured.join(ents)
    except:
        None
    try:
        joinedEnts = pw.BlockUnstructured.join(ents)
    except:
        None
    try:
        joinedEnts = pw.Connector.join(ents)
    except:
        None
    try:
        joinedEnts = pw.Curve.join(ents)
    except:
        None
    try:
        joinedEnts = pw.DomainStructured.join(ents)
    except:
        None
    try:
        joinedEnts = pw.DomainUnstructured.join(ents)
    except:
        None
        
    try:
        joinedEnts = pw.Shell.join(ents)
    except:
        None
        
    try:
        joinedEnts = pw.SourceCurve.join(ents)
    except:
        None
        
    try:
        joinedEnts = pw.Surface.join(ents)
    except:
        None
        
    return joinedEnts
    
def orient(pw,ents):
    """
    Orient entities.
    
    Arguments:
        pw: Requires Pointwise license
        ents: Pointwise object or list of objects.
    """
    if type(ents) == list:
        for ent in ents:
            with pw.Application.begin('Modify',ent) as modifier:
                ent.flipOrientation()
    else:
        with pw.Application.begin('Modify',ents) as modifier:
            ents.flipOrientation()
 
def alignOrientation(pw,main_ent,ents):
    """
    Align orientation of entities to match one entity. Not always accurate, check orientation manually in GUI.
    
    Arguments:
        pw: Requires Pointwise license
        main_ent: Pointwise object. Entity to match orientation to.
        ents: Pointwise object or list of objects to re-orient.
    """
    if type(ents) != list:
        ents = [ents]
  
    with pw.Application.begin('Modify',ents) as modifier:
        main_ent.alignOrientation(ents)


def exportGrid(pw,ents,filename,Type='Nastran',LargeWidth=False,FilePrecision='Double'):
    """
    Export grid entities to file. Default settings suitable for NastranToFro conversion.
    
    Arguments:
        pw: Requires Pointwise license
        ents: Pointwise object or list of objects.
        filename: Directory and filename to save to. Include extension.
        Type: file type. 'Nastran' (default), 'Automatic','Gridgen','IGES','STL','GridPro','VRML','VRML97','PLOT3D','Segment','Patran','UCD','Xpatch','FVUNS','FVUNS30','CGNS','CGNS-STRUCT','CGNS-UNSTR'
    """
    with pw.Application.begin('GridExport',ents) as exporter:
        exporter.initialize('-strict','-type',Type,filename)
        if Type=='Nastran':
            exporter.setAttribute('FileLargeWidthColumns',LargeWidth)
        if Type=='Segment':
            exporter.setAttribute('FilePrecision',FilePrecision)
        exporter.verify()
        exporter.write()
        exporter.end()
        print('Exported grid as {} to {}'.format(Type,filename))

def split(pw,ent,params):
    """
    Split entities.
    
    Arguments:
        pw: Requires Pointwise license
        ent: Pointwise object.
        params: Float between 0 and 1. Specifics for each object type can be found under Glyph function 'split' (https://pointwise.com/doc/glyph2/index/Functions16.html#S)
    """
    return ent.split(params)