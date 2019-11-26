# this program copy specified files (like txt or jpg) from root folder to destination
# all structure of the sub_folders are created.

import shutil
import os
import argparse
import sys


# root_source = "delicious"
# root_destination = "more_delicious"
# file_type = ".txt"

def get_arg_parse(args=None) :
    parser = argparse.ArgumentParser("Selective copy with argparse")
    parser.add_argument("source", help="provide source forder name")
    parser.add_argument("destination", help="provide destination folder name")
    parser.add_argument("fileType", help="provide file extension ex: .txt")
    args = parser.parse_args(args)

    return args.source, args.destination, args.fileType


def copy_selective(root_source, root_destination, file_type) :
    # if exist then remove destination folder and all folders/files inside.
    if os.path.exists(root_destination) :
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
        else :
            os.makedirs(destination)
            print("DESTINATION FOLDER CREATED")

        for sub_folder in sub_folders :
            print("SUB-FOLDER: " + sub_folder)
        for filename in file_names :
            print("FILE INSIDE SUB-FOLDER: " + folder_name + " : " + filename)

            # if TXT then copy file from root_source+sub_folder to root_destination+sub_folder
            if filename.endswith(file_type) :
                print("PATH FILE TO COPY: " + os.path.join(folder_name, filename))
                shutil.copy(os.path.join(folder_name, filename), os.path.join(destination))
                print("PATH FILE COPIED: " + os.path.join(destination, filename))


# user_args = sys.argv[1:] # get everything after the script name
#
# user_args = sys.argv[1:]
# fun, games = user_args


def main() :
    source, destination, file_type = get_arg_parse(sys.argv[1 :])
    copy_selective(source, destination, file_type)


if __name__ == "__main__" :
    main()

# example usage :
# python selective_copy.py -h
# python selective_copy.py delicious more_delicious .txt