from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class PyPushButton(QPushButton):
    def __init__(
            self,parent,index,label,led):
        QPushButton.__init__(self)
        # SET DEFAULT PARAMETERS
        self.parent=parent
        self.index =index
        self.led =led
        self.label=label
        self.setMinimumSize(180, 25)
        self.status=False
        self.setStyleSheet(u"QPushButton{\n"
                                     "font: 63 12pt Segoe UI Semibold;\n"
                                     "color: rgb(255,255,255);\n"
                                     "background-color:rgb(100, 100, 100);\n"
                                     "border-radius: 5px;\n"
                                     "border: none;\n"
                                     "}\n"
                                     "QPushButton::hover{\n"
                                     "background-color:rgb(120, 120, 120);\n"
                                     "border-radius: 5px;\n"
                                     "border: none;\n"
                                     "}\n"
                                     )

        self.setText(self.label)
        self.clicked.connect(self.selected)

    def selected(self):
        if(self.status==False):
            if (self.parent.maksSelectedValue < 4):
                self.parent.maksSelectedValue = self.parent.maksSelectedValue + 1
                self.setStyleSheet(u"QPushButton{\n"
                                   "font: 63 12pt Segoe UI Semibold;\n"
                                   "color: rgb(255,255,255);\n"
                                   "background-color: rgb(0, 130, 0);\n"
                                   "border-radius: 5px;\n"
                                   "border: none;\n"
                                   "}\n"
                                   "QPushButton::hover{\n"
                                   "background-color: rgb(0, 150, 0);\n"
                                   "border-radius: 5px;\n"
                                   "border: none;\n"
                                   "}\n"
                                   )

                self.status=True
                self.parent.selectedItems.append(self.label)
        else:
            self.parent.maksSelectedValue = self.parent.maksSelectedValue - 1
            self.setStyleSheet(u"QPushButton{\n"
                               "font: 63 12pt Segoe UI Semibold;\n"
                               "color: rgb(255,255,255);\n"
                               "background-color:rgb(100, 100, 100);\n"
                               "border-radius: 5px;\n"
                               "border: none;\n"
                               "}\n"
                               "QPushButton::hover{\n"
                               "background-color:rgb(120, 120, 120);\n"
                               "border-radius: 5px;\n"
                               "border: none;\n"
                               "}\n"
                               )
            self.status=False
            self.parent.selectedItems.remove(self.label)
        result = ""
        for i in self.parent.selectedItems:
            result=result+i+"-"
        self.parent.loading_ui.label_selectedItems.setText(result)
