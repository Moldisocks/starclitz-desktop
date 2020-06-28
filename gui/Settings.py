# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Settings.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("rsc/starclitz-logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Settings.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Settings)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tabDatabase = QtWidgets.QWidget()
        self.tabDatabase.setObjectName("tabDatabase")
        self.gridLayout = QtWidgets.QGridLayout(self.tabDatabase)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonClearDatabase = QtWidgets.QPushButton(self.tabDatabase)
        self.pushButtonClearDatabase.setObjectName("pushButtonClearDatabase")
        self.gridLayout.addWidget(self.pushButtonClearDatabase, 0, 0, 1, 1)
        self.pushButtonUpdateCache = QtWidgets.QPushButton(self.tabDatabase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonUpdateCache.sizePolicy().hasHeightForWidth())
        self.pushButtonUpdateCache.setSizePolicy(sizePolicy)
        self.pushButtonUpdateCache.setObjectName("pushButtonUpdateCache")
        self.gridLayout.addWidget(self.pushButtonUpdateCache, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tabDatabase, "")
        self.verticalLayout.addWidget(self.tabWidget)
        Settings.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(Settings)
        self.statusBar.setObjectName("statusBar")
        Settings.setStatusBar(self.statusBar)
        self.actionTest = QtWidgets.QAction(Settings)
        self.actionTest.setObjectName("actionTest")

        self.retranslateUi(Settings)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Settings"))
        self.pushButtonClearDatabase.setText(_translate("Settings", "Clear database"))
        self.pushButtonUpdateCache.setText(_translate("Settings", "Update cache"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDatabase), _translate("Settings", "Database"))
        self.actionTest.setText(_translate("Settings", "Test"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Settings = QtWidgets.QMainWindow()
    ui = Ui_Settings()
    ui.setupUi(Settings)
    Settings.show()
    sys.exit(app.exec_())
