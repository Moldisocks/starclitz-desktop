# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ShipHangar.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ShipHangar(object):
    def setupUi(self, ShipHangar):
        ShipHangar.setObjectName("ShipHangar")
        ShipHangar.resize(468, 551)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("rsc/starclitz-logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ShipHangar.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(ShipHangar)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayoutHeader = QtWidgets.QHBoxLayout()
        self.horizontalLayoutHeader.setObjectName("horizontalLayoutHeader")
        self.openGLWidgetShipView = QtWidgets.QOpenGLWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openGLWidgetShipView.sizePolicy().hasHeightForWidth())
        self.openGLWidgetShipView.setSizePolicy(sizePolicy)
        self.openGLWidgetShipView.setMinimumSize(QtCore.QSize(128, 128))
        self.openGLWidgetShipView.setMaximumSize(QtCore.QSize(128, 128))
        self.openGLWidgetShipView.setObjectName("openGLWidgetShipView")
        self.horizontalLayoutHeader.addWidget(self.openGLWidgetShipView)
        self.gridLayoutShipSelection = QtWidgets.QGridLayout()
        self.gridLayoutShipSelection.setObjectName("gridLayoutShipSelection")
        self.comboBoxVariant = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxVariant.setObjectName("comboBoxVariant")
        self.gridLayoutShipSelection.addWidget(self.comboBoxVariant, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayoutShipSelection.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayoutShipSelection.addWidget(self.label, 1, 0, 1, 1)
        self.labelMake = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMake.sizePolicy().hasHeightForWidth())
        self.labelMake.setSizePolicy(sizePolicy)
        self.labelMake.setObjectName("labelMake")
        self.gridLayoutShipSelection.addWidget(self.labelMake, 0, 0, 1, 1)
        self.comboBoxMake = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxMake.setObjectName("comboBoxMake")
        self.gridLayoutShipSelection.addWidget(self.comboBoxMake, 0, 1, 1, 1)
        self.comboBoxModel = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxModel.setObjectName("comboBoxModel")
        self.gridLayoutShipSelection.addWidget(self.comboBoxModel, 1, 1, 1, 1)
        self.pushButtonAdd = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.gridLayoutShipSelection.addWidget(self.pushButtonAdd, 3, 0, 1, 2)
        self.horizontalLayoutHeader.addLayout(self.gridLayoutShipSelection)
        self.verticalLayout.addLayout(self.horizontalLayoutHeader)
        self.treeWidgetShips = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidgetShips.setObjectName("treeWidgetShips")
        self.treeWidgetShips.headerItem().setText(0, "1")
        self.treeWidgetShips.header().setVisible(False)
        self.verticalLayout.addWidget(self.treeWidgetShips)
        ShipHangar.setCentralWidget(self.centralwidget)

        self.retranslateUi(ShipHangar)
        QtCore.QMetaObject.connectSlotsByName(ShipHangar)

    def retranslateUi(self, ShipHangar):
        _translate = QtCore.QCoreApplication.translate
        ShipHangar.setWindowTitle(_translate("ShipHangar", "Ship Hangar"))
        self.label_2.setText(_translate("ShipHangar", "Select Variant:"))
        self.label.setText(_translate("ShipHangar", "Select model:"))
        self.labelMake.setText(_translate("ShipHangar", "Select make:"))
        self.pushButtonAdd.setText(_translate("ShipHangar", "V Add to Hangar V"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ShipHangar = QtWidgets.QMainWindow()
    ui = Ui_ShipHangar()
    ui.setupUi(ShipHangar)
    ShipHangar.show()
    sys.exit(app.exec_())
