    
def setDefault(pw,default="Dimension",value=0):
    pw.Connector.setDefault(default,value)
def setCalculateDimensionMethod(pw,method="Spacing"):
    #"Spacing" "Explicit"
    pw.Connector.setCalculateDimensionMethod(method)
def setCalculateDimensionSpacing(pw,value):
    pw.Connector.setCalculateDimensionSpacing(value)
def setNormalMaximumDeviation(pw,value):
    pw.Connector.setNormalMaximumDeviation(value)
def setCurveMaximumDeviation(pw,value):
    pw.Connector.setCurveMaximumDeviation(value)
def setSurfaceCurvatureInfluence(pw,value=0):
    pw.Connector.setSurfaceCurvatureInfluence(value)
    

def setDefaultDimension(pw,dim=0):
    pw.Connector.setDefault('Dimension',dim)