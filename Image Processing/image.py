import os
from PIL import Image

# 源目录
project_dir = os.path.dirname(os.path.abspath(__file__))
input = os.path.join(project_dir, 'src')

# 输出目录
output = os.path.join(project_dir, 'dest')
def modify():
    # 切换目录
    os.chdir(input)

    # 遍历目录下所有的文件
    for image_name in os.listdir(os.getcwd()):
        print(image_name)
        im = Image.open(os.path.join(input, image_name))    #os.path.join()函数：连接两个或更多的路径名组件

        im = im.convert('L')
        threshold = 230  #阈值
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        # 图片二值化
        im = im.point(table, '1')

        img = im.crop((20, 20, 980, 980))  #(left upper right lower)
        #img = im.crop((1500, 1000, im.size[0] - 1500, im.size[1] - 1000))    #im.size[0]图片的长，im.size[1]图片的宽
        img.thumbnail((128, 128))            #thumbnail()可以指定大小的创建缩略图，改变像素
        img.save(os.path.join(output, image_name))

if __name__ == '__main__':
    modify()