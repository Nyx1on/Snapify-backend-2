from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from image2prompt import generateCaption
from create_story import generate_story

app = Flask(__name__)

CORS(app)

load_dotenv()

Backend_Base_url = "http://localhost:8000/uploads/"

@app.route('/captions/get', methods=['POST'])
def get_captions():
    data = request.json.get('data')
    imgUrls = []

    for imgName in data:
        imgUrl = Backend_Base_url + imgName
        imgUrls.append(imgUrl)

    if imgUrls:
        generatedCaptions = generateCaption(imgUrls)
        print(generatedCaptions)

    return jsonify(generatedCaptions)

@app.route('/story/get', methods=['POST'])
def get_story():
    captions = request.json.get("captions")

    print(captions)

    generated_story = generate_story(captions)

    print("Generated Story:")
    
    print(generated_story)

    return jsonify(generated_story)


if __name__ == '__main__':
    app.run(debug=True)
