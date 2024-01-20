import unittest
from src.models.molecule import Molecule


class TestMolecule(unittest.TestCase):

    def test_to_dict(self):
        name = "water"
        smiles = "O"
        molecule = Molecule(name, smiles)

        expected = {"name": name, "smiles": smiles}
        actual = molecule.to_dict()

        self.assertEqual(expected, actual)

