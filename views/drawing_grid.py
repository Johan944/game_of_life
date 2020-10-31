import math
from PySide2 import QtCore, QtGui, QtWidgets, QtCore


class DrawingGrid(QtWidgets.QWidget):
    clicked_signal = QtCore.Signal(int)
    resize_board_signal = QtCore.Signal(int, int)

    def __init__(self, parent):
        super().__init__(parent)
        self.grid_content = []

    def mousePressEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            x_coord = math.floor(event.x() / self.space_width)
            y_coord = math.floor(event.y() / self.space_height)

            self.clicked_signal.emit(y_coord * self.width + x_coord)

    @QtCore.Slot(list)
    def set_grid_content(self, grid_content):
        self.grid_content = grid_content
        self.update()

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
        self.resize_board_signal.emit(self.width, self.height)

    def resizeEvent(self, event):
        self.set_size(self.width, self.height)

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.draw_grid(qp)
        qp.end()

    def draw_grid(self, qp):
        cell_pos = 0
        y_coord = 0
        for __ in range(self.height):
            x_coord = 0
            for _ in range(self.width):
                if self.grid_content[cell_pos] == 1:
                    qp.fillRect(QtCore.QRect(x_coord, y_coord, self.space_width, self.space_height), QtGui.QColor(0, 0, 0))
                else:
                    qp.fillRect(QtCore.QRect(x_coord, y_coord, self.space_width, self.space_height), QtGui.QColor(255, 255, 255))
                qp.drawLine(x_coord, y_coord, x_coord, y_coord + self.widget_height)
                x_coord += self.space_width
                cell_pos += 1
            qp.drawLine(0, y_coord, self.widget_width, y_coord)
            y_coord += self.space_height
        qp.drawLine(self.widget_width- 1, 0, self.widget_width -1 , self.widget_height)
        qp.drawLine(0, self.widget_height-1, self.widget_width, self.widget_height-1)