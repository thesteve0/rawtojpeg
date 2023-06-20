import rawpy
import PIL


print("hello")

rawimg = rawpy.imread("C:/Users/steve/tmp\photo-rename-tester/orig-images/2017/DSC_0001.NEF")
print(rawimg.sizes)
rawimg.close()


# basic works - need to export to JPG, rename the file, and then walk the tree.
# Also need to detect if there are two files with the same name but one is .jpg and the other is raw. If so then just move the jpg but tag
# both with the same tags
#
# Maybe we don't rename the file, maybe we actually just embed the path in the JPG exif data (or header or something)