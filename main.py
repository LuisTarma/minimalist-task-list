# -*- coding: utf-8 -*-

import os
import sys
from PyQt5 import QtGui, QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QDesktopWidget
import ui

class Ui(QtWidgets.QDialog):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('ui.ui',self)
        self.setWindowFlags((QtCore.Qt.FramelessWindowHint))
        
        # Posicionamiento
        this = self.geometry()
        ag = QDesktopWidget().availableGeometry()
        sg = QDesktopWidget().screenGeometry()
        ANCHO_PANTALLA = sg.width()
        ALTO_PANTALLA = sg.height()
        ancho_ventana = this.width()
        alto_ventana = this.height()
        print("Available: " + str(ag.width())+ "x" + str(ag.height())+" Screen Geometry: "+ str(ANCHO_PANTALLA)+"x"+str(ALTO_PANTALLA) + " This: "+ str(this.width())+ "x"+str(this.height()))
        x = ag.width() - ancho_ventana
        y = 2 * ag.height() - ALTO_PANTALLA -this.height()
        print(str(x)+"x"+str(y))
        self.move(x, y)
        #Fin Posicionamiento

        #self.show()
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.setToolTip(f'Minimalist Task List')
        menu = QtWidgets.QMenu(parent)

        """ To add a action menu
        open_app = menu.addAction("Open Notepad")
        open_app.triggered.connect(self.open_notepad)
        open_app.setIcon(QtGui.QIcon("icon.png"))
        """

        exit_ = menu.addAction("Exit")
        exit_.triggered.connect(lambda: sys.exit())
        exit_.setIcon(QtGui.QIcon("icon.png"))

        menu.addSeparator()
        self.setContextMenu(menu)
        self.activated.connect(self.onTrayIconActivated)

    def onTrayIconActivated(self, reason):
        """
        This function will trigger function on click or double click :param reason:  :return:
        """
        if reason == self.DoubleClick:
            self.open_notepad()
        if reason == self.Trigger:
            pass
    
    """ Function of the action menu
    def open_notepad(self):
        os.system('notepad')
    """
    def open_ui(self, i):
        pass

def main():
    app = QtWidgets.QApplication(sys.argv)
    windows = Ui()
    
    windows.show()
    
    w = QtWidgets.QWidget()
    tray_icon = SystemTrayIcon(QtGui.QIcon("icon.png"), w)
    tray_icon.show()
    tray_icon.showMessage('MinTask', 'm')
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
