from django import forms

class CompoundNameForm(forms.Form):
    """
    Form to get compound name from user.
    """
    compound_name = forms.CharField(label='Compound Name', max_length=100)