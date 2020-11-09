import os
import cv2 as cv
from preprocess import preprocess
from postprocess import postprocess


# Get the names of the output layers
def get_outputs_names(_net):
    # Get the names of all the layers in the network
    layers_names = _net.getLayerNames()
    # Get the names of the output layers, i.e. the layers with unconnected outputs
    return [layers_names[i[0] - 1] for i in _net.getUnconnectedOutLayers()]


def detection(img, net):
    inpWidth = 416       # Width of network's input image
    inpHeight = 416       # Height of network's input image

    # Create a 4D blob from a frame.
    blob = cv.dnn.blobFromImage(img, 1/255, (inpWidth, inpHeight), swapRB=True)

    # Sets the input to the network
    net.setInput(blob)

    # Runs the forward pass to get output of the output layers
    outs = net.forward(get_outputs_names(net))

    # Put efficiency information. The function getPerfProfile returns the overall time for inference(t) and the timings for each of the layers(in layersTimes)
    # t, _ = net.getPerfProfile()
    # label = 'Inference time: %.2f ms' % (t * 1000.0 / cv.getTickFrequency())
    # cv.putText(img, label, (0, 15), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))

    return img, outs


def detect_card_details(card_img, net, save=False, image_path=".jpg", prepro=False):
    # Preprocess image
    if prepro:
        card_img = preprocess(card_img)

    # Predict classes from image
    card_img, outs = detection(card_img, net)

    # Postprocess to extract card details
    image_name = os.path.split(image_path)[1]
    _card_details = postprocess(card_img, outs, image_name, save)

    return _card_details
