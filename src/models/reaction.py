class Reaction:
    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {"name": self.name}
