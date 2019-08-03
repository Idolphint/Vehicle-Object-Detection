import matplotlib.pyplot as plt


res_name=open("predictions.txt", "r").readlines()

plt.ion()
for name in res_name:
    img = plt.imread("predictions/"+name.strip('\n'))
    plt.imshow(img)
    plt.pause(1)
    plt.close()

plt.ioff()

