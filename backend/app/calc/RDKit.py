from rdkit import Chem
from rdkit.Chem import AllChem, Draw


# Создание молекулы из SMILES
def create_molecule_from_smiles(smiles):
    return Chem.MolFromSmiles(smiles)


# Сохранение молекулы в формате SMILES
def save_molecule_to_smiles(molecule, filename):
    smiles = Chem.MolToSmiles(molecule)
    with open(filename, "w") as file:
        file.write(smiles)


# Сохранение молекулы в формате MOL
def save_molecule_to_mol(molecule, filename):
    mol_block = Chem.MolToMolBlock(molecule)
    with open(filename, "w") as file:
        file.write(mol_block)


# Сохранение молекулы в формате SDF
def save_molecule_to_sdf(molecule, filename):
    writer = Chem.SDWriter(filename)
    writer.write(molecule)
    writer.close()


# Сохранение молекулы в формате PDB
def save_molecule_to_pdb(molecule, filename):
    AllChem.Compute2DCoords(molecule)
    writer = Chem.PDBWriter(filename)
    writer.write(molecule)
    writer.close()


# Сохранение молекулы в формате InChI
def save_molecule_to_inchi(molecule, filename):
    inchi = Chem.MolToInchi(molecule)
    with open(filename, "w") as file:
        file.write(inchi)


# Сохранение молекулы в формате PNG (картинка)
def save_molecule_to_png(molecule, filename):
    AllChem.Compute2DCoords(molecule)
    img = Chem.Draw.MolToImage(molecule)
    img.save(filename)


"""
ethanol = create_molecule_from_smiles("CCO")
save_molecule_to_smiles(ethanol, "ethanol.smiles")
save_molecule_to_mol(ethanol, "ethanol.mol")
save_molecule_to_sdf(ethanol, "ethanol.sdf")
save_molecule_to_pdb(ethanol, "ethanol.pdb")
save_molecule_to_inchi(ethanol, "ethanol.inchi")
save_molecule_to_png(ethanol, "ethanol.png")
"""
