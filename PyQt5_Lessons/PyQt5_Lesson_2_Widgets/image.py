from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QApplication
from PyQt5.QtGui import QPixmap
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap('img/atom.jpg')
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        pixmap2 = QPixmap('img/robot.png')
        lbl2 = QLabel(self)
        lbl2.setPixmap(pixmap2)
        hbox.addWidget(lbl2)
        self.setLayout(hbox)
        self.move(300, 200)
        self.setWindowTitle('Image')
        self.show()

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()