from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getLanguages', methods=['GET'])
def get_languages():
    url = "https://text-translator2.p.rapidapi.com/getLanguages"
    headers = {
        "X-RapidAPI-Key": "31be6b785emshd266499d9f56b03p1972f6jsna70012e7808d",
        "X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    return jsonify(response.json())

@app.route('/translate', methods=['POST'])
def translate():
    source_language = request.form['source_language']
    target_language = request.form['target_language']
    text = request.form['text']
    url = "https://text-translator2.p.rapidapi.com/translate"
    payload = {
        "source_language": source_language,
        "target_language": target_language,
        "text": text
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "31be6b785emshd266499d9f56b03p1972f6jsna70012e7808d",
        "X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
    }
    response = requests.post(url, data=payload, headers=headers)
    json_response = response.json()
    translated_text = json_response.get('data', {}).get('translatedText')
    return jsonify({'translatedText': translated_text})

if __name__ == '__main__':
    app.run(debug=True)