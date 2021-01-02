from PyQt5.QtWidgets import QMainWindow, \
    QTextEdit, \
    QAction, \
    QFileDialog, \
    QApplication
from PyQt5.QtGui import QIcon
import sys
from pathlib import Path


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)
        self.statusBar()
        open_file = QAction(QIcon('img/open.png'), 'Open', self)
        open_file.setStatusTip('Open new File')
        open_file.triggered.connect(self.showDialog)
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(open_file)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('File manager')
        self.show()

    def showDialog(self):
        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)
        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.text_edit.setText(data)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
