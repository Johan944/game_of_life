import sys
import random
from PySide2.QtWidgets import (QApplication, QLabel, QPushButton,
                               QVBoxLayout, QWidget, QGridLayout, QHBoxLayout)
from PySide2.QtCore import Slot, Qt
from PySide2 import QtGui, QtWidgets

class MyWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.stable_shape_button = QPushButton("Structures Stables")
        self.periodic_shape_button = QPushButton("Structures Périodiques")
        self.ship_shape_button = QPushButton("Vaisseaux")
        self.mathusalem_shape_button = QPushButton("Mathusalems")
        self.puffer_shape_button = QPushButton("Puffeurs")
        self.gun_shape_button = QPushButton("Canons")
        self.eden_shape_button = QPushButton("Jardins D'Eden")
        self.spacefiller_shape_button = QPushButton("Spacefillers")


        self.layout = QGridLayout()

        self.shape_type_layout = QHBoxLayout()
        self.shape_type_layout.addWidget(self.stable_shape_button)
        self.shape_type_layout.addWidget(self.periodic_shape_button)
        self.shape_type_layout.addWidget(self.ship_shape_button)
        self.shape_type_layout.addWidget(self.mathusalem_shape_button)
        self.shape_type_layout.addWidget(self.puffer_shape_button)
        self.shape_type_layout.addWidget(self.gun_shape_button)
        self.shape_type_layout.addWidget(self.eden_shape_button)
        self.shape_type_layout.addWidget(self.spacefiller_shape_button)

        self.windows_width = self.frameGeometry().width()
        self.window_height = self.frameGeometry().height()

        self.canvas_layout = QtWidgets.QHBoxLayout()
        self.canvas = QtWidgets.QLabel("test")
        self.canvas_layout.addWidget(self.canvas)

        self.commands_layout = QtWidgets.QHBoxLayout()
        self.nb_horizontal_cells_input = QtWidgets.QLineEdit()
        self.nb_vertical_cells_input = QtWidgets.QLineEdit()
        self.play_button = QPushButton("Lecture")
        self.reset_button = QPushButton("Reset")
        self.nb_iteration_label = QtWidgets.QLabel("Nombre d'itérations : ")

        self.commands_layout.addWidget(self.nb_horizontal_cells_input)
        self.commands_layout.addWidget(self.nb_vertical_cells_input)
        self.commands_layout.addWidget(self.play_button)
        self.commands_layout.addWidget(self.reset_button)
        self.commands_layout.addWidget(self.nb_iteration_label)
        

        self.layout.addLayout(self.shape_type_layout, 1, 0)
        self.layout.addLayout(self.canvas_layout, 1, 0, 5, 1)
        self.layout.addLayout(self.commands_layout, 6, 0)

        
        self.setLayout(self.layout)

        print(self.geometry().width())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MyWidget()
    widget.showMaximized()

    sys.exit(app.exec_())