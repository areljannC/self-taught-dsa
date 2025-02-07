"""
Implement the function distance, which computes the distance between two city objects.
Recall that the distance between two coordinate pairs (x1, y1) and (x2, y2) can be found by calculating the sqrt of (x1 - x2)**2 + (y1 - y2)**2. We have already imported sqrt for your convenience.
"""

from math import sqrt
from city import City, make_city, get_name, get_latitude, get_longitude

def distance(city_a: City, city_b: City) -> float:
    latitude_a, latitude_b = get_latitude(city_a), get_latitude(city_b)
    longitude_a, longitude_b = get_longitude(city_a), get_longitude(city_b)
    latitude_distance = (latitude_a - latitude_b) ** 2
    longitude_distance = (longitude_a - longitude_b) ** 2
    return sqrt(latitude_distance + longitude_distance)

# Test cases
if __name__ == '__main__':
    try:
        city_a = make_city('city_a', 0, 1)
        city_b = make_city('city_b', 0, 2)
        result, expectation = distance(city_a, city_b), 1.0
        assert result == expectation, f'Expected {expectation} but got {result}'

        city_c = make_city('city_c', 6.5, 12)
        city_d = make_city('city_d', 2.5, 15)
        result, expectation = distance(city_c, city_d), 5.0
        assert result == expectation, f'Expected {expectation} but got {result}'

        print('All test cases passed!')
    except AssertionError as error:
        print('A test case failed.')
        print(error)
