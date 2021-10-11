from PyQt5.QtWidgets import QApplication
from main_frame import MainWindow
import sys

#INitializae app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())