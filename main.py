import sys
from PySide2.QtWidgets import QApplication
from controllers import main_controller
from views import main_view

class App(QApplication):
    def __init__(self, args):
        super(App, self).__init__(args)
        self.main_controller = main_controller.MainController()
        self.main_view = main_view.MainWindow(self.main_controller)
        self.main_controller.main_view = self.main_view
        self.main_controller.init_signals()


if __name__ == "__main__":
    app = App([])
    sys.exit(app.exec_())
