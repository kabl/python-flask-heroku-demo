from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def root():
    return "Request with /greeting"

@app.route("/greeting")
def greeting():
    return "Message: " + os.environ["MESSAGE"]


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
