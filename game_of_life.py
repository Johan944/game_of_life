import numpy as np

import matplotlib.pyplot as plt
import time
from IPython import display

class GameOfLife:
    def __init__(self, width, height):
        self.set_board(width, height)
        self.rule_alive_neighbours = np.zeros(8+9, np.uint8)
        self.rule_alive_neighbours[[2, 3]] = 1
        self.rule_dead_neighbours = np.zeros(8, np.uint8)
        self.rule_dead_neighbours[3] = 1


    def imshow_helper(self, sleepSeconds=0.5):
        ''' helper method to display a board for short time interval 
            being lazy and using the MATLAB style API '''
        print(np.reshape(self.board, (-1, self.width)))


    def set_board(self, width, height):
        self.width = width
        self.height = height
        self.board = np.zeros((width * height), dtype=np.uint8)
        self.neighbours_position = np.array([-width - 1, -width, -width + 1, -1, +1, +width - 1, +width, +width + 1])

    def run(self, nb_max_iterations=-1):
        nb_current_iterations = 0
        self.imshow_helper()
        while nb_current_iterations < nb_max_iterations:
            neighbours_count = self.get_neighbours()
            self.board = np.where(self.board, self.rule_alive_neighbours[neighbours_count], self.rule_dead_neighbours[neighbours_count])
            self.imshow_helper()
            nb_current_iterations += 1

    def select_cell(self, cell_pos):
        self.board[cell_pos] = np.where(self.board[cell_pos] == 1, 0, 1)

    def get_neighbours(self):
        return np.array([sum(self.board[(idx + self.neighbours_position) % (self.width*self.height)]) for idx, _ in np.ndenumerate(self.board)])
