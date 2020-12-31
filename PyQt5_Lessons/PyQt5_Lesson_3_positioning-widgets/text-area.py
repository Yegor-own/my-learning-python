import sys
from PyQt5.QtWidgets import QMainWindow, \
    QApplication, \
    QAction, \
    QTextEdit
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        text_edit = QTextEdit()
        self.setCentralWidget(text_edit)
        exit_act = QAction(QIcon('img/exit.svg'), 'Exit', self)
        exit_act.setShortcut('Ctrl+q')
        exit_act.setStatusTip('Exit application')
        exit_act.triggered.connect(self.close)
        self.statusBar()
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(exit_act)
        tool_bar = self.addToolBar('exit')
        tool_bar.addAction(exit_act)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Context Menu')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
