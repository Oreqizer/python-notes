# Records:
# besides Tuples being Immutable lists, they serve as anonymous records.
# you can also have named tuples, more on that later

lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '12345678'), ('BRA', 'CE765432'), ('ESP', 'LE1823746')]


def sorting():
    for passport in sorted(traveler_ids):
        print('%s - %s' % passport)


def choice():
    for country, _ in traveler_ids:
        print(country)


if __name__ == '__main__':
    print('> sorting')
    sorting()
    print('> choice')
    choice()
