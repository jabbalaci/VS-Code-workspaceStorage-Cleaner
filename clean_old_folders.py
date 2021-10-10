#!/usr/bin/env python3

"""
This script will remove VS Code workspaceStorage folders
that were last modified a long time ago.

Probably they are not needed and they just occupy your disk space.

Usage
-----

* put this script in the folder `~/.config/Code/User/workspaceStorage` (under Linux)
* modify LIMIT as you wish
* leave DRY_RUN = True and execute it
* If the output is OK and you want to get rid of the old folders,
  set DRY_RUN = False and re-execute the script. This time the old
  folders will be deleted.

Author: Laszlo Szathmary, alias Jabba Laci (jabba.laci@gmail.com), 2021
GitHub: https://github.com/jabbalaci
"""

import datetime
import os
import shutil
from pathlib import Path

BYTE = 1
KB = 1024 * BYTE
MB = 1024 * KB
GB = 1024 * MB
TB = 1024 * GB

LIMIT = 60    # in days (folders older than this will be deleted)
FNAME = "workspace.json"

DRY_RUN = True    # no folders will be deleted
# DRY_RUN = False    # Old folders will be DELETED!


def sizeof_fmt(size_in_bytes: int) -> str:
    """
    Convert file size (in bytes) to human readable format.
    """
    value: float = size_in_bytes
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if value < 1024.0:
            return "{0:.2f} {1}".format(value, x)
        #
        value /= 1024.0
    #
    return "?"    # for mypy, otherwise we never get here


def folder_size_in_bytes(dir_name: str) -> int:
    root_directory = Path(dir_name)
    return sum(f.stat().st_size for f in root_directory.glob('**/*') if f.is_file())


def main() -> None:
    folders: list[str] = [entry for entry in os.listdir(".") if os.path.isdir(entry)]
    now = datetime.datetime.now()
    # days = []
    total_size_in_bytes = 0

    for folder in folders:
        fname = Path(f"{folder}/{FNAME}")
        if not fname.is_file():
            print("Warning: {fname} doesn't exist")
            continue
        # else
        mtime = datetime.datetime.fromtimestamp(fname.stat().st_mtime)
        diff = (now - mtime).days
        if diff >= LIMIT:
            size_in_bytes = folder_size_in_bytes(folder)
            print(f"{folder}: modified {diff} days ago; size: {sizeof_fmt(size_in_bytes)}")
            total_size_in_bytes += size_in_bytes
            if not DRY_RUN:
                shutil.rmtree(folder)
                if not os.path.exists(folder):
                    print(f"{folder}: deleted")
                #
            #
        #
    #
    if total_size_in_bytes > 0:
        print()
        print(f"Total size of these folders: {sizeof_fmt(total_size_in_bytes)}")

##############################################################################

if __name__ == "__main__":
    main()
