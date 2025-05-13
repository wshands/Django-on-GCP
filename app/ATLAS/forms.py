from django import forms

class CompoundNameForm(forms.Form):
    """
    Form to get compound name from user.
    """
    compound_name = forms.CharField(label='Compound Name', max_length=100)

class AddCompoundForm(forms.Form):
    """
    Form to add compound information.
    """
    # compound_name = forms.CharField(label='Compound Name', max_length=100)
    # formula = forms.CharField(label='Formula', max_length=4096)
    # smiles = forms.CharField(label='SMILES', max_length=4096)
    # inchi = forms.CharField(label='InChI', max_length=255)