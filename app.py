from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from image2promptCPU import generateCaption

app = Flask(__name__)

CORS(app)

load_dotenv()

Backend_Base_url = "http://localhost:8000/uploads/"

@app.route('/image2prompt', methods=['POST'])
def image2prompt():
    data = request.json.get('data')
    imgUrls = []

    for imgName in data:
        imgUrl = Backend_Base_url + imgName
        imgUrls.append(imgUrl)

    if imgUrls:
        generatedCaptions = generateCaption(imgUrls)
        print(generatedCaptions)

    return jsonify(generatedCaptions)


if __name__ == '__main__':
    app.run(debug=True)
