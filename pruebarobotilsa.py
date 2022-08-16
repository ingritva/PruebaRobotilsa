# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer, QTime, QDate, QDateTime

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_PruebaRobotilsa

class PruebaRobotilsa(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PruebaRobotilsa()
        self.ui.setupUi(self)
        timer = QTimer(self)
        timer.timeout.connect(self.displayTime)
        timer.start(1000)

    def displayTime(self):
        currentTime = QTime.currentTime()
        currentDate = QDate.currentDate()
        tiempo = currentTime.toString('hh:mm:ss')
        fecha =  currentDate.toString('dd/MM/yyyy')
        self.ui.Hora.setText(tiempo)
        self.ui.Fecha.setText(fecha)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = PruebaRobotilsa()
    widget.show()
    sys.exit(app.exec())


