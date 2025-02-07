"""
Returns the name of either city_a or city_b, whichever is closest to coordinate (lat, lon).
If the two cities are the same distance away from the coordinate, consider city_b to be the closer city.
"""

from city import City, make_city, get_name, get_latitude, get_longitude
from distance import distance

def closer_city(latitude: float, longitude: float, city_a: City, city_b: City) -> str:
    target = make_city('target', latitude, longitude)
    a_distance = distance(target, city_a)
    b_distance = distance(target, city_b)
    return get_name(city_b) if b_distance <= a_distance else get_name(city_a) 

# Test cases
if __name__ == '__main__':
	try:
	    berkeley = make_city('Berkeley', 37.87, 112.26)
	    stanford = make_city('Stanford', 34.05, 118.25)
	    result, expectation = closer_city(38.33, 121.44, berkeley, stanford), 'Stanford'
	    assert result == expectation, f'Expected {expectation} but got {result}'
	
	    bucharest = make_city('Bucharest', 44.43, 26.10)
	    vienna = make_city('Vienna', 48.20, 16.37)
	    result, expectation = closer_city(41.29, 174.78, bucharest, vienna), 'Bucharest'
	    assert result == expectation, f'Expected {expectation} but got {result}'
	
	    print('All test cases passed!')
	except AssertionError as error:
	    print('A test case failed.')
	    print(error)
