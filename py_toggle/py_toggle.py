from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class PyToggle(QCheckBox):
    def __init__(self,
                 width=50,
                 bg_color="#777",
                 circle_color ="#DDD",
                 active_color = "#00BCff",
                 animation_curve = QEasingCurve.OutBounce ):
        QCheckBox.__init__(self)
        # SET DEFAULT PARAMETERS#

        self.setFixedSize(width,20)
        self.setCursor(Qt.PointingHandCursor)

        #COLORS
        self._bg_color = bg_color
        self._circle_color =circle_color
        self._active_color =active_color

        #CREATE ANİMATİON
        self._circle_position=3
        self.animation = QPropertyAnimation(self,b"circle_position",self)
        self.animation.setEasingCurve(animation_curve)
        self.animation.setDuration(500)

        self.stateChanged.connect(self.start_transition)

        #CREATE NEW SET AND GET PROPERTIE
    @Property(float) #GET
    def circle_position(self):
        return self._circle_position

    @circle_position.setter
    def circle_position(self,pos):
        self._circle_position=pos
        self.update()


    def start_transition(self,value):
        self.animation.stop()
        if value:
            self.animation.setEndValue(self.width()-20)
        else:
            self.animation.setEndValue(3)
        self.animation.start()
        print(f"status: {self.isChecked()}")

    #SET NEW HİT AREA
    def hitButton(self, pos:QPoint):
        return self.contentsRect().contains(pos)

    #DRAW NEW ITEM



    def paintEvent(self, e):
        #SET PAINTER
        p=QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        #SET AS NO PEN
        p.setPen(Qt.NoPen)
        rect = QRect(0,0,self.width(),self.height())

        #CHECK IF IS CHECKED
        if not self.isChecked():
            # DRAW BG
            p.setBrush((QColor(self._bg_color)))
            p.drawRoundedRect(0, 0, rect.width(), self.height(), self.height() / 2, self.height() / 2)

            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(self._circle_position, 3, 15, 15)
        else:
            # DRAW BG
            p.setBrush((QColor(self._active_color)))
            p.drawRoundedRect(0, 0, rect.width(), self.height(), self.height() / 2, self.height() / 2)

            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(self._circle_position, 3, 15, 15)
        #END DRAW
        p.end()

