# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_bodyMain(object):
    def setupUi(self, bodyMain):
        bodyMain.setObjectName("bodyMain")
        bodyMain.resize(402, 564)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(bodyMain.sizePolicy().hasHeightForWidth())
        bodyMain.setSizePolicy(sizePolicy)
        bodyMain.setMaximumSize(QtCore.QSize(402, 564))
        bodyMain.setWindowTitle("")
        bodyMain.setStyleSheet("\n"
"#wbodyMain\n"
"{\n"
" border-radius: 10px;\n"
" background-color:  #FFFFFF;\n"
"border: none;\n"
"\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    padding-right: 12px;\n"
"    padding-left: 12px;\n"
"}\n"
"")
        bodyMain.setSizeGripEnabled(False)
        bodyMain.setModal(False)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(bodyMain)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.wbodyMain = QtWidgets.QWidget(bodyMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wbodyMain.sizePolicy().hasHeightForWidth())
        self.wbodyMain.setSizePolicy(sizePolicy)
        self.wbodyMain.setMinimumSize(QtCore.QSize(402, 564))
        self.wbodyMain.setMaximumSize(QtCore.QSize(402, 564))
        self.wbodyMain.setStyleSheet("/* background-color: rgb(21, 32, 43);*/\n"
"\n"
"background-color: rgb(0,0,0);\n"
"")
        self.wbodyMain.setObjectName("wbodyMain")
        self.verticalLayout_wInfoDialogIn = QtWidgets.QVBoxLayout(self.wbodyMain)
        self.verticalLayout_wInfoDialogIn.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_wInfoDialogIn.setSpacing(0)
        self.verticalLayout_wInfoDialogIn.setObjectName("verticalLayout_wInfoDialogIn")
        self.wContainerHeader = QtWidgets.QWidget(self.wbodyMain)
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
        self.sTabs.setStyleSheet("/*background-color: rgb(21, 32, 43);*/\n"
"\n"
"background-color: rgb(0, 0, 0);")
        self.sTabs.setObjectName("sTabs")
        self.first_tab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.first_tab.sizePolicy().hasHeightForWidth())
        self.first_tab.setSizePolicy(sizePolicy)
        self.first_tab.setObjectName("first_tab")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.first_tab)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.textEdit = QtWidgets.QTextEdit(self.first_tab)
        font = QtGui.QFont()
        font.setFamily("Geometr212 BkCn BT")
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"margin: 10px;\n"
"border:none;")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_10.addWidget(self.textEdit)
        self.sTabs.addWidget(self.first_tab)
        self.second_tap = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.second_tap.sizePolicy().hasHeightForWidth())
        self.second_tap.setSizePolicy(sizePolicy)
        self.second_tap.setObjectName("second_tap")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.second_tap)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.textEdit2 = QtWidgets.QTextEdit(self.second_tap)
        self.textEdit2.setEnabled(False)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.textEdit2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Kalam")
        font.setPointSize(10)
        self.textEdit2.setFont(font)
        self.textEdit2.setStyleSheet("color: rgb(255, 255, 255);")
        self.textEdit2.setObjectName("textEdit2")
        self.verticalLayout_11.addWidget(self.textEdit2)
        self.sTabs.addWidget(self.second_tap)
        self.verticalLayout_15.addWidget(self.sTabs)
        self.verticalLayout_6.addWidget(self.wActiveTransfersContainer)
        self.verticalLayout_5.addWidget(self.wHeaderframe)
        self.verticalLayout_wInfoDialogIn.addWidget(self.wContainerHeader)
        self.wHeader = QtWidgets.QWidget(self.wbodyMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wHeader.sizePolicy().hasHeightForWidth())
        self.wHeader.setSizePolicy(sizePolicy)
        self.wHeader.setMinimumSize(QtCore.QSize(0, 45))
        self.wHeader.setMaximumSize(QtCore.QSize(16777215, 60))
        self.wHeader.setStyleSheet("border: none;\n"
"background-color: rgb(0, 0, 0);")
        self.wHeader.setObjectName("wHeader")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.wHeader)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.wHeader)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.pushButton_4.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton_4.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_clipboard = QtWidgets.QPushButton(self.wHeader)
        self.btn_clipboard.setAutoFillBackground(False)
        self.btn_clipboard.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/btn_normal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("img/btn_hover.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_clipboard.setIcon(icon)
        self.btn_clipboard.setIconSize(QtCore.QSize(32, 32))
        self.btn_clipboard.setFlat(False)
        self.btn_clipboard.setObjectName("btn_clipboard")
        self.horizontalLayout.addWidget(self.btn_clipboard)
        self.verticalLayout_wInfoDialogIn.addWidget(self.wHeader)
        self.verticalLayout_4.addWidget(self.wbodyMain)

        self.retranslateUi(bodyMain)
        self.sTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(bodyMain)

    def retranslateUi(self, bodyMain):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    bodyMain = QtWidgets.QDialog()
    ui = Ui_bodyMain()
    ui.setupUi(bodyMain)
    bodyMain.show()
    sys.exit(app.exec_())
