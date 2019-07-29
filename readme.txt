目标检测算法技术总结报告以及源代码 //我

仿真环境运行&评测分析&批量保存运行结果（以图片为准） // 评测以及反馈组

标签预测的生成与完备以及迭代结果提交 //提交组


训练：./darknet detector train cfg/my.data cfg/yolov3-my.cfg backup/yolov3-my.backup 




可视化测试：./darknet detector test cfg/my.data cfg/yolov3-my.cfg backup/yolov3-my.backup 
        ##根据网上的教程，对detector.c中的test_decetor函数做了修改后，可以根据test1_.txt里标明的图片路径逐一进行图片的检测




获取txt结果:./darknet detector valid cfg/my.data cfg/yolov3-my.cfg backup/yolov3-my.backup 

        ##会在results文件夹下根据类名生成几个txt文件
        通过运行scripts/run_xml.sh可以在results/out下获得000000.xml之类的文件



图片存放结构

        VOC2007--
                |--ImageSets--
                            |--Main （照片名字）
                            |--test1(测试图片，官方)
                            |--test(自造测试)
                            |--train(训练图集)

                |--JPEGImages--(本来以为存放了所有图片但是似乎名字相同被覆盖了，作用很迷)
                |--labels(官方初始标签数据)
                            

