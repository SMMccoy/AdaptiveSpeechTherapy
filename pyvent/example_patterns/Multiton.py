class Multiton:
    instances = {}

    def __init__(self, key):
        if not self.initialized:
            self.initialized = True

    def __new__(cls, key):
        if cls.instances.get(key) is None:
            instance = super().__new__(cls)
            cls.instances[key] = instance
            instance.initialized = False
        return cls.instances[key]
