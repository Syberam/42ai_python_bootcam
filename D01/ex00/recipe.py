#!/usr/bin/env python
import sys
import textwrap


class Recipe:
    def __init__(
        self, name=str(), cooking_level=int(), cooking_time=int(),
            ingredients=list(), description=str(), recipe_type=str()):
        wrong_args = self.check_args(
            name, cooking_level, cooking_time,
            ingredients, description, recipe_type)
        for w_arg in wrong_args:
            print(
                "Error: {a[id]}: {a[error]} {a[why]}".format(a=w_arg),
                file=sys.stderr)
        if len(wrong_args):
            return
        self.name = str(name)
        self.cooking_level = cooking_level
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = str(description)
        self.recipe_type = str(recipe_type)

    def check_args(
            self, name=str(), cooking_level=int(), cooking_time=int(),
            ingredients=list(), description=str(), recipe_type=str()):
        wrong_args = []
        if not name:
            wrong_args.append({'id': 'name', 'error': 'empty', 'why': ''})
        if not cooking_level:
            wrong_args.append({
                'id': 'cooking_level', 'error': 'empty', 'why': ''})
        elif type(cooking_level) != int or cooking_level not in range(1, 5):
            wrong_args.append({
                    'id': 'cooking_level',
                    'error': 'wrong format',
                    'why': "Should be an int between 1 and 5"})
        if not cooking_time:
            wrong_args.append({
                'id': 'cooking_time', 'error': 'empty', 'why': ''})
        elif type(cooking_time) != int:
            wrong_args.append({
                    'id': 'cooking_time',
                    'error': 'wrong format',
                    'why': "Should be an int()"})
        if not ingredients:
            wrong_args.append({
                'id': 'ingredients', 'error': 'empty', 'why': ''})
        elif type(ingredients) != list:
            wrong_args.append({
                    'id': 'cooking_ingredients',
                    'error': 'wrong format',
                    'why': "Should be a list of ingredients"})
        if not recipe_type:
            wrong_args.append({
                'id': 'recipe_type', 'error': 'empty', 'why': ''})
        return wrong_args

    def __str__(self):
        """Return the string to print with the recipe info"""
        if self.description:
            desc = textwrap.wrap(
                "Description: " + textwrap.dedent(self.description), 78)
            desc = ["|{:<78}|".format(l) for l in desc]
            desc = '\n'.join(desc)
        time = ' ~ [' + str(self.cooking_time) + 'min]'

        ag = (
            "{:_^80}".format(''),
            "|{:^78}|".format(self.name + time),
            "{:_^80}".format(''),
            "|Level:{:>72}|".format(self.cooking_level),
            "|Meal:{:>73}|".format(self.recipe_type),
            "|Ingredients:{:>66}|".format(str(self.ingredients)),
            '\n' + desc if self.description else '')
        txt = """{}
{}
{}

{}
{}
{}{}""".format(*ag)
        return txt
