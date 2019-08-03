import random


f = open("test2_.txt", "w")

for i in range(500):
    num = random.randint(0, 3298)
    f.write("/home/idolphint/lttWorkSpace/VOC2007/ImageSets/test1/" + str(num).zfill(6) + ".jpg\n")

f.close()
