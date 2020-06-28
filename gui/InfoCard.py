# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InfoCard.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Info(object):
    def setupUi(self, Info):
        Info.setObjectName("Info")
        Info.resize(490, 331)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("rsc/starclitz-logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Info.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Info)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayoutDescription = QtWidgets.QHBoxLayout()
        self.horizontalLayoutDescription.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayoutDescription.setObjectName("horizontalLayoutDescription")
        self.verticalLayoutLeft = QtWidgets.QVBoxLayout()
        self.verticalLayoutLeft.setObjectName("verticalLayoutLeft")
        self.labelDisplayname = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelDisplayname.sizePolicy().hasHeightForWidth())
        self.labelDisplayname.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.labelDisplayname.setFont(font)
        self.labelDisplayname.setObjectName("labelDisplayname")
        self.verticalLayoutLeft.addWidget(self.labelDisplayname)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QtCore.QSize(128, 128))
        self.graphicsView.setMaximumSize(QtCore.QSize(128, 128))
        self.graphicsView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView.setLineWidth(1)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayoutLeft.addWidget(self.graphicsView)
        self.horizontalLayoutDescription.addLayout(self.verticalLayoutLeft)
        self.scrollAreaDescription = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaDescription.sizePolicy().hasHeightForWidth())
        self.scrollAreaDescription.setSizePolicy(sizePolicy)
        self.scrollAreaDescription.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollAreaDescription.setLineWidth(1)
        self.scrollAreaDescription.setWidgetResizable(True)
        self.scrollAreaDescription.setObjectName("scrollAreaDescription")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 352, 223))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelDescription = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelDescription.setText("")
        self.labelDescription.setWordWrap(True)
        self.labelDescription.setObjectName("labelDescription")
        self.verticalLayout_2.addWidget(self.labelDescription)
        self.scrollAreaDescription.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutDescription.addWidget(self.scrollAreaDescription)
        self.verticalLayout.addLayout(self.horizontalLayoutDescription)
        self.tableWidgetDetails = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetDetails.sizePolicy().hasHeightForWidth())
        self.tableWidgetDetails.setSizePolicy(sizePolicy)
        self.tableWidgetDetails.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidgetDetails.setCornerButtonEnabled(True)
        self.tableWidgetDetails.setRowCount(1)
        self.tableWidgetDetails.setColumnCount(3)
        self.tableWidgetDetails.setObjectName("tableWidgetDetails")
        self.tableWidgetDetails.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidgetDetails.horizontalHeader().setMinimumSectionSize(36)
        self.tableWidgetDetails.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetDetails.verticalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidgetDetails)
        Info.setCentralWidget(self.centralwidget)

        self.retranslateUi(Info)
        QtCore.QMetaObject.connectSlotsByName(Info)

    def retranslateUi(self, Info):
        _translate = QtCore.QCoreApplication.translate
        Info.setWindowTitle(_translate("Info", "Info Card"))
        self.labelDisplayname.setText(_translate("Info", "Item name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Info = QtWidgets.QMainWindow()
    ui = Ui_Info()
    ui.setupUi(Info)
    Info.show()
    sys.exit(app.exec_())
