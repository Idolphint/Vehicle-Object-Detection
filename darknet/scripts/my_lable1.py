# train_.txt stores the full path of train_img
# train.txt stores the name_list of train_img without .jpg
# test_ & test .txt are as the same
# convert labels from .xml to .txt then labels can be seen at ./RaceData/label_intxt
# modify 7-5-2019

import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

#sets=[('2012', 'train'), ('2012', 'val'), ('2007', 'train'), ('2007', 'val'), ('2007', 'test')]

sets=['train1', 'test', 'test1', 'train']
classes = ["car", "person", "truck", "bus", "rider", "rear", "front"]


def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(image_id):
    in_file = open('/home/idolphint/lttWorkSpace/VOC2007/Annotations/%s.xml'%(image_id))
    out_file = open('/home/idolphint/lttWorkSpace/VOC2007/labels/%s.txt'%(image_id), 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or difficult==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

wd = getcwd()

for image_set in sets:
    if not os.path.exists('/home/idolphint/lttWorkSpace/VOC2007/labels'):
        os.makedirs('/home/idolphint/lttWorkSpace/VOC2007/labels')
    image_ids = open('/home/idolphint/lttWorkSpace/VOC2007/ImageSets/Main/%s.txt'%(image_set)).read().strip().split()
    list_file = open('%s_.txt'%(image_set), 'w')
    for image_id in image_ids:
        if image_set == "val":
            continue
        list_file.write('/home/idolphint/lttWorkSpace/VOC2007/ImageSets/%s/%s.jpg\n'%(image_set, image_id)) # maybe wrong
        # convert_annotation(image_id)
    list_file.close()

image_ids = open('/home/idolphint/lttWorkSpace/VOC2007/ImageSets/Main/train.txt').read().strip().split()
for image_id in image_ids:
    convert_annotation(image_id)

os.system("cat train_.txt val_.txt > train.txt") 
os.system("cat train_.txt val_.txt test_.txt test1_.txt > train.all.txt")

