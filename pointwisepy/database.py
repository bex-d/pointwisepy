
def trimBySurfaces(pw,ents1,ents2,mode='Both',keep='Both'):
    return pw.Quilt.trimBySurfaces('-mode',mode,'-keep',keep,ents1,ents2)
    
def interpolate(pw,ent1,ent2,tol=0,orient='Best'):
    try:
        with pw.Application.begin('Create') as creator:
            surf = pw.Surface.create()
            if tol != 0:
                surf.interpolate('-orient','Best','-tolerance',tol,ents)
            else:
                surf.interpolate('-orient','Best',ent1,ent2)
            return surf

    except: 
        print('Error: Could not create interpolated surface')