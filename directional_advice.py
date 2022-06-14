from PyQt5.QtWidgets import QSlider, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QToolButton, QStyle
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt, QPointF, QRectF
from PyQt5 import QtGui, QtCore, QtWidgets

from enum import Enum


# Todo: style with css
import css

class DisplayState(Enum):
    DOUBLE_INC =  2
    INC        =  1
    NORMAL     =  0
    DEC        = -1
    DOUBLE_DEC = -2


class _ArrowBox(QWidget):
    def __init__(self, orientation, is_inc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._orientation = orientation
        self.is_inc = is_inc

        self.setSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.MinimumExpanding
        )
        
        pal = QtGui.QPalette()
        pal.setColor(QtGui.QPalette.Background, Qt.black); 
        # self.setStyleSheet("background-color:black;")

    def sizeHint(self):
        return QtCore.QSize(70, 80)

    def draw(self):
        pass

    def paintEvent(self, e):
        # self.paint_triangle(e)
        # self.paint_chevron(e)
        self.paint_angle(e)

    def paint_angle(self, e):
            painter = QtGui.QPainter(self)
            painter.begin(self)
            painter.setRenderHint(QtGui.QPainter.Antialiasing)

            pen = QtGui.QPen()
            pen.setColor(QtCore.Qt.darkBlue)
            pen.setWidth(15)
            pen.setCapStyle(Qt.RoundCap)
            pen.setJoinStyle(Qt.MiterJoin)

            painter.setPen(pen)

            width = painter.device().width()
            height = painter.device().height()
            diag_length = (width**2 + height**2)**(1/2)

            # p_width = width - padding
            # p_height = height - padding

            xc = int(width/2)    # x center
            yc = int(height/2)   # y center

            if self.is_inc:
                 # draw first line
                angleLine = QtCore.QLineF()
                angleLine.setP1(QtCore.QPoint(xc, yc))
                angleLine.setAngle(135)
                
                if width < height:
                    angleLine.setLength(0.5 * width)
                elif width >= height:
                    angleLine.setLength(0.5 * height)

                painter.drawLine(angleLine)

                # draw second line
                pen.setColor(QtCore.Qt.blue)
                painter.setPen(pen)

                angleLine = QtCore.QLineF()
                angleLine.setP1(QtCore.QPoint(xc, yc))
                angleLine.setAngle(-135)
                
                if width < height:
                    angleLine.setLength(0.5 * width)
                elif width >= height:
                    angleLine.setLength(0.5 * height)

                painter.drawLine(angleLine)
            
            else:
                # draw first line
                angleLine = QtCore.QLineF()
                angleLine.setP1(QtCore.QPoint(xc, yc))
                angleLine.setAngle(45)
                
                if width < height:
                    angleLine.setLength(0.5 * width)
                elif width >= height:
                    angleLine.setLength(0.5 * height)

                painter.drawLine(angleLine)

                # draw second line
                pen.setColor(QtCore.Qt.blue)
                painter.setPen(pen)

                angleLine = QtCore.QLineF()
                angleLine.setP1(QtCore.QPoint(xc, yc))
                angleLine.setAngle(-45)
                
                if width < height:
                    angleLine.setLength(0.5 * width)
                elif width >= height:
                    angleLine.setLength(0.5 * height)

                painter.drawLine(angleLine)



    def paint_chevron(self, e):
        padding = 20
        painter = QtGui.QPainter(self)
        painter.begin(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)

        pen = QtGui.QPen()
        pen.setColor(QtCore.Qt.darkBlue)
        pen.setWidth(15)
        pen.setCapStyle(Qt.RoundCap)
        pen.setJoinStyle(Qt.MiterJoin)

        painter.setPen(pen)

        # define some points
        width = painter.device().width()
        height = painter.device().height()

        p_width = width - padding
        p_height = height - padding

        xc = int(width/2)    # x center
        yc = int(height/2)   # y center



        # paint the chevron
        # painter.drawLine(width - padding, 0 + padding, 0 + padding, painter.device().height() - padding)
        painter.drawLine(xc, yc, p_width, padding)
        pen.setColor(QtCore.Qt.blue)
        painter.setPen(pen)
        # painter.setBrush(QtCore.Qt.black)
        painter.drawLine(xc, yc, p_width, p_height)


    def paint_triangle(self, e):
        painter = QtGui.QPainter(self)


        # draw background
        brush = QtGui.QBrush()
        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#468faf')
        brush.setColor(color)
        brush.setStyle(Qt.SolidPattern)
        rect = QtCore.QRect(0, 0, painter.device().width(), painter.device().height())
        painter.fillRect(rect, brush)

        padding = 3

        # draw the triangle
        # start_point = QPointF(*((0, painter.device().height()/2 - (padding * 2)) if self._orientation else (painter.device().width() - padding * 2, painter.device().height()/2 - (padding * 2))))        # start_point = QPointF(*((0, painter.device().height()/2 - (padding * 2)) if self._orientation else (painter.device().width() - padding * 2, painter.device().height()/2 - (padding * 2))))
        start_point = QPointF(0 + 2 * padding, painter.device().height()/2)
        path = QtGui.QPainterPath(start_point)
        painter.begin(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setPen(Qt.black)
        painter.setBrush(QtGui.QColor(0, 0, 200, 127))

        path.lineTo(painter.device().width() - 2 * padding, painter.device().height() - 2 * padding)

        path.lineTo(painter.device().width() - 2 * padding, 0 + 2 * padding)

        path.lineTo(0 + 2 * padding, painter.device().height()/2)

        painter.drawPath(path)

    # def paintEvent(self, e):
    #     # if self.direction:
    #     painter = QtGui.QPainter(self)
    #     start_point = QPointF(*((0, painter.device().height()/2) if self._orientation else (painter.device().width(), painter.device().height()/2)))
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
        pass
        pixmap = QtGui.QPixmap(filename)

        # mask = pixmap.createMaskFromColor(QtGui.QColor('black'), Qt.MaskOutColor)
        # # pixmap.fill((QtGui.QColor('red')))
        # pixmap.setMask(mask)

        # self.btNew = QPushButton('Servus', self)
        self.btNew = QToolButton(self)
        self.btNew.setIcon(QtGui.QIcon(pixmap))


class DirectionWidget(QWidget):
    def __init__(self, text='', orientation=Qt.Horizontal, state = DisplayState.NORMAL, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._state = state
        self._orientation = orientation

        if not isinstance(self._orientation, Qt.Orientation):
            # TypeError: unable to convert a Python 'list' object to a C + + 'Qt::Orientation' instance
            raise TypeError('Orientation must be passed as Qt::Orientation instance')

        if self._orientation is Qt.Horizontal:
            self._layout = QHBoxLayout(self)
        else:
            print('Vertical not yet implemented')

        self._lbl_current_state = QLabel(text, self)
        self._lbl_current_state.setMargin(5)
        self._lbl_current_state.setAlignment(Qt.AlignCenter)

        self.inc_arrow = _ArrowBox(self._orientation, is_inc=True)
        self.dec_arrow = _ArrowBox(self._orientation, is_inc=False)

        if self._orientation == Qt.Horizontal:
            self._layout.addStretch()
            self._layout.addWidget(self.dec_arrow)
            self._layout.addWidget(self._lbl_current_state)
            self._layout.addWidget(self.inc_arrow)
            self._layout.addStretch()
        else:
            print('Vertical not yet implemented')

    def paintEvent(self, e):
        if self._state == DisplayState.INC:
            print('Drawing decrease')
            self.inc_arrow.draw()
        elif self._state == DisplayState.DEC:
            print('Drawing increase')
            self.dec_arrow.draw()


    def setStyleSheet(self, styleSheet: str) -> None:
        self._lbl_current_state.setStyleSheet(styleSheet)

    def setText(self, text):
        self._lbl_current_state.setText(text)

    def setState(self, state):
        if not (isinstance(state, DisplayState)):
            raise TypeError('State must be an enum from instance "DisplayState"')
        else:
            self._state = state
            print(f'New State: {state}')

    def increase_state(self):
        # implement if time left
        pass

    def decrease_state(self):
        # implement if time left
        pass

    def clear_state(self):
        # implement if time left
        pass
