# Train

![alt text](https://camo.githubusercontent.com/e69d4118b20a42de4e23b9549f9a6ec6dbbb0814/687474703a2f2f706a7265646469652e636f6d2f6d656469612f66696c65732f6461726b6e65742d626c61636b2d736d616c6c2e706e67)

### Requirements

[Darknet Requirements](https://github.com/AlexeyAB/darknet#requirements)


### Usage

1. Create the train-test split
```
python3 splitTrainAndTest.py ../../database/train
```

2. Install Darknet and compile it.
```
cd ~
git clone https://github.com/AlexeyAB/darknet.git
cd darknet
make
```

3. Get the pretrained model
```
wget https://pjreddie.com/media/files/darknet53.conv.74 -O path/to/darknet/darknet53.conv.74
```

4. Fill in correct paths in the darknet.data file, **Fill the full path!**.

5. Start the training as below, by giving the correct paths to all the files being used as arguments
```
cd ~/darknet\
```
```
./darknet detector train path/to/CC_Detection/train/darknet.data  path/to/CC_Detection/train/darknet-yolov3.cfg ./darknet53.conv.74 -map
```

**The train will take a few days, you can see at the buttom of the graph how many hours remain.**

* file yolo-obj_xxxx.weights will be saved to the /path/to/CC_Detection/train/weights for each 1000 iterations
* file yolo-obj_last.weights will be saved to the /path/to/CC_Detection/train/weights for each 100 iterations



If you need any help please contact me
