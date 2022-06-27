# -*- coding: utf-8 -*-
"""
Created on 26.06.2022

Author: Daniel Brems
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QGridLayout
from directional_advice import DirectionWidget, DisplayState
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Widget Example with Grid Layout")
        self.setGeometry(700, 500, 300, 100)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.central_layout = QGridLayout(self)
        self.main_widget.setLayout(self.central_layout)

        self.widget = DirectionWidget(text='H', orientation=Qt.Horizontal, color_1=Qt.red, color_2=Qt.darkRed, parent=self)
        self.widget.setStyleSheet('font-size: 30px; font-weight: 700;')

        self.widget_2 = DirectionWidget(text='E', orientation=Qt.Vertical, parent=self)
        self.widget_2.setStyleSheet('font-size: 25px; font-weight: 700;')

        self.widget_3 = DirectionWidget(text='Y', orientation=Qt.Vertical, color_1=Qt.green, color_2=Qt.darkGreen,
                                      parent=self)
        self.widget.setStyleSheet('font-size:20px; font-weight: 700;')

        self.widget_4 = DirectionWidget(text='!', orientation=Qt.Horizontal, color_1=Qt.magenta, color_2=Qt.darkMagenta,
                                      parent=self)


        # self.widget.setText('1')
        self.widget.setState(DisplayState.NORMAL)
        self.central_layout.addWidget(self.widget, 0, 0)
        self.central_layout.addWidget(self.widget_2, 0, 1)
        self.central_layout.addWidget(self.widget_3, 1, 0)
        self.central_layout.addWidget(self.widget_4, 1, 1)

        self.widget_list = [self.widget, self.widget_2, self.widget_3, self.widget_4]

        self.btn_dec = QPushButton('Decrement')
        self.btn_clear = QPushButton('Clear')
        self.btn_inc = QPushButton('Increment')
        self.btn_ch_text = QPushButton('Change Text')

        # self.btn_text = QPushButton('Change Text')
        # self.btn_text.clicked.connect(change_text)

        self.btn_dec.clicked.connect(self.decrement)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_inc.clicked.connect(self.increment)
        self.btn_ch_text.clicked.connect(self.change_text)

        self.btn_layout = QHBoxLayout()
        self.btn_layout.addWidget(self.btn_dec)
        self.btn_layout.addWidget(self.btn_clear)
        self.btn_layout.addWidget(self.btn_inc)
        self.btn_layout.addWidget(self.btn_ch_text)

        self.central_layout.addLayout(self.btn_layout, 2, 0, 2, 2)

        self.widget.stateChanged.connect(self.print_new_state)
        self.widget_2.stateChanged.connect(self.print_new_state)

        self.widget.textChanged.connect(self.print_new_text)
        self.widget_2.textChanged.connect(self.print_new_text)


    def print_new_state(self, state):
        print('New State: {}'.format(state))

    def print_new_text(self, text):
        print('New Text: {}'.format(text))

    def decrement(self):
        for w in self.widget_list:
            w.decrement()

    def clear(self):
        for w in self.widget_list:
            w.clear()

    def increment(self):
        for w in self.widget_list:
            w.increment()

    def change_text(self):
        for w in self.widget_list:
            if w.text == 'S':
                w.setText('Extra Extra Large Text')
            else:
                w.setText('S')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    # app.setStyleSheet(css.css_slider)
    w.show()
    sys.exit(app.exec_())
