from krita import *

class Resizer(Extension):
    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        pass
    
    def canvas(self):
        app = Krita.instance() 
        currentDocument = app.activeDocument()
        print(currentDocument)
        currentHeight = currentDocument.height()
        currentDocument.resizeImage(0,0,900,currentHeight + 900)
        print(currentHeight)

    #def createAction(self, window):
    #    action = window.createAction("myAction", "My Script")
    #    action.triggered.connect(self.canvas)
    
    def createActions(self, window):
        action = window.createAction("myResizeAction", "Resize")
        action.triggered.connect(self.canvas)

Krita.instance().addExtension(Resizer(Krita.instance()))
