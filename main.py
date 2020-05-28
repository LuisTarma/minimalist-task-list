# -*- coding: utf-8 -*-

import os
import sys
from PyQt5 import QtWidgets, QtGui
import ui


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
            appa = QtWidgets.QApplication(sys.argv)
            InfoDialog = QtWidgets.QDialog()
            I = ui.Ui_InfoDialog()
            I.setupUi(InfoDialog)
            self.open_ui(InfoDialog, appa)
    
    """ Function of the action menu
    def open_notepad(self):
        os.system('notepad')
    """
    def open_ui(self, i, appa):
        i.show()
        sys.exit(appa.exec_())

def main():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    tray_icon = SystemTrayIcon(QtGui.QIcon("icon.png"), w)
    tray_icon.show()
    tray_icon.showMessage('MinTask', 'm')
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
