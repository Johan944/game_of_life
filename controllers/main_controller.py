from PySide2 import QtCore
import game_of_life

class MainController(QtCore.QObject):
    cell_changed = QtCore.Signal(list)
    
    def __init__(self, width=20, height=10):
        super().__init__()
        self.main_view = None
        self.game_of_life = game_of_life.GameOfLife(width, height)
    
    def init_signals(self):
        self.main_view.ui.drawing_grid.clicked_signal.connect(self.select_cell)
        self.cell_changed.connect(self.main_view.ui.drawing_grid.set_grid_content)

    @QtCore.Slot(int)
    def select_cell(self, cell_pos):
        self.game_of_life.select_cell(cell_pos)
        self.cell_changed.emit(self.game_of_life.board)

    def run_algo(self):
        self.game_of_life.run(1)
        self.cell_changed.emit(self.game_of_life.board)