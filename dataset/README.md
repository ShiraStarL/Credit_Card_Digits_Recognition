# Dataset


Collecting the dataset was the difficult part because people don't want to share their credit cards details and I can get it ..

### Steps:

1. Ask from everyone you know to take a picture of his credit cards.
- If they don't trust you, ask them to delete the number but not the name and expire date, letters are harder to get.

2. In each image cut the redundant background, you have to do it yourself and not use script, so you can be sure you are not loosing important data.

3. Label your dataset - 
- Clone [labelImg](https://github.com/qaprosoft/labelImg)
- In labelImg/data replace `predefined_classes.txt`.
- Run
```
python3 labelImg.py
```
- Open your images directory.
- Label each one in YOLO format : just press on `PascalVOC` button and it will change to YOLO.

4. Data Augmentation

I used [Imagaug](https://github.com/aleju/imgaug) to do it. Check [image_augmantation.py](image_augmantation.py) and [image_augmantation_hard.py](image_augmantation_hard.py). There are also examples in [data](data/) directory.

![alt text](data/5/5_22.jpg) ![alt text](data/5/5_12.jpg)

5. Add labels to all new images with [labelImg](https://github.com/qaprosoft/labelImg).


**My dataset contains 132 real cards, 20 cards I downloaded from Google (here [data](data/)). Using data augmentation I got 3886 images in total.**


