import os    # Import os library
import shutil    # Import shutil library

def arrange_files(directory):    # arrange_files function
    
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]    # List all files in directory
    
    for f in files:    # iterate over the files in directory
        file_extension = os.path.splitext(f)[1]    # split the file name and extension
        folder_path = os.path.join(directory, file_extension[1:].upper() + "_Files")    # generate path of folder where file needs to be moved
        
        
        if not os.path.exists(folder_path):    # check if folder path exists or not
            os.makedirs(folder_path)    # create directories to the path
        
        original_file_path = os.path.join(directory, f)    # generate path of file to be moved
        new_file_path = os.path.join(folder_path, f)    # generate path of new location where file needs to be moved
        shutil.move(original_file_path, new_file_path)    # move the file from original location to new location
    
    print("Success!")    # print message on console


dir_to_organize = "/root/foo/bar"    # initialize variable with path of directory
arrange_files(dir_to_organize)    # call arrange_files function
