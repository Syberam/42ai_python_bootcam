#!/usr/bin/env python
from FileLoader import FileLoader


def proportionBySport(data, year, sport, gender):
    y = data[data['Year'] == year]
    g = y[y['Sex'] == gender]
    g_by_s = g[g['Sport'] == sport]
    nb_g = len(g.drop_duplicates(subset=['Name']).index)
    nb_g_by_s = len(g_by_s.drop_duplicates(subset=['Name']).index)
    return nb_g_by_s / nb_g



if __name__ == '__main__':
    loader = FileLoader()
    data = loader.load("../resources/athlete_events.csv")
    # loader.display(data, 20)
    print(proportionBySport(data, 2004, 'Tennis', 'F'))
