class City:
    def __init__(self, name: str, latitude: float, longitude: float):
        self._name = name
        self._latitude = latitude 
        self._longitude = longitude

    @property
    def name(self):
        return self._name

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

def make_city(name: str, latitude: float, longitde: float) -> City:
    return City(name, latitude, longitude)

def get_name(city: City) -> str:
    return city.name

def get_latitude(city: City) -> float:
    return city.latitude

def get_longitude(city: City) -> float:
    return city.longitude
