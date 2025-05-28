#!/usr/bin/env python3
"""
Local simulation of the bootdotdev/getting-started Docker container.
This serves a simple web page on port 8080 to simulate Google Cloud Run deployment.
(Alternative version that doesn't require sudo)
"""

import http.server
import socketserver
import sys
import signal
import os
from datetime import datetime

# HTML content that mimics what bootdotdev/getting-started would serve
HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Boot.dev Getting Started</title>
    <style>
        body {
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
        }
        .container {
            text-align: center;
            background: rgba(255, 255, 255, 0.1);
            padding: 3rem;
            border-radius: 20px;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        }
        h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }
        p {
            font-size: 1.2rem;
            margin-bottom: 2rem;
            opacity: 0.9;
        }
        .badge {
            background: rgba(255, 255, 255, 0.2);
            padding: 0.5rem 1rem;
            border-radius: 25px;
            font-size: 0.9rem;
            margin: 0.5rem;
            display: inline-block;
        }
        .footer {
            margin-top: 2rem;
            font-size: 0.8rem;
            opacity: 0.7;
        }
        .warning {
            background: rgba(255, 193, 7, 0.2);
            border: 1px solid rgba(255, 193, 7, 0.5);
            padding: 1rem;
            border-radius: 10px;
            margin: 1rem 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Boot.dev Getting Started</h1>
        <p>Congratulations! Your Cloud Run service is working perfectly.</p>

        <div class="badge">✅ Container Running</div>
        <div class="badge">🌐 Port 8080 Active</div>
        <div class="badge">☁️ Cloud Run Simulation</div>

        <div class="warning">
            <strong>⚠️ Note:</strong> This simulation runs on port 8080 instead of 80.<br>
            Use <code>http://localhost:8080</code> as your base URL.
        </div>

        <div class="footer">
            <p>This is a local simulation of the bootdotdev/getting-started container.</p>
            <p>Perfect for testing your Bootdev CLI assignment!</p>
            <p>Server started at: {timestamp}</p>
        </div>
    </div>
</body>
</html>""".format(
    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
)


class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests - serve our HTML content for any path"""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(HTML_CONTENT.encode("utf-8"))))
        self.end_headers()
        self.wfile.write(HTML_CONTENT.encode("utf-8"))

        # Log the request
        print(f"✅ Served GET {self.path} - Status: 200")


def signal_handler(sig, frame):
    """Handle Ctrl+C gracefully"""
    print("\n🛑 Shutting down Cloud Run simulation...")
    sys.exit(0)


def main():
    PORT = 8080

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

    except OSError as e:
        if "Address already in use" in str(e):
            print("❌ Error: Port 8080 is already in use")
            print("💡 Try stopping other services or choose a different port")
        else:
            print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
