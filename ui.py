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
        InfoDialog.setWindowTitle("")
        InfoDialog.setStyleSheet("\n"
"#wInfoDialogIn\n"
"{\n"
" border-radius: 16px;\n"
" border: 1px solid rgba(100, 100, 100);\n"
" background-color:  #F4F6F8;\n"
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
        self.wHeader = QtWidgets.QWidget(self.wHeaderframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wHeader.sizePolicy().hasHeightForWidth())
        self.wHeader.setSizePolicy(sizePolicy)
        self.wHeader.setMinimumSize(QtCore.QSize(0, 60))
        self.wHeader.setMaximumSize(QtCore.QSize(16777215, 60))
        self.wHeader.setStyleSheet("")
        self.wHeader.setObjectName("wHeader")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.wHeader)
        self.horizontalLayout.setContentsMargins(15, -1, 13, -1)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bUpgrade = QtWidgets.QPushButton(self.wHeader)
        self.bUpgrade.setMinimumSize(QtCore.QSize(0, 30))
        self.bUpgrade.setMaximumSize(QtCore.QSize(16777215, 30))
        self.bUpgrade.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.bUpgrade.setMouseTracking(False)
        self.bUpgrade.setStyleSheet("#bUpgrade\n"
"{\n"
"font-family: Lato;\n"
"font-size: 14px;\n"
"border: 1px solid rgba(0, 0, 0, 5%);\n"
"border-radius: 3px;\n"
"color: #333333;\n"
"padding: 3px 12px 3px 12px;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #ffffff, stop: 1 #fafafa);\n"
"}\n"
"\n"
"#bUpgrade::hover\n"
"{\n"
"border: 1px solid rgba(0, 0, 0, 10%);\n"
"}\n"
"\n"
"#bUpgrade::pressed\n"
"{\n"
"font-family: Lato;\n"
"font-size: 14px;\n"
"border: 1px solid rgba(0, 0, 0, 5%);\n"
"border-radius: 3px;\n"
"color: #333333;\n"
"padding: 6px 12px 6px 12px;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #ffffff, stop: 1 #fafafa);\n"
"}")
        self.bUpgrade.setFlat(True)
        self.bUpgrade.setObjectName("bUpgrade")
        self.horizontalLayout.addWidget(self.bUpgrade)
        self.bSettings = QtWidgets.QPushButton(self.wHeader)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bSettings.sizePolicy().hasHeightForWidth())
        self.bSettings.setSizePolicy(sizePolicy)
        self.bSettings.setMinimumSize(QtCore.QSize(24, 24))
        self.bSettings.setMaximumSize(QtCore.QSize(24, 24))
        self.bSettings.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bSettings.setStyleSheet("#bSettings\n"
"{\n"
"border: none;\n"
"}\n"
"")
        self.bSettings.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/more_settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bSettings.setIcon(icon)
        self.bSettings.setIconSize(QtCore.QSize(24, 24))
        self.bSettings.setFlat(True)
        self.bSettings.setObjectName("bSettings")
        self.horizontalLayout.addWidget(self.bSettings)
        self.verticalLayout_6.addWidget(self.wHeader)
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
        self.sTabs.addWidget(self.pNotificationsTab)
        self.verticalLayout_15.addWidget(self.sTabs)
        self.verticalLayout_6.addWidget(self.wActiveTransfersContainer)
        self.verticalLayout_5.addWidget(self.wHeaderframe)
        self.verticalLayout_wInfoDialogIn.addWidget(self.wContainerHeader)
        self.verticalLayout_4.addWidget(self.wInfoDialogIn)

        self.retranslateUi(InfoDialog)
        self.sTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(InfoDialog)

    def retranslateUi(self, InfoDialog):
        _translate = QtCore.QCoreApplication.translate
        self.bUpgrade.setText(_translate("InfoDialog", "demo boton"))
        self.bSettings.setToolTip(_translate("InfoDialog", "Show MEGAsync options"))
#import Resources_win_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InfoDialog = QtWidgets.QDialog()
    ui = Ui_InfoDialog()
    ui.setupUi(InfoDialog)
    InfoDialog.show()
    sys.exit(app.exec_())
