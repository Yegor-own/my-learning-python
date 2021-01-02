import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # define status bar
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')
        # define menu bar
        menubar = self.menuBar()
        view_menu = menubar.addMenu('View')
        view_stat_act = QAction('View status', self, checkable=True)
        view_stat_act.setChecked(True)
        view_stat_act.triggered.connect(self.toggleMenu)
        view_menu.addAction(view_stat_act)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Check Menu')
        self.show()

    def toggleMenu(self, state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
