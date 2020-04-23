#! /usr/bin/env python


if __name__ == '__main__':
    languages = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf',
    }
    for language, creator in languages.items():
        print("%s was created by %s" % (language, creator))
