import os
from pathlib import Path
from PIL import Image

from ExifWorker import get_exif

not_doing_extensions = {'.png', '.bmp', '.PNG', '.gif', '.GIF', '.tif', '.TIF'}
fine_extensions = {'.JPG', '.jpg', '.jpeg' }
raw_extensions = {'.RW2', '.ORF', '.NEF', '.ARW'}
camera_only = {'EASTMAN KODAK COMPANY',
               'FUJIFILM',
               'NIKON',
               'Panasonic',
               'Canon',
               'NIKON CORPORATION',
               'Konica Minolta Photo Imaging, Inc.',
               'OLYMPUS CORPORATION    ',
               'Sony',
               'SONY'}

# 602 Files, 8 Folders
# 6.19 GB (6,654,582,784 bytes)


# export_location = 'C:/Users/steve/tmp/photo-rename-tester/processed-images/'
# copy_location = 'C:/Users/steve/tmp/photo-rename-tester/camera_files_only/'
search_path = 'C:/Users/steve/tmp\photo-rename-tester/orig-images'

#search_path = 'D:/pictures_for_AI'

top_path = Path(search_path)

i = 1
for path in top_path.rglob('*.*'):
    file_extension = path.suffix

    # Get rid of the XMP files
    if file_extension == '.xmp':
        os.remove(path)
        continue

    # Get rid of non-JPEG or RAW files
    if file_extension in not_doing_extensions:
        os.remove(path)
        continue

    # Get rid of JPEGs that are not from a dedicated Camera (phone pictures)
    if file_extension in fine_extensions:
        if str(path).find("embedded") > 0 or str(path).find("shotwell") > 0 :
            os.remove(path)
            continue
        try:
            im = Image.open(path)
            exif_make = get_exif(image=im)
            im.close()

            if exif_make not in camera_only:
                os.remove(path)

            if i % 1000 == 0:
                print("Another thousand: " + str(i))

        except Exception as e:
                print("threw an exception: " + str(e) + " on: " + str(path))
                im.close()
                os.remove(path)
        i += 1