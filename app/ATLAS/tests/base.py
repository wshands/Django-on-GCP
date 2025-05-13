"""
Base test classes.

import inspect

from google.cloud import ndb

from django.conf import settings
from django.test import (
    SimpleTestCase,
    override_settings
)

from app.datastore import get_client

from ATLAS import models

TEST_NAMESPACE = f'test_{settings.DATASTORE_NAMESPACE}'

@override_settings(
    DATASTORE_NAMESPACE=TEST_NAMESPACE,
)
class DatastoreTestCase(SimpleTestCase):
    Base test case for Google Cloud Datastore.
    """
