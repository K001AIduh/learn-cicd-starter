#!/bin/bash

# Helper script to configure and test Cloud Run deployment
# Usage: ./setup_bootdev_test.sh <your-cloud-run-url>

if [ $# -eq 0 ]; then
    echo "Usage: $0 <cloud-run-url>"
    echo "Example: $0 https://test-vo4kpyh36a-uc.a.run.app"
    exit 1
fi

CLOUD_RUN_URL=$1

echo "🚀 Setting up Bootdev CLI for Cloud Run testing..."
echo "📍 Cloud Run URL: $CLOUD_RUN_URL"

# Configure the base URL
echo "⚙️  Configuring base URL..."
bootdev config base_url "$CLOUD_RUN_URL"

# Verify configuration
echo "✅ Current configuration:"
bootdev config base_url

# Test the endpoint
echo "🧪 Testing the endpoint..."
curl -s -o /dev/null -w "HTTP Status: %{http_code}\n" "$CLOUD_RUN_URL"

# Run the Bootdev test
echo "🏃 Running Bootdev test..."
bootdev run 1bf5c34f-3ca5-4b5c-8897-9d2a52d9406d

echo ""
echo "📝 If the test passes, submit with:"
echo "   bootdev run 1bf5c34f-3ca5-4b5c-8897-9d2a52d9406d -s"
