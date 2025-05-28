# Google Cloud Run Deployment Guide

## Overview

This guide will help you complete the Google Cloud Run assignment by deploying a test service and configuring the Bootdev CLI.

## Step 1: Deploy to Google Cloud Run

1. **Navigate to Google Cloud Console**

   - Go to [Google Cloud Console](https://console.cloud.google.com)
   - Navigate to Cloud Run section

2. **Create Service**
   - Click "Create Service"
   - Fill in the following details:

### Required Configuration:

- **Container image URL**: `bootdotdev/getting-started`
- **Service name**: `test`
- **Region**: `us-central1`
- **Authentication**: ✅ Check "Allow unauthenticated invocations"
- **Ingress control**: ✅ "All" checked (allow direct access)

### Container Settings:

- Go to "Container(s), Volumes, Networking, Security"
- Under "Container(s)":
  - **Container port**: Change from `8080` to `80`
  - **Maximum number of instances**: `4`

3. **Deploy**
   - Click "Create" to deploy the service
   - Wait for deployment to complete
   - Copy the service URL (e.g., `https://test-vo4kpyh36a-uc.a.run.app/`)

## Step 2: Test Your Deployment

1. **Click the service URL** to verify it's working
   - You should see a webpage served by the container

## Step 3: Configure Bootdev CLI

Use the helper script provided:

```bash
./setup_bootdev_test.sh https://your-actual-service-url-here
```

Or manually:

```bash
# Set the base URL
bootdev config base_url https://your-actual-service-url-here

# Run the test
bootdev run 1bf5c34f-3ca5-4b5c-8897-9d2a52d9406d

# Submit when ready
bootdev run 1bf5c34f-3ca5-4b5c-8897-9d2a52d9406d -s
```

## What the Test Checks

The Bootdev CLI will test:

- **GET /**: Expecting status code 200
- That your service is accessible and responding correctly

## Troubleshooting

### Common Issues:

1. **Wrong port**: Make sure container port is set to `80`, not `8080`
2. **Authentication**: Ensure "Allow unauthenticated invocations" is checked
3. **URL format**: Use the complete URL including `https://`

### Verification Steps:

```bash
# Check current base URL
bootdev config base_url

# Test the endpoint manually
curl -I https://your-service-url-here

# Should return: HTTP/2 200
```

## Files Created for This Assignment

- `setup_bootdev_test.sh`: Helper script to configure and test
- `CLOUD_RUN_DEPLOYMENT_GUIDE.md`: This guide

## Success Criteria

✅ Service deployed to Cloud Run
✅ Service accessible via public URL
✅ Bootdev CLI configured with correct base URL
✅ Test passes with status code 200
✅ Assignment submitted successfully

## Next Steps

Once this assignment is complete, you'll be ready to deploy the actual Notely application to Cloud Run using similar principles!
