from PyQt5.QtWidgets import QWidget, \
    QPushButton, \
    QApplication, \
    QProgressBar
from PyQt5.QtCore import QBasicTimer
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.progressbar = QProgressBar(self)
        self.progressbar.setGeometry(10, 10, 200, 15)
        self.button = QPushButton('Start', self)
        self.button.move(10, 30)
        self.button.clicked.connect(self.doAction)
        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Window')
        self.show()

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.button.setText('Finished')
            return
        self.step = self.step + 1
        self.progressbar.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.button.setText('Start')
        else:
            self.timer.start(100, self)
            self.button.setText('Stop')


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
