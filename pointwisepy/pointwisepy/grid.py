def merge(pw,con1,con2,mode='autoreplace'):
    
    if type(con1) == str:
        con1 = pw.GridEntity.getByName(con1)
    if type(con2) == str:
        con2 = pw.GridEntity.getByName(con2)
            
    with pw.Application.begin('Merge') as merger:
        if mode == 'autoreplace':
            return merger.replace('-automatic',con1,con2)
  
def setConnectorSpacings(pw,cons,spacing,mode='avg'):
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
    if type(ents) == list:
        for ent in ents:
            with pw.Application.begin('Modify',ent) as modifier:
                ent.flipOrientation()
    else:
        with pw.Application.begin('Modify',ents) as modifier:
            ents.flipOrientation()
 
def alignOrientation(pw,master_ent,ents):
    if type(ents) != list:
        ents = [ents]
  
    with pw.Application.begin('Modify',ents) as modifier:
        master_ent.alignOrientation(ents)


def exportGrid(pw,ents,filename,Type='Nastran',LargeWidth=False,FilePrecision='Double'):
    with pw.Application.begin('GridExport',ents) as exporter:
        exporter.initialize('-strict','-type',Type,filename)
        if Type=='Nastran':
            exporter.setAttribute('FileLargeWidthColumns',LargeWidth)
        if Type=='Segment':
            exporter.setAttribute('FilePrecision',FilePrecision)
        exporter.verify()
        exporter.write()
        exporter.end()

def split(pw,ent,params):
    return ent.split(params)