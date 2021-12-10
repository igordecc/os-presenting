# This is script presenting functionality of os python module

import os

# Windows functionality only (sorry)

WRITE_FILE = "D:\\src\\writefile.txt" 
READ_FILE = "D:\\dst\\readfile.txt"

def print_hi():
    print("os.name: " + str(os.name))


def throw_error():
    print(os.error())
    print(os.error("aaaaaaa",   ))
    print(os.error("aaaaaaa", "asdfasdf",   ))
    print(os.error("aaaaaaa", "asdfasdf", "sdfsdf",  ))
    print(os.error("aaaaaaa", "asdfasdf", "sdfsdf", "fffff" ))
    print(os.error("aaaaaaa", "asdfasdf", "sdfsdf", "fffff", "ddddd" ))
    print(os.error("aaaaaaa", "asdfasdf", "sdfsdf", "fffff", "ddddd", "rrrr", ))
    print(os.error("aaaaaaa", "asdfasdf", "sdfsdf", "fffff", "ddddd", "rrrr", "bbb"))

def change_dir():
    print(os.chdir("C:\\Users"))
    print(os.getcwd())

def link_a_file():
    # file will be basicaly the same one, changing accordingly to one another
    os.link(WRITE_FILE, READ_FILE)

def realtime_file_monitor():
    # For Windows: Get-Content filename.txt -wait
    # For Unix: tail -f filename.txt
    # in python:
    import time

    with open(READ_FILE) as file:
        while True:
            where = file.tell()
            line = file.readline()
            if not line:
                time.sleep(1)
                file.seek(where)
            else:
                print(line) # already has newline
    ...

def open_file_descriptor_and_then_file():
    # os.O_RDONLY
    # os.O_WRONLY
    # os.O_RDWR
    # os.O_APPEND
    # os.O_CREAT
    # os.O_EXCL
    # os.O_TRUNC
    fd = os.open(READ_FILE, os.O_RDONLY)
    file = os.fdopen(fd)
    d_encoding = os.device_encoding(fd)
    print(fd)
    print(file)
    print(d_encoding) # None cause not in terminal
    # TODO create virtual (!!!) terminal with pty to get it

if __name__ == '__main__':
    print_hi()
    throw_error()
    change_dir()
    print(os.listdir())
    # realtime_file_monitor()
    open_file_descriptor_and_then_file()

