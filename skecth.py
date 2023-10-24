#library numpy -> install numpy
#library imageio -> install imageio
#library scipy -> install scipy
#library opencv -> install opencv-python
#kita pakai library image yang kemarin (pip isntall image)
# siapkan 1 gambar di folder yg sama untuk diconvert menjadi sketsa pensil

import numpy as np
import imageio
import scipy.ndimage
import cv2

img = "makima 2.jpg" #nama file outputnya

def rgb2gray(rgb):
        return np.dot(rgb[...,:3],[0.2989,0.5870,0.1140])
#formula untuk convert img -> grayscale // pakai kode warna matlab

def dodge(front,back):
            final_sketch = front*255/(255-back)
            # kalau gambarnya lebih besar dari 255 bit/px maka akan diconvert jadi 255
            final_sketch[final_sketch>255]=255
            final_sketch[back==255]=255
            return final_sketch.astype('uint8')

#untuk read gambar yang dipilih (code 14)
ss= imageio.imread(img) #untuk read gambar yang dipilih diawal tadi
gray = rgb2gray(ss) # untuk convert gambar jadi blcak and white

i = 255-gray

#untuk memberi efek blur
blur = scipy.ndimage.filters.gaussian_filter(i, sigma=15)
#sigma=15 adalah intensitas blurnya & black white tadi
r = dodge (blur,gray)
# untuk convert gambarnya (dengan meengaplikasikan blur & black & white tadi) 

cv2.imwrite("sketsas.jpg", r ) 
#untuk menghasil output gambar 
# run > start debugging