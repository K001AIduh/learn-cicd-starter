#!/usr/bin/env python3
"""
Local simulation of the bootdotdev/getting-started Docker container.
This serves a simple web page on port 80 to simulate Google Cloud Run deployment.
"""

import http.server
import socketserver
import sys
import signal
import os
from datetime import datetime


def get_html_content():
    """Generate HTML content with current timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Boot.dev Getting Started</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }}
        .container {{
            text-align: center;
            background: rgba(255, 255, 255, 0.1);
            padding: 3rem;
            border-radius: 20px;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        }}
        h1 {{
            font-size: 3rem;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }}
        p {{
            font-size: 1.2rem;
            margin-bottom: 2rem;
            opacity: 0.9;
        }}
        .badge {{
            background: rgba(255, 255, 255, 0.2);
            padding: 0.5rem 1rem;
            border-radius: 25px;
            font-size: 0.9rem;
            margin: 0.5rem;
            display: inline-block;
        }}
        .footer {{
            margin-top: 2rem;
            font-size: 0.8rem;
            opacity: 0.7;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Boot.dev Getting Started</h1>
        <p>Congratulations! Your Cloud Run service is working perfectly.</p>

        <div class="badge">✅ Container Running</div>
        <div class="badge">🌐 Port 80 Active</div>
        <div class="badge">☁️ Cloud Run Simulation</div>

        <div class="footer">
            <p>This is a local simulation of the bootdotdev/getting-started container.</p>
            <p>Perfect for testing your Bootdev CLI assignment!</p>
            <p>Server started at: {timestamp}</p>
        </div>
    </div>
</body>
</html>"""


class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests - serve our HTML content for any path"""
        html_content = get_html_content()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(html_content.encode("utf-8"))))
        self.end_headers()
        self.wfile.write(html_content.encode("utf-8"))

        # Log the request
        print(f"✅ Served GET {self.path} - Status: 200")


def signal_handler(sig, frame):
    """Handle Ctrl+C gracefully"""
    print("\n🛑 Shutting down Cloud Run simulation...")
    sys.exit(0)


def main():
    PORT = 80

    # Check if we can bind to port 80 (requires sudo on most systems)
    try:
        with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
            print("🚀 Boot.dev Cloud Run Simulation Starting...")
            print(f"📍 Serving on port {PORT}")
            print(f"🌐 Access at: http://localhost:{PORT}")
            print("📝 This simulates the bootdotdev/getting-started container")
            print("⚡ Press Ctrl+C to stop")
            print("-" * 50)

            # Set up signal handler for graceful shutdown
            signal.signal(signal.SIGINT, signal_handler)

            # Start serving
            httpd.serve_forever()

    except PermissionError:
        print("❌ Error: Permission denied to bind to port 80")
        print("💡 Try running with sudo: sudo python3 simulate_cloud_run.py")
        print("💡 Or use the alternative script that runs on port 8080")
        sys.exit(1)
    except OSError as e:
        if "Address already in use" in str(e):
            print("❌ Error: Port 80 is already in use")
            print("💡 Try stopping other services or use the alternative script")
        else:
            print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
