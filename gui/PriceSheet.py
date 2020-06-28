# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PriceSheet.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PriceSheet(object):
    def setupUi(self, PriceSheet):
        PriceSheet.setObjectName("PriceSheet")
        PriceSheet.resize(1476, 612)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("rsc/starclitz-logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PriceSheet.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(PriceSheet)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidgetPrices = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidgetPrices.setRowCount(1)
        self.tableWidgetPrices.setColumnCount(1)
        self.tableWidgetPrices.setObjectName("tableWidgetPrices")
        self.verticalLayout.addWidget(self.tableWidgetPrices)
        PriceSheet.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(PriceSheet)
        self.toolBar.setMovable(True)
        self.toolBar.setAllowedAreas(QtCore.Qt.BottomToolBarArea|QtCore.Qt.TopToolBarArea)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName("toolBar")
        PriceSheet.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSave = QtWidgets.QAction(PriceSheet)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("rsc/save.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon1)
        self.actionSave.setObjectName("actionSave")
        self.toolBar.addAction(self.actionSave)

        self.retranslateUi(PriceSheet)
        QtCore.QMetaObject.connectSlotsByName(PriceSheet)

    def retranslateUi(self, PriceSheet):
        _translate = QtCore.QCoreApplication.translate
        PriceSheet.setWindowTitle(_translate("PriceSheet", "Starclitz - Price Sheet"))
        self.tableWidgetPrices.setSortingEnabled(True)
        self.toolBar.setWindowTitle(_translate("PriceSheet", "toolBar"))
        self.actionSave.setText(_translate("PriceSheet", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PriceSheet = QtWidgets.QMainWindow()
    ui = Ui_PriceSheet()
    ui.setupUi(PriceSheet)
    PriceSheet.show()
    sys.exit(app.exec_())
