#!/usr/bin/env python
import pandas as pd


class FileLoader:
    def load(self, path):
        pf = pd.read_csv(path)
        print("Loading dataset of dimensions {} x {}".format(*pf.shape))
        return pf

    def display(self, df, n):
        print(df.head(n))


if __name__ == '__main__':
    loader = FileLoader()
    data = loader.load("../resources/athlete_events.csv")
    print(type(data))
    loader.display(data, 12)
