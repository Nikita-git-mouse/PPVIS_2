class ModelCookBook:
    def __init__(self, catalog: list, recipe):
        self.catalog = catalog
        self.recipe = recipe

    def start(self):
        pass

    def userAuth(self):
        pass

    def createCatalog(self):
        pass

    def getCatalog(self):
        pass

    def addRecipe(self, recipe):
        pass

    def editRecipe(self, id):
        pass

    def defRecipe(self, id):
        pass

    def auth(self, profile):
        pass


class Recipe:

    def __init__(self, name, description, stepCook, ingridients, tags):
        self.name = name
        self.description = description
        self.stepCook = stepCook
        self.ingridients = ingridients
        self.tags = tags


class Ingridients:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


class Profile:
    def __init__(self, login, password):
        self.login = login
        self.password = password
