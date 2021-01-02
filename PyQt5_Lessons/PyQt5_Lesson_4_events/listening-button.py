import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('Button 1', self)
        btn.move(10, 10)
        btn2 = QPushButton('Button 2', self)
        btn2.move(10, 50)
        btn.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)
        self.statusBar()
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Signal and slot')
        self.show()

    def buttonClicked(self):
        sends = self.sender()
        self.statusBar().showMessage(sends.text() + 'was pushed')


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()