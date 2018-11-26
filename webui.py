from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngine import *
from PyQt5.QtWebChannel import *
from PyQt5.QtWebEngineWidgets import *

from MyObjectCls import MyObjectCls

class MainWin(QWebEngineView):
    def __init__(self,main_entry):
        QWebEngineView.__init__(self)
        self.__channel = QWebChannel(self.page())
        self.__my_object = MyObjectCls(self)
        self.__channel.registerObject('MyObject',self.__my_object)
        self.page().setWebChannel(self.__channel)       
        self.__my_object.sigSetParentWindowTitle.connect(self.setWindowTitle)
        self.page().load(QUrl.fromLocalFile(main_entry))

if __name__ == '__main__':
    import sys,os
    app = QApplication(sys.argv)
    main_entry = os.path.realpath(os.path.dirname(__file__) + "/content/index.html") 
    w = MainWin(main_entry)
    w.resize(400,500)
    w.show()
    app.exec_()