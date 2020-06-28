# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Admin(object):
    def setupUi(self, Admin):
        Admin.setObjectName("Admin")
        Admin.resize(574, 450)
        Admin.setMinimumSize(QtCore.QSize(500, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("rsc/starclitz-logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Admin.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Admin)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidgetMain = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidgetMain.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidgetMain.setObjectName("tabWidgetMain")
        self.tabEntry = QtWidgets.QWidget()
        self.tabEntry.setObjectName("tabEntry")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabEntry)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidgetItemType = QtWidgets.QTabWidget(self.tabEntry)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidgetItemType.sizePolicy().hasHeightForWidth())
        self.tabWidgetItemType.setSizePolicy(sizePolicy)
        self.tabWidgetItemType.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidgetItemType.setObjectName("tabWidgetItemType")
        self.tabCommodities = QtWidgets.QWidget()
        self.tabCommodities.setObjectName("tabCommodities")
        self.gridLayout = QtWidgets.QGridLayout(self.tabCommodities)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.pushButtonCommoditiesAdd = QtWidgets.QPushButton(self.tabCommodities)
        self.pushButtonCommoditiesAdd.setObjectName("pushButtonCommoditiesAdd")
        self.gridLayout.addWidget(self.pushButtonCommoditiesAdd, 4, 0, 1, 1)
        self.labelCommoditiesSell = QtWidgets.QLabel(self.tabCommodities)
        self.labelCommoditiesSell.setObjectName("labelCommoditiesSell")
        self.gridLayout.addWidget(self.labelCommoditiesSell, 2, 0, 1, 1)
        self.labelCommoditiesBuy = QtWidgets.QLabel(self.tabCommodities)
        self.labelCommoditiesBuy.setObjectName("labelCommoditiesBuy")
        self.gridLayout.addWidget(self.labelCommoditiesBuy, 1, 0, 1, 1)
        self.labelCommoditiesName = QtWidgets.QLabel(self.tabCommodities)
        self.labelCommoditiesName.setObjectName("labelCommoditiesName")
        self.gridLayout.addWidget(self.labelCommoditiesName, 0, 0, 1, 1)
        self.lineEditCommoditiesName = QtWidgets.QLineEdit(self.tabCommodities)
        self.lineEditCommoditiesName.setObjectName("lineEditCommoditiesName")
        self.gridLayout.addWidget(self.lineEditCommoditiesName, 0, 2, 1, 2)
        self.doubleSpinBoxCommoditiesBuy = QtWidgets.QDoubleSpinBox(self.tabCommodities)
        self.doubleSpinBoxCommoditiesBuy.setMaximum(99999999.0)
        self.doubleSpinBoxCommoditiesBuy.setObjectName("doubleSpinBoxCommoditiesBuy")
        self.gridLayout.addWidget(self.doubleSpinBoxCommoditiesBuy, 1, 2, 1, 1)
        self.doubleSpinBoxCommoditiesSell = QtWidgets.QDoubleSpinBox(self.tabCommodities)
        self.doubleSpinBoxCommoditiesSell.setMaximum(99999999.0)
        self.doubleSpinBoxCommoditiesSell.setObjectName("doubleSpinBoxCommoditiesSell")
        self.gridLayout.addWidget(self.doubleSpinBoxCommoditiesSell, 2, 2, 1, 1)
        self.labelDescription = QtWidgets.QLabel(self.tabCommodities)
        self.labelDescription.setObjectName("labelDescription")
        self.gridLayout.addWidget(self.labelDescription, 3, 0, 1, 1)
        self.lineEditCommoditiesDescription = QtWidgets.QLineEdit(self.tabCommodities)
        self.lineEditCommoditiesDescription.setObjectName("lineEditCommoditiesDescription")
        self.gridLayout.addWidget(self.lineEditCommoditiesDescription, 3, 2, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 0, 1, 1)
        self.tabWidgetItemType.addTab(self.tabCommodities, "")
        self.tabLocations = QtWidgets.QWidget()
        self.tabLocations.setObjectName("tabLocations")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tabLocations)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelLocationsName = QtWidgets.QLabel(self.tabLocations)
        self.labelLocationsName.setObjectName("labelLocationsName")
        self.gridLayout_2.addWidget(self.labelLocationsName, 0, 0, 1, 1)
        self.pushButtonLocationsAdd = QtWidgets.QPushButton(self.tabLocations)
        self.pushButtonLocationsAdd.setObjectName("pushButtonLocationsAdd")
        self.gridLayout_2.addWidget(self.pushButtonLocationsAdd, 6, 0, 1, 1)
        self.labelLocationsSystem = QtWidgets.QLabel(self.tabLocations)
        self.labelLocationsSystem.setObjectName("labelLocationsSystem")
        self.gridLayout_2.addWidget(self.labelLocationsSystem, 4, 0, 1, 1)
        self.lineEditLocationsMoon = QtWidgets.QLineEdit(self.tabLocations)
        self.lineEditLocationsMoon.setObjectName("lineEditLocationsMoon")
        self.gridLayout_2.addWidget(self.lineEditLocationsMoon, 2, 2, 1, 1)
        self.lineEditLocationsPlanet = QtWidgets.QLineEdit(self.tabLocations)
        self.lineEditLocationsPlanet.setObjectName("lineEditLocationsPlanet")
        self.gridLayout_2.addWidget(self.lineEditLocationsPlanet, 3, 2, 1, 1)
        self.labelLocationsPlanet = QtWidgets.QLabel(self.tabLocations)
        self.labelLocationsPlanet.setObjectName("labelLocationsPlanet")
        self.gridLayout_2.addWidget(self.labelLocationsPlanet, 3, 0, 1, 1)
        self.lineEditLocationsSystem = QtWidgets.QLineEdit(self.tabLocations)
        self.lineEditLocationsSystem.setObjectName("lineEditLocationsSystem")
        self.gridLayout_2.addWidget(self.lineEditLocationsSystem, 4, 2, 1, 1)
        self.labelLocationsDescription = QtWidgets.QLabel(self.tabLocations)
        self.labelLocationsDescription.setObjectName("labelLocationsDescription")
        self.gridLayout_2.addWidget(self.labelLocationsDescription, 5, 0, 1, 1)
        self.lineEditLocationsStation = QtWidgets.QLineEdit(self.tabLocations)
        self.lineEditLocationsStation.setObjectName("lineEditLocationsStation")
        self.gridLayout_2.addWidget(self.lineEditLocationsStation, 1, 2, 1, 1)
        self.lineEditLocationsName = QtWidgets.QLineEdit(self.tabLocations)
        self.lineEditLocationsName.setObjectName("lineEditLocationsName")
        self.gridLayout_2.addWidget(self.lineEditLocationsName, 0, 2, 1, 1)
        self.labelLocationsMoon = QtWidgets.QLabel(self.tabLocations)
        self.labelLocationsMoon.setObjectName("labelLocationsMoon")
        self.gridLayout_2.addWidget(self.labelLocationsMoon, 2, 0, 1, 1)
        self.labelLocationsStation = QtWidgets.QLabel(self.tabLocations)
        self.labelLocationsStation.setObjectName("labelLocationsStation")
        self.gridLayout_2.addWidget(self.labelLocationsStation, 1, 0, 1, 1)
        self.lineEditLocationsDescription = QtWidgets.QLineEdit(self.tabLocations)
        self.lineEditLocationsDescription.setObjectName("lineEditLocationsDescription")
        self.gridLayout_2.addWidget(self.lineEditLocationsDescription, 5, 2, 1, 1)
        self.tabWidgetItemType.addTab(self.tabLocations, "")
        self.tabShips = QtWidgets.QWidget()
        self.tabShips.setObjectName("tabShips")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tabShips)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEditShipsManufacturer = QtWidgets.QLineEdit(self.tabShips)
        self.lineEditShipsManufacturer.setObjectName("lineEditShipsManufacturer")
        self.gridLayout_3.addWidget(self.lineEditShipsManufacturer, 0, 1, 1, 2)
        self.pushButtonShipsAdd = QtWidgets.QPushButton(self.tabShips)
        self.pushButtonShipsAdd.setObjectName("pushButtonShipsAdd")
        self.gridLayout_3.addWidget(self.pushButtonShipsAdd, 5, 0, 1, 1)
        self.lineEditShipsModel = QtWidgets.QLineEdit(self.tabShips)
        self.lineEditShipsModel.setObjectName("lineEditShipsModel")
        self.gridLayout_3.addWidget(self.lineEditShipsModel, 1, 1, 1, 2)
        self.labelShipsVariant = QtWidgets.QLabel(self.tabShips)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelShipsVariant.sizePolicy().hasHeightForWidth())
        self.labelShipsVariant.setSizePolicy(sizePolicy)
        self.labelShipsVariant.setObjectName("labelShipsVariant")
        self.gridLayout_3.addWidget(self.labelShipsVariant, 2, 0, 1, 1)
        self.labelShipsModel = QtWidgets.QLabel(self.tabShips)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelShipsModel.sizePolicy().hasHeightForWidth())
        self.labelShipsModel.setSizePolicy(sizePolicy)
        self.labelShipsModel.setObjectName("labelShipsModel")
        self.gridLayout_3.addWidget(self.labelShipsModel, 1, 0, 1, 1)
        self.labelShipsDescription = QtWidgets.QLabel(self.tabShips)
        self.labelShipsDescription.setObjectName("labelShipsDescription")
        self.gridLayout_3.addWidget(self.labelShipsDescription, 4, 0, 1, 1)
        self.labelShipsBuy = QtWidgets.QLabel(self.tabShips)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelShipsBuy.sizePolicy().hasHeightForWidth())
        self.labelShipsBuy.setSizePolicy(sizePolicy)
        self.labelShipsBuy.setObjectName("labelShipsBuy")
        self.gridLayout_3.addWidget(self.labelShipsBuy, 3, 0, 1, 1)
        self.lineEditShipsVariant = QtWidgets.QLineEdit(self.tabShips)
        self.lineEditShipsVariant.setObjectName("lineEditShipsVariant")
        self.gridLayout_3.addWidget(self.lineEditShipsVariant, 2, 1, 1, 2)
        self.labelShipsManufacturer = QtWidgets.QLabel(self.tabShips)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelShipsManufacturer.sizePolicy().hasHeightForWidth())
        self.labelShipsManufacturer.setSizePolicy(sizePolicy)
        self.labelShipsManufacturer.setObjectName("labelShipsManufacturer")
        self.gridLayout_3.addWidget(self.labelShipsManufacturer, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 6, 0, 1, 1)
        self.lineEditShipsDescription = QtWidgets.QLineEdit(self.tabShips)
        self.lineEditShipsDescription.setObjectName("lineEditShipsDescription")
        self.gridLayout_3.addWidget(self.lineEditShipsDescription, 4, 1, 1, 2)
        self.doubleSpinBoxShipsBuy = QtWidgets.QDoubleSpinBox(self.tabShips)
        self.doubleSpinBoxShipsBuy.setMaximum(9999999999.0)
        self.doubleSpinBoxShipsBuy.setObjectName("doubleSpinBoxShipsBuy")
        self.gridLayout_3.addWidget(self.doubleSpinBoxShipsBuy, 3, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 3, 2, 1, 1)
        self.tabWidgetItemType.addTab(self.tabShips, "")
        self.verticalLayout_2.addWidget(self.tabWidgetItemType)
        self.tableWidgetCurrent = QtWidgets.QTableWidget(self.tabEntry)
        self.tableWidgetCurrent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidgetCurrent.setObjectName("tableWidgetCurrent")
        self.tableWidgetCurrent.setColumnCount(0)
        self.tableWidgetCurrent.setRowCount(0)
        self.tableWidgetCurrent.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetCurrent.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.tableWidgetCurrent)
        self.tabWidgetMain.addTab(self.tabEntry, "")
        self.verticalLayout.addWidget(self.tabWidgetMain)
        Admin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Admin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 574, 21))
        self.menubar.setObjectName("menubar")
        Admin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Admin)
        self.statusbar.setObjectName("statusbar")
        Admin.setStatusBar(self.statusbar)

        self.retranslateUi(Admin)
        self.tabWidgetMain.setCurrentIndex(0)
        self.tabWidgetItemType.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Admin)
        Admin.setTabOrder(self.lineEditCommoditiesName, self.doubleSpinBoxCommoditiesBuy)
        Admin.setTabOrder(self.doubleSpinBoxCommoditiesBuy, self.doubleSpinBoxCommoditiesSell)
        Admin.setTabOrder(self.doubleSpinBoxCommoditiesSell, self.lineEditCommoditiesDescription)
        Admin.setTabOrder(self.lineEditCommoditiesDescription, self.pushButtonCommoditiesAdd)
        Admin.setTabOrder(self.pushButtonCommoditiesAdd, self.lineEditLocationsName)
        Admin.setTabOrder(self.lineEditLocationsName, self.lineEditLocationsStation)
        Admin.setTabOrder(self.lineEditLocationsStation, self.lineEditLocationsMoon)
        Admin.setTabOrder(self.lineEditLocationsMoon, self.lineEditLocationsPlanet)
        Admin.setTabOrder(self.lineEditLocationsPlanet, self.lineEditLocationsSystem)
        Admin.setTabOrder(self.lineEditLocationsSystem, self.lineEditLocationsDescription)
        Admin.setTabOrder(self.lineEditLocationsDescription, self.pushButtonLocationsAdd)
        Admin.setTabOrder(self.pushButtonLocationsAdd, self.lineEditShipsManufacturer)
        Admin.setTabOrder(self.lineEditShipsManufacturer, self.lineEditShipsModel)
        Admin.setTabOrder(self.lineEditShipsModel, self.lineEditShipsVariant)
        Admin.setTabOrder(self.lineEditShipsVariant, self.doubleSpinBoxShipsBuy)
        Admin.setTabOrder(self.doubleSpinBoxShipsBuy, self.lineEditShipsDescription)
        Admin.setTabOrder(self.lineEditShipsDescription, self.pushButtonShipsAdd)

    def retranslateUi(self, Admin):
        _translate = QtCore.QCoreApplication.translate
        Admin.setWindowTitle(_translate("Admin", "Admin Center"))
        self.pushButtonCommoditiesAdd.setText(_translate("Admin", "Add"))
        self.labelCommoditiesSell.setText(_translate("Admin", "Sell"))
        self.labelCommoditiesBuy.setText(_translate("Admin", "Buy"))
        self.labelCommoditiesName.setText(_translate("Admin", "Name"))
        self.labelDescription.setText(_translate("Admin", "Description"))
        self.tabWidgetItemType.setTabText(self.tabWidgetItemType.indexOf(self.tabCommodities), _translate("Admin", "Commodities"))
        self.labelLocationsName.setText(_translate("Admin", "Name"))
        self.pushButtonLocationsAdd.setText(_translate("Admin", "Add"))
        self.labelLocationsSystem.setText(_translate("Admin", "System"))
        self.labelLocationsPlanet.setText(_translate("Admin", "Planet"))
        self.labelLocationsDescription.setText(_translate("Admin", "Description"))
        self.labelLocationsMoon.setText(_translate("Admin", "Moon"))
        self.labelLocationsStation.setText(_translate("Admin", "Station"))
        self.tabWidgetItemType.setTabText(self.tabWidgetItemType.indexOf(self.tabLocations), _translate("Admin", "Locations"))
        self.pushButtonShipsAdd.setText(_translate("Admin", "Add"))
        self.labelShipsVariant.setText(_translate("Admin", "Variant"))
        self.labelShipsModel.setText(_translate("Admin", "Model"))
        self.labelShipsDescription.setText(_translate("Admin", "Description"))
        self.labelShipsBuy.setText(_translate("Admin", "Buy"))
        self.labelShipsManufacturer.setText(_translate("Admin", "Manufacturer"))
        self.tabWidgetItemType.setTabText(self.tabWidgetItemType.indexOf(self.tabShips), _translate("Admin", "Ships"))
        self.tabWidgetMain.setTabText(self.tabWidgetMain.indexOf(self.tabEntry), _translate("Admin", "Entry"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Admin = QtWidgets.QMainWindow()
    ui = Ui_Admin()
    ui.setupUi(Admin)
    Admin.show()
    sys.exit(app.exec_())
