#! /usr/bin/env python


if __name__ == '__main__':
    languages = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf',
    }
    for language in languages:
        print("%s was created by %s" % (language, languages[language]))
