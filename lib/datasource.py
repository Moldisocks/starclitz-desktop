import csv

class table():
    def __init__(self,path:str):
        with open(path,'r') as f:
            reader = csv.reader(f,delimiter=",")
            self.data = list()
            for row in reader:
                self.data.append(row)

    def findInRow(self,row_index:int,search:str):
        index = 0
        for column in self.data[row_index]:
            if column == search:
                return index
            index += 1
        return -1

    def findInColumn(self,col_index:int,search:str):
        index = 0
        for row in self.data:
            if row[col_index] == search:
                return index
            index += 1
        return -1
    
    def getRow(self,row_index:int):
        return self.data[row_index] 
        
    def getColumn(self,col_index:int):
        col_list = list()
        for row in self.data:
            col_list.append(row[col_index])
        if len(col_list) > 0:
            return col_list
        else:
            return []
    
    def get(self,row_index:int,col_index:int):
        index = 0
        for row in self.data:
            if index == row_index:
                return row[col_index]
            index += 1
        return -1   

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= len(self.data):
            row = self.data[self.n]
            self.n += 1
            return row
    
    def __len__(self):
        return len(self.data)

class prices():
    
    class tradeType:
        buy = True
        sell = False

    def __init__(self,data:table):
        self.pricetable = data

    def getPrice(self,direction:tradeType,commodity:str,tradeport:str):
        tp_index = -1
        com_index = -1
        price = -1

        tp_index = self.pricetable.findInRow(3,tradeport)
        if tp_index == -1:
            return -1.0

        com_index = self.pricetable.findInColumn(0,commodity)
        if com_index == -1:
            return -1.0

        if direction == prices.tradeType.buy:
            price = self.pricetable.get(com_index,tp_index)
        else:
            price = self.pricetable.get(com_index,tp_index + 1)
        if price == '':
            return -1.0
        else:
            return float(price)

    def getPrices(self,direction:tradeType,commodity="",tradeport="",useDict = False):
        sel_index = -1
        items = list()

        if commodity != "":
            sel_index = self.pricetable.findInColumn(0,commodity)
        elif tradeport != "":
            sel_index = self.pricetable.findInRow(3,tradeport)
        
        if sel_index == -1:
            return []
        
        if commodity != "":
            count = 1
            for col in self.pricetable.getRow(sel_index)[1:]:
                if direction == prices.tradeType.buy:
                    if count % 2 != 0:
                        if col != '':
                            items.append(col)
                else:
                    if count % 2 == 0:
                        if col != '':
                            items.append(col)
                count += 1
            return items #Strip off commodity name

        elif tradeport != "":
            for row in self.pricetable:
                if direction == prices.tradeType.sell:
                    sel_index += 1
                else:
                    if row[sel_index] != '':
                        items.append(row[sel_index])
            return items[5:] #Strip off header data

    def getTradeportsByCommodity(self,direction:tradeType,commodity:str, bothDirections = False):
        count = 0
        tradeports = list()
        row = self.pricetable.findInColumn(0,commodity)
        if row == -1:
            return []
        for col in self.pricetable.getRow(row):
            add = False
            if direction == prices.tradeType.buy:
                if count % 2 != 0:
                    add = True
            else:
                if count % 2 == 0:
                    add = True
            if add:
                try:
                    price = float(col)
                except ValueError:
                    count += 1
                    continue
                else:
                    tradeport = self.pricetable.get(4,count)
                    if tradeport != '':
                        tradeports.append(tradeport)
            count += 1
        tp_return = list()
        for tp in tradeports:
            tp_return.append(self.getPath(tp))

        return tp_return

    def getCommoditiesByTradeport(self,direction:tradeType,tradeport:str,bothDirections = False):
        count = 0
        commodities = list()
        
        tp_index = self.pricetable.findInRow(3,tradeport)
        if tp_index == -1:
            return []
        
        if direction == prices.tradeType.sell:
            if not bothDirections:
                tp_index += 1 #Adjust to sell price column

            for item in self.pricetable.getColumn(tp_index):
                if item == '':
                    count += 1
                    continue
                
                try:
                    price = float(item)
                except ValueError:
                    count += 1
                    continue
                else:
                    commodity = self.pricetable.get(count,0)
                    if commodity != '':
                        if bothDirections:
                            commodities.append({"buy":commodity})
                        else:
                            commodities.append(commodity)
                count += 1
            
            count = 0
            if bothDirections:
                for item in self.pricetable.getColumn(tp_index+1):
                    if item == '':
                        count += 1
                        continue
                    try:
                        price = float(item)
                    except ValueError:
                        count += 1
                        continue
                    else:
                        commodity = self.pricetable.get(count,0)
                        if commodity != '':
                            try:
                                commodities[count]["sell"] = commodity
                            except IndexError:
                                commodities.append({"sell":commodity})
                    count += 1

        return commodities

    def findBestTradeport(self,direction:tradeType,commodity:str):
        count = 0
        best_index = 0
        best = -1.0
        row = self.pricetable.findInColumn(0,commodity)
        if row == -1:
            return ''
        for col in self.pricetable.getRow(row):
            if direction == prices.tradeType.buy:
                if count % 2 != 0:
                    try:
                        price = float(col)
                    except ValueError:
                        count += 1
                        continue
                    else:
                        if (best == -1.0) or (price < best):
                            best = price
                            best_index = count
            else:
                if count % 2 == 0:
                    
                    try:
                        price = float(col)
                    except ValueError:
                        count += 1
                        continue
                    else:
                        if price > best:
                            best = price
                            best_index = count
            count += 1
        
        return (self.pricetable.getRow(3)[best_index],best)

    def getPath(self,tradeport:str):
        tp_index = self.pricetable.findInRow(3,tradeport)
        if tp_index == -1:
            return "/Unknown"
        
        bodies = list()
        for row in range(0,4):
            body = self.pricetable.get(row,tp_index)
            if body != -1:
                try:
                    bodies.index(body)
                except ValueError:
                    bodies.append(body)
                else:
                    continue
        buildStr = str()
        for body in bodies:
            buildStr += f"/{body}"
        return buildStr

    def getTradeportList(self):
        return self.pricetable.getRow(3)[1:]
    
    def getCommodityList(self):
        return self.pricetable.getColumn(0)[5:]
    
    def getRawPriceData(self):
        rows = list()
        for i in range(5,len(self.pricetable) -1):
            rows.append(self.pricetable.getRow(i)[1:])
        return rows
