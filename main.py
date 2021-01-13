import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from random import randrange


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('pepega.ui', self)
        self.setWindowTitle('Git и желтые окружности')
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False
        self.diam = randrange(0, 100)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        for i in range(25):
            self.diam = randrange(0, 120)
            qp.setBrush(QColor(255, 255, 0))
            qp.drawEllipse(randrange(0, 400), randrange(0, 400), self.diam, self.diam)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
