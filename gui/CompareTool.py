# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CompareTool.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CompareTool(object):
    def setupUi(self, CompareTool):
        CompareTool.setObjectName("CompareTool")
        CompareTool.resize(1316, 618)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("rsc/starclitz-logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CompareTool.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(CompareTool)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayoutHeader = QtWidgets.QHBoxLayout()
        self.horizontalLayoutHeader.setObjectName("horizontalLayoutHeader")
        self.labelHeading = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelHeading.setFont(font)
        self.labelHeading.setObjectName("labelHeading")
        self.horizontalLayoutHeader.addWidget(self.labelHeading)
        self.verticalLayout.addLayout(self.horizontalLayoutHeader)
        self.horizontalLayoutBody = QtWidgets.QHBoxLayout()
        self.horizontalLayoutBody.setObjectName("horizontalLayoutBody")
        self.treeWidgetFields = QtWidgets.QTreeWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidgetFields.sizePolicy().hasHeightForWidth())
        self.treeWidgetFields.setSizePolicy(sizePolicy)
        self.treeWidgetFields.setColumnCount(2)
        self.treeWidgetFields.setObjectName("treeWidgetFields")
        self.treeWidgetFields.headerItem().setText(0, "1")
        self.treeWidgetFields.headerItem().setText(1, "2")
        self.treeWidgetFields.header().setVisible(False)
        self.horizontalLayoutBody.addWidget(self.treeWidgetFields)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutBody.addWidget(self.line)
        self.tableWidgetData = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidgetData.setObjectName("tableWidgetData")
        self.tableWidgetData.setColumnCount(0)
        self.tableWidgetData.setRowCount(0)
        self.horizontalLayoutBody.addWidget(self.tableWidgetData)
        self.verticalLayout.addLayout(self.horizontalLayoutBody)
        CompareTool.setCentralWidget(self.centralwidget)

        self.retranslateUi(CompareTool)
        QtCore.QMetaObject.connectSlotsByName(CompareTool)

    def retranslateUi(self, CompareTool):
        _translate = QtCore.QCoreApplication.translate
        CompareTool.setWindowTitle(_translate("CompareTool", "Compare Tool"))
        self.labelHeading.setText(_translate("CompareTool", "Title"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CompareTool = QtWidgets.QMainWindow()
    ui = Ui_CompareTool()
    ui.setupUi(CompareTool)
    CompareTool.show()
    sys.exit(app.exec_())
