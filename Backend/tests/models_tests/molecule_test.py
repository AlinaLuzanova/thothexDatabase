import unittest
from app.models.molecule import Molecule

class TestMolecule(unittest.TestCase):

    def test_to_dict(self):
        molecule_data = {
            'name_properties': {'IUPAK': 'value1', 'SMILES': 'value2', 'InChi': 'value3', 'CAS': 'value4', 'brutto': 'value5'},
            'file_formats': {'xyz': 'content_xyz', 'mol': 'content_mol', 'sdf': 'content_sdf', 'cif': 'content_cif'},
            'physical_properties': {'molecular_weight': 'value6', 'boiling_point': 'value7', 'density': 'value8', 'melting_point': 'value9'},
            'chemical_properties': {'dissociation_constant': 'value10', 'dipole_moment': 'value11'},
        }
        molecule = Molecule(**molecule_data)

        expected = {
            "name_properties": molecule_data['name_properties'],
            "file_formats": molecule_data['file_formats'],
            "physical_properties": molecule_data['physical_properties'],
            "chemical_properties": molecule_data['chemical_properties'],
        }

        self.assertDictEqual(molecule.to_dict(), expected)

if __name__ == '__main__':
    unittest.main()
