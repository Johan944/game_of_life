import os
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from PySide2 import QtGui, QtWidgets
from views import drawing_grid

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, main_controller):
        super(MainWindow, self).__init__()
        self.main_controller = main_controller
        self.load_ui()

        self.init_widgets()
        self.ui.showMaximized()

    def load_ui(self):
        loader = QUiLoader()
        loader.registerCustomWidget(drawing_grid.DrawingGrid)
        path = os.path.join(os.path.dirname(__file__), "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        self.ui.drawing_grid.grid_content = self.main_controller.game_of_life.board
        ui_file.close()

    def init_widgets(self):
        integer_validator = QtGui.QIntValidator(5, 200)
        self.ui.input_nb_columns.setValidator(integer_validator)
        self.ui.input_nb_lines.setValidator(integer_validator)

        self.ui.input_nb_columns.setText(str(self.main_controller.game_of_life.width))
        self.ui.input_nb_columns.textChanged.connect(self.on_text_changed_width)
        self.ui.input_nb_lines.textChanged.connect(self.on_text_changed_height)
        self.ui.input_nb_lines.setText(str(self.main_controller.game_of_life.height))
        self.ui.button_reset.clicked.connect(self.main_controller.clear_board)

    def on_text_changed_width(self, nb_columns):
        self.ui.drawing_grid.set_size(nb_columns, self.ui.input_nb_lines.text())

    def on_text_changed_height(self, nb_lines):
        self.ui.drawing_grid.set_size(self.ui.input_nb_columns.text(), nb_lines)
