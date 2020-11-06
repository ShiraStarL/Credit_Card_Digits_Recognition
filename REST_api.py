import cv2
import argparse
import jsonpickle
import numpy as np
from flask_restful import Resource, Api
from detection import detect_card_details
from flask import Flask, request, Response

save = False

app = Flask(__name__)
api = Api(app)

# Give the configuration and weight files for the model and load the network using them.
model_configuration = "models/darknet-yolov3.cfg"
model_weights = "models/darknet-yolov3_best.weights"
net = cv2.dnn.readNetFromDarknet(model_configuration, model_weights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)


class GetPicture(Resource):
    def post(self):
        img = request.files['image'].read()
        # convert string of image data to uint8
        nparr = np.frombuffer(img, np.uint8)
        # decode image
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        if save:
            cv2.imwrite("output_imgs/raw_output.jpg", img)

        # detect credit card
        card_details = detect_card_details(img, net, save=save, prepro=True)

        # check if any details return
        if card_details:
            card_details["status"] = True
        else:
            card_details["status"] = False

        # Add missing keys
        keys = ["card_type", "card_number", "valid_date", "full_name"]
        for key in keys:
            if key not in card_details:
                card_details[key] = ""

        # encode response using jsonpickle
        response_pickled = jsonpickle.encode(card_details)

        return Response(response=response_pickled, status=200, mimetype="application/json")

    def get(self):
        return {"get": "hello friend <3"}


api.add_resource(GetPicture, '/pic')

# python REST_api.py --save
if __name__ == '__main__':
    # Parse program arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", help="Host ip", default='0.0.0.0')
    parser.add_argument("--port", help="Port", default="5000")
    parser.add_argument("--dev", help="True for development server", action="store_true")
    parser.add_argument("--save", help="Save output image", action="store_true")
    args = parser.parse_args()

    save = args.save
    # run server
    app.run(debug=args.dev, host=args.host, port=args.port)
