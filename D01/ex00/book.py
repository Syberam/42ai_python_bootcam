#!/usr/bin/env python


# The Book class also has some attributes:
# • name (str)
# • last_update (datetime)
# • creation_date (datetime)
# • recipes_list (dict) : a dictionnary why 3 keys: “starter”, “lunch”, “dessert”.


class Book:
    def __init__(
        self,
        name=str(),
        last_update=datetime(), creation_date=datetime(),
        recipes_list=dict()):
        pass


    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        pass


    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        pass


    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        pass