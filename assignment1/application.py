from flask import Flask, request
import os

app = Flask(__name__)

# This is the "/" endpoint
@app.route("/")
def hello():
    return "Hello World!"

# Add "greetings" endpoint
# Read "GREETING" environment variable and return its value


# Add "listcontents" endpoint
# Read contents of "hostfolder" and return the contents


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000) # Change port to 5001
