class Bundle:
    def __init__(self):
        self.__map = {}

    def add(self, key, value):
        self.__map[key] = value

    def get(self, key):
        return self.__map[key]
