import os

# This is the shit show we are dealing with
#
# "P:\2012\12\24\DSC_0039_NEF_embedded_1.jpg"
# "P:\2012\12\24\DSC_0039_NEF_embedded_1.jpg.xmp"
# "P:\2012\12\24\DSC_0039_NEF_shotwell.jpg"
# "P:\2012\12\24\DSC_0039_NEF_shotwell.jpg.xmp"
# "P:\2012\12\24\DSC_0039.NEF"
# "P:\2012\12\24\DSC_0039.NEF.xmp"
# "P:\2012\12\24\DSC_0039_NEF_embedded.jpg"
# "P:\2012\12\24\DSC_0039_NEF_embedded.jpg.xmp"

# we just want to keep
# DSC_0039.NEF

fine_extensions = {'.JPG', '.jpg', '.jpeg', '.tif', '.TIF'}
raw_extensions = {'.RW2', '.ORF', '.NEF', '.ARW'}

def look_for_duplicates(directory):
    print("Loop through and remove all the JPGs we have for RAW files")
    for path in directory.rglob('*.*'):
        file_extension = path.suffix

        # We have a raw file, now we need to see if there are jpegs with the same name in the directory
        #if file_extension in raw_extensions:
        if file_extension in fine_extensions:
            for possible_raw in path.parent.rglob('*.*'):
                    if possible_raw.suffix in raw_extensions:
                        # compare everything before the extension
                        # if they are the same then delete the "same" RAW file
                        if path.name[0:-4] == possible_raw.name[0:-4]:
                            # check to see if the names are an exact match - if so delete the raw
                            # if not then delete the JPG
                            os.remove(possible_raw)
                            continue

# Need to decide how I am going to clear this up. Do I delete all teh jpgs or do I just move them somewhere else?