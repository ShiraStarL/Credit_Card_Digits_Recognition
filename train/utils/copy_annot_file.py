from os import listdir
from shutil import copyfile

path = "/home/shira/Documents/Projects/OCR/datasets/new"
classes_file = path + "/classes.txt"
dirs = range(79, 106)
for _dir in dirs:
    with open(classes_file) as fi:
        lines = fi.readlines()
        with open(path + "/" + str(_dir) + "/" + "classes.txt", "w") as f1:
            f1.writelines(lines)
    images = [f for f in listdir(path+'/'+str(_dir)) if f.endswith(".jpg")]
    print(images)
    src = path + '/' + str(_dir) + '/' + str(_dir) + '.txt'
    for image in images:
        dst = path + '/' + str(_dir) + '/' + image.split(".")[0] + '.txt'
        print(src, dst)
        try:
            copyfile(src, dst)
        except:
            continue
