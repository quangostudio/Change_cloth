from model.Model import Model
import numpy as np
from PIL import Image
import configparser
import sys
import base64
import os
import io
sys.path.append('./src/model')
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
config = configparser.ConfigParser()
config.read('config.ini')

class Process(object):
    def __init__(self):
        super().__init__()
        self._model = Model("./src/model/checkpoints/jpp.pb",
                    "./src/model/checkpoints/gmm.pth", 
                    "./src/model/checkpoints/tom.pth", use_cuda=False)
        self._width = config.getint("IMAGE", "width")
        self._height = config.getint("IMAGE", "heigth")

    def _process(self, image):
        image = image.resize((self._width, self._height), Image.ANTIALIAS)
        return image

    def _predict(self, img1, img2):
        result,trusts = self._model.predict(img1, img2, need_pre=False,check_dirty=False)
        result = Image.fromarray(result.astype('uint8'), 'RGB')
        return result
    
    @staticmethod
    def _img_encode(results):
        rawBytes = io.BytesIO()
        results.save(rawBytes, "JPEG")
        rawBytes.seek(0)
        img_base64 = base64.b64encode(rawBytes.read())
        return img_base64
    
