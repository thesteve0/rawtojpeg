import rawpy

from pathlib import Path
from PIL import Image

import ExifWorker
from ExifWorker import update_exif, get_exif

# This needs the trailing slash
export_location = 'D:/pictures-for-AI/processed/'
search_path = 'D:/pictures-for-AI/to-process/'
# search_path = 'P:/'
top_path = Path(search_path)

fine_extensions = {'.JPG', '.jpg', '.jpeg', '.tif', '.TIF'}
# We are not doing , '.png', '.bmp', '.PNG'}
raw_extensions = {'.RW2', '.ORF', '.NEF', '.ARW'}


i = 1
for path in top_path.rglob('*.*'):
    file_extension = path.suffix
    if file_extension in fine_extensions:
        try:
            im = Image.open(path)
            # Add the exif metadata
            im_exif = update_exif(im, path)

            # check the size and fix if needed
            height = im.height
            width = im.width
            if height > 15000:
                ratio = 15000.0/height
                new_height = height * ratio
                new_width = width * ratio
                im = im.resize((new_width, new_height))
                width = new_width
                height = new_height

            # we need this as separate because even after resizing for height, the width might still be too big
            if width > 15000:
                ratio = 15000.0/width
                new_height = width * ratio
                new_width = height * ratio
                im = im.resize((new_width, new_height))

            # rename and save to the output location
            # TODO File names are not saving correctly
            new_filename = str(path).strip(search_path).replace('\\', '_')
            im.save(export_location +  new_filename, exif=im_exif)
            im.close

        except Exception as e:
            print("threw an exception: " + str(e))
        im.close()
        i += 1

    elif file_extension in raw_extensions:

        rawimg = rawpy.imread(str(path))
        rgb_array = rawimg.postprocess(use_camera_wb=True)
        pre_jpg_img = Image.fromarray(rgb_array)

        pre_jpg_img_exif = ExifWorker.raw_exif_to_jpeg(raw_file_string=path, jpg=pre_jpg_img)
        #print("hello")
        rawimg.close()
        new_filename = str(path).strip(search_path).replace('\\', '_')

        # TODO File names are not saving correctly
        pre_jpg_img.save(export_location +  new_filename + '.jpg', exif=pre_jpg_img_exif)
        pre_jpg_img.close()
        #.save('image.jpg', quality=90, optimize=True)
        # print(rawimg.sizes)
        # rawimg.close()

        #print("this has to be converted to JPG, add the metadata, and then moved over")
    if i % 1000 == 0:
        print("Another thousand: " + str(i))


print("Done and processed: " + str(i))