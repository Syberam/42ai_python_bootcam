#!/usr/bin/env python
from FileLoader import FileLoader


def youngestFellah(data, year):
    y = data[data['Year'] == year]
    return {
        'F': y[y['Sex'] == 'F']['Age'].min(),
        'M': y[y['Sex'] == 'M']['Age'].min()
    }


if __name__ == '__main__':
    loader = FileLoader()
    data = loader.load("../resources/athlete_events.csv")
    # loader.display(data, 20)
    for year in range(1970, 2019):
        print("{}: {}".format(year, youngestFellah(data, year)))
