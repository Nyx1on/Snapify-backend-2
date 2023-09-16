from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from image2text import generate_text_from_image
from openaiLLM import generate_story, generate_caption

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
        generatedCaptions = generate_text_from_image(imgUrls)
        print(generatedCaptions)

    return jsonify(generatedCaptions)


@app.route('/story/get', methods=['POST'])
def get_story():
    title = request.json.get('title')
    captions = request.json.get("captions")
    prompt = request.json.get("prompt")
    print(captions)

    generated_story = generate_story(title, captions, prompt)

    print("Generated Story:")

    print(generated_story)

    return jsonify(generated_story)


@app.route('/generate-caption', methods=['POST'])
def generate_caption_api():
    title = request.json.get('title')
    captions = request.json.get("captions")
    prompt = request.json.get("prompt")
    print(captions)

    generated_caption = generate_caption(title, captions, prompt)

    print("Generated Caption:")

    print(generated_caption)

    return jsonify(generated_caption)


if __name__ == '__main__':
    app.run(debug=True)
