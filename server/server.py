from flask import Flask, request, jsonify
from models import classify_image,load_saved_artifacts

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"mg":"jkndf"})

@app.route('/classifier', methods=['GET', 'POST'])
def classify():
    image_data = request.form['image_data']
    print("Hello")
    print(image_data)
    response = jsonify(classify_image(image_data))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    load_saved_artifacts()
    app.run(port=5000,debug=True)