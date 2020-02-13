import os

script_dir = os.path.dirname(__file__)
rel_path = 'filename.txt'
abs_file_path = os.path.join(script_dir, rel_path)

for line in reversed(list(open(abs_file_path))):
    print(line.rstrip())