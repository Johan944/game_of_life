from PySide2 import QtCore, QtWidgets
import functools
import figures_manager
import game_of_life
import time


class ThreadRunAlgo(QtCore.QThread):
    def __init__(self, main_controller):
        QtCore.QThread.__init__(self, main_controller)
        self.main_controller = main_controller

    def run(self):
        while self.main_controller.running is True:
            self.main_controller.game_of_life.run(1)
            self.main_controller.cell_changed.emit(self.main_controller.game_of_life.board)
            self.main_controller.main_view.ui.label_nb_iterations.setText(str(self.main_controller.game_of_life.nb_current_iterations))
            time.sleep(self.main_controller.time_value)

class MainController(QtCore.QObject):
    cell_changed = QtCore.Signal(list)
    
    def __init__(self, width=100, height=50):
        super().__init__()
        self.main_view = None
        self.running = False
        self.game_of_life = game_of_life.GameOfLife(width, height)
        self.time_value = 1
        self.figures_manager = figures_manager.FiguresManager(self.game_of_life.width, self.game_of_life.height)
        self.figure_to_place = ()
    
    def init_signals(self):
        self.main_view.ui.drawing_grid.clicked_signal.connect(self.select_cell)
        self.cell_changed.connect(self.main_view.ui.drawing_grid.set_grid_content)
        self.main_view.ui.drawing_grid.resize_board_signal.connect(self.resize_board)
        self.main_view.ui.slider_time.valueChanged.connect(self.set_time_value)
        self.main_view.ui.button_play.clicked.connect(self.run_start)
        self.main_view.ui.button_stable.clicked.connect(lambda: self.select_figures("stable"))
        self.main_view.ui.button_periodic.clicked.connect(lambda: self.select_figures("periodic"))
        self.main_view.ui.button_ship.clicked.connect(lambda: self.select_figures("ship"))
        self.main_view.ui.button_mathusalem.clicked.connect(lambda: self.select_figures("mathusalem"))
        self.main_view.ui.button_puffer.clicked.connect(lambda: self.select_figures("puffer"))
        self.main_view.ui.button_gun.clicked.connect(lambda: self.select_figures("gun"))
        self.main_view.ui.button_eden.clicked.connect(lambda: self.select_figures("eden"))

    def select_figures(self, figure_type):
        self.dialog = QtWidgets.QDialog(self.main_view)
        layout = QtWidgets.QHBoxLayout()
        self.buttons = []
        for figure in self.figures_manager.figures[figure_type]:
            button = QtWidgets.QPushButton(figure)
            button.clicked.connect(functools.partial(self.on_clicked_figure_button, figure_type, figure))
            self.buttons.append(button)
        for button in self.buttons:
            layout.addWidget(button)
        self.dialog.setLayout(layout)
        self.dialog.show()

    def on_clicked_figure_button(self, figure_type, figure_name):
        self.figure_to_place = (figure_type, figure_name)

    @QtCore.Slot(int)
    def select_cell(self, cell_pos):
        if self.figure_to_place:
            coords_to_place = self.figures_manager.get_coords_from_figure(self.figure_to_place[0], self.figure_to_place[1], cell_pos)
            for pos in coords_to_place:
                if self.game_of_life.board[pos] == 0:
                    self.game_of_life.select_cell(pos)
            self.figure_to_place = ()
        else:
            self.game_of_life.select_cell(cell_pos)
            self.main_view.ui.label_nb_iterations.setText("0")
        self.cell_changed.emit(self.game_of_life.board)

    @QtCore.Slot(int, int)
    def resize_board(self, width, height):
        self.game_of_life.set_board(width, height)
        self.figures_manager.set_size(width, height)
        self.cell_changed.emit(self.game_of_life.board)

    @QtCore.Slot()
    def clear_board(self):
        self.game_of_life.reset_board()
        self.cell_changed.emit(self.game_of_life.board)
        self.main_view.ui.label_nb_iterations.setText("0")

    @QtCore.Slot()
    def set_time_value(self, value):
        self.time_value = (100 - value) / 100

    @QtCore.Slot()
    def run_start(self):
        if self.running:
            self.running = False
            self.main_view.ui.button_play.setText("Lecture")
        else:
            self.running = True
            self.main_view.ui.button_play.setText("Pause")
            thread = ThreadRunAlgo(self)
            thread.start()
