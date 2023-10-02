
def ExtrusionSolver(pw,ents,mode,parameters,setKeepFailingStep=1):
    # parameters: rotate: [RotateAxisStart,RotateAngle,steps,RotateAxisEnd (optional)]
    #mode: 'Rotate'
    with pw.Application.begin('Create') as create:
        edge = pw.Edge.createFromConnectors(ents)
        dom = pw.DomainStructured.create()
        dom.addEdge(edge)
        
    with pw.Application.begin('ExtrusionSolver',dom) as extrude:
        extrude.setKeepFailingStep(setKeepFailingStep)
        dom.setExtrusionSolverAttribute('Mode',mode)
        dom.setExtrusionSolverAttribute('RotateAxisStart',parameters[0])
        dom.setExtrusionSolverAttribute('RotateAngle',parameters[1])
        if len(parameters)==4:
            dom.setExtrusionSolverAttribute('RotateAxisEnd',parameters[3])
        extrude.run(parameters[2])
        
        return dom