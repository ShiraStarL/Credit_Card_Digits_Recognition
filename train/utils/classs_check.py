# Check how many examples there are of each class
import argparse
from os import listdir
from collections import Counter

parser = argparse.ArgumentParser()
parser.add_argument("dir", help="labels directory path", default="")
parser.add_argument("classes", help="path to classes.names file")
args = parser.parse_args()

labels_dir = args.dir
classes = args.classes

with open(classes) as f:
    classes_names = f.read().splitlines()

labels_files = [x for x in listdir(labels_dir) if x.endswith(".txt")]

classes_count = Counter()
for label_file in labels_files:
    with open(labels_dir + '/' + label_file) as f:
        lines = f.read().splitlines()
        classes_ids = [x[:2].strip() for x in lines]
        classes_count.update(Counter(classes_ids))

sort_classes = {k: v for k, v in sorted(zip(classes_names, classes_count.values()), key=lambda item: item[1])}
print(sort_classes)
