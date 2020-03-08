from flask import Flask, request, jsonify
from flask_cors import CORS
import findData
import cv2
import os
app = Flask(__name__)
CORS(app)


@app.route('/upload', methods=['POST'])
def upload():
    try:
        file = request.files['file']
        image_path = os.getcwd()+"//uploaded" + "//" + file.filename
        img = findData.remove_noise_and_smooth(image_path)
        cv2.imwrite("uploaded/"+file.filename, img)
        data = findData.findDateAndTime(file)
        return jsonify(status='success', message='uploaded-{}'.format(file.filename), data=data), 200
    except KeyError as e:
        return jsonify(status='failed', message='file not present'), 400


if __name__ == '__main__':
    app.run()
