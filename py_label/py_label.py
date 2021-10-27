from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class PyLabel(QFrame):
    def __init__(self,index,x,y,z):
        QFrame.__init__(self)
        # SET DEFAULT PARAMETERS
        self.setMinimumSize(200,50)
        self.x = x
        self.y = y
        self.z = z
        self.setStyleSheet("background:none;")
        self.label = QLabel("{}. X: {} Y: {} Z: {}".format(index,x,y,z))
        self.label.setAlignment(Qt.AlignCenter)
        if(index%2==0):
            self.label.setStyleSheet(u"QLabel{\n"
                                                    "font: 63 10pt Segoe UI Semibold;\n"
                                                    "color: rgb(255,255,255);\n"
                                                    "background-color:rgba(200, 200, 200, 100);\n"
                                                    "border-radius: 3px;\n"
                                                    "border: none;\n"
                                                    "}\n"
                                                    )
        else:
            self.label.setStyleSheet(u"QLabel{\n"
                                     "font: 63 10pt Segoe UI Semibold;\n"
                                     "color: rgb(255,255,255);\n"
                                     "background-color:rgba(200, 200, 200, 150);\n"
                                     "border-radius: 3px;\n"
                                     "border: none;\n"
                                     "}\n"
                                     )
        self.label.setMinimumSize(200,25)
        self.label.setMaximumSize(200,25)
        self.layoutV = QVBoxLayout()
        self.layoutV .addWidget(self.label,Qt.AlignCenter,Qt.AlignCenter)
        self.setLayout(self.layoutV )

