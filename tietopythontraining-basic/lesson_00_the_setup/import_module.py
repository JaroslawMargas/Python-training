# this module will be imported to "hello_world"
from __future__ import print_function

def function():
    print('Function executed')


if __name__ == '__main__':
    print('This module name is {}'.format(__name__))
    function()
else:
    print('This module is running from import')
    print('Module name is {}'.format(__name__))
