import numpy as np

import matplotlib.pyplot as plt
import time

class GameOfLife:
    def __init__(self, width, height):
        self.set_board(width, height)
        self.init_rules()
        self.time_value = 1
        self.nb_current_iterations = 0


    def init_rules(self):
        self.rule_alive_neighbours = np.zeros(9, np.uint8)
        self.rule_alive_neighbours[[2, 3]] = 1
        self.rule_dead_neighbours = np.zeros(9, np.uint8)
        self.rule_dead_neighbours[3] = 1

    def set_board(self, width, height):
        self.width = width
        self.height = height
        self.board = np.zeros((width * height), dtype=np.uint8)
        self.neighbours_position = np.array([-width - 1, -width, -width + 1, -1, +1, +width - 1, +width, +width + 1])

    def reset_board(self):
        self.board = np.zeros((self.width * self.height), dtype=np.uint8)
        self.nb_current_iterations = 0

    def run(self, nb_max_iterations=-1):
        neighbours_count = self.get_neighbours()
        self.board = np.where(self.board, self.rule_alive_neighbours[neighbours_count], self.rule_dead_neighbours[neighbours_count])
        self.nb_current_iterations += 1

    def select_cell(self, cell_pos):
        self.board[cell_pos] = np.where(self.board[cell_pos] == 1, 0, 1)
        self.nb_current_iterations = 0

    def get_neighbours(self):
        return np.array([sum(self.board[(idx + self.neighbours_position) % (self.width*self.height)]) for idx, _ in np.ndenumerate(self.board)])

