import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic
from random import randint, randrange


class Window(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_circle(self, qp):
        for x in range(randrange(2, 10)):
            qp.setBrush(QColor(randrange(0, 255), randrange(0, 255), randrange(0, 255)))
            coor = [randint(0, 400), randint(0, 300)]
            qp.drawEllipse(coor[0], coor[0], coor[1], coor[1])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())