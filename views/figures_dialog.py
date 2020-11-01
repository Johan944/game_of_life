import functools

from PySide2 import QtCore, QtWidgets


class FiguresDialog(QtWidgets.QDialog):
    def __init__(self, figures, figure_type):
        super(FiguresDialog, self).__init__()

        self.setWindowTitle("Sélectionnez une figure")

        self.layout = QtWidgets.QHBoxLayout()

        self.buttons = []
        for figure in figures:
            button = QtWidgets.QPushButton(figure)
            button.clicked.connect(
                functools.partial(self.on_clicked_figure_button, figure_type, figure)
            )
            self.buttons.append(button)
        for button in self.buttons:
            self.layout.addWidget(button)
        self.setLayout(self.layout)

        self.current_figure_type = None
        self.current_figure = None

    @QtCore.Slot(str, str)
    def on_clicked_figure_button(self, figure_type, figure):
        self.current_figure_type = figure_type
        self.current_figure = figure
        self.accept()
