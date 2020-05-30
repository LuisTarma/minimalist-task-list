# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InfoDialog(object):
    def setupUi(self, InfoDialog):
        InfoDialog.setObjectName("InfoDialog")
        InfoDialog.resize(402, 564)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(InfoDialog.sizePolicy().hasHeightForWidth())
        InfoDialog.setSizePolicy(sizePolicy)
        InfoDialog.setMaximumSize(QtCore.QSize(402, 564))
        InfoDialog.setWindowTitle("")
        InfoDialog.setStyleSheet("\n"
"#wInfoDialogIn\n"
"{\n"
" border-radius: 10px;\n"
" background-color:  #FFFFFF;\n"
"border: none;\n"
"\n"
"}\n"
"#tTransfers, #tNotifications\n"
"{\n"
"  font-family: \"Lato\";\n"
"  font-size: 15px;\n"
"  color: rgba(0, 0, 0, 40%);\n"
"  padding: 0px 8px 0px 8px;\n"
"  border: none;\n"
"}\n"
"#tNotifications\n"
"{\n"
"  padding: 0px 4px 0px 16px;\n"
"}\n"
"\n"
"#bAvatar, #bState, #bMEGAheader, #bClockDown, #bClockUp, #bOQIcon, #bBusinessQuota, #bBusinessStorage\n"
"{\n"
"    border: none;\n"
"}\n"
"\n"
"#wSeparator, #wSeparatorStats, #wSeparatorNotificationsOpts\n"
"{\n"
"background-color:  rgb(231, 231, 231);\n"
"}\n"
"\n"
"#lTotalUsedStorage,  #lTotalUsedQuota\n"
"{\n"
"font-family: \"Lato\";\n"
"font-size: 13px;\n"
"font-weight: normal;\n"
"border: none;\n"
"color: #333333;\n"
"}\n"
"QPushButton\n"
"{\n"
"    padding-right: 12px;\n"
"    padding-left: 12px;\n"
"}\n"
"")
        InfoDialog.setSizeGripEnabled(False)
        InfoDialog.setModal(False)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(InfoDialog)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.wInfoDialogIn = QtWidgets.QWidget(InfoDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wInfoDialogIn.sizePolicy().hasHeightForWidth())
        self.wInfoDialogIn.setSizePolicy(sizePolicy)
        self.wInfoDialogIn.setMinimumSize(QtCore.QSize(402, 564))
        self.wInfoDialogIn.setMaximumSize(QtCore.QSize(402, 564))
        self.wInfoDialogIn.setObjectName("wInfoDialogIn")
        self.verticalLayout_wInfoDialogIn = QtWidgets.QVBoxLayout(self.wInfoDialogIn)
        self.verticalLayout_wInfoDialogIn.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_wInfoDialogIn.setSpacing(0)
        self.verticalLayout_wInfoDialogIn.setObjectName("verticalLayout_wInfoDialogIn")
        self.wContainerHeader = QtWidgets.QWidget(self.wInfoDialogIn)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wContainerHeader.sizePolicy().hasHeightForWidth())
        self.wContainerHeader.setSizePolicy(sizePolicy)
        self.wContainerHeader.setMinimumSize(QtCore.QSize(0, 0))
        self.wContainerHeader.setStyleSheet("")
        self.wContainerHeader.setObjectName("wContainerHeader")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.wContainerHeader)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.wHeaderframe = QtWidgets.QFrame(self.wContainerHeader)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wHeaderframe.sizePolicy().hasHeightForWidth())
        self.wHeaderframe.setSizePolicy(sizePolicy)
        self.wHeaderframe.setStyleSheet("#wHeaderframe\n"
"{\n"
"border: none;\n"
"}")
        self.wHeaderframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.wHeaderframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wHeaderframe.setObjectName("wHeaderframe")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.wHeaderframe)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.wActiveTransfersContainer = QtWidgets.QWidget(self.wHeaderframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wActiveTransfersContainer.sizePolicy().hasHeightForWidth())
        self.wActiveTransfersContainer.setSizePolicy(sizePolicy)
        self.wActiveTransfersContainer.setMinimumSize(QtCore.QSize(0, 0))
        self.wActiveTransfersContainer.setStyleSheet("")
        self.wActiveTransfersContainer.setObjectName("wActiveTransfersContainer")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.wActiveTransfersContainer)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.sTabs = QtWidgets.QStackedWidget(self.wActiveTransfersContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sTabs.sizePolicy().hasHeightForWidth())
        self.sTabs.setSizePolicy(sizePolicy)
        self.sTabs.setMinimumSize(QtCore.QSize(0, 50))
        self.sTabs.setStyleSheet("background-color: rgb(21, 32, 43);")
        self.sTabs.setObjectName("sTabs")
        self.pTransfersTab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pTransfersTab.sizePolicy().hasHeightForWidth())
        self.pTransfersTab.setSizePolicy(sizePolicy)
        self.pTransfersTab.setObjectName("pTransfersTab")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.pTransfersTab)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.textEdit = QtWidgets.QTextEdit(self.pTransfersTab)
        font = QtGui.QFont()
        font.setFamily("Lemon")
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_10.addWidget(self.textEdit)
        self.sTabs.addWidget(self.pTransfersTab)
        self.pNotificationsTab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pNotificationsTab.sizePolicy().hasHeightForWidth())
        self.pNotificationsTab.setSizePolicy(sizePolicy)
        self.pNotificationsTab.setObjectName("pNotificationsTab")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.pNotificationsTab)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.textEdit2 = QtWidgets.QTextEdit(self.pNotificationsTab)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(21, 32, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(21, 32, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(21, 32, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(21, 32, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(21, 32, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(21, 32, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(21, 32, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(21, 32, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(21, 32, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.textEdit2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Kalam")
        font.setPointSize(10)
        self.textEdit2.setFont(font)
        self.textEdit2.setObjectName("textEdit2")
        self.verticalLayout_11.addWidget(self.textEdit2)
        self.sTabs.addWidget(self.pNotificationsTab)
        self.verticalLayout_15.addWidget(self.sTabs)
        self.verticalLayout_6.addWidget(self.wActiveTransfersContainer)
        self.verticalLayout_5.addWidget(self.wHeaderframe)
        self.verticalLayout_wInfoDialogIn.addWidget(self.wContainerHeader)
        self.wHeader = QtWidgets.QWidget(self.wInfoDialogIn)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wHeader.sizePolicy().hasHeightForWidth())
        self.wHeader.setSizePolicy(sizePolicy)
        self.wHeader.setMinimumSize(QtCore.QSize(0, 45))
        self.wHeader.setMaximumSize(QtCore.QSize(16777215, 60))
        self.wHeader.setStyleSheet("")
        self.wHeader.setObjectName("wHeader")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.wHeader)
        self.horizontalLayout.setContentsMargins(15, -1, 13, -1)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_wInfoDialogIn.addWidget(self.wHeader)
        self.verticalLayout_4.addWidget(self.wInfoDialogIn)

        self.retranslateUi(InfoDialog)
        self.sTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(InfoDialog)

    def retranslateUi(self, InfoDialog):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InfoDialog = QtWidgets.QDialog()
    ui = Ui_InfoDialog()
    ui.setupUi(InfoDialog)
    InfoDialog.show()
    sys.exit(app.exec_())
