"""
Retrieves secrets from Google Secret Manager.
"""
import os
from google.cloud.secretmanager import SecretManagerServiceClient
from google.cloud.secretmanager import AccessSecretVersionRequest

def get(name):
    """
    Get a secret from Google Secret Manager.
    """
    project = os.environ.get('GOOGLE_CLOUD_PROJECT')
    is_gae = os.environ.get('GAE_APPLICATION')

    print(f"is GAE: {is_gae}")

    if is_gae:
        # Use the Secret Manager client for Google App Engine
        client = SecretManagerServiceClient()
        secret_path = f'projects/{project}/secrets/{name}/versions/latest'

        #print(f"GAE Secret path: {secret_path}")
        #response = client.access_secret_version(request={'name': secret_path})

        # Initialize request argument(s)
        request = AccessSecretVersionRequest(name=name)
        print(f"request: {request} GAE Secret path: {secret_path}")
        response = client.access_secret_version(request=request)


        value = response.payload.data.decode('UTF-8')
        print(f"value: {value}")
        return value

    # Use the environment variable for local development
    return os.environ.get(name)