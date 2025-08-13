# SPDX-FileCopyrightText: 2024 MoonlightByte
# SPDX-License-Identifier: Fair-Source-1.0
#
# app.py - Production Web Server Entry Point
#
# This script is the entry point for running the web application in a production
# environment using a WSGI server like Waitress. It imports the Flask app and
# SocketIO instances from the main web interface module and serves them.

import os
from waitress import serve
from web.web_interface import app, socketio

if __name__ == '__main__':
    # Use the PORT environment variable provided by the hosting service, or default to 8357
    port = int(os.environ.get('PORT', 8357))
    
    # Use '0.0.0.0' to make the server accessible externally
    host = '0.0.0.0'
    
    print(f"Starting server on {host}:{port}")
    
    # Use waitress to serve the SocketIO application
    # socketio.run(app) is for development, for production we pass the app to waitress
    serve(app, host=host, port=port)
