# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dashboard(object):
    def setupUi(self, Dashboard):
        Dashboard.setObjectName("Dashboard")
        Dashboard.resize(950, 550)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dashboard.sizePolicy().hasHeightForWidth())
        Dashboard.setSizePolicy(sizePolicy)
        Dashboard.setMinimumSize(QtCore.QSize(950, 550))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("rsc/starclitz-logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dashboard.setWindowIcon(icon)
        Dashboard.setDockNestingEnabled(True)
        Dashboard.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(Dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayoutLeftMenu = QtWidgets.QVBoxLayout()
        self.verticalLayoutLeftMenu.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayoutLeftMenu.setContentsMargins(-1, -1, 6, -1)
        self.verticalLayoutLeftMenu.setSpacing(0)
        self.verticalLayoutLeftMenu.setObjectName("verticalLayoutLeftMenu")
        self.labelTitle = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setObjectName("labelTitle")
        self.verticalLayoutLeftMenu.addWidget(self.labelTitle)
        self.pushButtonGotoTradeRuns = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonGotoTradeRuns.sizePolicy().hasHeightForWidth())
        self.pushButtonGotoTradeRuns.setSizePolicy(sizePolicy)
        self.pushButtonGotoTradeRuns.setObjectName("pushButtonGotoTradeRuns")
        self.verticalLayoutLeftMenu.addWidget(self.pushButtonGotoTradeRuns)
        self.pushButtonGotoMiniCalc = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonGotoMiniCalc.sizePolicy().hasHeightForWidth())
        self.pushButtonGotoMiniCalc.setSizePolicy(sizePolicy)
        self.pushButtonGotoMiniCalc.setObjectName("pushButtonGotoMiniCalc")
        self.verticalLayoutLeftMenu.addWidget(self.pushButtonGotoMiniCalc)
        self.pushButtonGotoPriceSheet = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonGotoPriceSheet.setObjectName("pushButtonGotoPriceSheet")
        self.verticalLayoutLeftMenu.addWidget(self.pushButtonGotoPriceSheet)
        self.pushButtonGotoShipHangar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonGotoShipHangar.setObjectName("pushButtonGotoShipHangar")
        self.verticalLayoutLeftMenu.addWidget(self.pushButtonGotoShipHangar)
        self.pushButtonCompareTool = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCompareTool.setObjectName("pushButtonCompareTool")
        self.verticalLayoutLeftMenu.addWidget(self.pushButtonCompareTool)
        self.pushButtonSettings = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSettings.setObjectName("pushButtonSettings")
        self.verticalLayoutLeftMenu.addWidget(self.pushButtonSettings)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutLeftMenu.addItem(spacerItem)
        self.verticalLayoutLeftMenu.setStretch(1, 1)
        self.horizontalLayout.addLayout(self.verticalLayoutLeftMenu)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        Dashboard.setCentralWidget(self.centralwidget)
        self.dockWidgetWallet = QtWidgets.QDockWidget(Dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetWallet.sizePolicy().hasHeightForWidth())
        self.dockWidgetWallet.setSizePolicy(sizePolicy)
        self.dockWidgetWallet.setMinimumSize(QtCore.QSize(400, 200))
        self.dockWidgetWallet.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dockWidgetWallet.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidgetWallet.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidgetWallet.setObjectName("dockWidgetWallet")
        self.dockWidgetContentsWallet = QtWidgets.QWidget()
        self.dockWidgetContentsWallet.setObjectName("dockWidgetContentsWallet")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContentsWallet)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayoutBalance = QtWidgets.QHBoxLayout()
        self.horizontalLayoutBalance.setObjectName("horizontalLayoutBalance")
        self.labelBalance = QtWidgets.QLabel(self.dockWidgetContentsWallet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelBalance.sizePolicy().hasHeightForWidth())
        self.labelBalance.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelBalance.setFont(font)
        self.labelBalance.setObjectName("labelBalance")
        self.horizontalLayoutBalance.addWidget(self.labelBalance)
        self.lineEditBalance = QtWidgets.QLineEdit(self.dockWidgetContentsWallet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditBalance.sizePolicy().hasHeightForWidth())
        self.lineEditBalance.setSizePolicy(sizePolicy)
        self.lineEditBalance.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEditBalance.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEditBalance.setObjectName("lineEditBalance")
        self.horizontalLayoutBalance.addWidget(self.lineEditBalance)
        self.pushButtonBalanceSave = QtWidgets.QPushButton(self.dockWidgetContentsWallet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonBalanceSave.sizePolicy().hasHeightForWidth())
        self.pushButtonBalanceSave.setSizePolicy(sizePolicy)
        self.pushButtonBalanceSave.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("rsc/save.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonBalanceSave.setIcon(icon1)
        self.pushButtonBalanceSave.setObjectName("pushButtonBalanceSave")
        self.horizontalLayoutBalance.addWidget(self.pushButtonBalanceSave)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutBalance.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayoutBalance)
        self.listViewTransactionHistory = QtWidgets.QListView(self.dockWidgetContentsWallet)
        self.listViewTransactionHistory.setStyleSheet("background-color:#919191 ;")
        self.listViewTransactionHistory.setObjectName("listViewTransactionHistory")
        self.verticalLayout.addWidget(self.listViewTransactionHistory)
        self.dockWidgetWallet.setWidget(self.dockWidgetContentsWallet)
        Dashboard.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidgetWallet)
        self.dockWidgetFavouriteCommodities = QtWidgets.QDockWidget(Dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetFavouriteCommodities.sizePolicy().hasHeightForWidth())
        self.dockWidgetFavouriteCommodities.setSizePolicy(sizePolicy)
        self.dockWidgetFavouriteCommodities.setMinimumSize(QtCore.QSize(404, 297))
        self.dockWidgetFavouriteCommodities.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidgetFavouriteCommodities.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidgetFavouriteCommodities.setObjectName("dockWidgetFavouriteCommodities")
        self.dockWidgetContentsFavouriteCommodities = QtWidgets.QWidget()
        self.dockWidgetContentsFavouriteCommodities.setObjectName("dockWidgetContentsFavouriteCommodities")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContentsFavouriteCommodities)
        self.verticalLayout_2.setContentsMargins(2, 3, 2, 3)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.treeViewFavouriteCommodities = QtWidgets.QTreeView(self.dockWidgetContentsFavouriteCommodities)
        self.treeViewFavouriteCommodities.setStyleSheet("background-color:#919191 ;")
        self.treeViewFavouriteCommodities.setObjectName("treeViewFavouriteCommodities")
        self.verticalLayout_2.addWidget(self.treeViewFavouriteCommodities)
        self.dockWidgetFavouriteCommodities.setWidget(self.dockWidgetContentsFavouriteCommodities)
        Dashboard.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidgetFavouriteCommodities)
        self.dockWidgetTradeHistory = QtWidgets.QDockWidget(Dashboard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetTradeHistory.sizePolicy().hasHeightForWidth())
        self.dockWidgetTradeHistory.setSizePolicy(sizePolicy)
        self.dockWidgetTradeHistory.setMinimumSize(QtCore.QSize(400, 200))
        self.dockWidgetTradeHistory.setBaseSize(QtCore.QSize(0, 0))
        self.dockWidgetTradeHistory.setFloating(False)
        self.dockWidgetTradeHistory.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidgetTradeHistory.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidgetTradeHistory.setObjectName("dockWidgetTradeHistory")
        self.dockWidgetContentsTradeHistory = QtWidgets.QWidget()
        self.dockWidgetContentsTradeHistory.setObjectName("dockWidgetContentsTradeHistory")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dockWidgetContentsTradeHistory)
        self.verticalLayout_3.setContentsMargins(2, 3, 2, 3)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.treeViewTradeHistory = QtWidgets.QTreeView(self.dockWidgetContentsTradeHistory)
        self.treeViewTradeHistory.setStyleSheet("background-color:#919191 ;")
        self.treeViewTradeHistory.setObjectName("treeViewTradeHistory")
        self.verticalLayout_3.addWidget(self.treeViewTradeHistory)
        self.dockWidgetTradeHistory.setWidget(self.dockWidgetContentsTradeHistory)
        Dashboard.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidgetTradeHistory)

        self.retranslateUi(Dashboard)
        QtCore.QMetaObject.connectSlotsByName(Dashboard)

    def retranslateUi(self, Dashboard):
        _translate = QtCore.QCoreApplication.translate
        Dashboard.setWindowTitle(_translate("Dashboard", "Starclitz - Dashboard"))
        self.labelTitle.setText(_translate("Dashboard", "Dashboard"))
        self.pushButtonGotoTradeRuns.setText(_translate("Dashboard", "Trade Runs🚚"))
        self.pushButtonGotoMiniCalc.setText(_translate("Dashboard", "Mini Calculator 🧮"))
        self.pushButtonGotoPriceSheet.setText(_translate("Dashboard", "Price sheet 💲"))
        self.pushButtonGotoShipHangar.setText(_translate("Dashboard", "Ship Hangar 🚀"))
        self.pushButtonGotoShipHangar.setShortcut(_translate("Dashboard", "Ctrl+S"))
        self.pushButtonCompareTool.setText(_translate("Dashboard", "Compare Tool 📱📲"))
        self.pushButtonSettings.setText(_translate("Dashboard", " Settings⚙"))
        self.dockWidgetWallet.setWindowTitle(_translate("Dashboard", "Wallet"))
        self.labelBalance.setText(_translate("Dashboard", "Balance"))
        self.dockWidgetFavouriteCommodities.setWindowTitle(_translate("Dashboard", "Favourite Commodities"))
        self.dockWidgetTradeHistory.setWindowTitle(_translate("Dashboard", "Trade History"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dashboard = QtWidgets.QMainWindow()
    ui = Ui_Dashboard()
    ui.setupUi(Dashboard)
    Dashboard.show()
    sys.exit(app.exec_())
