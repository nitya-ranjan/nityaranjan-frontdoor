# main.py
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    # Get the port from the PORT environment variable, defaulting to 8080 for local development
    port = int(os.environ.get("PORT", 8080))
    
    # Run the app, listening on all network interfaces and on the dynamic port.
    app.run(host='0.0.0.0', port=port)