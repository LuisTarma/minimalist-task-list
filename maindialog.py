# -*- coding: utf-8 -*-

import os
import sys
from PyQt5 import QtGui, QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QDesktopWidget
import ui
#import traybar
import database

ANCHO_W = 402
ALTO_W = 564

class Ui(QtWidgets.QDialog, ui.Ui_bodyMain):
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)
        #uic.loadUi('ui.ui',self) #old way
        self.setWindowFlags((QtCore.Qt.FramelessWindowHint) | QtCore.Qt.Popup)
        
        ##### Database ###############################################################################
        self.connection = database.create_connection("notes.db")
        database.create_table(self.connection)
        ##############################################################################################

        ##### Posicionamiento ########################################################################
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
        #############################################################################################

        #self.tray_icon = traybar.SystemTrayIcon(QtGui.QIcon("icon.png"), self)
        #self.tray_icon.show()
        #Evento del TextEdit
        # TODO
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
        print(event.key()) # Only work for special keys
        return super().keyPressEvent(event)
    
    def keyReleaseEvent(self, a0):
        """
        On any key pressed
        """
        return super().keyReleaseEvent(a0)
    
    def focusInEvent(self, a0):
        print("En foco")
        self.textEdit.setFocus() # Edit Text from the app start.
        sql = "SELECT * FROM notes WHERE id=1"
        cur = self.connection.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            print(row)
            self.textEdit.setText(row[1])
        return super().focusInEvent(a0)

    def hideEvent(self, a0):
        print("ocultado")
        note = self.textEdit.toPlainText()
        database.updateNote(self.connection, (note, 1))
        #self.trayicon.setShow(False, self)
        return super().hideEvent(a0)
    
    def showEvent(self, a0):
        #self.tray_icon.setShow(True, self)
        return super().showEvent(a0)

def main():
    ##### Test ######
    app = QtWidgets.QApplication(sys.argv)
    Interfaz = Ui()
    Interfaz.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
