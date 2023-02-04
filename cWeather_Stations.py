class Weather_Station:
    # class for storing all data for weather stations
    # https://docs.python.org/3/tutorial/classes.html

    def __init__(self, id, code, street, location, coordinates, lastUpdate) -> None:
        self.id = id
        self.code = code 
        self.street = street
        self.location = location
        self.coordinates = coordinates
        self.lastUpdate = lastUpdate
