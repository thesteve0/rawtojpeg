from PIL import Image


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
def update_exif(self, image, path, has_duplicate):
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


def get_exif(image):
    im_exif = image.getexif()
    return im_exif[271]
    print("hello")
