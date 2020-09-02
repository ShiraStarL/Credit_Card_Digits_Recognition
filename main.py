import os
import sys
import argparse
import cv2
from detection import detect_card_details
import cProfile

# standalone app
# The image must include credit card with no background
# The results will be saved in 'output_imgs' directory
# $ python3 main.py <image path>
if __name__ == "__main__":
    # Parse program arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("image", help="add image to inference path")
    args = parser.parse_args()

    # Give the configuration and weight files for the model and load the network using them.
    model_configuration = "models/darknet-yolov3.cfg"
    model_weights = "models/darknet-yolov3_best.weights"
    net = cv2.dnn.readNetFromDarknet(model_configuration, model_weights)
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

    if not os.path.isfile(args.image):
        print("Input image file ", args.image, " doesn't exist")
        sys.exit(1)
    for i in range(1):
        img = cv2.imread(args.image)
        card_details = detect_card_details(img, net, save=True, image_path=args.image)
        print("card details: ", card_details)
