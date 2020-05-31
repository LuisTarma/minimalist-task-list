# -*- coding: utf-8 -*-

from sys import exit, argv
from PyQt5 import QtGui, QtWidgets, QtCore
import traybar

def main():
    app = QtWidgets.QApplication(argv)
    w = QtWidgets.QWidget()
    tray_icon = traybar.SystemTrayIcon(QtGui.QIcon("icon.png"), w)
    tray_icon.show()
    tray_icon.showMessage('MinTask', 'm')
    exit(app.exec_())

if __name__ == '__main__':
    main()
