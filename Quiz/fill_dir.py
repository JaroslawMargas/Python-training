import os


def print_directory_contents(s_path):
    print(s_path)
    for sChild in os.listdir(s_path):
        # sChild is filename
        sChildPath = os.path.join(s_path, sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)


path = os.getcwd()
print_directory_contents(path)

# D:\Python\tietopythontraining-basic\Quiz

# D:\Python\tietopythontraining-basic\Quiz\example.py
# D:\Python\tietopythontraining-basic\Quiz\fill_dir.py
