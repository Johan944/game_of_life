from PyQt5.QtCore import QObject, pyqtSlot
import game_of_life

class MainController(QObject):
    def __init__(self, width=20, height=10):
        self.game_of_life = game_of_life.GameOfLife(width, height)