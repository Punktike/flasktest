from stuff.Category import Category
import random

import os

class Idea:
    def __init__(self, text : str, category : Category):
        self.text = text
        self.category = category


    def getidea(self):

        # Need to add support for subcategories



        with open(self.category.filepath, "r") as file:
            content = file.read()
            lines = content.split("\n")
            return random.choice(lines)