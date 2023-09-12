from flask import Flask

app = Flask(__name__)

@app.route('/image2prompt')
def image2prompt():
    