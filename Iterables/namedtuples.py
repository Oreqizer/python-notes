# Named tuples:
# handy when creating records,
# or simple objects to store data in
# that don't need methods

from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
LatLng = namedtuple('LatLng', 'lat long')


# instances of classes built with 'namedtuples' take
# as much memory, as regular tuples, because field names
# are stored in the class, not the instance
#
# they use less memory than regular objects, because
# they don't store values in per-instance __dict__
def instantiation():
    tokyo = City('Tokyo', 'JP', '36.933', (35.6, 139.7))
    print(tokyo)
    print(tokyo.country)  # dot notation allowed
    print(tokyo[1])  # also this one


def under_the_hood():
    print(City._fields)
    delhi_data = ('Delhi NCR', 'IN', '21.9', LatLng(' 28.6', '77.2'))

    # tuples: take a single iterable
    # namedtuples: take positional arguments - City(name, country, population, coordinates)
    delhi = City._make(delhi_data)  # same as City(*delhi_data), City._make takes an iterable

    print(delhi._asdict())  # don't do this in real life
    for key, value in delhi._asdict().items():
        print('{}: {}'.format(key, value))


if __name__ == '__main__':
    print('> instantiation')
    instantiation()
    print('> under_the_hood')
    under_the_hood()
