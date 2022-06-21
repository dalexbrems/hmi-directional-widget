# -*- coding: utf-8 -*-
"""
Created on 15.04.2022

Author: Daniel Brems
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton
from directional_advice import DirectionWidget, DisplayState
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Widget Example")
        self.setGeometry(700, 500, 300, 100)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.central_layout = QVBoxLayout(self)
        self.main_widget.setLayout(self.central_layout)

        self.widget = DirectionWidget(text='Extra Extra Large Text', orientation=Qt.Horizontal, parent=self)
        self.widget.setStyleSheet('font-size: 30px; font-weight: 700;')

        self.widget_2 = DirectionWidget(text='E', orientation=Qt.Vertical, parent=self)
        self.widget_2.setStyleSheet('font-size: 30px; font-weight: 700;')

        # self.widget.setText('1')
        self.widget.setState(DisplayState.NORMAL)
        self.central_layout.addWidget(self.widget_2)
        self.central_layout.addWidget(self.widget)

        self.btn_dec = QPushButton('Decrement')
        self.btn_clear = QPushButton('Clear')
        self.btn_inc = QPushButton('Increment')

        # self.btn_text = QPushButton('Change Text')
        # self.btn_text.clicked.connect(change_text)

        self.btn_dec.clicked.connect(self.decrement)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_inc.clicked.connect(self.increment)

        self.btn_layout = QHBoxLayout()
        self.btn_layout.addWidget(self.btn_dec)
        self.btn_layout.addWidget(self.btn_clear)
        self.btn_layout.addWidget(self.btn_inc)

        self.central_layout.addLayout(self.btn_layout)

        self.widget.stateChanged.connect(self.print_new_state)
        self.widget_2.stateChanged.connect(self.print_new_state)

        self.widget.textChanged.connect(self.print_new_text)
        self.widget_2.textChanged.connect(self.print_new_text)

    # def change_text(self):
    #     if self.widget.

    def print_new_state(self, state):
        print('New State: {}'.format(state))

    def print_new_text(self, text):
        print('New Text: {}'.format(text))

    def decrement(self):
        self.widget.decrement()
        self.widget_2.decrement()

    def clear(self):
        self.widget.clear()
        self.widget_2.clear()

    def increment(self):
        self.widget.increment()
        self.widget_2.increment()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    # app.setStyleSheet(css.css_slider)
    w.show()
    sys.exit(app.exec_())
