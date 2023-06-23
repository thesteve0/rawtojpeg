from PIL import Image

# PILLOW_TAGS = [
#     315,     # Artist Name
#     33432,   # Copyright Message
#     40094,   # XPKeywords
#     41728    # FileSource
# ]
#
# TAG_VALUES = [
#     "Steven Pousty",  # 0 My Name
#     "Copyright 2023 Steven Pousty. All Rights Reserved.", # 1 My copyright
#     "",  # 2 Need to fill in the keywords
#     ""   # 3 Need to add the original path
# ]

def update_exif(self, image, path):
    im_exif = image.getexif()
    if im_exif is None:
        print("blah")
        # No exif so we need to make a new one
    im_exif[256] = image.size[1]   #height
    im_exif[257]= image.size[0]  #width
    if height > 16000 or width > 16000:
        print("we have an image bigger than 16k in one dimensions")
    im_exif[315] = "Steven Pousty"
    im_exif[33432] = "Copyright 2023 Steven Pousty. All Rights Reserved."
    im_exif[41728] = str(path)
    im_exif[40094] = ""

    return im_exif