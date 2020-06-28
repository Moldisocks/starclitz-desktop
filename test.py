from models.commodity import Commodity
from models.locations import Location
from models.ship import Ship
from lib.datasource import prices,table
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

transport = RequestsHTTPTransport("http://localhost:8000/graphql/",verify=False)
gqlclient = Client(transport=transport,fetch_schema_from_transport=True)

def addLocations():
    
    
    p = prices(table("data/prices.csv"))
    locations = p.getTradeportList()
    locationListStr = "["
    for loc in locations:

        loc_arr = p.getPath(loc).split("/")
        if loc_arr[0] == "":
            loc_arr = loc_arr[1:]
        validFields = dict()
        if len(loc_arr) == 3:
            if loc_arr[0] != "":
                validFields["system"] = loc_arr[0]
            if loc_arr[1] != "":
                validFields["planet"] = loc_arr[1]
            if loc_arr[2] != "":
                validFields["name"] = loc_arr[2]
        elif len(loc_arr) == 4:
            if loc_arr[0] != "":
                validFields["system"] = loc_arr[0]
            if loc_arr[1] != "":
                validFields["planet"] = loc_arr[1]
            if loc_arr[2] != "":
                validFields["moon"] = loc_arr[2]
            if loc_arr[3] != "":
                validFields["name"] = loc_arr[3]
        else:
            continue
        
        fieldStr = "{"
        for key,value in validFields.items():
            fieldStr += f'{key}:"{value}",\n'
        fieldStr = fieldStr[:-2] + "}"
        
        locationListStr += fieldStr + ","

    locationListStr = locationListStr[:-1] + "]"
    mutation = gql(f"mutation addLocations {{ addLocations(input:{locationListStr}){{ok\nmessage}}}}")
    try:
        result = gqlclient.execute(mutation)
    except Exception as e:
        print(f"Error {e}")
    else:
        try:
            result = result["addLocations"]
        except KeyError as e:
            print(f"Failed to get resultant payload. {e} {result}")
        else:
            success = result.get("ok",False)
            message = result.get("message","null message")
            print(f"Success:{success} Message: {message}")

def addCommodities():
    #Get price data
    p = prices(table('data/prices.csv'))
    commodities = p.getCommodityList()

    commodityStr = "["
    for commodity in commodities:
        commodityStr += f'{{name:"{commodity}"}},'
    commodityStr = commodityStr[:-1] + "]"
    commodityIDs = list()

    try:
        commodityCommit = gql(f'mutation addCommodities {{ addCommodities(input:{commodityStr}){{ok\nmessage\nids}}}}')
        result = gqlclient.execute(commodityCommit)
    except Exception as e:
        print(f"Error {e}")
    else:
        try:
            result = result["addCommodities"]
        except KeyError as e:
            print(f"Failed to get resultant payload. {e} {result}")
        else:
            success = result.get("ok",False)
            message = result.get("message","null message")
            print(f"Success:{success} Message: {message}")
            if success:
                commodityIDs = result.get("ids")

def addPrices():
    """Creates price data and links to location

    """
    p = prices(table('data/prices.csv'))
    #Setup gql client

    locquery = gql(f'''query listLocations {{
        locations {{id
        name
        }}
    }}''')

    comquery = gql(f'''query listCommodities {{
        commodities {{
            id
            name
        }}
    }}
    ''')

    
    #Read location data
    try:
        locationResult = gqlclient.execute(locquery)
        comResult = gqlclient.execute(comquery)
    except Exception as e:
        print(f"Failed to retrive location data. Reason: {e}")
    else:
        def getComId(name:str):
            for com in comResult["commodities"]:
                com_id = int(com.get("id"))
                com_name = com.get("name")
                if com_name == name:
                    return com_id
            return None

        def addPrice(com_id,buy=None,sell=None):
            priceStr = str()
            if buy:
                priceStr += f"buy: {buy},"
            if sell:
                priceStr += f"sell: {sell},"
            priceStr = priceStr[:-1]
            queryStr = f'''mutation addPrice {{
                addPrice(input:{{
                    commodity: {{
                        id:{com_id}
                    }},
                    {priceStr}
                }}) {{
                    ok
                    id
                    message
                }}
            }}'''
            mutation = gql(queryStr)

            result = gqlclient.execute(mutation)
            if result["addPrice"].get("ok"):
                return result["addPrice"].get("id")
            else:
                return None

        for loc in locationResult["locations"]:
            loc_id = int(loc.get("id"))
            loc_name = loc.get("name")
            price_ids = []

            for com in p.getCommoditiesByTradeport(False,loc_name,bothDirections=True):
                try:
                    buy = p.getPrice(prices.tradeType.buy,com["buy"],loc_name)
                except KeyError:
                    buy = -1
                try:
                    sell = p.getPrice(prices.tradeType.sell,com["sell"],loc_name)
                except KeyError:
                    sell = -1
        
                if buy < 0:
                    buy = None
                else:
                    com = com["buy"]
                if sell < 0:
                    sell = None
                else:
                    com = com["sell"]

                com_id  = getComId(com)
                price_id = None
                if com_id:
                    price_id = addPrice(com_id,buy,sell)
                    price_ids.append(price_id)
            
            if price_ids == []:
                print(f"Location: {loc_name} doesn't have any prices")
                continue

            locPriceStr = "["
            for id in price_ids:
                locPriceStr += f"{{id:{id}}},"
            locPriceStr = locPriceStr[:-1] + "]"

            locUpdateMuation = gql(f'''mutation updateLocation {{
            updateLocation(input:{{
                id: {loc_id},
                prices: {locPriceStr}
            }}) {{
                    ok
                    message
                }}
            }}           
            ''')

            try:
                loc_result = gqlclient.execute(locUpdateMuation)
            except Exception as e:
                print(f"Failed to update location. Reason: {e}")

if __name__ == "__main__":
    addLocations()
    addCommodities()
    addPrices()