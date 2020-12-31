import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, qApp, QMenu


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Context Menu')
        self.show()

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        new_act = cmenu.addAction('New')
        open_act = cmenu.addAction('Open')
        quit_act = cmenu.addAction('Quit')
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        if action == quit_act:
            qApp.quit()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
