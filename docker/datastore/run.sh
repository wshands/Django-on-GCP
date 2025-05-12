#!/bin/sh

set -e

if [[ -z "${DATASTORE_PROJECT_ID}" ]]; then
  echo "DATASTORE_PROJECT_ID is not set. Please set it to your Google Cloud project ID." >&2
  exit 1
fi

# Configure the Google Cloud SDK
gcloud config set project "${DATASTORE_PROJECT_ID}"
# Start the Datastore emulator
gcloud beta emulators datastore start \
    --consistency=1.0 \
    --host-port=0.0.0.0:8001 \
    --quiet \
    --data-dir /data