from gql import gql,Client
from gql.transport.requests import RequestsHTTPTransport
from models import ship

def getCommodities():
    pass

def getLocations():
    pass

def getShips():
    transport = RequestsHTTPTransport("http://localhost:8000/graphql/",verify=False)
    gqlclient = Client(transport=transport,fetch_schema_from_transport=True)
    query = gql('''query listShips{
        ships {
            manufacturer
            model
            variant
            buy
            description
        }
    }''')

    try:
        result = gqlclient.execute(query)
    except Exception as e:
        print(f"Failed to get ships. Reason: {e}")
    else:
        return result

def updateCache():
    """Updates local cache

    """
    print("Updating local cache")
    ships = getShips()
    for shipData in ships["ships"]:
        manufacturer = shipData.get("manufacturer")
        model = shipData.get("model")
        variant = shipData.get("variant")
        buy = shipData.get("buy")
        description = shipData.get("description")

        if variant is None:
            variant = "Base"
        try:
            newShip = ship.Ship.create(manufacturer=manufacturer,model=model,variant=variant)
            if buy is not None:
                newShip.buy = buy
            if description is not None:
                newShip.description = description
            newShip.save()
        except Exception as e:
            print(f"Exception encountered when saving ship. Details: {e}")
            continue
    print("Finished updating local cache")