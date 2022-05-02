from flask import Flask

app = Flask(__name__)

print("Hi, from development mode and new greet app!")

@app.route("/welcome")
def say_welcome():
    return "welcome"

@app.route("/welcome/home")
def say_welcome_home():
    return "welcome home"

@app.route("/welcome/back")
def say_welcome_back():
    return "welcome back"

