import sys
from PyQt5.QtWidgets import \
    QApplication, \
    QMainWindow, \
    QToolTip, \
    QPushButton, \
    QMessageBox, \
    QDesktopWidget, \
    QAction, \
    qApp

from PyQt5.QtGui import QFont, QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # define top menu
        exitAct = QAction(QIcon('exit.svg'), '&Exit', self)
        exitAct.setShortcut('Ctrl+q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)
        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        # define status bar
        self.statusBar().showMessage('Ready')
        # define font
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is widget <b> QWidget </b>')
        # define button
        btn = QPushButton('Quit', self)
        btn.clicked.connect(QApplication.instance().quit)
        btn.setToolTip('This is a widget <b> QPushButton </b>')
        btn.resize(btn.sizeHint())
        btn.move(113, 89)
        # set geometry
        # you can do it like this
        # self.setGeometry(300, 300, 300, 200)
        # or like this
        self.resize(300, 200)
        self.centre()
        # define window title
        self.setWindowTitle('Tooltip')
        # define window icon
        self.setWindowIcon(QIcon('robot.png'))
        self.show()

    # set window in centre of the screen
    def centre(self):
        qr = self.frameGeometry()
        # set centre point
        cp = QDesktopWidget().availableGeometry().center()
        # move app to centre
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # question user, want he to exit or not
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     'Are you sure to exit?',
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
