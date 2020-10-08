# Dataset


Collecting the dataset was the hardest because people don't want to share their credit cards details and I can get it ..

### Steps:

1. Ask from everyone you know to take a picture of his credit cards.
- If they don't trust you ask them to the delete the number but not the name and exprie date, letters are harder to get.

2. Cut the reduntant background on every image, you have to do it by yourself and not by script to make sure you are not loosing important data.

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

I used [Imagaug](https://github.com/aleju/imgaug) for it. Check [image_augmantation.py](image_augmantation.py) and [image_augmantation_hard.py](image_augmantation_hard.py). There are also examples in [data](data/) directory.

![alt text](data/5/5_22.jpg) ![alt text](data/5/5_12.jpg)

5. Add lebals to all new images with [labelImg](https://github.com/qaprosoft/labelImg).


**My dataset contain 132 real cards, 20 cards I download from Google (here [data](data/)). Using data augmentation I got 3886 images in total.**


