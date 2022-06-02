from PyQt5.QtWidgets import QSlider, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QToolButton, QStyle
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt, QPointF, QRectF
from PyQt5 import QtGui, QtCore

from enum import Enum


# Todo: style with css
import css

class DisplayState(Enum):
    DOUBLE_INC =  2
    INC        =  1
    NORMAL     =  0
    DEC        = -1
    DOUBLE_DEC = -2


class _Arrow(QWidget):
    def __init__(self, orientation, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.orientation = orientation

    # def paintEvent(self, e):
    #     painter = QtGui.QPainter(self)
    #     brush = QtGui.QBrush()
    #     brush.setColor(QtGui.QColor('black'))
    #     brush.setStyle(Qt.SolidPattern)
    #     rect = QtCore.QRect(0, 0, painter.device().width(), painter.device().height())
    #     painter.fillRect(rect, brush)
    #     self.set_icon('right.bmp')

    # def paintEvent(self, e):
    #     # if self.direction:
    #     painter = QtGui.QPainter(self)
    #     start_point = QPointF(*((0, painter.device().height()/2) if self.direction else (painter.device().width(), painter.device().height()/2)))
    #     path = QtGui.QPainterPath(start_point)
    #     painter.begin(self)
    #     painter.setRenderHint(QtGui.QPainter.Antialiasing)
    #     painter.setPen(Qt.black)
    #     painter.setBrush(QtCore.Qt.green)
    #
    #     path.lineTo(painter.device().width(), painter.device().height())
    #
    #     path.lineTo(painter.device().width(), 0)
    #
    #     path.lineTo(0, painter.device().height()/2)
    #
    #     painter.drawPath(path)

    # def paintEvent(self, e):
    #     painter = QtGui.QPainter(self)
    #     target = QRectF(10.0, 20.0, 80.0, 60.0)
    #     source = QRectF(0.0, 0.0, 1000.0, 1000.0)
    #     pixmap = QtGui.QPixmap('right.bmp')

    #       painter.drawPixmap(target, pixmap, source)

    def set_icon(self, filename):
        pixmap = QtGui.QPixmap(filename)

        # mask = pixmap.createMaskFromColor(QtGui.QColor('black'), Qt.MaskOutColor)
        # # pixmap.fill((QtGui.QColor('red')))
        # pixmap.setMask(mask)

        # self.btNew = QPushButton('Servus', self)
        self.btNew = QToolButton(self)
        self.btNew.setIcon(QtGui.QIcon(pixmap))


class DirectionWidget(QWidget):
    def __init__(self, text='', orientation=Qt.Horizontal, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not isinstance(orientation, Qt.Orientation):
            # TypeError: unable to convert a Python 'list' object to a C + + 'Qt::Orientation' instance
            raise TypeError('Orientation must be passed as Qt::Orientation instance')

        if orientation is Qt.Horizontal:
            self._layout = QHBoxLayout(self)
        else:
            print('Vertical not yet implemented')

        self._lbl_current_state = QLabel(text, self)
        self._lbl_current_state.setAlignment(Qt.AlignCenter)

        self.arrow = _Arrow(orientation)
        # self.decrement_arrow = _Arrow(1)

        self._layout.addWidget(self.decrement_arrow)
        self._layout.addWidget(self._lbl_current_state)
        self._layout.addWidget(self.increment_arrow)

    def setStyleSheet(self, styleSheet: str) -> None:
        self._lbl_current_state.setStyleSheet(styleSheet)

    def setText(self, text):
        self._lbl_current_state.setText(text)

    def setState(self, state):
        if not (isinstance(state, DisplayState) or isinstance(state, int)):
            raise TypeError('State must be an enum from instance "DisplayState"')
        # Todo: check the int here



