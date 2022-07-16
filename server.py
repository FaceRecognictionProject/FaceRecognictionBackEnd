from flask import Flask, request, jsonify, make_response, abort
from flask_cors import CORS
import json
import numpy as np
import cv2

app = Flask(__name__)
CORS(app)

"""
@app.route('/api/upload', methods=['POST'])
def upload():
    import base64
    from PIL import Image
    import io
    data = request.get_json();
    imdata = base64.b64decode(str(data['imagedata']))
    image = Image.open(io.BytesIO(imdata))
    im = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)
    # cv2.imshow("face",im)
    # cv2.waitKey(0)
    import facedetect
    f = facedetect.faceD(im)
    return jsonify(f)
"""

@app.route('/api/face_recogni', methods=['POST'])
def upload():
    import base64
    from PIL import Image
    import io
    import face_recogni

    data = request.get_json();
    imdata = base64.b64decode(str(data['imagedata']))
    image = Image.open(io.BytesIO(imdata))
    recogni = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)
    person = face_recogni.face_recogintion(recogni)
    return jsonify(person)

if __name__ == '__main__':
   app.run(host="192.168.43.229", port=5000, debug=True)
  