import rawpy
import PIL


print("hello")

rawimg = rawpy.imread("C:/Users/steve/tmp\photo-rename-tester/orig-images/2017/DSC_0001.NEF")
print(rawimg.sizes)
rawimg.close()