class Parameters:

    __instance = None
    
    def __init__(self):
        if Parameters.__instance == None:
            self.resolutionDPI = "200"
            self.backgroundColour = "#33363D"
            self.textColour = "white"
            self.margins = "1"
            self.opacity = "1"
            Parameters.__instance = self

    @staticmethod
    def getInstance():
        return Parameters.__instance
    
    @staticmethod
    def getResolution():
        return Parameters.__instance.resolutionDPI

    @staticmethod
    def getBackgroundColour():
        return Parameters.__instance.backgroundColour

    @staticmethod
    def getTextcolour():
        return Parameters.__instance.textColour

    @staticmethod
    def getMargin():
        return Parameters.__instance.margins

    @staticmethod
    def getOpacity():
        return Parameters.__instance.opacity

    def setResolution(res):
        Parameters.__instance.resolutionDPI = res

    def setBackgroundColour(bgc):
        Parameters.__instance.backgroundColour = bgc

    def setTextcolour(tc):
        Parameters.__instance.textColour = tc

    def setMargin(mar):
        Parameters.__instance.margins = mar

    def setOpacity(op):
        Parameters.__instance.opacity = op




Parameters()
def getResolution():
    return Parameters.getResolution()

def getBackgroundColour():
    return Parameters.getBackgroundColour()

def getTextcolour():
    return Parameters.getTextcolour()

def getMargin():
    return Parameters.getMargin()

def getOpacity():
    return Parameters.getOpacity()

def setResolution(res):
    Parameters.setResolution(res=res)

def setBackgroundColour(bgc):
    Parameters.setBackgroundColour(bgc=bgc)

def setTextcolour(tc):
    Parameters.setTextcolour(tc=tc)

def setMargin(mar):
    Parameters.setMargin(mar=mar)

def setOpacity(op):
    Parameters.setOpacity(op=op)