#!/usr/bin/env python3
"""
Local simulation of Notely deployed to Google Cloud Run.
This runs the actual Notely application locally to simulate the Cloud Run deployment.
"""

import subprocess
import sys
import signal
import time
import os
import requests
from datetime import datetime


def check_dependencies():
    """Check if required dependencies are available"""
    print("🔍 Checking dependencies...")

    # Check if the notely binary exists
    if not os.path.exists("./notely"):
        print("❌ Error: notely binary not found")
        print("💡 Make sure you're in the correct directory with the notely binary")
        return False

    # Check if the binary is executable
    if not os.access("./notely", os.X_OK):
        print("🔧 Making notely binary executable...")
        os.chmod("./notely", 0o755)

    print("✅ Dependencies check passed")
    return True


def setup_environment():
    """Set up environment variables for the Notely application"""
    print("⚙️  Setting up environment...")

    # Set the PORT environment variable
    os.environ["PORT"] = "8080"

    # Set a dummy DATABASE_URL to avoid database errors (optional for this simulation)
    if "DATABASE_URL" not in os.environ:
        print("💡 No DATABASE_URL set - running without database features")

    print("✅ Environment configured")


def start_notely_server():
    """Start the Notely application server"""
    print("🚀 Starting Notely application...")
    print("📍 Port: 8080")
    print("🌐 URL: http://localhost:8080")
    print("📝 This simulates Notely deployed to Google Cloud Run")
    print("⚡ Press Ctrl+C to stop")
    print("-" * 50)

    try:
        # Start the notely application
        process = subprocess.Popen(
            ["./notely"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            bufsize=1,
        )

        # Give the server time to start
        time.sleep(3)

        # Check if the process is still running
        if process.poll() is not None:
            print("❌ Failed to start Notely application")
            output, _ = process.communicate()
            print(f"Error output: {output}")
            return None

        print("✅ Notely application started successfully!")
        return process

    except FileNotFoundError:
        print("❌ Error: Could not find notely binary")
        print("💡 Make sure you're in the correct directory")
        return None
    except Exception as e:
        print(f"❌ Error starting Notely: {e}")
        return None


def test_server():
    """Test if the server is responding correctly"""
    print("\n🧪 Testing server response...")

    try:
        response = requests.get("http://localhost:8080", timeout=5)
        if response.status_code == 200:
            if "Notely" in response.text:
                print("✅ Server responding correctly (HTTP 200)")
                print("✅ Response contains 'Notely' as expected")
                return True
            else:
                print("⚠️  Server responding but 'Notely' not found in response")
                return False
        else:
            print(f"❌ Server responding with HTTP {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Server not responding: {e}")
        return False


def signal_handler(sig, frame):
    """Handle Ctrl+C gracefully"""
    print("\n🛑 Shutting down Notely simulation...")
    sys.exit(0)


def main():
    print("🚀 Notely Cloud Run Simulation")
    print("==============================")
    print("")

    # Check dependencies
    if not check_dependencies():
        sys.exit(1)

    # Set up environment
    setup_environment()

    # Start the server
    process = start_notely_server()
    if not process:
        sys.exit(1)

    # Test the server
    if not test_server():
        print("⚠️  Server started but may not be working correctly")

    print("")
    print("🎯 Ready for Bootdev testing!")
    print("📋 Use this URL: http://localhost:8080")
    print("🔧 Configure with: bootdev config base_url http://localhost:8080")
    print("🧪 Test with: bootdev run 20a64a5e-47e6-4c2d-819f-93647248bb6c")
    print("")

    # Set up signal handler
    signal.signal(signal.SIGINT, signal_handler)

    try:
        # Keep the script running and monitor the process
        while True:
            if process.poll() is not None:
                print("❌ Notely application stopped unexpectedly")
                break
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Shutting down Notely simulation...")
    finally:
        if process and process.poll() is None:
            print("🛑 Stopping Notely application...")
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
        print("✅ Cleanup complete")


if __name__ == "__main__":
    main()
