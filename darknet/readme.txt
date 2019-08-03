测试命令： 
./darknet detector test  cfg/my.data cfg/yolov3-my.cfg backup/yolov3-my.backup


训练命令：
./darknet detector train  cfg/my.data cfg/yolov3-my.cfg backup/yolov3-my.backup


计算recall：
./darknet detector recall  cfg/my.data cfg/yolov3-my.cfg backup/yolov3-my.backup

生成检测结果：
./darknet detector valid  cfg/my.data cfg/yolov3-my.cfg backup/yolov3-my.backup



以上命令均可以指定-thresh -gpu
=============================主要函数和各个文件说明=====================================

命令行命令的直接接口是example/detector.c函数，修改对应名字的函数可以直接修改命令的结果
cfg/my.data里是命令所用的默认参数的定义处，修改这里的配置可以改变训练测试集
train_, test_, 系列的txt文件应该存放自己训练测试图片的路径,val_.txt是验证集图片路径

通过scripts/my_label.py从图片集生成合适的路径文件
通过run_xml.sh得到xml的结果，保存在results/下
