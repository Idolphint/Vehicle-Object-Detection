import os

sets = {"car", "front", "rear", "person", "truck", "bus", "rider"}

def add_info(obj, photo_name, x1, y1, x2, y2, confi):
    content = ""
    if not os.path.exists("../results/out/" + photo_name + ".xml"):
        content += "<annotation>\n"
        content += "<filename>" + photo_name + ".jpg</filename>\n"
        
    f = open("../results/out/" + photo_name + ".xml", 'a')
    content += "<object>\n"
    content += "\t<name>" + obj + "</name>\n"
    content += "\t<bndbox>\n"
    content += "\t\t<xmin>" + str(x1) + "</xmin>\n"
    content += "\t\t<ymin>" + str(y1) + "</ymin>\n"
    content += "\t\t<xmax>" + str(x2) + "</xmax>\n"
    content += "\t\t<ymax>" + str(y2) + "</ymax>\n"
    
    content += "\t</bndbox>\n"
    content += "</object>\n"
    f.write(content)
    f.close()

def add_end(photo_name):
    content = ""
    if not os.path.exists("../results/out/" + photo_name + ".xml"):
        print(photo_name)
        content += "<annotation>\n"
    content += "</annotation>\n"
    f = open("../results/out/" + photo_name + ".xml", "a")
    f.write(content)
    f.close()

for obj in sets:
    txt = open("../results/comp4_det_test_"+obj+".txt", 'r').readlines()

    for info in txt:
        info = info.split()
        photo_name = info[0]

        confidence = float(info[1])

        if confidence<0.5:
            continue
        x1 = int(float(info[2]))
        y1 = int(float(info[3]))
        x2 = int(float(info[4]))
        y2 = int(float(info[5]))
        
        add_info(obj, photo_name, x1, y1, x2, y2, confidence);
    print("finish " + obj)

for name in range(0, 3298):
    add_end(str(name).zfill(6))

