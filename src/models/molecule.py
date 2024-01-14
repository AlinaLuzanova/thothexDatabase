class Molecule:
    def __init__(self, name_properties, file_formats, physical_properties, chemical_properties):
        self.name_properties = name_properties
        self.file_formats = file_formats
        self.physical_properties = physical_properties
        self.chemical_properties = chemical_properties

    def to_dict(self):
        return {
            "name_properties": self.name_properties,
            "smiles": self.name_properties.get("SMILES", ""),  # Assuming SMILES is always present
        }

    def create_node(self, tx):
        query = (
            "CREATE (m:Molecule {name_properties: $name_properties, smiles: $smiles, file_formats: $file_formats, physical_properties: $physical_properties, chemical_properties: $chemical_properties})"
        )
        result = tx.run(query, **self.to_dict())
        return result.single()[0]


"""
# Example usage
molecule_data = {
    'name_properties': {'IUPAK': 'value1', 'SMILES': 'value2', 'InChi': 'value3', 'CAS': 'value4', 'brutto': 'value5'},
    'file_formats': {'xyz': 'content_xyz', 'mol': 'content_mol', 'sdf': 'content_sdf', 'cif': 'content_cif'},
    'physical_properties': {'molecular_weight': 'value6', 'boiling_point': 'value7', 'density': 'value8', 'melting_point': 'value9'},
    'chemical_properties': {'dissociation_constant': 'value10', 'dipole_moment': 'value11'},
}

molecule_instance = Molecule(**molecule_data)
"""
