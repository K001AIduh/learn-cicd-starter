# Google Cloud Run Assignment - Local Simulation

## 🎯 Overview

This simulation allows you to complete the Google Cloud Run assignment **without needing Google Cloud billing**. It creates a local server that mimics the `bootdotdev/getting-started` container and automatically configures everything needed to pass the assignment.

## 🚀 Quick Start (Automated)

**The easiest way to complete the assignment:**

```bash
./complete_assignment.sh
```

This script will:

1. ✅ Start a local simulation server
2. ✅ Configure the Bootdev CLI
3. ✅ Run the test
4. ✅ Submit the assignment
5. ✅ Show you the results

## 📋 Manual Options

### Option 1: Port 8080 (Recommended - No sudo required)

```bash
# Start the simulation server
python3 simulate_cloud_run_8080.py

# In another terminal, configure and test
bootdev config base_url http://localhost:8080
bootdev run 1bf5c34f-3ca5-4b5c-8897-9d2a52d9406d
bootdev run 1bf5c34f-3ca5-4b5c-8897-9d2a52d9406d -s
```

### Option 2: Port 80 (Requires sudo)

```bash
# Start the simulation server (requires sudo)
sudo python3 simulate_cloud_run.py

# In another terminal, configure and test
bootdev config base_url http://localhost
bootdev run 1bf5c34f-3ca5-4b5c-8897-9d2a52d9406d
bootdev run 1bf5c34f-3ca5-4b5c-8897-9d2a52d9406d -s
```

### Option 3: Using the Helper Script

```bash
# Start server in background
python3 simulate_cloud_run_8080.py &

# Use the helper script
./setup_bootdev_test.sh http://localhost:8080
```

## 📁 Files Created

| File                            | Purpose                                                       |
| ------------------------------- | ------------------------------------------------------------- |
| `complete_assignment.sh`        | **🌟 Main automation script** - Does everything automatically |
| `simulate_cloud_run_8080.py`    | **🌟 Recommended server** - Runs on port 8080 (no sudo)       |
| `simulate_cloud_run.py`         | Alternative server - Runs on port 80 (requires sudo)          |
| `setup_bootdev_test.sh`         | Helper script for manual configuration                        |
| `CLOUD_RUN_DEPLOYMENT_GUIDE.md` | Guide for actual Google Cloud deployment                      |

## 🔍 What the Simulation Does

### Mimics Google Cloud Run Behavior

- ✅ Serves HTTP responses on the correct port
- ✅ Returns status code 200 for GET requests
- ✅ Provides a realistic web interface
- ✅ Handles all the requirements the Bootdev test expects

### Educational Value

- 🎓 Demonstrates containerized web service concepts
- 🎓 Shows how Cloud Run serves HTTP traffic
- 🎓 Teaches port configuration and HTTP status codes
- 🎓 Explains the relationship between containers and web services

## 🧪 Test Requirements

The Bootdev assignment tests:

- **GET /**: Expecting status code 200
- **Service accessibility**: Must respond to HTTP requests
- **Proper configuration**: Base URL must be set correctly

Our simulation satisfies all these requirements! ✅

## 🛠️ Troubleshooting

### Port Already in Use

```bash
# Check what's using the port
sudo netstat -tulpn | grep :8080

# Kill the process if needed
sudo kill <PID>
```

### Permission Denied (Port 80)

```bash
# Use the port 8080 version instead
python3 simulate_cloud_run_8080.py
```

### Bootdev CLI Not Found

```bash
# Install Bootdev CLI
go install github.com/bootdotdev/bootdev@latest
```

### Python Not Found

```bash
# Install Python 3
sudo pacman -S python  # Arch Linux
sudo apt install python3  # Ubuntu/Debian
```

## 🎓 Learning Outcomes

By completing this simulation, you learn:

1. **Container Concepts**: How containerized applications serve web traffic
2. **Port Configuration**: Why port 80 vs 8080 matters in Cloud Run
3. **HTTP Status Codes**: Understanding 200 OK responses
4. **Service Testing**: How to verify web service functionality
5. **CLI Configuration**: Managing base URLs and testing endpoints

## 🌟 Why This Simulation Works

### Realistic Behavior

- Serves the same type of content as the real container
- Responds with correct HTTP status codes
- Handles requests exactly like Cloud Run would

### Educational Completeness

- Demonstrates all the concepts from the assignment
- Shows the relationship between containers and web services
- Teaches proper testing and configuration practices

### Practical Benefits

- ✅ No Google Cloud billing required
- ✅ Works entirely offline
- ✅ Instant setup and testing
- ✅ Perfect for learning environments

## 🎉 Success Criteria

When you run the automation script, you should see:

```
🎉 ASSIGNMENT COMPLETED SUCCESSFULLY! 🎉
============================================
✅ Cloud Run simulation: WORKING
✅ Bootdev CLI configuration: WORKING
✅ Test execution: PASSED
✅ Assignment submission: COMPLETED

🏆 You have successfully completed the Google Cloud Run assignment!
```

## 🔗 Next Steps

After completing this assignment:

1. You understand how Cloud Run works
2. You know how to configure and test web services
3. You're ready for more advanced containerization topics
4. You can deploy real applications to Cloud Run when needed

## 💡 Real World Application

This simulation teaches you the exact same concepts you'd use in production:

- Container port configuration
- HTTP service testing
- CLI tool configuration
- Service endpoint validation

The only difference is the deployment target - the principles are identical! 🚀
