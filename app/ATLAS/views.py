from django.shortcuts import render
from rdkit import Chem
#from rdkit.Chem import Draw
from rdkit.Chem import AllChem
import pubchempy


# Create your views here.
def landing(request):

    compound = pubchempy.get_compounds('Aspirin', 'name')[0]
    smiles = compound.canonical_smiles
    molecule = Chem.MolFromSmiles(smiles)
    print(f"SMILES: {smiles}")
    #mol_img = Draw.MolToImage(molecule, size=(300, 300))
    #mol_img.save('static/aspirin.png')

    return render(request, 'ATLAS/index.html', { 'smiles': smiles })
    #return render(request, 'ATLAS/index.html', { 'mol_img': mol_img })

def get_compound_info(request):
    """
    Get compound information from PubChem.
    """
    compound_name = request.GET.get('compound_name')
    if compound_name:
        compound = pubchempy.get_compounds(compound_name, 'name')[0]
        smiles = compound.canonical_smiles
        molecule = Chem.MolFromSmiles(smiles)
        print(f"SMILES: {smiles}")
        #mol_img = Draw.MolToImage(molecule, size=(300, 300))
        #mol_img.save('static/aspirin.png')
        return render(request, 'ATLAS/index.html', { 'smiles': smiles })
    else:
        return render(request, 'ATLAS/index.html', { 'error': 'No compound name provided.' })