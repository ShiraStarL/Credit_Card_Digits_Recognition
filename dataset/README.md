# Dataset


Collecting the dataset was the hardest because people don't want to share their credit cards details and I can get it ..

### Steps:

1. Ask from everyone you know to take a picture of his credit cards.

2. Cut the reduntant background on every image, you need to it by yourself and not by script to make sure you are not loosing important data.

3. Add lebals to your dataset - 
- Clone [labelImg](https://github.com/qaprosoft/labelImg)
- In labelImg/data replace predefined_classes.txt
- Run it
```
python3 labelImg.py
```
- Open the directory with the images you colleced
- Label each one in YOLO format : just press on the button "PascalVOC" and you will see it changes to YOLO.

4. Data Augmentation

![alt text](data/7/7_3.jpg) ![alt text](data/6/6_4.jpg)

I used [Imagaug](https://github.com/aleju/imgaug) for it. Check [image_augmantation.py](image_augmantation.py) and [image_augmantation_hard.py](image_augmantation_hard.py). There are also examples in [data](data/) directory.


