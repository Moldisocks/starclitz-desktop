import sys, functools
from PyQt5.QtWidgets import QApplication, QMainWindow, QAbstractScrollArea
from PyQt5.QtCore import pyqtSlot, Qt, pyqtSignal
from PyQt5.Qt import QStandardItemModel, QStandardItem, QColor, QFont, QTableWidgetItem, QStyleFactory, QMenu, QDockWidget

from gui.Dashboard import Ui_Dashboard
from gui.MiniCalc import Ui_MiniCalc
from gui.TradeRuns import Ui_TradeRuns
from gui.TradeCard import Ui_TradeCard
from gui.PriceSheet import Ui_PriceSheet
from gui.InfoCard import Ui_Info
from gui.Settings import Ui_Settings
from gui.ShipHangar import Ui_ShipHangar
from gui.CompareTool import Ui_CompareTool
from gui.LocationSelector import Ui_LocationSelector
from lib.datasource import table,prices
from lib import apiclient
from models import trade, wallet, locations, ship,base

class Info(QMainWindow,Ui_Info):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
class Dashboard(QMainWindow,Ui_Dashboard):
    signalGotoTradeRuns = pyqtSignal()
    signalGotoMiniCalc = pyqtSignal()
    signalGotoPriceSheet = pyqtSignal()
    signalGotoShipHangar = pyqtSignal()
    signalGotoCompareTool = pyqtSignal()
    signalGotoSettings = pyqtSignal()

    signalShowInfo = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loadValues()
        self.setupEvents()
    
    def loadValues(self):
        self.balance = wallet.getBalance()
        self.lineEditBalance.setText(str(self.balance))
        self.loadTransactionHistory()
    
    def setupEvents(self):
        self.pushButtonGotoMiniCalc.clicked.connect(self.emitterGotoMiniCalc)
        self.pushButtonGotoTradeRuns.clicked.connect(self.emitterGotoTradeRuns)
        self.pushButtonGotoPriceSheet.clicked.connect(self.emitterGotoPriceSheet)
        self.pushButtonGotoShipHangar.clicked.connect(self.emitterGotoShipHangar)
        self.pushButtonCompareTool.clicked.connect(self.emitterGotoCompareTool)
        self.pushButtonSettings.clicked.connect(self.emitterGotoSettings)
        self.lineEditBalance.editingFinished.connect(self.balanceSave)
        self.pushButtonBalanceSave.clicked.connect(self.balanceSave)
        self.listViewTransactionHistory.doubleClicked.connect(self.emitterShowInfo)

    def show(self):
        super().show()
        self.loadValues()

    def loadTransactionHistory(self):
        self.ModelTransactionHistory = QStandardItemModel(self.listViewTransactionHistory)
        hist = wallet.getTransactionHistory()
        if hist:
            for trans in hist:
                item = QStandardItem()
                f = QFont()
                f.setBold(True)
                if trans.amount < 0:
                    item.setBackground(QColor("#e77c7c"))
                else:
                    item.setBackground(QColor("#89d17e"))

                item.setFont(f)
                item.setText(str(trans))
                self.ModelTransactionHistory.appendRow(item)
            self.listViewTransactionHistory.setModel(self.ModelTransactionHistory)
        else:
            self.ModelTransactionHistory = QStandardItemModel(self.listViewTransactionHistory)
            self.listViewTransactionHistory.setModel(self.ModelTransactionHistory)
    #Slots
    @pyqtSlot()
    def balanceSave(self):
        bal = self.lineEditBalance.text()
        if not (bal == str(self.balance)):
            wallet.setBalance(float(bal))
            self.balance = float(bal)
        self.loadTransactionHistory()
    #Emitters
    def emitterGotoMiniCalc(self):
        self.signalGotoMiniCalc.emit()
    def emitterGotoTradeRuns(self):
        self.signalGotoTradeRuns.emit()
    def emitterGotoPriceSheet(self):
        self.signalGotoPriceSheet.emit()
    def emitterGotoShipHangar(self):
        self.signalGotoShipHangar.emit()
    def emitterGotoCompareTool(self):
        self.signalGotoCompareTool.emit()
    def emitterGotoSettings(self):
        self.signalGotoSettings.emit()
    def emitterShowInfo(self):
        self.signalShowInfo.emit()

class Settings(QMainWindow,Ui_Settings):
    signalWindowClosing = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loadValues()
        self.setupEvents()
    
    def loadValues(self):
        pass

    def setupEvents(self):
        self.pushButtonClearDatabase.clicked.connect(self.clearDatabase)
        self.pushButtonUpdateCache.clicked.connect(apiclient.updateCache)

    def closeEvent(self,event):
        self.signalWindowClosing.emit()
        event.accept()

    def clearDatabase(self):
        pass

class ShipHangar(QMainWindow,Ui_ShipHangar):
    signalWindowClosing = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loadValues()
        self.setupEvents()

    def loadValues(self):
        self.manufacturers = list()
        self.models = list()
        self.variants = list()
        self.comboBoxMake.clear()
        self.comboBoxModel.clear()
        self.comboBoxVariant.clear()
        for manufacturer in ship.Ship.select(ship.Ship.manufacturer):
            if manufacturer.manufacturer not in self.manufacturers:
                self.manufacturers.append(manufacturer.manufacturer)
        self.comboBoxMake.addItems(self.manufacturers)


    def setupEvents(self):
        self.comboBoxMake.activated.connect(self.loadModels)
        self.comboBoxModel.activated.connect(self.loadVariants)

    def closeEvent(self,event):
        self.signalWindowClosing.emit()
        event.accept()

    def loadModels(self,index):
        self.comboBoxModel.clear()
        self.models = list()
        manufacturer = self.manufacturers[index]
        for model in ship.Ship.select(ship.Ship.model).where(ship.Ship.manufacturer == manufacturer):
            if model.model not in self.models:
                self.models.append(model.model)
        self.comboBoxModel.addItems(self.models)
    
    def loadVariants(self,index):
        self.comboBoxVariant.clear()
        model = self.models[index]
        manufacturer = self.manufacturers[self.comboBoxMake.currentIndex()]
        for variant in ship.Ship.select(ship.Ship.variant).where((ship.Ship.model == model) & (ship.Ship.manufacturer == manufacturer)):
            self.comboBoxVariant.addItem(variant.variant)

    @pyqtSlot()
    def addShip(self):
        pass

class CompareTool(QMainWindow,Ui_CompareTool):
    signalWindowClosing = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loadValues()
        self.setupEvents()

    def loadValues(self):
        pass
    
    def setupEvents(self):
        pass

    def closeEvent(self,event):
        self.signalWindowClosing.emit()
        event.accept()

class MiniCalc(QMainWindow,Ui_MiniCalc):
    signalWindowClosing = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loadValues()
        self.setupEvents()
    
    def loadValues(self):
        self.onTopStatus = False
        self.balance = wallet.getBalance()
        
        # lt = trade.getLastMiniCalcTrade()
        # if lt:
        #     self.lastTrade = lt
        # else:
        #     self.lastTrade = trade.miniCalcTrade()
        self.lineEditBalance.setText(str(self.balance))
        self.resetSlider()

    def resetSlider(self):
        self.tradeCount = trade.miniCalcTrade.select().count()

        if self.tradeCount == -1:
            self.tradeCount == 1
        self.verticalSliderRecent.setMaximum(self.tradeCount)
        self.verticalSliderRecent.setProperty('value',self.tradeCount)

    def setupEvents(self):
        #Need verification on edit
        self.pushButtonCalculate.clicked.connect(self.calculate)
        self.lineEditBalance.editingFinished.connect(self.balanceSave)
        self.pushButtonOntop.clicked.connect(self.setWindowOnTop)
        self.verticalSliderRecent.valueChanged[int].connect(self.restoreTrade)
        self.pushButtonClear.clicked.connect(self.clearTrades)
    
    def show(self):
        super().show()
        self.loadValues()

    def closeEvent(self,event):
        self.signalWindowClosing.emit()
        event.accept()
    
    def balanceSave(self):
        #Verification needed.
        bal = self.lineEditBalance.text()
        if not (bal == str(self.balance)):
            wallet.setBalance(float(bal))
            self.balance = float(bal)
    
    @pyqtSlot()
    def clearTrades(self):
        trade.miniCalcTrade.delete().where(trade.miniCalcTrade.id > 0)
        self.resetSlider()

    @pyqtSlot()
    def calculate(self,byButton=True):
        newTrade = trade.miniCalcTrade()
        newTrade.buyPrice = float(self.lineEditBuyPrice.text())
        newTrade.sellPrice = float(self.lineEditSellPrice.text())
        newTrade.cargo = int(self.lineEditCargo.text()) * 100 #1 SCU = 100 units
        newTrade.balance = self.balance

        if byButton:
            newTrade.save()

        #If player doesn't have enough money, return
        if (self.balance < newTrade.buyPrice):
            return

        self.labelCapital.setText(f"{round(newTrade.getCapital())} aUEC")
        self.labelReturn.setText(f"{round(newTrade.getUnitCount()*newTrade.sellPrice)} aUEC")
        self.labelProfit.setText(f"{round(newTrade.getProfit())} aUEC ({round((newTrade.getProfit() / newTrade.getReturn())*100)}%)")
        self.labelProfitCeiling.setText(f"{round(newTrade.getProfitCeiling())} aUEC")
        self.labelCeilingCapital.setText(f"{round(newTrade.cargo*newTrade.buyPrice)} aUEC")
        self.labelUnits.setText(f"{newTrade.getUnitCount()} unit(s) | {round(newTrade.getUnitCount() / 100)} SCU | {round((newTrade.getUnitCount()/newTrade.cargo)*100)}%")
        if byButton:
            self.resetSlider()


    @pyqtSlot()
    def setWindowOnTop(self):
        if not self.onTopStatus:
            self.pushButtonOntop.setText("Disable Always On-top")
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
            self.show()
            self.onTopStatus = True
        else:
            self.pushButtonOntop.setText("Enable Always On-top")
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint)
            self.show()
            self.onTopStatus = False
    
    def restoreTrade(self,val):
        currentTrade = trade.miniCalcTrade.select().where(trade.miniCalcTrade.id == val)[0]
        if currentTrade:
            self.lineEditBuyPrice.setText(str(currentTrade.buyPrice))
            self.lineEditSellPrice.setText(str(currentTrade.sellPrice))
            self.lineEditCargo.setText(str(round(currentTrade.cargo/100)))
            self.calculate(False)

class TradeCard(QDockWidget,Ui_TradeCard):
    def __init__(self,parent):
        super().__init__("Dockable",parent)
        self.setupUi(self)

class TradeRuns(QMainWindow,Ui_TradeRuns):
    signalWindowClosing = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loadValues()
        self.setupEvents()
    
    def loadValues(self):
        self.balance = wallet.getBalance()
        self.lineEditBalance.setText(str(self.balance))
        self.lineEditBalance.setClearButtonEnabled(False)
        self.tradecards = list()
        
        #Locations
        self.tradeports = ["None"]
        for tp in self.tradeports:
            self.comboBoxBuyLocation.addItem(str(tp))
            self.comboBoxSellLocation.addItem(str(tp))

    def setupEvents(self):
        self.lineEditBalance.editingFinished.connect(self.balanceSave)
        self.lineEditBalance.textEdited.connect(self.balanceOnEdit)
        self.pushButtonBalanceSave.clicked.connect(self.balanceSave)
        self.pushButtonFindRun.clicked.connect(self.showTradeCardTemp)

    def closeEvent(self,event):
        self.signalWindowClosing.emit()
        event.accept()

    def show(self):
        super().show()
        self.loadValues()

    def loadLocations(self):
        self.locations = list()
        self.comboBoxBuyLocation.clear()
        self.comboBoxSellLocation.clear()
        for loc in locations.Location.select():
            if str(loc) not in self.locations:
                self.locations.append(str(loc))
        self.comboBoxBuyLocation.addItems(self.locations)
        self.comboBoxSellLocation.addItems(self.locations)
    
    def loadCommodities(self):
        self.commodities = list()
        self.comboBoxBuyCommodity.clear()
        self.comboBoxSellCommodity.clear()

    def balanceOnEdit(self):
        bal = self.lineEditBalance.text()
        if bal == str(self.balance):
            self.lineEditBalance.setClearButtonEnabled(False)
        else:
            self.lineEditBalance.setClearButtonEnabled(True)

    def balanceSave(self):
        #Verification needed.
        bal = self.lineEditBalance.text()
        if not (bal == str(self.balance)):
            wallet.setBalance(float(bal))
            self.balance = float(bal)
            self.lineEditBalance.setClearButtonEnabled(False)
    
    def showTradeCardTemp(self):
        newCard = TradeCard(self)
        newCard.setAllowedAreas(Qt.BottomDockWidgetArea)
        self.addDockWidget(Qt.BottomDockWidgetArea,newCard)
        if len(self.tradecards) >= 1:
            lastTradecard = self.tradecards[len(self.tradecards) - 1]
            self.splitDockWidget(lastTradecard,newCard,Qt.Vertical)
        self.tradecards.append(newCard)

class PriceSheet(QMainWindow,Ui_PriceSheet):
    signalWindowClosing = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loadValues()
        self.setupEvents()

    def loadValues(self):
        self.pricedata = prices(table("data/prices.csv"))
        self.tableWidgetPrices.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)

        #Tradeport column header
        tradeports = self.pricedata.getTradeportList()
        self.tableWidgetPrices.setColumnCount(len(tradeports))

        count = 1
        for tradeport in tradeports:
            newItem = QTableWidgetItem(tradeport)
            if count % 2 == 0: #Sell
                c = QColor("#00cc00")
                newItem.setForeground(c) #TODO - Set background instead of foreground.
            else:
                c = QColor("#ff0000")
                newItem.setForeground(c)
            self.tableWidgetPrices.setHorizontalHeaderItem(count - 1,newItem)
            count += 1
        
        #Commodity row header
        commodities = self.pricedata.getCommodityList()
        self.tableWidgetPrices.setRowCount(len(commodities))
        count = 1
        for commodity in commodities:
            self.tableWidgetPrices.setVerticalHeaderItem(count - 1,QTableWidgetItem(commodity))
            count += 1
        
        #Data
        row_count = 0
        for row in self.pricedata.getRawPriceData():
            col_count = 0
            for col in row:
                self.tableWidgetPrices.setItem(row_count,col_count,QTableWidgetItem(col))
                col_count += 1
            row_count += 1

    def setupEvents(self):
        pass
    def closeEvent(self,event):
        self.signalWindowClosing.emit()
        event.accept()

    def contextMenuEvent(self,event):
        menu = QMenu()
        showInfo = menu.addAction("Show Info")
        action = menu.exec_(self.tableWidgetPrices.mapToGlobal(event.pos()))

class WindowController():
    def __init__(self):
        self.dashboardW = Dashboard()
        self.MiniCalcW = MiniCalc()
        self.TradeRunsW = TradeRuns()
        self.PriceSheetW = PriceSheet()
        self.ShipHangarW = ShipHangar()
        self.CompareToolW = CompareTool()
        self.SettingsW = Settings()
        self.infoW = Info()
        self.setupEvents()
        self.dashboardW.show()
    
    def setupEvents(self):
        #Open sub-windows
        self.dashboardW.signalGotoMiniCalc.connect(self.gotoMiniCalc)
        self.dashboardW.signalGotoTradeRuns.connect(self.gotoTradeRuns)
        self.dashboardW.signalGotoPriceSheet.connect(self.gotoPriceSheet)
        self.dashboardW.signalGotoShipHangar.connect(self.gotoShipHangar)
        self.dashboardW.signalGotoCompareTool.connect(self.gotoCompareTool)
        self.dashboardW.signalGotoSettings.connect(self.gotoSettings)

        self.dashboardW.signalShowInfo.connect(self.showInfo)

        #Back to dash
        self.MiniCalcW.signalWindowClosing.connect(self.backToDash)
        self.TradeRunsW.signalWindowClosing.connect(self.backToDash)
        self.PriceSheetW.signalWindowClosing.connect(self.backToDash)
        self.ShipHangarW.signalWindowClosing.connect(self.backToDash)
        self.CompareToolW.signalWindowClosing.connect(self.backToDash)
        self.SettingsW.signalWindowClosing.connect(self.backToDash)

    def gotoMiniCalc(self):
        self.dashboardW.close()
        self.MiniCalcW.show()
    def gotoTradeRuns(self):
        self.dashboardW.close()
        self.TradeRunsW.show()
    def gotoPriceSheet(self):
        self.dashboardW.close()
        self.PriceSheetW.show()
    def gotoShipHangar(self):
        self.dashboardW.close()
        self.ShipHangarW.show()
    def gotoCompareTool(self):
        self.dashboardW.close()
        self.CompareToolW.show()
    def gotoSettings(self):
        self.dashboardW.close()
        self.SettingsW.show()
    def showInfo(self):
        self.infoW.show()
    def backToDash(self):
        self.dashboardW.show()

app = QApplication(sys.argv)
w = WindowController()
sys.exit(app.exec_())
base.close()