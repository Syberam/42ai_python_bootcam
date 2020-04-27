#!/usr/bin/env python


class CsvReader():
    def __init__(
            self, filename, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

    def __enter__(self):
        try:
            self.file = open(self.filename)
            self.lines = [line.replace('\n', '') for line in list(self.file)]
            lines = self.lines
            self.cols = len(lines[self.skip_top].split(self.sep))
            self.nb_lines = len(lines)
            l_bound = self.skip_top
            l_bound += 0 if self.header else 1  # del l20 if data must hve head
            r_bound = self.nb_lines - self.skip_bottom
            head = self.lines[0] if self.header else self.lines[self.skip_top]
            self.header_values = [
                data.strip() for data in head.split(self.sep)]

            self.data = list()
            for line in lines[l_bound:r_bound]:
                line_values = list(filter(None, line.split(self.sep)))
                if len(line_values) != self.cols:
                    return None
                self.data.append([data.strip() for data in line_values])
        except Exception:
            return None
        return self

    def __exit__(self, type, value, traceback):
        if self.file:
            self.file.close()

    def getdata(self):
        return self.data

    def getheader(self):
        return self.header_values


if __name__ == "__main__":
    with CsvReader('../resources/good.csv') as file:
        print("_____DATA_____")

        for data in file.getdata():
            print(data)
        header = file.getheader()
        print("____HEADER____")
        print(header)

    with CsvReader(
            '../resources/good.csv',
            header=True, skip_top=1, skip_bottom=3) as file:
        print("_____DATA_____")
        for data in file.getdata():
            print(data)
        header = file.getheader()
        print("____HEADER____")
        print(header)

    with CsvReader(
            '../resources/good.csv', skip_top=5, skip_bottom=3) as file:
        print("_____DATA_____")
        for data in file.getdata():
            print(data)
        header = file.getheader()
        print("____HEADER____")
        print(header)

    print("____SKIP TOP TOO MUCH____")

    with CsvReader('../resources/good.csv', skip_top=100) as file:
        if file is None:
            print("File is corrupted")

    print("____SKIP BOTTOM TOO MUCH____")
    with CsvReader('../resources/good.csv', skip_bottom=100) as file:
        if file is None:
            print("File is corrupted")
        print("_____DATA_____")
        for data in file.getdata():
            print(data)
        header = file.getheader()
        print("____HEADER____")
        print(header)

    print("____SKIP BOTH TOO MUCH____")
    with CsvReader('../resources/good.csv', skip_top=20, skip_bottom=10) as f:
        if f is None:
            print("File is corrupted")

    with CsvReader('../resources/bad.csv') as file:
        if file is None:
            print("File is corrupted")
