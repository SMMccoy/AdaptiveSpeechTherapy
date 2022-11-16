class Singleton:
    instance = None

    def __init__(self):
        if not self.initialized:
            self.initialized = True

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.initialized = False
        return cls.instance
