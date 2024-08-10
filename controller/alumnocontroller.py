import sys
from PyQt5 import QtWidgets, uic
from dao.alumnodao import alumnodao
from PyQt5.QtWidgets import QTableWidgetItem
from model.alumno import alumno

class alumnocontroller:
    def __init__(self) -> None:
        app=QtWidgets.QApplication([])
        self.ventana = uic.loadUi("view/frmalumno.ui")
        self.ventana.show()
        app.exec()
        