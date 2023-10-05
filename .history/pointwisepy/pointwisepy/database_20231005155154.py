def trimBySurfaces(pw,ents1,ents2,mode='Both',keep='Both'):
    """
    Trims database entities
    
    Arguments:
    ents1: First group of entities
    ents2: Second group of entities
    mode: 'Both','First' Imprint 'Both' sets of entities on each other, or only first set on second. 
    keep: Which set of entities to keep. 'Inside','Outside','Both' 
    
    Returns:
    List of trimmed entities
    
    """
    return pw.Quilt.trimBySurfaces('-mode',mode,'-keep',keep,ents1,ents2)
    
def interpolate(pw,ent1,ent2,tol=0,orient='Best'):
    """
    Interpolate surface between two database entities
    
    Arguments:
    ents1: First entity
    ents2: Second entity
    tol: Fit tolerance. Optional. Defaults to default tolerance.
    orient:  
    
    Returns:
    List of trimmed entities
    
    """
    try:
        with pw.Application.begin('Create') as creator:
            surf = pw.Surface.create()
            if tol != 0:
                surf.interpolate('-orient',orient,'-tolerance',tol,ent1,ent2)
            else:
                surf.interpolate('-orient',orient,ent1,ent2)
            return surf

    except: 
        print('Error: Could not create interpolated surface')