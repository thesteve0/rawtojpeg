

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
        if file_extension in raw_extensions:
            for possible_jpeg in path.parent.rglob('*.*'):
                    if possible_jpeg.suffix in fine_extensions:
                        # Grab the first 5 character from each file name and compare them
                        # if they are the same then delete the "same" not RAW file
                        if path.name[0:5] == possible_jpeg.name[0:5]:
                            print("Raw: " + str(path) + " : would move : " +str(possible_jpeg))


# Need to decide how I am going to clear this up. Do I delete all teh jpgs or do I just move them somewhere else?