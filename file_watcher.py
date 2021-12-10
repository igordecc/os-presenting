import os
from typing import Mapping

# Windows functionality only (sorry)


def realtime_file_watcher(read_file):
    # For Windows: Get-Content filename.txt -wait
    # For Unix: tail -f filename.txt
    # in python:
    import time

    with open(read_file, "rb") as file:
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
                t = time.localtime()
                print("Changed " + os.path.basename(READ_FILE) + " at time " + f"{t.tm_mday}.{t.tm_mon}.{t.tm_year} {t.tm_hour}:{t.tm_min}:{t.tm_sec} :" ) # already has newline
                print(line)
                

if __name__=="__main__":
    READ_FILE = "D:\\dst\\readfile.txt"
    realtime_file_watcher(READ_FILE)
