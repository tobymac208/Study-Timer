## Functions that define how the operating system should handle a folder not existing ##
import os
import os.path
import errno


## Create directories to path if they don't exist ##
# https://stackoverflow.com/questions/23793987/write-file-to-a-directory-that-doesnt-exist #
def mkdir_path(path_to_create):
    try:
        # If the path doesn't exist then create it
        if not (os.path.exists(path_to_create)):
            os.makedirs(path_to_create)
    except OSError as exception:
        if exception.errno != errno.EEXIST and os.path.isdir(path_to_create):
            pass
        else:
            raise


## Safely write to a file, first ensuring the path exists ##
def safe_open_read(path):
    # create the path to the directory
    mkdir_path(os.path.dirname(path))

    # open the file and return it to the caller. make sure to add '+' to create the file, in case something doesn't work
    return open(path, 'a+')
