from PySide2 import QtCore
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
            time.sleep(self.main_controller.game_of_life.time_value)

class MainController(QtCore.QObject):
    cell_changed = QtCore.Signal(list)
    
    def __init__(self, width=20, height=10):
        super().__init__()
        self.main_view = None
        self.running = False
        self.game_of_life = game_of_life.GameOfLife(width, height)
    
    def init_signals(self):
        self.main_view.ui.drawing_grid.clicked_signal.connect(self.select_cell)
        self.cell_changed.connect(self.main_view.ui.drawing_grid.set_grid_content)
        self.main_view.ui.drawing_grid.resize_board_signal.connect(self.resize_board)
        self.main_view.ui.slider_time.valueChanged.connect(self.set_time_value)
        self.main_view.ui.button_play.clicked.connect(self.run_start)

    @QtCore.Slot(int)
    def select_cell(self, cell_pos):
        self.game_of_life.select_cell(cell_pos)
        self.main_view.ui.label_nb_iterations.setText("0")
        self.cell_changed.emit(self.game_of_life.board)

    @QtCore.Slot(int, int)
    def resize_board(self, width, height):
        self.game_of_life.set_board(width, height)
        self.cell_changed.emit(self.game_of_life.board)

    def clear_board(self):
        self.game_of_life.reset_board()
        self.cell_changed.emit(self.game_of_life.board)

    def run_algo(self):
        self.game_of_life.run(-1)
        self.cell_changed.emit(self.game_of_life.board)

    def set_time_value(self, value):
        self.game_of_life.time_value = (value + 1) / 100

    def run_start(self):
        if self.running:
            self.running = False
        else:
            self.running = True
            thread = ThreadRunAlgo(self)
            thread.start()
