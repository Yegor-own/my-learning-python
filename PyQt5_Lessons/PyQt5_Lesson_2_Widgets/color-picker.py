from PyQt5.QtWidgets import QWidget, \
    QPushButton, \
    QFrame, \
    QApplication
from PyQt5.QtGui import QColor
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # define default color
        self.col = QColor(0, 0, 0)

        # define red button
        redbtn = QPushButton('Red', self)
        redbtn.setCheckable(True)
        redbtn.move(10, 10)
        redbtn.clicked[bool].connect(self.setColor)

        # define green button
        greenbtn = QPushButton('Green', self)
        greenbtn.setCheckable(True)
        greenbtn.move(10, 60)
        greenbtn.clicked[bool].connect(self.setColor)

        # define blue button
        bluebtn = QPushButton('Blue', self)
        bluebtn.setCheckable(True)
        bluebtn.move(10, 110)
        bluebtn.clicked[bool].connect(self.setColor)

        # define frame with color of clicked button
        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget {background-color: %s}" % self.col.name())

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Window')
        self.show()

    def setColor(self, pressed):
        source = self.sender()
        if pressed:
            val = 255
        else:
            val = 0
        if source.text() == 'Red':
            self.col.setRed(val)
        elif source.text() == 'Green':
            self.col.setGreen(val)
        elif source.text() == 'Blue':
            self.col.setBlue(val)
        self.square.setStyleSheet("QWidget {background-color: %s}" % self.col.name())

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
