import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from directional_advice import DirectionWidget, DisplayState
from PyQt5.QtCore import Qt
import css


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tuner Widget Example")
        self.setGeometry(700, 500, 200, 100)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.central_layout = QVBoxLayout(self)
        self.main_widget.setLayout(self.central_layout)

        self.widget = DirectionWidget(text='E', orientation=Qt.Horizontal, parent=self)
        self.widget.setStyleSheet('font-size: 30px; font-weight: 700;'
                                  ' background-color: rgb(13, 147, 214, 0.33);')

        self.widget.setText('Hallo')
        self.widget.setState(1)
        self.central_layout.addWidget(self.widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    # app.setStyleSheet(css.css_slider)
    w.show()
    sys.exit(app.exec_())
