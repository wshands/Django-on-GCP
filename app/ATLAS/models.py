from django.db import models


#from google.cloud import ndb

# Create your models here.

# class Redirect(ndb.Model):
#     """
#     Model to store redirect information.
#     """
#     name = ndb.StringProperty()
#     destination_url = ndb.StringProperty()
#     created_at = ndb.DateTimeProperty(auto_now_add=True)


# class Compound(ndb.Model):
#     """
#     Model to store compound information.
#     """
#     name = ndb.StringProperty()
#     formula = ndb.StringProperty()
#     smiles = ndb.StringProperty()
#     inchi = ndb.StringProperty()
#     created_at = ndb.DateTimeProperty(auto_now_add=True)

# class Protein(ndb.Model):
#     """
#     Model to store protein information.
#     """
#     name = ndb.StringProperty()
#     sequence = ndb.TextProperty()
#     created_at = ndb.DateTimeProperty(auto_now_add=True)

class Compound(models.Model):
    """
    Model to store compound information.
    """
    name = models.CharField(max_length=255)
    formula = models.CharField(blank=True, max_length=4096)
    smiles = models.CharField(blank=True, max_length=4096)
    inchi = models.CharField(blank=True, max_length=255)
    #image = models.ImageField(upload_to='compound_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Protein(models.Model):
    """
    Model to store protein information.
    """
    name = models.CharField(blank=True, max_length=255)
    sequence = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name