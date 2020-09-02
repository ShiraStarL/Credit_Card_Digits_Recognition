# make sure I have examples of all classes in dataset
from os import listdir
import argparse

# Parse program arguments
parser = argparse.ArgumentParser()
parser.add_argument("--file", help="path to file with images paths", default="")
parser.add_argument("--dir", help="labels directory path", default="")
parser.add_argument("--classes", help="path to classes.txt file")
args = parser.parse_args()

# classes.txt path
classes_path = args.classes

with open(classes_path) as f:
    classes_names = f.readlines()
num_of_classes = len(classes_names)
classes_names = [x.strip() for x in classes_names]

classes = {}
for i in range(num_of_classes):
    classes[i] = 0

if args.file:
    with open(args.file) as f:
        lines = f.read().splitlines()
        imgs_names = [line.split('/')[-1] for line in lines]
    label_path = '/home/shira/Documents/Projects/OCR/datasets/annotation/train/yolo_new/'
    for img in imgs_names:
        with open(label_path + img.split('.')[0] + ".txt") as f:
            lines = f.readlines()
            for line in lines:
                cls = line.split()[0]
                classes[int(cls)] += 1

if args.dir:
    path_to_files = args.dir
    for file in listdir(path_to_files):
        with open(path_to_files + '/' + file) as f:
            lines = f.readlines()
            for line in lines:
                cls = line.split()[0]
                classes[int(cls)] += 1

sort_classes = {k: v for k, v in sorted(zip(classes.items(), classes_names), key=lambda item: item[0][1])}
for item in sort_classes:
    print(sort_classes[item], ":", item[1])

