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

def make_city(name: str, latitude: float, longitude: float) -> City:
    return City(name, latitude, longitude)

def get_name(city: City) -> str:
    return city.name

def get_latitude(city: City) -> float:
    return city.latitude

def get_longitude(city: City) -> float:
    return city.longitude

# Test cases
if __name__ == '__main__':
    try:
        name, latitude, longitude = 'Berkeley', 11.11, 22.22
        city = make_city(name, latitude, longitude)
        assert get_name(city) == name, f'Expected {name} but got {get_name(city)}'
        assert get_latitude(city) == latitude, f'Expected {latitude} but got {get_name(latitude)}'
        assert get_longitude(city) == longitude, f'Expected {longitude} but got {get_name(longitude)}'

        print('All test cases passed!')
    except AssertionError as error:
        print('A test case failed.')
        print(error)
