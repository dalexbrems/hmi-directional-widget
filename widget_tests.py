from PyQt5.QtWidgets import QSlider, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QToolButton, QStyle
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt, QPointF, QRectF
from PyQt5 import QtGui, QtCore

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tuner Widget Example")
        self.setGeometry(700, 500, 200, 100)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.central_layout = QVBoxLayout(self)
        self.main_widget.setLayout(self.central_layout)

        self.test_widget = QLabel()
        self.test_widget.setStyleSheet('font-size: 30px; font-weight: 700;'
                                              ' background-color: rgb(13, 147, 214, 0.33);')
        self.central_layout.addWidget(self.test_widget)

        self.second = QLabel('Jetza')
        self.central_layout.addWidget(self.second)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    # app.setStyleSheet(css.css_slider)
    w.show()
    sys.exit(app.exec_())
