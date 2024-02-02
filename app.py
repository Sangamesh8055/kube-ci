from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Please i do subscribe, like, and comment on this video, TY!!!'
