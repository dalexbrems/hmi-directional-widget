# -*- coding: utf-8 -*-
"""
Created on 15.04.2022

Author: Daniel Brems
"""

from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QLabel
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5 import QtGui, QtCore, QtWidgets

from enum import IntEnum

# Todo: style with css
import css


class DisplayState(IntEnum):
    """Defines the possible states for the widget"""
    DOUBLE_INC = 2
    INC = 1
    NORMAL = 0
    DEC = -1
    DOUBLE_DEC = -2


class _ArrowBox(QWidget):
    """Widget that acts as a canvas to draw the chevrons onto"""
    def __init__(self, orientation, is_inc, color_1, color_2, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._orientation = orientation
        self._is_inc = is_inc
        self._is_double = False

        self._color_1 = color_1
        self._color_2 = color_2

        # this makes the ArrowBox still use it's space, even when no chevron is drawn
        self.setSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.MinimumExpanding
        )

        # define offsets and rotations depending on the orientation of the whole widget
        if orientation == Qt.Horizontal:
            self.rotation = 0
            self.x_offset = 40
            self.y_offset = 0
        elif orientation == Qt.Vertical:
            self.rotation = 90
            self.x_offset = 0
            self.y_offset = -40

    def sizeHint(self):
        return QtCore.QSize(100, 100)

    def setDouble(self, b):
        """flag for indicating if double or single chevron should be drawn"""
        self._is_double = b

    def paintEvent(self, e):
        """overriding parents paint event for intelligent redrawing of the arrows. See Qt Docs"""
        self.paint_angle()

    def paint_angle(self):
        """paints one or two chevrons with the respective orientation on the canvas"""
        painter = QtGui.QPainter(self)

        # enable antialiasing to prevent artifacts ("Jaggies")
        painter.setRenderHint(QtGui.QPainter.Antialiasing)

        pen = QtGui.QPen()
        pen.setColor(self._color_1)
        pen.setWidth(12)
        pen.setCapStyle(Qt.SquareCap)
        pen.setJoinStyle(Qt.MiterJoin)

        painter.setPen(pen)

        width = painter.device().width()
        height = painter.device().height()

        # diag_length = (width ** 2 + height ** 2) ** (1 / 2)
        # p_width = width - padding
        # p_height = height - padding

        xc = int(width / 2)  # x center
        yc = int(height / 2)  # y center

        if self._is_inc:
            #  first chevron draw first line
            angleLine = QtCore.QLineF()
            angleLine.setP1(QtCore.QPoint(xc, yc))
            angleLine.setAngle(135 + self.rotation)

            if width < height:
                angleLine.setLength(0.5 * width)
            elif width >= height:
                angleLine.setLength(0.5 * height)

            painter.drawLine(angleLine)

            # first chevron draw second line
            pen.setColor(self._color_2)
            painter.setPen(pen)

            angleLine = QtCore.QLineF()
            angleLine.setP1(QtCore.QPoint(xc, yc))
            angleLine.setAngle(-135 + self.rotation)

            if width < height:
                angleLine.setLength(0.5 * width)
            elif width >= height:
                angleLine.setLength(0.5 * height)

            painter.drawLine(angleLine)

            if self._is_double:

                # second chevron draw first line
                angleLine = QtCore.QLineF()
                angleLine.setP1(QtCore.QPoint(xc + self.x_offset, yc + self.y_offset))
                angleLine.setAngle(135 + self.rotation)

                if width < height:
                    angleLine.setLength(0.5 * width)
                elif width >= height:
                    angleLine.setLength(0.5 * height)

                pen.setColor(self._color_1)
                painter.setPen(pen)

                painter.drawLine(angleLine)

                # second chevron draw second line
                pen.setColor(self._color_2)
                painter.setPen(pen)

                angleLine = QtCore.QLineF()
                angleLine.setP1(QtCore.QPoint(xc + self.x_offset, yc + self.y_offset))
                angleLine.setAngle(-135 + self.rotation)

                if width < height:
                    angleLine.setLength(0.5 * width)
                elif width >= height:
                    angleLine.setLength(0.5 * height)

                pen.setColor(self._color_2)
                painter.setPen(pen)

                painter.drawLine(angleLine)

        else:
            # draw first line
            angleLine = QtCore.QLineF()
            angleLine.setP1(QtCore.QPoint(xc, yc))
            angleLine.setAngle(45 + self.rotation)

            if width < height:
                angleLine.setLength(0.5 * width)
            elif width >= height:
                angleLine.setLength(0.5 * height)

            painter.drawLine(angleLine)

            # draw second line
            pen.setColor(self._color_2)
            painter.setPen(pen)

            angleLine = QtCore.QLineF()
            angleLine.setP1(QtCore.QPoint(xc, yc))
            angleLine.setAngle(-45 + self.rotation)

            if width < height:
                angleLine.setLength(0.5 * width)
            elif width >= height:
                angleLine.setLength(0.5 * height)

            painter.drawLine(angleLine)

            if self._is_double:
                # second chevron draw first line
                angleLine = QtCore.QLineF()
                angleLine.setP1(QtCore.QPoint(xc - self.x_offset, yc - self.y_offset))
                angleLine.setAngle(45 + self.rotation)

                if width < height:
                    angleLine.setLength(0.5 * width)
                elif width >= height:
                    angleLine.setLength(0.5 * height)

                pen.setColor(self._color_1)
                painter.setPen(pen)

                painter.drawLine(angleLine)

                # second chevron second line
                angleLine = QtCore.QLineF()
                angleLine.setP1(QtCore.QPoint(xc - self.x_offset, yc - self.y_offset))
                angleLine.setAngle(-45 + self.rotation)

                if width < height:
                    angleLine.setLength(0.5 * width)
                elif width >= height:
                    angleLine.setLength(0.5 * height)

                pen.setColor(self._color_2)
                painter.setPen(pen)

                painter.drawLine(angleLine)


class DirectionWidget(QWidget):
    """directional widget for indicating the user a increment or decrement in state"""
    # signals need to be defined as class variables

    textChanged = pyqtSignal(str)
    stateChanged = pyqtSignal(DisplayState)

    def __init__(self, text='', orientation=Qt.Horizontal, state=DisplayState.NORMAL, color_1=QtCore.Qt.darkBlue,
                 color_2=QtCore.Qt.blue, background_color=None,  *args, **kwargs):
        super().__init__(*args, **kwargs)

        # member variables
        self._state = state
        self._orientation = orientation
        self._color_1 = color_1
        self._color_2 = color_2
        self._background_color = background_color

        # sanity check for orientation
        if not isinstance(self._orientation, Qt.Orientation):
            raise TypeError('unable to convert a Python ' + str(type(self._orientation)) +
                            ' object to a C++ \'Qt::Orientation\' instance')

        # choose layout according to orientation
        if self._orientation is Qt.Horizontal:
            self._layout = QHBoxLayout(self)
        else:
            self._layout = QVBoxLayout(self)

        self._lbl_current_state = QLabel(text, self)
        self._lbl_current_state.setMargin(5)
        self._lbl_current_state.setAlignment(Qt.AlignCenter)

        # create two ArrowBox instances for displaying the chevrons
        self.inc_arrow = _ArrowBox(self._orientation, is_inc=True, color_1=self._color_1, color_2=self._color_2)
        self.dec_arrow = _ArrowBox(self._orientation, is_inc=False, color_1=self._color_1, color_2=self._color_2)

        # first, dont show any chevrons by disabling updates for the ArrowBoxes
        self.inc_arrow.setUpdatesEnabled(False)
        self.dec_arrow.setUpdatesEnabled(False)

        # choose widget order according to orientation
        if self._orientation == Qt.Horizontal:
            self._layout.addStretch()
            self._layout.addWidget(self.dec_arrow)
            self._layout.addWidget(self._lbl_current_state)
            self._layout.addWidget(self.inc_arrow)
            self._layout.addStretch()
        else:
            self._layout.addStretch()
            self._layout.addWidget(self.inc_arrow)
            self._layout.addWidget(self._lbl_current_state)
            self._layout.addWidget(self.dec_arrow)
            self._layout.addStretch()

    def setStyleSheet(self, styleSheet: str) -> None:
        self._lbl_current_state.setStyleSheet(styleSheet)

    def setText(self, text):
        """Set a new text for the center label of the widget"""
        self._lbl_current_state.setText(text)
        self.textChanged.emit(text)

    def setState(self, state):
        """set a new state for the widget. State must be of type DisplayState"""
        if not (isinstance(state, DisplayState)):
            raise TypeError('State must be an enum of type "DisplayState"')
        else:
            self._state = state

            # emit a stateChange signal with the new state
            self.stateChanged.emit(self._state)
            if self._state == DisplayState.DOUBLE_INC:
                # print('Drawing double inc')
                self.inc_arrow.setDouble(True)
                self.inc_arrow.setUpdatesEnabled(True)
                self.dec_arrow.setUpdatesEnabled(False)
            if self._state == DisplayState.INC:
                # print('Drawing inc')
                self.inc_arrow.setDouble(False)
                self.inc_arrow.setUpdatesEnabled(True)
                self.dec_arrow.setUpdatesEnabled(False)
            elif self._state == DisplayState.NORMAL:
                self.dec_arrow.setUpdatesEnabled(False)
                self.inc_arrow.setUpdatesEnabled(False)
            elif self._state == DisplayState.DOUBLE_DEC:
                # print('Drawing dec')
                self.dec_arrow.setDouble(True)
                self.dec_arrow.setUpdatesEnabled(True)
                self.inc_arrow.setUpdatesEnabled(False)
            elif self._state == DisplayState.DEC:
                # print('Drawing double dec')
                self.dec_arrow.setDouble(False)
                self.dec_arrow.setUpdatesEnabled(True)
                self.inc_arrow.setUpdatesEnabled(False)
            self.update()

    def setColor(self, color):
        # if not isinstance(color, ...)
        pass

    def increment(self):
        """increment the current state by one. If max state is reached, nothing will happen."""
        s = self._state
        if s.value < 2:
            new_state = DisplayState(s + 1)
            self.setState(new_state)

    def decrement(self):
        """decrement the current state by one. If min state is reached, nothing will happen."""
        s = self._state
        if s.value > -2:
            new_state = DisplayState(self._state.value - 1)
            self.setState(new_state)

    def clear(self):
        """clear the current state (no direction is shown)"""
        self.setState(DisplayState.NORMAL)
