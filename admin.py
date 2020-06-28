import sys, functools
from PyQt5.QtWidgets import QApplication, QMainWindow, QAbstractScrollArea, QWidget, QMessageBox
from PyQt5.QtCore import pyqtSlot, Qt, pyqtSignal
from PyQt5.Qt import QStandardItemModel, QStandardItem, QColor, QFont, QTableWidgetItem, QTableWidget, QVBoxLayout, QStyleFactory, QMenu, QDockWidget, QRegExpValidator, QRegExp, QPushButton

from peewee import *
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

from gui.Admin import Ui_Admin

class SubItemWindow(QMainWindow):
    def __init__(self,parent):
        self.parent = parent
        super().__init__(parent)
        self.setupUi()
    
    def setupUi(self):
        self.setObjectName("Subitem")
        self.resize(500,500)

        self.tableSubItems = QTableWidget()
        self.tableSubItems.horizontalHeader().setStretchLastSection(True)
        self.setCentralWidget(self.tableSubItems)        
        

class AdminWindow(QMainWindow,Ui_Admin):
    LIST_COMMODITIES_QUERY = gql('''query listcommodities {
        commodities {
            id,
            name,
            description
            }
        }''')

    LIST_LOCATIONS_QUERY = gql('''query listLocations {
        locations {
            id
            name
            moon
            #station
            planet
            system
            prices {
            id
                commodity {
                    id
                    name
                    description
                }
            buy
            sell
            }
            description
        }
    }''')

    LIST_SHIPS_QUERY = gql('''query listShips {
        ships {
            id
            manufacturer
            model
            variant
            buy
            description
        }
    }''')

    def __init__(self):
        super().__init__()
    
        self.setupUi(self)
        self.show()
        try:
            transport = RequestsHTTPTransport(url="http://localhost:8000/graphql/",verify=False,retries=3)
            self.gqlClient = Client(transport=transport,fetch_schema_from_transport=True)
        except Exception as e:
            m = QMessageBox()
            m.setText(f"Failed to connect to API. Reason: {e}")
            m.show()
            exit(1)
            
        self.setupValidators()
        self.loadValues()
        self.setupEvents()
        
    def loadValues(self):
        self.listCommodities()
        self.subitemWindows = list()
    def setupValidators(self):
        basicText = QRegExp("[a-z-A-Z-0-9 _]+")
        self.lineEditCommoditiesName.setValidator(QRegExpValidator(basicText))
        self.lineEditCommoditiesDescription.setValidator(QRegExpValidator(basicText))
        self.lineEditLocationsName.setValidator(QRegExpValidator(basicText))
        self.lineEditLocationsStation.setValidator(QRegExpValidator(basicText))
        self.lineEditLocationsMoon.setValidator(QRegExpValidator(basicText))
        self.lineEditLocationsPlanet.setValidator(QRegExpValidator(basicText))
        self.lineEditLocationsSystem.setValidator(QRegExpValidator(basicText))
        self.lineEditLocationsDescription.setValidator(QRegExpValidator(basicText))
        self.lineEditShipsManufacturer.setValidator(QRegExpValidator(basicText))
        self.lineEditShipsModel.setValidator(QRegExpValidator(basicText))
        self.lineEditShipsVariant.setValidator(QRegExpValidator(basicText))
        self.lineEditShipsDescription.setValidator(QRegExpValidator(basicText))
    def setupEvents(self):
        self.tabWidgetItemType.currentChanged.connect(self.changeTabs)

        self.pushButtonCommoditiesAdd.clicked.connect(self.addCommodity)
        self.pushButtonLocationsAdd.clicked.connect(self.addLocation)
        self.pushButtonShipsAdd.clicked.connect(self.addShip)
    def changeTabs(self):
        index = self.tabWidgetItemType.currentIndex()
        switch={
            0:self.listCommodities,
            1:self.listLocations,
            2:self.listShips
        }
        switch.get(index,self.listCommodities)()

    def listCommodities(self):        
        gqlresult = self.gqlClient.execute(self.LIST_COMMODITIES_QUERY)
        self.setupTable()
        self.updateTable(gqlresult["commodities"])
    def listLocations(self):
        gqlresult = self.gqlClient.execute(self.LIST_LOCATIONS_QUERY)
        self.setupTable()
        self.updateTable(gqlresult["locations"])
    def listShips(self):
        gqlresult = self.gqlClient.execute(self.LIST_SHIPS_QUERY)
        self.setupTable()
        self.updateTable(gqlresult["ships"])

    #Table 
    def setupTable(self):
        self.tableWidgetCurrent.setRowCount(0)
        self.tableWidgetCurrent.setColumnCount(0)
        self.tableWidgetCurrent.clear()
        self.subitemsList = list()
    def updateTable(self,data,col_count=-1,row_count=-1,subitem=0):
        """Recursively add data to table from gql result

        Args:
            data (dict or list): Iterable data to add to table
            col_count (int, optional): Current column count. Defaults to 0.
        """


        if type(data) is list:
            for item in data:
                if (type(item) is dict) or (type(item) is list):
                    row_count += 1
                    self.tableWidgetCurrent.setRowCount(row_count + 1)
                    self.updateTable(item,col_count=col_count,row_count=row_count)
                else:
                    raise ValueError(f"Cannot have type \"{type(item)}\" directly under a list") 
        elif type(data) is dict:
            for key,value in data.items():
                if type(value) is dict:
                    subitem += 1
                    self.updateTable(value,col_count=col_count,subitem=subitem)
                elif type(value) is list:
                    self.subitemsList.append(value)
                    col_count += 1
                    if self.tableWidgetCurrent.columnCount() < (col_count + 1):
                        self.tableWidgetCurrent.setColumnCount(col_count + 1)
                    headerItem = QTableWidgetItem()
                    headerItem.setText(str(key))
                    headerItem.setBackground(QColor("#d6aef5"))
                    self.tableWidgetCurrent.setHorizontalHeaderItem(col_count,headerItem)
                    if not value == []:
                        gotoButton = QPushButton()
                        gotoButton.setText("Sub-items")
                        gotoButton.clicked.connect(functools.partial(self.showSubList,{"row":row_count + 1,"title":f"Showing {key} for row {row_count + 1}"}))
                        self.tableWidgetCurrent.setCellWidget(row_count,col_count,gotoButton)
                    else:
                        self.tableWidgetCurrent.setItem(row_count,col_count,QTableWidgetItem(f"No {key}"))
                else:
                    col_count += 1
                    if self.tableWidgetCurrent.columnCount() < (col_count + 1):
                        self.tableWidgetCurrent.setColumnCount(col_count + 1)
                    headerItem = QTableWidgetItem()
                    headerItem.setText(str(key))
                    if subitem > 0:
                        switch = {
                            0:"#d6aef5",
                            1:"#52adf2",
                            2:"#71d993",
                            3:"#eda96d"
                        }
                        colorCode = switch.get(subitem,"#bdbdbd")
                        headerItem.setBackground(QColor(colorCode))
                    self.tableWidgetCurrent.setHorizontalHeaderItem(col_count,headerItem)
                    self.tableWidgetCurrent.setItem(row_count,col_count,QTableWidgetItem(str(value)))
        else:
            raise ValueError(f"Cannot recurse on type \"{type(item)}\"") 
    @pyqtSlot()
    def showSubList(self,data):
        newSubitemWindow = SubItemWindow(self)
        title = data.get("title","Showing subitems")
        newSubitemWindow.setWindowTitle(title)
        row = data.get("row",-1)
        if row == -1:
            raise RuntimeError("Failed to get row for sub items")
        itemList = self.subitemsList[row - 1]
        newSubitemWindow.show()
        row_count = -1
        for item in itemList:
            col_count = -1
            newSubitemWindow.tableSubItems.setRowCount(row_count+1)
            for key, value in item.items():
                if type(value) == dict:
                    for l2_key,l2_value in value.items():
                        col_count += 1
                        if newSubitemWindow.tableSubItems.columnCount() < (col_count + 1):
                            newSubitemWindow.tableSubItems.setColumnCount(col_count + 1)
                        headeritem = QTableWidgetItem()
                        headeritem.setText(f"{key}_{l2_key}")
                        f = QFont()
                        f.setBold(True)
                        headeritem.setBackground(QColor("#71d993"))
                        headeritem.setFont(f)
                        newSubitemWindow.tableSubItems.setHorizontalHeaderItem(col_count,headeritem)
                        newSubitemWindow.tableSubItems.setItem(row_count,col_count,QTableWidgetItem(str(l2_value)))        
                else:
                    col_count += 1
                    if newSubitemWindow.tableSubItems.columnCount() < (col_count + 1):
                        newSubitemWindow.tableSubItems.setColumnCount(col_count + 1)
                    newSubitemWindow.tableSubItems.setHorizontalHeaderItem(col_count,QTableWidgetItem(key))
                    newSubitemWindow.tableSubItems.setItem(row_count,col_count,QTableWidgetItem(str(value)))
            row_count += 1
   
    def addCommodity(self):
        name = self.lineEditCommoditiesName.text()
        buy = self.doubleSpinBoxCommoditiesBuy.value()
        sell = self.doubleSpinBoxCommoditiesSell.value()
        description = self.lineEditCommoditiesDescription.text()
        mutation = gql(f'''mutation addCommodity {{
            addCommodity(input: {{
                name: "{name}",
                description: "{description}"
            }}) {{
                ok
            }}
        }}
        ''')
        try:
            self.gqlClient.execute(mutation)
        except Exception as e:
            self.statusbar.showMessage(f"Failed to add commodity. {e}")
        else:
            self.statusbar.showMessage("Successfully added commodity.")
            self.listCommodities()
    def addLocation(self):
        name = self.lineEditLocationsName.text()
        station = self.lineEditLocationsStation.text()
        moon = self.lineEditLocationsMoon.text()
        planet = self.lineEditLocationsPlanet.text()
        system = self.lineEditLocationsSystem.text()
        description = self.lineEditLocationsDescription.text()

        mutation = gql(f'''mutation addLocation {{
            addLocation(input:{{
                name: "{name}",
                station: "{station}",
                moon: "{moon}",
                planet: "{planet}",
                system: "{system}",
                description: "{description}"
            }}) {{
                ok
            }}
        }}''')
        try:
            self.gqlClient.execute(mutation)
        except Exception as e:
            self.statusbar.showMessage(f"Failed to add location. {e}")
        else:
            self.statusbar.showMessage("Successfully added location.")
            self.listLocations()
    def addShip(self):
        manufacturer = self.lineEditShipsManufacturer.text()
        model = self.lineEditShipsModel.text()
        variant = self.lineEditShipsVariant.text()
        buy = self.doubleSpinBoxShipsBuy.value()
        description = self.lineEditShipsDescription.text()

        mutation = gql(f'''mutation addShip {{
            addShip(input:{{
                manufacturer: "{manufacturer}",
                model: "{model}",
                variant: "{variant}",
                buy: {buy},
                description: "{description}"
            }}) {{
                ok
            }}
        }}''')

        try:
            self.gqlClient.execute(mutation)
        except Exception as e:
            self.statusbar.showMessage(f"Failed to add ship. {e}")
        else:
            self.statusbar.showMessage("Successfully added ship.")
            self.listShips()

app = QApplication(sys.argv)
app.setStyle(QStyleFactory.create("Fusion"))
w = AdminWindow()
sys.exit(app.exec_())