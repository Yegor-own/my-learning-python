import sys
from PyQt5.QtWidgets import QMainWindow,\
    QPushButton,\
    QApplication,\
    QLineEdit,\
    QInputDialog


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Dialog', self)
        self.btn.move(10, 10)
        self.btn.clicked.connect(self.showDialog)
        self.le = QLineEdit(self)
        self.le.move(10, 50)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Dialog window ')
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter a name')
        if ok:
            self.le.setText(str(text))


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()