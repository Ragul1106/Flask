from flask import Flask, request
import socket
import os

app = Flask(__name__)

@app.route("/")
def home():
    ip_address = request.remote_addr
    port = request.environ.get('SERVER_PORT')
    environment = os.getenv("FLASK_ENV", "production")
    return f"""
    <h2>Server Info Dashboard</h2>
    <p><b>IP Address:</b> {ip_address}</p>
    <p><b>Port:</b> {port}</p>
    <p><b>Environment:</b> {environment}</p>
    """

@app.route("/status")
def status():
    debug_mode = app.debug
    if debug_mode:
        return "Running in Debug Mode"
    return "Running in Production Mode"

if __name__ == "__main__":
    app.run(debug=True, port=8000)
