from django.shortcuts import render
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import AllChem
import pubchempy

from .forms import CompoundNameForm
from .forms import AddCompoundForm

from .models import Compound

from io import BytesIO
import io
import base64

def get_compound_information(compound_name):

    """
    Get compound information from PubChem.
    """
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
    img_encoded_string = img_encoded_bytes.decode('utf-8')
    
    return smiles, img_encoded_string


# Create your views here.
def landing(request):
    compound_name = ''
    smiles = ''
    image_bytes = b''
    img_encoded_string = ''
    formula = ''
    inchi = ''
    # Check if the request method is GET or POST
    print("Request method:", request.method)
    if request.method == 'GET':
        compound_form = CompoundNameForm(request.GET)
        if compound_form.is_valid():
            compound_name = request.GET.get('compound_name')
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
                img_encoded_string = img_encoded_bytes.decode('utf-8')

                #compounds_in_db = Compound.objects.all()
                #print(f"Compound in DB: {compounds_in_db}")

                # Save the compound information to the database
                # compound = Compound(
                #     name=compound_name,
                #     formula=formula,
                #     smiles=smiles,
                #     inchi=inchi
                # )
                #print("about to save compound")
                #compound.save()
                 
    elif request.method == 'POST':
        add_compound_form = AddCompoundForm(request.POST)
        if add_compound_form.is_valid():
            # compound_name = request.POST.get('compound_name')
            # formula = request.POST.get('formula')
            # smiles = request.POST.get('smiles')
            # inchi = request.POST.get('inchi')
            print(f"Compound name: {compound_name}")
            print(f"Formula: {formula}")
            print(f"SMILES: {smiles}")
            print(f"InChI: {inchi}")
            # Save the compound information to the database
            compound = Compound(
                name=compound_name,
                formula=formula,
                smiles=smiles,
                inchi=inchi
            )
            compound.save()
            # Optionally, you can redirect to a success page or render the same page with a success message
            # For now, we'll just render the same page with the compound information

    compound_form = CompoundNameForm()
    add_compound_form = AddCompoundForm()
    return render(request, 'ATLAS/index.html', { 
        'compound_form': compound_form,
        'add_compound_form': add_compound_form,
        'compound_name': compound_name,
        'smiles': smiles,
        'mol_img': img_encoded_string 
        })
