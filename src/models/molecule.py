
class Molecule:
    def __init__(self, name, smiles):
        self.name = name
        self.smiles = smiles

    def to_dict(self):
        return {"name": self.name, "smiles": self.smiles}


