class Dough:
    def __init__(self, flour_type, baking_technique, weight):
        self.__flour_type = flour_type
        self.__baking_technique = baking_technique
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def get_flour_type(self):
        return self.__flour_type

    def get_baking_technique(self):
        return self.__baking_technique

    def set_weight(self, new_value):
        self.__weight = new_value

    def set_flour_type(self, new_value):
        self.__flour_type = new_value

    def set_baking_technique(self, new_value):
        self.__baking_technique = new_value

