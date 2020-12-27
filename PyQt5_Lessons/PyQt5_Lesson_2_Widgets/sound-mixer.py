from PyQt5.QtWidgets import QWidget, \
    QApplication, \
    QSlider, \
    QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        slider = QSlider(Qt.Horizontal, self)
        slider.setFocusPolicy(Qt.NoFocus)
        slider.setGeometry(10, 10, 200, 30)
        slider.valueChanged[int].connect(self.changeValue)
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('img/mute.png'))
        self.label.setGeometry(10, 50, 27, 22)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Window')
        self.show()

    # define sound image setter
    def changeValue(self, value):
        if value == 0:
            self.label.setPixmap(QPixmap('img/mute.png'))
        elif 0 < value <= 30:
            self.label.setPixmap(QPixmap('img/min.png'))
        elif 30 < value <= 80:
            self.label.setPixmap(QPixmap('img/medium.png'))
        else:
            self.label.setPixmap(QPixmap('img/max.png'))

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
