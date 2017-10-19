# -*- coding: utf-8 -*-

#解压train-images.idx3-ubyte的60000张图片到test1目录下，test1必须先被创建，MNIST数据好像不断更新，我解压了60000个图片，之前好像有人说是55000
from PIL import Image
import struct
#import PIL

def read_image(filename):
  f = open(filename, 'rb')
  index = 0
  buf = f.read()
  f.close()
  magic, images, rows, columns = struct.unpack_from('>IIII' , buf , index)
  index += struct.calcsize('>IIII')
  for i in range(images):
  #for i in xrange(2000):
    image = Image.new('L', (columns, rows))
    for x in range(rows):
      for y in range(columns):
        image.putpixel((y, x), int(struct.unpack_from('>B', buf, index)[0]))
        index += struct.calcsize('>B')
    print('save ' + str(i) + 'image')
    image.save('test1/' + str(i) + '.png')
def read_label(filename, saveFilename):
  f = open(filename, 'rb')
  index = 0
  buf = f.read()
  f.close()
  magic, labels = struct.unpack_from('>II' , buf , index)
  index += struct.calcsize('>II')
  labelArr = [0] * labels
  #labelArr = [0] * 2000
  for x in range(labels):
  #for x in xrange(2000):
    labelArr[x] = int(struct.unpack_from('>B', buf, index)[0])
    index += struct.calcsize('>B')
  save = open(saveFilename, 'w')
  save.write(','.join(map(lambda x: str(x), labelArr)))
  save.write('\n')
  save.close()
  print('save labels success')


if __name__ == '__main__':
  read_image('train-images.idx3-ubyte')
  read_label('train-labels.idx1-ubyte', 'test1/label.txt') 
