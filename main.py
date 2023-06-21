import rawpy
from pathlib import Path
import PIL


export_location = ''
search_path = 'C:/Users/steve/tmp\photo-rename-tester/orig-images'
#search_path = 'P:/'
top_path = Path(search_path)

fine_extensions = {'.JPG', '.jpg', '.jpeg', '.png', '.tif', '.bmp', '.TIF', '.PNG', '.gif'}
raw_extensions = {'.RW2', '.ORF', '.NEF', '.ARW'}

for path in top_path.rglob('*.*'):
    if path.suffix in fine_extensions:
        print("We can just add the metadata and move it over")
    elif path.suffix in raw_extensions:
        # rawimg = rawpy.imread("C:/Users/steve/tmp\photo-rename-tester/orig-images/2017/DSC_0001.NEF")
        # print(rawimg.sizes)
        # rawimg.close()

        print("this has to be converted to JPG, add the metadata, and then moved over")


# basic works - need to export to JPG, rename the file, and then walk the tree.
# Also need to detect if there are two files with the same name but one is .jpg and the other is raw. If so then just move the jpg but tag
# both with the same tags eventually
#
# Maybe we don't rename the file, maybe we actually just embed the path in the JPG exif data (or header or something)