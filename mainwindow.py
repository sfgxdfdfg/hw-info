# This Python file uses the following encoding: utf-8
import sys
import platform
import cpuinfo
import psutil

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        cpu_cores = cpuinfo.get_cpu_info()

        self.ui.cpubrand.setText(f"CPU brand:  {cpu_cores['brand_raw']}")
        self.ui.cpuarch.setText(f"CPU arch:  {platform.machine()}")
        self.ui.cpucores.setText(f"CPU cores:  {cpu_cores['count']}")

        self.ui.cpubrand.setStyleSheet("color: red")
        self.ui.cpuarch.setStyleSheet("color: green")
        self.ui.cpucores.setStyleSheet("color: yellow")
        
        def get_size(bytes, suffix="B"):
            """
            Scale bytes to its proper format
            e.g:
                1253656 => '1.20MB'
                1253656678 => '1.17GB'
            """
            factor = 1024
            for unit in ["", "K", "M", "G", "T", "P"]:
                if bytes < factor:
                    return f"{bytes:.2f}{unit}{suffix}"
                bytes /= factor

        svmem = psutil.virtual_memory()
        self.ui.totalram.setText(f"Total ram: {get_size(svmem.total)}")
        
        self.ui.totalram.setStyleSheet("color: red")

        self.ui.cpubrand.setStyleSheet("color: red")
        self.ui.cpuarch.setStyleSheet("color: green")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
