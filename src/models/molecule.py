
class Molecule:
    def __init__(self, name, smiles):
        self.name = name
        self.smiles = smiles

    def to_dict(self):
        return {"name": self.name, "smiles": self.smiles}

    def create_node(self, tx):
        query = (
            "CREATE (m:Molecule {name: $name, smiles: $smiles}) "
            "RETURN m"
        )
        result = tx.run(query, **self.to_dict())
        return result.single()[0]


