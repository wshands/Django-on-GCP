from django.shortcuts import render
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import AllChem
import pubchempy

from .forms import CompoundNameForm

from io import BytesIO
import io
import base64

# Create your views here.
def landing(request):
    smiles = ''
    image_bytes = b''
    if request.method == 'POST':
        compound_form = CompoundNameForm(request.POST)
        if compound_form.is_valid():
            compound_name = request.POST.get('compound_name')
            print(f"Compound name: {compound_name}")
            if compound_name:
                compound = pubchempy.get_compounds(compound_name, 'name')[0]
                smiles = compound.canonical_smiles
                print(f"SMILES: {smiles}")
                molecule = Chem.MolFromSmiles(smiles)
                mol_img = Draw.MolToImage(molecule, size=(300, 300))
                # Convert the PIL Image to a byte string
                buffer = io.BytesIO()
                mol_img.save(buffer, format='PNG')  # or 'SVG' for vector image
                image_bytes = buffer.getvalue()
                img_encoded_bytes = base64.b64encode(image_bytes)
                print(f"Image bytes length: {len(img_encoded_bytes)}")
                #mol_img.save(f'data/{compound_name}.png')

    compound_form = CompoundNameForm()
    return render(request, 'ATLAS/index.html', { 'compound_form': compound_form, 'smiles': smiles, 'mol_img': image_bytes })
