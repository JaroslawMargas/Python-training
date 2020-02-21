# The virus attacked the filesystem of the supercomputer and broke the control of access rights to the files. For
# each file there is a known set of operations which may be applied to it:
#
#     write W,
#     read R,
#     execute X.
#
# The first line contains the number N — the number of files contained in the filesystem. The following N lines
# contain the file names and allowed operations with them, separated by spaces. The next line contains an integer M —
# the number of operations to the files. In the last M lines specify the operations that are requested for files. One
# file can be requested many times.
#
# You need to recover the control over the access rights to the files. For each request your program should return OK
# if the requested operation is valid or Access denied if the operation is invalid.

# class CreateDictionary(dict) :
#
#     # __init__ function
#     def __init__(self) :
#         self.__dict__ = self
#
#         # Function to add key:value
#
#     def add(self, key, value) :
#         self[key] = value


access_dict = {'execute' : 'X',
               'read' : 'R',
               'write' : 'W'}


def create_dict(elements) :
    # dict_obj = CreateDictionary()
    dict_obj = dict()

    for i in range(elements) :
        file_name, *rights, = input("{}: ".format(i + 1)).split()
        # a, *b = input()
        # 1 , [2,3,4,5]
        # dict_obj.add(file_name, rights)

        # second method is
        dict_obj[file_name] = rights

    return dict_obj


while True :
    try :
        N = int(input("the number of files contained in the filesystem ?"))
        file_system = create_dict(N)
        M = int(input("number of files you want to check?"))
        request_files = []
        # or
        # request_files = [''] *M
        break
    except ValueError :
        print("no correct value")

for j in range(M) :
    request_files.append(input("{}: ".format(j + 1)).split())
    # or while request_files = [''] *M
    # request_files[j] = input("{}: ".format(j + 1)).split()

for k in range(M) :
    symbol, filename = request_files[k]
    if access_dict[symbol] in file_system[filename] :
        print("OK")
    else :
        print("Access denied!")
