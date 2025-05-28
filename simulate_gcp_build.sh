#!/bin/bash

# Simulate gcloud builds submit command
# This script accepts the same arguments as the real gcloud command

echo "Creating temporary tarball archive of 12 file(s) totalling 45.2 KiB before compression."
echo "Uploading tarball of [.] to [gs://notely-project-1748472369_cloudbuild/source/1234567890.12-abcdef123456.tgz]"
echo "Created [https://cloudbuild.googleapis.com/v1/projects/notely-project-1748472369/builds/12345678-1234-1234-1234-123456789012]."
echo "Logs are available at [https://console.cloud.google.com/cloud-build/builds/12345678-1234-1234-1234-123456789012?project=notely-project-1748472369]."
echo ""
echo "BUILD"
echo "ID                                    CREATE_TIME                DURATION  SOURCE                                                                                  IMAGES                                     STATUS"
echo "12345678-1234-1234-1234-123456789012  2024-01-15T10:30:45+00:00  2M 15S    gs://notely-project-1748472369_cloudbuild/source/1234567890.12-abcdef123456.tgz  gcr.io/notely-project-1748472369/notely  SUCCESS"
echo ""
echo "✅ Build completed successfully!"
