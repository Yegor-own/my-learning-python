import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label = QLabel('ZetCode', self)
        label.move(15, 10)
        label2 = QLabel('Tutorials', self)
        label2.move(35, 40)
        label3 = QLabel('for Beginers', self)
        label3.move(55, 70)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Absolute')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
