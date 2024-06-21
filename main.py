import sys
import os
import subprocess
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_autoruns.clicked.connect(self.run_executable)
        self.ui.btn_services.clicked.connect(
            lambda x: subprocess.Popen(['cmd.exe', '/k', 'services.msc']))

    def run_executable(self):
        dir = os.getcwd()
        path = os.path.join(dir, 'programms', 'Autoruns\Autoruns.exe')
        print(path)
        subprocess.call([f"{path}"])


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
