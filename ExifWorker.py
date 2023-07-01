import PIL.Image
from PIL import Image
import exiftool

# PILLOW_TAGS = [
#     315,     # Artist Name
#     316,     # Host computer - If there is a JPEG and a RAW file - this points to the JPEG original
#     33432,   # Copyright Message
#     40094,   # XPKeywords
#     41728    # FileSource - if there is both a JPEG and a RAW file, this points to the RAW
# ]
#
# TAG_VALUES = [
#     "Steven Pousty",  # 0 My Name
#     "Copyright 2023 Steven Pousty. All Rights Reserved.", # 1 My copyright
#     "",  # 2 Need to fill in the keywords
#     ""   # 3 Need to add the original path
# ]


# This needs a flag to specify whether there is a JPG and RAW with the same name
def update_exif(image, path):
    im_exif = image.getexif()
    if im_exif is None:
        print("blah")
        # No exif so we need to make a new one
    im_exif[256] = image.size[1]  # height
    im_exif[257] = image.size[0]  # width
    im_exif[315] = "Steven Pousty"
    im_exif[33432] = "Copyright 2023 Steven Pousty. All Rights Reserved."
    im_exif[41728] = str(path)
    im_exif[40094] = ""

    return im_exif

def raw_exif_to_jpeg(raw_file_string, jpg):
    files = [str(raw_file_string)]
    pillow_exif = jpg.getexif()
    pillow_exif[315] = "Steven Pousty"
    pillow_exif[33432] = "Copyright 2023 Steven Pousty. All Rights Reserved."

    pillow_exif[40094] = ""
    try:
        with exiftool.ExifToolHelper() as et:
            raw_exif = et.get_metadata(raw_file_string)
            # I need to copy over just the exif I want to a new Pillow exif object and then
            # attach that to teh JPG
            pillow_exif[41728] = raw_exif[0]['SourceFile']

            pillow_exif[256] = raw_exif[0]['EXIF:ImageHeight']  # height
            pillow_exif[257] = raw_exif[0]['EXIF:ImageWidth'] # width

            pillow_exif[271] = raw_exif[0]['EXIF:Make']
            pillow_exif[272] = raw_exif[0]['EXIF:Model']
            pillow_exif[306] = raw_exif[0]['EXIF:CreateDate']
    except Exception as e:
        print("threw an exception: " + str(e) + " on file: " + str(raw_file_string))

    return pillow_exif

def get_exif(image):
    im_exif = image.getexif()
    return im_exif[271]
    print("hello")
