import os
import random
from stuff.Category import Category

class Idea:
    def __init__(self, category: Category):
        self.category = category

    def getidea(self):
        # Call getideas with the category's filepath
        # It would probably be better to not remake the whole list every time
        ideas = self.getideas(self.category.filepath)
        return random.choice(ideas) if ideas else "No ideas found."

    def getallideas(self):
        ideas = self.getideas(self.category.filepath)
        return ideas

    # Recursion
    def getideas(self, path: str):
        ideas = []
        with os.scandir(path) as entries:
            for entry in entries:
                if not entry.is_dir():
                    with open(entry.path, "r") as file:
                        content = file.read()
                        lines = content.split("\n")
                        ideas.extend(lines)
                else:
                    ideas.extend(self.getideas(entry.path))
        return ideas
