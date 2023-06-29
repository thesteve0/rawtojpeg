import rawpy

from pathlib import Path
from PIL import Image
from ExifWorker import update_exif, get_exif

export_location = 'C:/Users/steve/tmp/photo-rename-tester/processed-images/'
search_path = 'C:/Users/steve/tmp\photo-rename-tester/orig-images'
# search_path = 'P:/'
top_path = Path(search_path)

fine_extensions = {'.JPG', '.jpg', '.jpeg', '.tif', '.TIF'}
# We are not doing , '.png', '.bmp', '.PNG'}
raw_extensions = {'.RW2', '.ORF', '.NEF', '.ARW'}





i = 1
manufacturers = {}
for path in top_path.rglob('*.*'):
    file_extension = path.suffix
    if file_extension in fine_extensions:
        try:
            im = Image.open(path)
            im_exif = update_exif(im, path)
            #
            # height = im.size[1]   #height
            # width = im.size[0]  #width
            # if height > 16000 or width > 16000:
            #    print("we have an image bigger than 16k in one dimensions")
            # The saved file name needs to be unique since they are all getting dumped in 1 directory
            #            im.save(export_location + filename, exif=im_exif)

            if i % 1000 == 0:
                print("Another thousand: " + str(i) + "manu: " + str(manufacturers))

        except Exception as e:
            print("threw an exception: " + str(e))
        im.close()
        i += 1

    # elif file_extension in raw_extensions:
    #     continue
        # rawimg = rawpy.imread("C:/Users/steve/tmp\photo-rename-tester/orig-images/2017/DSC_0001.NEF")
        # print(rawimg.sizes)
        # rawimg.close()

        #print("this has to be converted to JPG, add the metadata, and then moved over")
print(str(manufacturers))

# basic works - need to export to JPG, rename the file, and then walk the tree.
# Also need to detect if there are two files with the same name but one is .jpg and the other is raw. If so then just move the jpg but tag
# both with the same tags eventually
#
# Maybe we don't rename the file, maybe we actually just embed the path in the JPG exif data (or header or something)