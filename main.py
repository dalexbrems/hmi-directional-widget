import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton
from directional_advice import DirectionWidget, DisplayState
from PyQt5.QtCore import Qt
import css


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Widget Example")
        self.setGeometry(700, 500, 200, 100)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.central_layout = QVBoxLayout(self)
        self.main_widget.setLayout(self.central_layout)

        self.widget = DirectionWidget(text='E', orientation=Qt.Horizontal, parent=self)
        self.widget.setStyleSheet('font-size: 30px; font-weight: 700;'
                                  ' background-color: rgb(13, 147, 214, 0.33);')

        self.widget.setText('Hallo')
        # self.widget.setState(DisplayState.NORMAL)
        self.central_layout.addWidget(self.widget)

        self.btn_dec = QPushButton('Decrement')
        self.btn_clear = QPushButton('Clear')
        self.btn_inc = QPushButton('Increment')

        self.btn_dec.clicked.connect(self.decrement)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_inc.clicked.connect(self.increment)

        self.btn_layout = QHBoxLayout()
        self.btn_layout.addWidget(self.btn_dec)
        self.btn_layout.addWidget(self.btn_clear)
        self.btn_layout.addWidget(self.btn_inc)

        self.central_layout.addLayout(self.btn_layout)

    def decrement(self):
        self.widget.setState(DisplayState.DEC)

    def clear(self):
        self.widget.setState(DisplayState.NORMAL)

    def increment(self):
        self.widget.setState(DisplayState.INC)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    # app.setStyleSheet(css.css_slider)
    w.show()
    sys.exit(app.exec_())
