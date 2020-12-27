from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QComboBox
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel('Linux', self)
        combo = QComboBox(self)
        combo.addItem('Ubuntu')
        combo.addItem('Manjaro')
        combo.addItem('Arch')
        combo.addItem('Kali')
        combo.addItem('Gentoo')
        combo.move(10, 10)
        self.lbl.move(80, 13)
        combo.activated[str].connect(self.onActivated)
        self.setGeometry(300, 300, 250, 100)
        self.setWindowTitle('Dropdown')
        self.show()

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()