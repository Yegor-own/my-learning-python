import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, \
    QGridLayout, \
    QLabel, \
    QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        x = 0
        y = 0
        self.text = f'x:{x}, y:{y}'
        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)
        self.setMouseTracking(True)
        self.setLayout(grid)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Mouse tracking')
        self.show()

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()
        text = f'x:{x}, y:{y}'
        self.label.setText(text)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()