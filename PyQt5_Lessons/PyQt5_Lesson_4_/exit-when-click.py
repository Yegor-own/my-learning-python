import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication


class Communicate(QObject):
    close_app = pyqtSignal()


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.c = Communicate()
        self.c.close_app.connect(self.close)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Signal and slot')
        self.show()

    def mousePressEvent(self, event):
        self.c.close_app.emit()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()