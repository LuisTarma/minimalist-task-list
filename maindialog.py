# -*- coding: utf-8 -*-

from sys import exit, argv
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QDesktopWidget, QApplication
import ui
import database
from configparser import ConfigParser

ANCHO_W = 402
ALTO_W = 564
DATABASE_NAME = "notes.db"

class Ui(QtWidgets.QDialog, ui.Ui_bodyMain):
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)
        self.showed = True
        #uic.loadUi('ui.ui',self) #old way
        self.setWindowFlags((QtCore.Qt.FramelessWindowHint) | QtCore.Qt.Popup)
        
        ##### Database #############################################
        self.connection = database.create_connection(DATABASE_NAME)
        database.create_table(self.connection)
        ############################################################

        ##### Posicionamiento ######################################
        self.posicionar()
        ############################################################

        ##### UI design ############################################
        
        ############################################################

        ##### Events ############################################
        self.btn_clipboard.clicked.connect(self.clipboard)
        self.btn_expand.clicked.connect(self.expand)
        self.btn_setvisible.clicked.connect(self.AlwaysVisible)
        ############################################################

    def expand(self):
        """
        Expand window size to all screen
        """
        if self.geometry().width() <= ANCHO_W:
            self.wbodyMain.resize(self.ANCHO_PANTALLA, self.ALTO_PANTALLA)
            self.resize(self.ANCHO_PANTALLA, self.ALTO_PANTALLA)
            self.move(0,0)
        else:
            self.wbodyMain.resize(ANCHO_W, ALTO_W)
            self.resize(ANCHO_W, ALTO_W)
            self.move(self.x, self.y)

    def AlwaysVisible(self):
        """
        TODO: Windows would keep fixed on the top if lost the focus
        """
        print("Activando siempre visible...")
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlag(QtCore.Qt.Window)

    def clipboard(self):
        """
        Paste clipboard content to TextEdit
        """
        #previus_txt = self.textEdit.toPlainText()      #Ridiculus
        clip = QApplication.clipboard().text()          #Capture clipboard
        cursor = self.textEdit.textCursor()             #Get the cursor "I"
        try:
            new_txt = str(clip)
            #self.textEdit.setText(new_txt)             #Dont work
            cursor.insertText(new_txt)
        except:
            print("Cannot paste the clipboard")
        self.textEdit.setFocus()
        cursor.setPosition(5, 0)
        cursor.movePosition(11,0,2)
        self.textEdit.setTextCursor(cursor)

    def posicionar(self):
        #this = self.geometry()
        self.ag = QDesktopWidget().availableGeometry()
        self.sg = QDesktopWidget().screenGeometry()
        self.ANCHO_PANTALLA = self.ag.width()
        self.ALTO_PANTALLA = self.ag.height()
        #ancho_ventana = this.width() #Dont work idk why
        #alto_ventana = this.height()  #Dont work idk why
        #print("Available: " + str(ag.width())+ "x" + str(ag.height())+" Screen Geometry: "+ str(ANCHO_PANTALLA)+"x"+str(ALTO_PANTALLA) + " This: "+ str(ANCHO_W)+ "x"+str(ALTO_W))
        self.x = self.ANCHO_PANTALLA - ANCHO_W
        self.y = 2 * self.ALTO_PANTALLA - self.sg.height() - ALTO_W
        #print(str(x)+"x"+str(y))
        self.move(self.x, self.y)

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
        #self.textEdit.textCursor().setPosition(2)
        return super().keyReleaseEvent(a0)
    
    def focusInEvent(self, a0):
        self.cursor = self.textEdit.textCursor()
        self.showed = False
        self.textEdit.setFocus() # Edit Text from the app start.
        sql = "SELECT * FROM notes WHERE id=1"
        cur = self.connection.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            print(row)
            self.cursor.insertText(row[1])
            #self.textEdit.setText(row[1]) # Using the cursor cannot use "setText" normally idk why
        self.textEdit.setFocus() # Edit Text from the app start.s
        print("Cursor position: " + str(self.textEdit.textCursor().anchor()))
        #self.textEdit.textCursor().setPosition(12, 0)      #This dont work
        #self.textEdit.textCursor().movePosition(11, 0, 1)  #This dont work
        self.cursor.setPosition(5, 0)
        self.cursor.movePosition(11,0,2)
        self.textEdit.setTextCursor(self.cursor)
        print("Cursor position: " + str(self.textEdit.textCursor().anchor()))
        return super().focusInEvent(a0)

    def hideEvent(self, a0):
        #print("ocultado")
        note = self.textEdit.toPlainText()
        database.updateNote(self.connection, (note, 1))
        #self.showed = True
        return super().hideEvent(a0)
    
    def getShowed(self):
        return self.showed

    def setShowed(self, show):
        self.showed = show
    
    def showEvent(self, a0):
        #self.tray_icon.setShow(True, self)
        return super().showEvent(a0)

def main():
    ##### Test ######
    app = QtWidgets.QApplication(argv)
    Interfaz = Ui()
    Interfaz.show()
    exit(app.exec_())

if __name__ == '__main__':
    main()
