# -*- coding: utf-8 -*-

from sys import exit, argv
from PyQt5 import QtGui, QtWidgets
import maindialog

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
        exit_.triggered.connect(lambda: exit())
        exit_.setIcon(QtGui.QIcon("icon.png"))

        menu.addSeparator()
        self.setContextMenu(menu)
        self.activated.connect(self.onTrayIconActivated)

        self.ui = maindialog.Ui()
        self.showed = True

    def onTrayIconActivated(self, reason):
        """
        This function will trigger function on click or double click :param reason:  :return:
        """
        #folder = os.getcwd()+"\\"
        if reason == self.DoubleClick:
            pass
        if reason == self.Trigger:
            print("Debe mostarse: " + str(self.showed) + " Segun main: "+ str(self.ui.getShowed()))
            if self.ui.getShowed():
                self.ui.setShowed(False)
                self.ui.posicionar()
                self.ui.exec_()
            else:
                self.showed = True
                self.ui.setShowed(True)
                self.ui.hide()

    def setShow(self, isShowed):
        self.showed = isShowed
        self.ui = ui

def main():
    app = QtWidgets.QApplication(argv)
    w = QtWidgets.QWidget()
    tray_icon = SystemTrayIcon(QtGui.QIcon("icon.png"), w)
    tray_icon.show()
    tray_icon.showMessage('MinTask', 'm')
    exit(app.exec_())

if __name__ == '__main__':
    main()
