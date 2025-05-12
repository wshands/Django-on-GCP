#from django.db import models

from google.cloud import ndb

# Create your models here.

class Redirect(ndb.Model):
    """
    Model to store redirect information.
    """
    name = ndb.StringProperty()
    destination_url = ndb.StringProperty()
    created_at = ndb.DateTimeProperty(auto_now_add=True)


class Compound(ndb.Model):
    """
    Model to store compound information.
    """
    name = ndb.StringProperty()
    formula = ndb.StringProperty()
    smiles = ndb.StringProperty()
    inchi = ndb.StringProperty()
    created_at = ndb.DateTimeProperty(auto_now_add=True)

class Protein(ndb.Model):
    """
    Model to store protein information.
    """
    name = ndb.StringProperty()
    sequence = ndb.TextProperty()
    created_at = ndb.DateTimeProperty(auto_now_add=True)

