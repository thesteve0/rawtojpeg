import rawpy
from pathlib import Path
from PIL import Image


export_location = 'C:/Users/steve/tmp/photo-rename-tester/processed-images'
search_path = 'C:/Users/steve/tmp\photo-rename-tester/orig-images'
#search_path = 'P:/'
top_path = Path(search_path)

fine_extensions = {'.JPG', '.jpg', '.jpeg', '.png', '.tif', '.bmp', '.TIF', '.PNG'}
raw_extensions = {'.RW2', '.ORF', '.NEF', '.ARW'}

i = 1
for path in top_path.rglob('*.*'):
    file_extension = path.suffix
    if file_extension in fine_extensions:
        try:
            im = Image.open(path)
            exif = im.getexif()

            if exif is None:
                print("blah")
                # No exif so we need to make a new one

            print("copy file to the new location")
            print("call the 'add to exif function")

            if i % 1000 == 0:
                print("Another thousand: " + str(i))

        except:
            print("threw an exception")
        i += 1

    elif file_extension in raw_extensions:
        continue
        # rawimg = rawpy.imread("C:/Users/steve/tmp\photo-rename-tester/orig-images/2017/DSC_0001.NEF")
        # print(rawimg.sizes)
        # rawimg.close()

        #print("this has to be converted to JPG, add the metadata, and then moved over")


# basic works - need to export to JPG, rename the file, and then walk the tree.
# Also need to detect if there are two files with the same name but one is .jpg and the other is raw. If so then just move the jpg but tag
# both with the same tags eventually
#
# Maybe we don't rename the file, maybe we actually just embed the path in the JPG exif data (or header or something)