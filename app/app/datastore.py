"""
Google Cloud Datastore helpers.
"""

# # This module provides helpers for using Google Cloud Datastore with Django.
# from google.cloud import ndb
# from google.auth.credentials import AnonymousCredentials

# from django.conf import settings
# from django.test.runner import DiscoverRunner

# def get_client():
#     """
#     Create and return a Google Cloud Datastore client.
#     """
#     # Use AnonymousCredentials for local development
#     # and GoogleCredentials for production
#     if settings.IS_GAE:
#         # Use the default credentials for Google App Engine
#         return ndb.Client(namespace=settings.DATASTORE_NAMESPACE)
    
#     # Use AnonymousCredentials for local development
#     # and GoogleCredentials for production
#     # Use AnonymousCredentials for local development
#     return ndb.Client(
#         credentials=AnonymousCredentials(),
#         namespace=settings.DATASTORE_NAMESPACE,
#         project=settings.GOOGLE_CLOUD_PROJECT
#     )

# class NDBMiddleware:
#     """
#     Middleware to set up the NDB client for each request.
#     """
#     def __init__(self, get_response):
#         self.get_response = get_response
#         self.client = get_client()
    
#     def __call__(self, request):
#         """ Create a context for the request. """
#         context = self.client.context()
#         request.ndb_context = context
#         with context:
#             # Call the view
#             response = self.get_response(request)
#         return response
    
# class TestRunner(DiscoverRunner):
#     """
#     Custom test runner to set up the NDB client for tests.
#     """
#     def setup_databases(self, **kwargs):
#         pass
#     def teardown_databases(self, old_config, **kwargs):
#         pass

