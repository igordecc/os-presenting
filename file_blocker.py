import os
from typing import Mapping
import time
import sys

t = time.localtime()
local_time_stamp =  lambda : f"{t.tm_mday}.{t.tm_mon}.{t.tm_year} {t.tm_hour}:{t.tm_min}:{t.tm_sec} :"

# Windows functionality only (sorry)


def realtime_file_watcher(read_file):
    # For Windows: Get-Content filename.txt -wait
    # For Unix: tail -f filename.txt
    # in python:
    with open(read_file, "rb") as file:
        print(f"Blocking file: {read_file}")
        while True:
            where = file.tell()
            try:
                line = file.readline()
            except:
                line = None
            if not line:
                time.sleep(1)
                file.seek(where)
            else:
                print("Changed " + os.path.basename(READ_FILE) + " at time " + local_time_stamp()) # already has newline
                print(line)
                

if __name__=="__main__":
    READ_FILE = "D:\\dst\\readfile.txt"
    if sys.argv[1]:
        READ_FILE = sys.argv[1]
    realtime_file_watcher(READ_FILE)
