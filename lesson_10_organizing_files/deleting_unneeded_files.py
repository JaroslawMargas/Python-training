# list files if size more then byte_range

import os

byte_range = 1024
root_source = "D:\\"


def format_bytes(size_in_byte) :
    # 2**10 = 1024
    power = 2 ** 10
    n = 0
    power_labels = {0 : '', 1 : 'kilo', 2 : 'mega', 3 : 'giga', 4 : 'tera'}
    while size_in_byte > power :
        size_in_byte = size_in_byte / power
        n += 1
    return size_in_byte, power_labels[n] + 'bytes'


for folder_name, sub_folders, file_names, in os.walk(root_source) :
    for filename in file_names :
        size = os.path.getsize(os.path.join(folder_name, filename))
        if size > byte_range :
            convert_size, format_byte = format_bytes(size)
            print("FILE: " + folder_name + " : " + filename)
            # truncate float to 3
            print(str('%.3f' % convert_size) + " " + format_byte)
