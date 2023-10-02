def getByName(pw,name):
    try:
        return  pw.GridEntity.getByName(name)
    except:
        try:
            return  pw.DatabaseEntity.getByName(name)
        except:
            try:
                return  pw.SourceEntity.getByName(name)
            except:
                None

def getPosition(pw,entity,position,value):
    #position: -grid | -control | '-parameter' | #-arc' | -X | -Y | -Z | -closest >? value
    pos = entity.getPosition(position,value)
# def getPosition(pw,entity,value):
    # #position: -grid | -control | '-parameter' | #-arc' | -X | -Y | -Z | -closest >? value
    # entity.getPosition(value)
    return pos

def getXYZ(pw,entity,position='-closest',value=(0,0,0)):
    if type(entity) == str:
        # if 'con' in entity or 'dom' in entity: 
        try:
            entity = getByName(pw,entity)
        # elif 'curve' in entity or 'surface' in entity: 
            # entity = getByName(pw,'d',entity)
        # elif 'source' in entity:
            # entity = getByName(pw,'s',entity)
        except:
            print("no entity by name: {}".format(entity))
    #$con getXYZ ?< -grid | -control | -parameter | -arc | -X | -Y | -Z | -closest >? value
    XYZ = entity.getXYZ(position,value)
    return XYZ
    
def getParameter(pw,entity,position='-closest',value=(0,0,0)):
    if type(entity) == str:
        try: 
            entity = getByName(pw,'g',entity)
        except:
            try:
                entity = getByName(pw,'d',entity)
            except:
                try:
                    entity = getByName(pw,'s',entity)
                except:
                    print("no entity by name: {}".format(entity))
    #$con getXYZ ?< -grid | -control | -parameter | -arc | -X | -Y | -Z | -closest >? value
    XYZ = entity.getParameter(position,value)
    return XYZ
    
def getByType(pw,Type):
    if Type == 'Block' or Type == 'block' or Type == 'BL' or Type == 'bl' or Type == 'B' or Type == 'b': 
        # return pw.Grid.getAll('-type','Block')
        blks = []
        for blk in pw.Grid.getAll():
            if 'blk' in blk.getName():
                blks.append(blk)
        return blks
    elif Type == 'Connector' or Type == 'connector' or Type == 'C' or Type == 'c' or Type == 'Con' or Type == 'con': 
        # return pw.Grid.getAll('-type','Connector')
        cons = []
        for con in pw.Grid.getAll():
            if 'con' in con.getName():
                cons.append(con)
        return cons
        
    elif Type == 'Curve' or Type == 'curve': 
        # return pw.Database.getAll('-type','Curve')
        curves = []
        for ent in pw.Database.getAll():
            if 'curve' in ent.getName():
                curves.append(ent)
        return curves
        
    elif Type == 'Database' or Type == 'database' or Type == 'DB' or Type == 'db': 
        return pw.Database.getAll()
        
    elif Type == 'Domain' or Type == 'domain' or Type == 'dom' or Type == 'Dom' or Type == 'DM' or Type == 'dm': 
        # return pw.Grid.getAll('-type','Domain')
        doms = []
        for domain in pw.Grid.getAll():
            if 'dom' in domain.getName() or 'farfield' in domain.getName() or 'symmetry' in domain.getName():
                doms.append(domain)
        return doms
        
    elif Type == 'Grid' or Type == 'grid' or Type == 'G' or Type == 'g': 
        return pw.Grid.getAll()
    elif Type == 'Model' or Type == 'model': 
        return pw.Database.getAll('-type','Model')
    elif Type == 'Note' or Type == 'note': 
        return pw.Database.getAll('-type','Note')
    elif Type == 'Plane' or Type == 'plane': 
        return pw.Database.getAll('-type','Plane')
    elif Type == 'Point' or Type == 'point': 
        return pw.Database.getAll('-type','Point')
    elif Type == 'Quilt' or Type == 'quilt': 
        return pw.Database.getAll('-type','Quilt')
    elif Type == 'Shape' or Type == 'shape': 
        return pw.Database.getAll('-type','Shape')
    elif Type == 'Shell' or Type == 'shell': 
        return pw.Database.getAll('-type','Shell')
    elif Type == 'Source' or Type == 'source' or Type == 'S' or Type == 's': 
        return pw.Source.getAll()
    elif Type == 'Surface' or Type == 'surface': 
        # return pw.Database.getAll('-type','Surface')
        surfs = []
        for ent in pw.Database.getAll():
            if 'surface' in ent.getName():
                surfs.append(ent)
        return surfs
    elif Type == 'SurfaceTrim' or Type == 'surfaceTrim': 
        return pw.Database.getAll('-type','SurfaceTrim')    
