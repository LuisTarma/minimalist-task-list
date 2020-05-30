# -*- coding: utf-8 -*-

import os
import sys
from PyQt5 import QtGui, QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QDesktopWidget
import ui

ANCHO_W = 402
ALTO_W = 564

class Ui(QtWidgets.QDialog, ui.Ui_InfoDialog):
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)
        #uic.loadUi('ui.ui',self) #old way
        self.setWindowFlags((QtCore.Qt.FramelessWindowHint) | QtCore.Qt.Popup)
        
        # Posicionamiento
        this = self.geometry()
        ag = QDesktopWidget().availableGeometry()
        sg = QDesktopWidget().screenGeometry()
        ANCHO_PANTALLA = sg.width()
        ALTO_PANTALLA = sg.height()
        #ancho_ventana = this.width() #Dont work idk why
        #alto_ventana = this.height()  #Dont work idk why
        print("Available: " + str(ag.width())+ "x" + str(ag.height())+" Screen Geometry: "+ str(ANCHO_PANTALLA)+"x"+str(ALTO_PANTALLA) + " This: "+ str(ANCHO_W)+ "x"+str(ALTO_W))
        x = ag.width() - ANCHO_W
        y = 2 * ag.height() - ALTO_PANTALLA - ALTO_W
        print(str(x)+"x"+str(y))
        self.move(x, y)
        #Fin Posicionamiento
        
        #Evento del TextEdit
        
        #Fin del evento

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()
    
    def keyPressEvent(self, event):
        return super().keyPressEvent(event)

    def focusInEvent(self, a0):
        print("En foco")
        
        return super().focusInEvent(a0)

    def hideEvent(self, a0):
        """
        Evento que se dispara cuando se pierde el foco de la aplicacion
        """
        print("ocultado")
        sys.exit()
        return super().hideEvent(a0)

def main():
    app = QtWidgets.QApplication(sys.argv)
    Interfaz = Ui()
    Interfaz.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
