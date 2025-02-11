class Category:
    def __init__(self, name: str, filepath: str):
        self.filepath = filepath
        self.name = name


class Categories:
    all = Category("all", "choices")
    outdoors = Category("outdoors", "choices/outdoors")
    indoors = Category("indoors", "choices/indoors")
