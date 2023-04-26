from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS,cross_origin
from cnnClassifier.utils import decodeImage,encodeImageIntoBase64
from cnnClassifier.pipeline.predict import DogCat

os.putenv("LANG", "en_US.UTF-8")
os.putenv("LC_ALL", "en_US.UTF-8")

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = DogCat(self.filename)

clApp = ClientApp()

@cross_origin
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@cross_origin
@app.route('/train', methods = ["GET", "POST"])
def trainRoute():
    os.system("python main.py")
    return "Training Done sucessfully"

@cross_origin
@app.route('/predict',methods=["POST"])
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predictiondogcat()
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
