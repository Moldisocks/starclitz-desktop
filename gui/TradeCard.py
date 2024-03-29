# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TradeCard.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TradeCard(object):
    def setupUi(self, TradeCard):
        TradeCard.setObjectName("TradeCard")
        TradeCard.resize(590, 203)
        TradeCard.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        TradeCard.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBoxProfit = QtWidgets.QGroupBox(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxProfit.sizePolicy().hasHeightForWidth())
        self.groupBoxProfit.setSizePolicy(sizePolicy)
        self.groupBoxProfit.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBoxProfit.setObjectName("groupBoxProfit")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBoxProfit)
        self.verticalLayout_4.setContentsMargins(6, 1, 3, 3)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayoutProfitRow2 = QtWidgets.QHBoxLayout()
        self.horizontalLayoutProfitRow2.setObjectName("horizontalLayoutProfitRow2")
        self.lineEditProfitCosts = QtWidgets.QLineEdit(self.groupBoxProfit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditProfitCosts.sizePolicy().hasHeightForWidth())
        self.lineEditProfitCosts.setSizePolicy(sizePolicy)
        self.lineEditProfitCosts.setObjectName("lineEditProfitCosts")
        self.horizontalLayoutProfitRow2.addWidget(self.lineEditProfitCosts)
        self.pushButtonProfitCostsSave = QtWidgets.QPushButton(self.groupBoxProfit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonProfitCostsSave.sizePolicy().hasHeightForWidth())
        self.pushButtonProfitCostsSave.setSizePolicy(sizePolicy)
        self.pushButtonProfitCostsSave.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("rsc/save.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonProfitCostsSave.setIcon(icon)
        self.pushButtonProfitCostsSave.setFlat(True)
        self.pushButtonProfitCostsSave.setObjectName("pushButtonProfitCostsSave")
        self.horizontalLayoutProfitRow2.addWidget(self.pushButtonProfitCostsSave)
        self.verticalLayout_4.addLayout(self.horizontalLayoutProfitRow2)
        self.gridLayoutProfitRow1 = QtWidgets.QGridLayout()
        self.gridLayoutProfitRow1.setObjectName("gridLayoutProfitRow1")
        self.labelProfitRawProfit = QtWidgets.QLabel(self.groupBoxProfit)
        self.labelProfitRawProfit.setObjectName("labelProfitRawProfit")
        self.gridLayoutProfitRow1.addWidget(self.labelProfitRawProfit, 2, 0, 1, 1)
        self.labelProfitCapital = QtWidgets.QLabel(self.groupBoxProfit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelProfitCapital.sizePolicy().hasHeightForWidth())
        self.labelProfitCapital.setSizePolicy(sizePolicy)
        self.labelProfitCapital.setObjectName("labelProfitCapital")
        self.gridLayoutProfitRow1.addWidget(self.labelProfitCapital, 0, 0, 1, 1)
        self.labelProfitCapitalValue = QtWidgets.QLabel(self.groupBoxProfit)
        self.labelProfitCapitalValue.setObjectName("labelProfitCapitalValue")
        self.gridLayoutProfitRow1.addWidget(self.labelProfitCapitalValue, 0, 1, 1, 1)
        self.labelProfitReturn = QtWidgets.QLabel(self.groupBoxProfit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelProfitReturn.sizePolicy().hasHeightForWidth())
        self.labelProfitReturn.setSizePolicy(sizePolicy)
        self.labelProfitReturn.setObjectName("labelProfitReturn")
        self.gridLayoutProfitRow1.addWidget(self.labelProfitReturn, 1, 0, 1, 1)
        self.labelProfitReturnValue = QtWidgets.QLabel(self.groupBoxProfit)
        self.labelProfitReturnValue.setObjectName("labelProfitReturnValue")
        self.gridLayoutProfitRow1.addWidget(self.labelProfitReturnValue, 1, 1, 1, 1)
        self.labelProfitRawProfitValue = QtWidgets.QLabel(self.groupBoxProfit)
        self.labelProfitRawProfitValue.setObjectName("labelProfitRawProfitValue")
        self.gridLayoutProfitRow1.addWidget(self.labelProfitRawProfitValue, 2, 1, 1, 1)
        self.labelProfitActualProfit = QtWidgets.QLabel(self.groupBoxProfit)
        self.labelProfitActualProfit.setObjectName("labelProfitActualProfit")
        self.gridLayoutProfitRow1.addWidget(self.labelProfitActualProfit, 3, 0, 1, 1)
        self.labelProfitActualProfitValue = QtWidgets.QLabel(self.groupBoxProfit)
        self.labelProfitActualProfitValue.setObjectName("labelProfitActualProfitValue")
        self.gridLayoutProfitRow1.addWidget(self.labelProfitActualProfitValue, 3, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayoutProfitRow1)
        self.progressBarProfit = QtWidgets.QProgressBar(self.groupBoxProfit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBarProfit.sizePolicy().hasHeightForWidth())
        self.progressBarProfit.setSizePolicy(sizePolicy)
        self.progressBarProfit.setMinimumSize(QtCore.QSize(0, 40))
        self.progressBarProfit.setMaximumSize(QtCore.QSize(16777215, 40))
        self.progressBarProfit.setAutoFillBackground(False)
        self.progressBarProfit.setStyleSheet(" QProgressBar::chunk {\n"
"     background-color: #76ff63;\n"
"     width: 1px;\n"
" }\n"
"\n"
" QProgressBar {\n"
"     border: 1px solid black;\n"
"     background-color: #d1b969;\n"
"     border-radius: 0px;\n"
"     text-align: right;\n"
" }")
        self.progressBarProfit.setMinimum(0)
        self.progressBarProfit.setMaximum(100)
        self.progressBarProfit.setProperty("value", 45)
        self.progressBarProfit.setInvertedAppearance(True)
        self.progressBarProfit.setObjectName("progressBarProfit")
        self.verticalLayout_4.addWidget(self.progressBarProfit)
        self.horizontalLayout.addWidget(self.groupBoxProfit)
        self.groupBoxTravel = QtWidgets.QGroupBox(self.dockWidgetContents)
        self.groupBoxTravel.setObjectName("groupBoxTravel")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBoxTravel)
        self.verticalLayout_5.setContentsMargins(6, 1, 3, 3)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayoutTravelRow1 = QtWidgets.QGridLayout()
        self.gridLayoutTravelRow1.setObjectName("gridLayoutTravelRow1")
        self.labelTravelBuyLocation = QtWidgets.QLabel(self.groupBoxTravel)
        self.labelTravelBuyLocation.setObjectName("labelTravelBuyLocation")
        self.gridLayoutTravelRow1.addWidget(self.labelTravelBuyLocation, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBoxTravel)
        self.label.setObjectName("label")
        self.gridLayoutTravelRow1.addWidget(self.label, 1, 0, 1, 1)
        self.labelTravelBuyLocationValue = QtWidgets.QLabel(self.groupBoxTravel)
        self.labelTravelBuyLocationValue.setText("")
        self.labelTravelBuyLocationValue.setObjectName("labelTravelBuyLocationValue")
        self.gridLayoutTravelRow1.addWidget(self.labelTravelBuyLocationValue, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBoxTravel)
        self.label_2.setObjectName("label_2")
        self.gridLayoutTravelRow1.addWidget(self.label_2, 2, 0, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayoutTravelRow1)
        self.horizontalLayoutTravelRow2 = QtWidgets.QHBoxLayout()
        self.horizontalLayoutTravelRow2.setObjectName("horizontalLayoutTravelRow2")
        self.lineEditTravelBugs = QtWidgets.QLineEdit(self.groupBoxTravel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditTravelBugs.sizePolicy().hasHeightForWidth())
        self.lineEditTravelBugs.setSizePolicy(sizePolicy)
        self.lineEditTravelBugs.setObjectName("lineEditTravelBugs")
        self.horizontalLayoutTravelRow2.addWidget(self.lineEditTravelBugs)
        self.pushButtonTravelBugsSave = QtWidgets.QPushButton(self.groupBoxTravel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonTravelBugsSave.sizePolicy().hasHeightForWidth())
        self.pushButtonTravelBugsSave.setSizePolicy(sizePolicy)
        self.pushButtonTravelBugsSave.setText("")
        self.pushButtonTravelBugsSave.setIcon(icon)
        self.pushButtonTravelBugsSave.setFlat(True)
        self.pushButtonTravelBugsSave.setObjectName("pushButtonTravelBugsSave")
        self.horizontalLayoutTravelRow2.addWidget(self.pushButtonTravelBugsSave)
        self.verticalLayout_5.addLayout(self.horizontalLayoutTravelRow2)
        self.horizontalLayout.addWidget(self.groupBoxTravel)
        self.groupBoxCommodity = QtWidgets.QGroupBox(self.dockWidgetContents)
        self.groupBoxCommodity.setObjectName("groupBoxCommodity")
        self.horizontalLayout.addWidget(self.groupBoxCommodity)
        TradeCard.setWidget(self.dockWidgetContents)

        self.retranslateUi(TradeCard)
        QtCore.QMetaObject.connectSlotsByName(TradeCard)

    def retranslateUi(self, TradeCard):
        _translate = QtCore.QCoreApplication.translate
        TradeCard.setWindowTitle(_translate("TradeCard", "Trade cards"))
        self.groupBoxProfit.setTitle(_translate("TradeCard", "Profit"))
        self.lineEditProfitCosts.setPlaceholderText(_translate("TradeCard", "Costs in UEC"))
        self.labelProfitRawProfit.setText(_translate("TradeCard", "Raw Profit:"))
        self.labelProfitCapital.setText(_translate("TradeCard", "Capital Outlay:"))
        self.labelProfitCapitalValue.setText(_translate("TradeCard", "x UEC"))
        self.labelProfitReturn.setText(_translate("TradeCard", "Raw Return:"))
        self.labelProfitReturnValue.setText(_translate("TradeCard", "x UEC"))
        self.labelProfitRawProfitValue.setText(_translate("TradeCard", "x UEC x %"))
        self.labelProfitActualProfit.setText(_translate("TradeCard", "Actual Profit:"))
        self.labelProfitActualProfitValue.setText(_translate("TradeCard", "x UEC x %"))
        self.groupBoxTravel.setTitle(_translate("TradeCard", "Travel"))
        self.labelTravelBuyLocation.setText(_translate("TradeCard", "Buy location:"))
        self.label.setText(_translate("TradeCard", "TextLabel"))
        self.label_2.setText(_translate("TradeCard", "TextLabel"))
        self.lineEditTravelBugs.setPlaceholderText(_translate("TradeCard", "Bug Rating"))
        self.groupBoxCommodity.setTitle(_translate("TradeCard", "Commodity"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TradeCard = QtWidgets.QDockWidget()
    ui = Ui_TradeCard()
    ui.setupUi(TradeCard)
    TradeCard.show()
    sys.exit(app.exec_())
