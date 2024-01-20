class Reaction:
    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {"name": self.name}

    def create_node(self, tx):
        query = (
            "CREATE (r:Reaction {name: $name}) "
            "RETURN r"
        )
        result = tx.run(query, **self.to_dict())
        return result.single()[0]
