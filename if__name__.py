from PyQt5 import QtWidgets
import sys
from Ui_MainWindow import Ui_MainWindow
from logika import W_search
# Begin

if __name__ == "__main__":
    data=W_search()
    data.create_sql()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())