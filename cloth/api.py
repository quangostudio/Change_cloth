from flask.wrappers import Request
from cloth import app
from flask import Flask, request
from PIL import Image
import io
import base64
import json
import sys, time
sys.path.append("./src/")
from model.Model import Model
from infer import Process

infer = Process()
app.config['ALLOWED_EXTENSION'] = ['.jpg', '.png']
app.config['IMAGE'] = ['./static/image/']

@app.route("/cloth", methods=["GET", "POST"])
def cloth():
    if request.method=="POST":
        image = request.files["image"].read()
        image1 = request.files["image1"].read()
        start = time.time()
        img = Image.open(io.BytesIO(image))
        img = infer._process(img)
        img1 = Image.open(io.BytesIO(image1))
        img1 = infer._process(img1)
        try:
            result = infer._predict(img, img1)
            image = base64.b64decode((infer._img_encode(result)).decode())
            img = Image.open(io.BytesIO(image))
            imagePath = ("./result/result.jpeg")
            img.save(imagePath, 'jpeg')
        except EOFError:
            data_error = {
            "status": False,
            "message": "Results is empty!"
            }
            return json.dumps(data_error), 400
        spendtime = time.time() - start
        data = {
            "status": True,
            "result": (infer._img_encode(result)).decode(),
            "input": {
                "human": (infer._img_encode(img)).decode(),
                "clothes": (infer._img_encode(img1)).decode()
            },
            "time": {
                "spendtime": spendtime,
                "timestamp": time.time()
            },
        }
        return json.dumps(data), 200
    else:
        data = {
            "status": False,
            "message": "File empty image or image1 or error method!"
        }
        return json.dumps(data), 400

# @app.route("/segment", methods=['GET', 'POST'])
# def segment():
#     pass



