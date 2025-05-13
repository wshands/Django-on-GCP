"""
Retrieves secrets from Google Secret Manager.
"""
import os
from google.cloud.secretmanager import SecretManagerServiceClient

def get(name):
    """
    Get a secret from Google Secret Manager.
    """
    project = os.environ.get('GOOGLE_CLOUD_PROJECT')
    is_gae = os.environ.get('GAE_APPLICATION')

    if is_gae:
        # Use the Secret Manager client for Google App Engine
        client = SecretManagerServiceClient()
        secret_path = f'projects/{project}/secrets/{name}/versions/latest'
        response = client.access_secret_version(name=secret_path)
        value = response.payload.data.decode('UTF-8')
        return value

    # Use the environment variable for local development
    return os.environ.get(name)