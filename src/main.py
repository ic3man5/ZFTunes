from PySide6 import QtCore, QtGui, QtWidgets
import sys

from uimain import MainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
