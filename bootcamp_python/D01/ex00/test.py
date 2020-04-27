#!/usr/bin/env python

# from book import Book
from recipe import Recipe

if __name__ == '__main__':
    print("___________TEST args _________")
    print("_________ args empty _________")
    cake = Recipe()
    print("______ args wrong values ______")
    cake = Recipe(1, 'toto', 'tutu', 5, '', ('bouli', 'bilu'))
    print("______ args good values ______")
    cake = Recipe(
        "cake", 2, 3, ['a', 'b'],
        """Tu touilles, Tu touilles, Tu touilles, Tu touilles, Tu touilles,
Tu touilles, Tu touilles, Tu touilles, Tu touilles, Tu touilles,
Tu touilles, Tu touilles, Tu touilles, Tu touilles, Tu touilles""",
        ('bouli', 'bilu'))
    print(str(cake))
    cake_undescribe = Recipe("cake", 2, 3, ['a', 'b'], '', ('bouli', 'bilu'))
    print(str(cake_undescribe))
