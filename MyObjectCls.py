#MyObjectCls.py
from PyQt5.QtCore import *

class MyObjectCls(QObject):
    sigSetParentWindowTitle = pyqtSignal(str)
    
    def __init__(self,parent=None):
        QObject.__init__(self,parent)
    @pyqtSlot(str)
    def consolePrint(self,msg):
        print(msg)
    @pyqtSlot(str)
    def setParentWindowTitle(self,msg):
        self.sigSetParentWindowTitle.emit(msg)
    @pyqtSlot(str,str)
    def saveFile(self,content,fileName):
        with open(str(fileName),"w") as fp:
            fp.write(str(content))