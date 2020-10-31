class FiguresManager():
    def __init__(self, width, height):
        self.set_size(width, height)

    def set_size(self, width, height):
        self.width = width
        self.height = height
        self.set_figures()

    def set_figures(self):
        stables_figure = {
            "square": [0, 1, self.width, self.width + 1],
            "pipe":  [0, self.width - 1, self.width + 1, self.width * 2]
        }
        periodic_figures = {
            "blinker": [0, 1, 2],

            "cross": [0, 1, 2, 3,
            self.width, self.width + 3,
            self.width * 2 - 2, self.width * 2 - 1, self.width * 2, self.width * 2 + 3, self.width * 2 + 4, self.width * 2 + 5,
            self.width * 3 - 2, self.width * 3 + 5,
            self.width * 4 - 2, self.width * 4 + 5,
            self.width * 5 - 2, self.width * 5 - 1, self.width * 5, self.width * 5 + 3, self.width * 5 + 4, self.width * 5 + 5,
            self.width * 6, self.width * 6 + 3,
            self.width * 7, self.width * 7 + 1, self.width * 7 + 2, self.width * 7 + 3],

            "clock": [0, 1,
            self.width, self.width + 1,
            self.width * 3 - 2, self.width * 3 - 1, self.width * 3, self.width * 3 + 1,
            self.width * 4 - 6, self.width * 4 - 5, self.width * 4 - 3, self.width * 4 + 2,
            self.width * 5 - 6, self.width * 5 - 5, self.width * 5 - 3, self.width * 5 - 1, self.width * 5, self.width * 5 + 2,
            self.width * 6 - 3, self.width * 6 + 1, self.width * 6 + 2, self.width * 6 + 4, self.width * 6 + 5,
            self.width * 7 - 3, self.width * 7 + 2, self.width * 7 + 4, self.width * 7 + 5,
            self.width * 8 - 2, self.width * 8 - 1, self.width * 8, self.width * 8 + 1,
            self.width * 10 - 2, self.width * 10 - 1,
            self.width * 11 - 2, self.width * 11 - 1
            ]
        }

        ship_figures = {
            "glider": [0, self.width + 1, self.width * 2 - 1, self.width * 2, self.width * 2 + 1],
            "LWSS": [0, 3, self.width + 4, self.width * 2, self.width * 2 + 4, self.width * 3 + 1, self.width * 3 + 2, self.width * 3 + 3,self.width * 3 + 4]
        }

        mathusalem_figures = {
            "pentomino R": [0, self.width, self.width + 1, self.width * 2 - 1, self.width * 2]
        }

        puffer_figures = {
            "rake": [0, 1, 7, 8, 9, 10,
            self.width - 2, self.width - 1, self.width + 1, self.width + 2, self.width + 6, self.width + 10,
            self.width * 2 - 2, self.width * 2 - 1, self.width * 2, self.width * 2 + 1, self.width * 2 + 10,
            self.width * 3 - 1, self.width * 3, self.width * 3 + 6, self.width * 3 + 9,
            self.width * 6 + 7,
            self.width * 7 + 8,
            self.width * 8 + 8,
            self.width * 9 + 7, self.width * 9 + 8,
            self.width * 10 + 6,
            self.width * 14 + 7, self.width * 14 + 8, self.width * 14 + 9, self.width * 14 + 10,
            self.width * 15 - 11, self.width * 15 - 8, self.width * 15 + 6, self.width * 15 + 10,
            self.width * 16 - 7, self.width * 16 + 10,
            self.width * 17 - 11, self.width * 17 - 7, self.width * 17 + 6, self.width * 17 + 9,
            self.width * 18 - 10, self.width * 18 - 9,self.width * 18 - 8, self.width * 18 - 7
            ]
        }

        gun_figures = {
            "gun": [0,
            self.width - 2, self.width,
            self.width * 2 - 12, self.width * 2 - 11, self.width * 2 - 4, self.width * 2 - 3, self.width * 2 + 10, self.width * 2 + 11,
            self.width * 3 - 13, self.width * 3 - 9, self.width * 3 - 4, self.width * 3 - 3, self.width * 3 + 10, self.width * 3 + 11,
            self.width * 4 - 24, self.width * 4 - 23, self.width * 4 - 14, self.width * 4 - 8, self.width * 4 - 4, self.width * 4 - 3,
            self.width * 5 - 24, self.width * 5 - 23, self.width * 5 - 14, self.width * 5 - 10, self.width * 5 - 8, self.width * 5 - 7, self.width * 5 - 2, self.width * 5,
            self.width * 6 - 14, self.width * 6 - 8, self.width * 6,
            self.width * 7 - 13, self.width * 7 - 9,
            self.width * 8 - 12, self.width * 8 - 11, self.width * 8 - 1, 
            ]
        }

        eden_figures = {
            "Flammenkamp": [0, 2, 3, 5, 6, 9,
            self.width + 1, self.width + 3, self.width + 4, self.width + 5, self.width + 7, self.width + 8, self.width + 9,
            self.width * 2 + 1, self.width * 2 + 2, self.width * 2 + 4, self.width * 2 + 5, self.width * 2 + 6, self.width * 2 + 8, self.width * 2 + 10,
            self.width * 3, self.width * 3 + 2, self.width * 3 + 3, self.width * 3 + 4, self.width * 3 + 5, self.width * 3 + 6, self.width * 3 + 7, self.width * 3 + 8, self.width * 3 + 10,
            self.width * 4 - 1, self.width * 4 + self.width * 4, self.width * 4 + 1, self.width * 4 + 2, self.width * 4 + 3, self.width * 4 + 6,self.width * 4 + 7, self.width * 4 + 8, self.width * 4 + 9,
            self.width * 5, self.width * 5 + 1, self.width * 5 + 3, self.width * 5 + 4, self.width * 5 + 5, self.width * 5 + 7, self.width * 5 + 10,
            self.width * 6, self.width * 6 + 1, self.width * 6 + 2, self.width * 6 + 4, self.width * 6 + 6, self.width * 6 + 9,
            self.width * 7, self.width * 7 + 1, self.width * 7 + 3, self.width * 7 + 4, self.width * 7 + 5, self.width * 7 + 8, self.width * 7 + 9,
            self.width * 8 - 1, self.width * 8 + 1, self.width * 8 + 2, self.width * 8 + 3, self.width * 8 + 5, self.width * 8 + 6, self.width * 8 + 7, self.width * 8 + 9,
            self.width * 9 - 1, self.width * 9 + 2, self.width * 9 + 3, self.width * 9 + 6, self.width * 9 + 8, self.width * 9 + 10,
            self.width * 10 + 9 
            ]
        }

        self.figures = {
            "stable": stables_figure,
            "periodic": periodic_figures,
            "ship": ship_figures,
            "mathusalem": mathusalem_figures,
            "puffer": puffer_figures,
            "gun": gun_figures,
            "eden": eden_figures,
        }

    def get_coords_from_figure(self, figure_type, figure_name, cell_pos):
        points = self.figures[figure_type][figure_name]
        return [cell_pos + point for point in points]


