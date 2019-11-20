# Usage: python.exe clipboard.py save <keyword> - Saves clipboard to keyword.
#        python.exe clipboard.py delete <keyword> - delete keyword.
#        python.exe clipboard.py <keyword> - Loads keyword to clipboard.
#        python.exe clipboard.py delete - delete all keywords.
#        python.exe clipboard.py list - Loads all keywords to clipboard.

# python.exe arg[0] arg[1] arg[2]
# arg[0] name of the script
# arg[1] save,delete, <key>
# arg[2] <key>

import shelve, pyperclip, sys
# Shelve is a powerful Python module for object persistence. When you shelve an object, you must assign a KEY by
# which the object value is known. In this way, the shelve file becomes a DATABASE  of STORED values, any of which can
# be accessed at any time.

# pyperclip - module for copying and pasting text to the clipboard

mbc_shelve = shelve.open('mbc')

# sys.argv  - commandline arguments
# sys.argv.lower()  makes lowercase SaVe -> save

if len(sys.argv) == 3 :
    if sys.argv[1].lower() == 'save':
        mbc_shelve[sys.argv[2]] = pyperclip.paste()
        # paste content in clipboard and store in shelve
    if sys.argv[1].lower() == 'delete' and sys.argv[2] in mbc_shelve:
        # arg delete and arg exist in shelve
        del mbc_shelve[sys.argv[2]]
if len(sys.argv) == 2 :
    if sys.argv[1].lower() == 'delete':
        for key in mbc_shelve :
            del mbc_shelve[key]
        # get a key by iteration and del all with key
    if sys.argv[1].lower() == 'list':
        my_keys = list(mbc_shelve.keys())
        my_keys.sort()
        pyperclip.copy(str(my_keys))
    elif sys.argv[1] in mbc_shelve:
        pyperclip.copy(mbc_shelve[sys.argv[1]])
        # loads (copy to) keyword to clipboard

mbc_shelve.close()