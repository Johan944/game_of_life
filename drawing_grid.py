import math
from PySide2 import QtCore, QtGui, QtWidgets


class DrawingGrid(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)

    def mousePressEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            x = event.x()
            y = event.y()

            x_coord = math.floor(x / self.space_width)
            y_coord = math.floor(y / self.space_height)

            print(y_coord * self.width + x_coord)

            

    def set_size(self, width, height):
        try:
            self.width = int(width)
            self.height = int(height)
        except ValueError as e:
            return
        self.widget_width = self.frameGeometry().width()
        self.widget_height = self.frameGeometry().height()
        self.space_width = self.widget_width / self.width
        self.space_height = self.widget_height / self.height
        self.update()

    def resizeEvent(self, event):
        self.set_size(self.width, self.height)

    def set_width(self, width):
        try:
            self.set_size(int(width), self.height)
        except ValueError:
            pass

    def set_height(self, height):
        try:
            self.set_size(self.width, int(height))
        except ValueError:
            pass

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.draw_grid(qp)
        qp.end()

    def draw_grid(self, qp):
        y_coord = 0
        while y_coord < self.height * self.space_height:
            x_coord = 0
            qp.drawLine(x_coord, y_coord, x_coord + self.widget_width, y_coord)
            while x_coord < self.width * self.space_width:
                qp.drawLine(x_coord, y_coord, x_coord, y_coord + self.widget_height)
                x_coord += self.space_width
            y_coord += self.space_height
        qp.drawLine(self.widget_width- 1, 0, self.widget_width -1 , self.widget_height)
        qp.drawLine(0, self.widget_height-1, self.widget_width, self.widget_height-1)