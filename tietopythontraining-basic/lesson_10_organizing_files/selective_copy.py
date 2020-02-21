# this program copy specified files (like txt or jpg) from root folder to destination
# all structure of the sub_folders are created.

import shutil
import os

root_source = "delicious"
root_destination = "more_delicious"

# if exist then remove destination folder and all folders/files inside.
if os.path.exists(root_destination):
    shutil.rmtree(root_destination)

# walk through root_source
for folder_name, sub_folders, file_names, in os.walk(root_source) :
    print("THE CURRENT PATH IS: " + folder_name)

    # remove from full path the root name
    current_folders = folder_name.replace(root_source, "")
    print("CURRENT FOLDERS: " + current_folders)

    # create the full destination path name with root_destination and current sub_folders
    destination = root_destination + current_folders

    # create full destination path
    if os.path.exists(destination) :
        print("DESTINATION EXIST")
    else:
        os.makedirs(destination)
        print("DESTINATION FOLDER CREATED")

    for sub_folder in sub_folders:
        print("SUB-FOLDER: " + sub_folder)
    for filename in file_names :
        print("FILE INSIDE SUB-FOLDER: " + folder_name + " : " + filename)

    # if TXT then copy file from root_source+sub_folder to root_destination+sub_folder
        if filename.endswith(".txt") or\
                filename.endswith(".TXT"):
            print("PATH FILE TO COPY: " + os.path.join(folder_name, filename))
            shutil.copy(os.path.join(folder_name, filename), os.path.join(destination))
            print("PATH FILE COPIED: " + os.path.join(destination, filename))
