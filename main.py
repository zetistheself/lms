from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import *
import sys
import requests


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.pushButton.clicked.connect(self.search)

    def search(self):
        x = self.lineEdit.text()
        y = self.lineEdit_3.text()
        spn = self.lineEdit_2.text()
        print(x)
        print(y)
        print(spn)
        r = requests.get(f'https://static-maps.yandex.ru/1.x/?ll={x},{y}&spn={spn},{spn}&l=map')
        out = open("img.jpg", "wb")
        out.write(r.content)
        out.close()
        pixmap = QPixmap()
        pixmap.load('img.jpg')
        self.label_4.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())

# 37.530887,55.703118
# 0.002