# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LocationSelector.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LocationSelector(object):
    def setupUi(self, LocationSelector):
        LocationSelector.setObjectName("LocationSelector")
        LocationSelector.resize(300, 120)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LocationSelector.sizePolicy().hasHeightForWidth())
        LocationSelector.setSizePolicy(sizePolicy)
        LocationSelector.setMinimumSize(QtCore.QSize(300, 120))
        LocationSelector.setMaximumSize(QtCore.QSize(300, 120))
        self.gridLayout = QtWidgets.QGridLayout(LocationSelector)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(LocationSelector)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(LocationSelector)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(LocationSelector)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(LocationSelector)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(LocationSelector)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(LocationSelector)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout.addWidget(self.comboBox_3, 2, 1, 1, 1)
        self.pushButtonDone = QtWidgets.QPushButton(LocationSelector)
        self.pushButtonDone.setObjectName("pushButtonDone")
        self.gridLayout.addWidget(self.pushButtonDone, 3, 0, 1, 2)

        self.retranslateUi(LocationSelector)
        QtCore.QMetaObject.connectSlotsByName(LocationSelector)

    def retranslateUi(self, LocationSelector):
        _translate = QtCore.QCoreApplication.translate
        LocationSelector.setWindowTitle(_translate("LocationSelector", "Form"))
        self.label_3.setText(_translate("LocationSelector", "Select location"))
        self.label.setText(_translate("LocationSelector", "Select system"))
        self.label_2.setText(_translate("LocationSelector", "Select planet"))
        self.pushButtonDone.setText(_translate("LocationSelector", "Done"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LocationSelector = QtWidgets.QWidget()
    ui = Ui_LocationSelector()
    ui.setupUi(LocationSelector)
    LocationSelector.show()
    sys.exit(app.exec_())
