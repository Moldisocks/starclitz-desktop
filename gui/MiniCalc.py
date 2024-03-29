# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MiniCalc.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MiniCalc(object):
    def setupUi(self, MiniCalc):
        MiniCalc.setObjectName("MiniCalc")
        MiniCalc.resize(450, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MiniCalc.sizePolicy().hasHeightForWidth())
        MiniCalc.setSizePolicy(sizePolicy)
        MiniCalc.setMinimumSize(QtCore.QSize(0, 200))
        MiniCalc.setMaximumSize(QtCore.QSize(600, 200))
        MiniCalc.setBaseSize(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("rsc/starclitz-logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MiniCalc.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MiniCalc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalSliderRecent = QtWidgets.QSlider(self.centralwidget)
        self.verticalSliderRecent.setMinimum(1)
        self.verticalSliderRecent.setMaximum(10)
        self.verticalSliderRecent.setProperty("value", 1)
        self.verticalSliderRecent.setTracking(True)
        self.verticalSliderRecent.setOrientation(QtCore.Qt.Vertical)
        self.verticalSliderRecent.setInvertedAppearance(True)
        self.verticalSliderRecent.setInvertedControls(False)
        self.verticalSliderRecent.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.verticalSliderRecent.setTickInterval(1)
        self.verticalSliderRecent.setObjectName("verticalSliderRecent")
        self.verticalLayout.addWidget(self.verticalSliderRecent)
        self.labelRecent = QtWidgets.QLabel(self.centralwidget)
        self.labelRecent.setObjectName("labelRecent")
        self.verticalLayout.addWidget(self.labelRecent)
        self.pushButtonClear = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonClear.sizePolicy().hasHeightForWidth())
        self.pushButtonClear.setSizePolicy(sizePolicy)
        self.pushButtonClear.setMaximumSize(QtCore.QSize(38, 16777215))
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.verticalLayout.addWidget(self.pushButtonClear)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.verticalLayoutLeft = QtWidgets.QVBoxLayout()
        self.verticalLayoutLeft.setObjectName("verticalLayoutLeft")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelBalance = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelBalance.sizePolicy().hasHeightForWidth())
        self.labelBalance.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelBalance.setFont(font)
        self.labelBalance.setObjectName("labelBalance")
        self.horizontalLayout.addWidget(self.labelBalance)
        self.lineEditBalance = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditBalance.sizePolicy().hasHeightForWidth())
        self.lineEditBalance.setSizePolicy(sizePolicy)
        self.lineEditBalance.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEditBalance.setObjectName("lineEditBalance")
        self.horizontalLayout.addWidget(self.lineEditBalance)
        self.verticalLayoutLeft.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.labelBuy = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelBuy.sizePolicy().hasHeightForWidth())
        self.labelBuy.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelBuy.setFont(font)
        self.labelBuy.setObjectName("labelBuy")
        self.gridLayout.addWidget(self.labelBuy, 0, 0, 1, 1)
        self.lineEditCargo = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditCargo.sizePolicy().hasHeightForWidth())
        self.lineEditCargo.setSizePolicy(sizePolicy)
        self.lineEditCargo.setObjectName("lineEditCargo")
        self.gridLayout.addWidget(self.lineEditCargo, 2, 1, 1, 1)
        self.lineEditSellPrice = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditSellPrice.sizePolicy().hasHeightForWidth())
        self.lineEditSellPrice.setSizePolicy(sizePolicy)
        self.lineEditSellPrice.setObjectName("lineEditSellPrice")
        self.gridLayout.addWidget(self.lineEditSellPrice, 1, 1, 1, 1)
        self.labelSCU = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSCU.sizePolicy().hasHeightForWidth())
        self.labelSCU.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelSCU.setFont(font)
        self.labelSCU.setObjectName("labelSCU")
        self.gridLayout.addWidget(self.labelSCU, 2, 0, 1, 1)
        self.lineEditBuyPrice = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditBuyPrice.sizePolicy().hasHeightForWidth())
        self.lineEditBuyPrice.setSizePolicy(sizePolicy)
        self.lineEditBuyPrice.setMinimumSize(QtCore.QSize(120, 0))
        self.lineEditBuyPrice.setObjectName("lineEditBuyPrice")
        self.gridLayout.addWidget(self.lineEditBuyPrice, 0, 1, 1, 1)
        self.labelSell = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSell.sizePolicy().hasHeightForWidth())
        self.labelSell.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelSell.setFont(font)
        self.labelSell.setObjectName("labelSell")
        self.gridLayout.addWidget(self.labelSell, 1, 0, 1, 1)
        self.verticalLayoutLeft.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutLeft.addItem(spacerItem)
        self.pushButtonCalculate = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonCalculate.sizePolicy().hasHeightForWidth())
        self.pushButtonCalculate.setSizePolicy(sizePolicy)
        self.pushButtonCalculate.setObjectName("pushButtonCalculate")
        self.verticalLayoutLeft.addWidget(self.pushButtonCalculate)
        self.horizontalLayout_2.addLayout(self.verticalLayoutLeft)
        self.lineMiddleDivider = QtWidgets.QFrame(self.centralwidget)
        self.lineMiddleDivider.setFrameShape(QtWidgets.QFrame.VLine)
        self.lineMiddleDivider.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineMiddleDivider.setObjectName("lineMiddleDivider")
        self.horizontalLayout_2.addWidget(self.lineMiddleDivider)
        self.verticalLayoutRight = QtWidgets.QVBoxLayout()
        self.verticalLayoutRight.setContentsMargins(-1, -1, -1, 1)
        self.verticalLayoutRight.setSpacing(6)
        self.verticalLayoutRight.setObjectName("verticalLayoutRight")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelUnits_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelUnits_2.sizePolicy().hasHeightForWidth())
        self.labelUnits_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelUnits_2.setFont(font)
        self.labelUnits_2.setObjectName("labelUnits_2")
        self.gridLayout_2.addWidget(self.labelUnits_2, 3, 0, 1, 1)
        self.labelUnits = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelUnits.sizePolicy().hasHeightForWidth())
        self.labelUnits.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.labelUnits.setFont(font)
        self.labelUnits.setText("")
        self.labelUnits.setObjectName("labelUnits")
        self.gridLayout_2.addWidget(self.labelUnits, 3, 1, 1, 1)
        self.labelProfit = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelProfit.sizePolicy().hasHeightForWidth())
        self.labelProfit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.labelProfit.setFont(font)
        self.labelProfit.setText("")
        self.labelProfit.setObjectName("labelProfit")
        self.gridLayout_2.addWidget(self.labelProfit, 2, 1, 1, 1)
        self.labelCeilingCapital = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.labelCeilingCapital.setFont(font)
        self.labelCeilingCapital.setText("")
        self.labelCeilingCapital.setObjectName("labelCeilingCapital")
        self.gridLayout_2.addWidget(self.labelCeilingCapital, 5, 1, 1, 1)
        self.labelProfitCeiling = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelProfitCeiling.sizePolicy().hasHeightForWidth())
        self.labelProfitCeiling.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.labelProfitCeiling.setFont(font)
        self.labelProfitCeiling.setText("")
        self.labelProfitCeiling.setObjectName("labelProfitCeiling")
        self.gridLayout_2.addWidget(self.labelProfitCeiling, 4, 1, 1, 1)
        self.labelCapital = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelCapital.sizePolicy().hasHeightForWidth())
        self.labelCapital.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.labelCapital.setFont(font)
        self.labelCapital.setText("")
        self.labelCapital.setObjectName("labelCapital")
        self.gridLayout_2.addWidget(self.labelCapital, 0, 1, 1, 1)
        self.labelProfitCeiling_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelProfitCeiling_2.sizePolicy().hasHeightForWidth())
        self.labelProfitCeiling_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelProfitCeiling_2.setFont(font)
        self.labelProfitCeiling_2.setObjectName("labelProfitCeiling_2")
        self.gridLayout_2.addWidget(self.labelProfitCeiling_2, 4, 0, 1, 1)
        self.labelCapital_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelCapital_2.sizePolicy().hasHeightForWidth())
        self.labelCapital_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelCapital_2.setFont(font)
        self.labelCapital_2.setObjectName("labelCapital_2")
        self.gridLayout_2.addWidget(self.labelCapital_2, 0, 0, 1, 1)
        self.labelProfit_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelProfit_2.sizePolicy().hasHeightForWidth())
        self.labelProfit_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelProfit_2.setFont(font)
        self.labelProfit_2.setObjectName("labelProfit_2")
        self.gridLayout_2.addWidget(self.labelProfit_2, 2, 0, 1, 1)
        self.labelCeilingCapital_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelCeilingCapital_2.setFont(font)
        self.labelCeilingCapital_2.setObjectName("labelCeilingCapital_2")
        self.gridLayout_2.addWidget(self.labelCeilingCapital_2, 5, 0, 1, 1)
        self.labelReturn_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelReturn_2.setFont(font)
        self.labelReturn_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelReturn_2.setObjectName("labelReturn_2")
        self.gridLayout_2.addWidget(self.labelReturn_2, 1, 0, 1, 1)
        self.labelReturn = QtWidgets.QLabel(self.centralwidget)
        self.labelReturn.setText("")
        self.labelReturn.setObjectName("labelReturn")
        self.gridLayout_2.addWidget(self.labelReturn, 1, 1, 1, 1)
        self.verticalLayoutRight.addLayout(self.gridLayout_2)
        self.pushButtonOntop = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonOntop.sizePolicy().hasHeightForWidth())
        self.pushButtonOntop.setSizePolicy(sizePolicy)
        self.pushButtonOntop.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButtonOntop.setObjectName("pushButtonOntop")
        self.verticalLayoutRight.addWidget(self.pushButtonOntop)
        self.horizontalLayout_2.addLayout(self.verticalLayoutRight)
        MiniCalc.setCentralWidget(self.centralwidget)
        self.actionAlways_On_Top = QtWidgets.QAction(MiniCalc)
        self.actionAlways_On_Top.setObjectName("actionAlways_On_Top")
        self.actionExit = QtWidgets.QAction(MiniCalc)
        self.actionExit.setObjectName("actionExit")

        self.retranslateUi(MiniCalc)
        QtCore.QMetaObject.connectSlotsByName(MiniCalc)
        MiniCalc.setTabOrder(self.lineEditBalance, self.lineEditBuyPrice)
        MiniCalc.setTabOrder(self.lineEditBuyPrice, self.lineEditSellPrice)
        MiniCalc.setTabOrder(self.lineEditSellPrice, self.lineEditCargo)

    def retranslateUi(self, MiniCalc):
        _translate = QtCore.QCoreApplication.translate
        MiniCalc.setWindowTitle(_translate("MiniCalc", "Starclitz - Mini Calc"))
        self.label.setText(_translate("MiniCalc", "Oldest"))
        self.labelRecent.setText(_translate("MiniCalc", "Current"))
        self.pushButtonClear.setText(_translate("MiniCalc", "Clear"))
        self.labelBalance.setText(_translate("MiniCalc", "Balance"))
        self.labelBuy.setText(_translate("MiniCalc", "Buy"))
        self.lineEditCargo.setPlaceholderText(_translate("MiniCalc", "Enter ship\'s cargo capacity"))
        self.lineEditSellPrice.setPlaceholderText(_translate("MiniCalc", "Enter sell price"))
        self.labelSCU.setText(_translate("MiniCalc", "SCU"))
        self.lineEditBuyPrice.setPlaceholderText(_translate("MiniCalc", "Enter buy price"))
        self.labelSell.setText(_translate("MiniCalc", "Sell"))
        self.pushButtonCalculate.setText(_translate("MiniCalc", "Calculate"))
        self.labelUnits_2.setText(_translate("MiniCalc", "Unit Count:"))
        self.labelProfitCeiling_2.setText(_translate("MiniCalc", "Profit Ceiling:"))
        self.labelCapital_2.setText(_translate("MiniCalc", "Capital:"))
        self.labelProfit_2.setText(_translate("MiniCalc", "Profit:"))
        self.labelCeilingCapital_2.setText(_translate("MiniCalc", "Max Outlay:"))
        self.labelReturn_2.setText(_translate("MiniCalc", "Return:"))
        self.pushButtonOntop.setToolTip(_translate("MiniCalc", "<html><head/><body><p>Always on top.</p></body></html>"))
        self.pushButtonOntop.setText(_translate("MiniCalc", "Enable Always On-top"))
        self.actionAlways_On_Top.setText(_translate("MiniCalc", "Always On Top"))
        self.actionExit.setText(_translate("MiniCalc", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MiniCalc = QtWidgets.QMainWindow()
    ui = Ui_MiniCalc()
    ui.setupUi(MiniCalc)
    MiniCalc.show()
    sys.exit(app.exec_())
