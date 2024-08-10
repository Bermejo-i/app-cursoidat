import sys
from PyQt5 import QtWidgets, uic
from dao.cursodao import cursodao
from PyQt5.QtWidgets import QTableWidgetItem
from model.curso import Curso

class cursocontroller:
    def __init__(self) -> None:
        app = QtWidgets.QApplication([])
        self.ventana= uic.loadUi('view/frmcursos.ui')
        self.ventana.tblcursos.setColumnWidth(0,80)
        self.ventana.tblcursos.setColumnWidth(1,290)
        self.ventana.tblcursos.setColumnWidth(2,70)
        self.ventana.tblcursos.cellClicked.connect(self.onCellClick_tblcursos)
        self.ventana.btnnuevo.clicked.connect(self.onClick_btnnuevo)
        self.ventana.btnguardar.clicked.connect(self.onClick_btnguardar)
        self.cursodao=cursodao()
        self.listarcursos()
        self.ventana.show()
        app.exec()

    def listarcursos(self):
        listacurso= self.cursodao.listarcursos()
        cantidad = len(listacurso)
        self.ventana.tblcursos.setRowCount(cantidad)
        fila = 0
        for objcurso in listacurso:
            self.ventana.tblcursos.setItem(fila, 0, QTableWidgetItem(objcurso[0]))
            self.ventana.tblcursos.setItem(fila, 1, QTableWidgetItem(objcurso[1]))
            self.ventana.tblcursos.setItem(fila, 2, QTableWidgetItem(str(objcurso[2])))
            fila += 1
    
    def onClick_btnguardar(self):
        idcurso= self.ventana.txtcodigo.text()
        nomcurso= self.ventana.txtnombre.text()
        credito= self.ventana.txtcreditos.text()
        nuevocurso = Curso(idcurso, nomcurso, credito)
        if self.ventana.txtcodigo.isEnabled():
            self.cursodao.insertarcurso(nuevocurso)
        else:
            self.cursodao.actualizarcurso(nuevocurso)
        self.listarcursos()

    def onClick_btnnuevo(self):
        self.ventana.txtcodigo.setText("")
        self.ventana.txtcodigo.setEnabled(True)
        self.ventana.txtnombre.setText("")
        self.ventana.txtcreditos.setText("")

    def onCellClick_tblcursos(self, fila):
        idcurso= self.ventana.tblcursos.item(fila, 0).text()
        self.ventana.txtcodigo.setText(idcurso)
        self.ventana.txtcodigo.setEnabled(False)
        objcurso = self.cursodao.obtenercursos(idcurso)
        self.ventana.txtnombre.setText(objcurso[1])
        self.ventana.txtcreditos.setText(str(objcurso[2]))


    