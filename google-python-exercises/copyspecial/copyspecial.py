#!/usr/bin/env python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
In a given directory, there may be one or more files which are special. A special file
has __wordcharacters__ in its name. The goal is for copyspecial.py to be a utility that
somehow copies these files.
"""
def listSpecials(dir): #Inputs a directory name dir. Outputs a list of special files in dir.
    fullDirFilenames = os.listdir(dir)
    specials = []
    for name in fullDirFilenames:
        if re.search(r'__\w+__',name):
            specials.append(os.path.join(dir, name))
    return specials

def get_special_paths(dir):
    localPaths = listSpecials(dir)
    spec_paths = []
    for i in range(len(localPaths)):
        spec_paths.append(os.path.abspath(localPaths[i]))
    return spec_paths

def copy_to(paths, dir):
    if not os.path.exists(dir):
        os.mkdir(dir)
    for path in paths:
        shutil.copy(path, dir)
    return

#paths is a python list of paths to certain files or directories.
#zippath is the path of the zipfile to be created (I hope)
def zip_to(paths, zippath):
    pathsString = ' '.join(paths)
    cmd = 'zip -j ' + zippath + ' ' + pathsString
    zippedProcess = subprocess.run(cmd,shell=True)
    return

def main():
    args = sys.argv[1:]
    if not args:
        print('usage: [--todir dir][--tozip zipfile] dir [dir ...]')
        sys.exit(1)

    #todir and tozip are either set from command line
    #or left as the empty string.
    #The args array is left just containing the dirs.
   
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print("error: must specify one or more dirs")
        sys.exit(1)
    
    if not todir and not tozip:
        for di in args:
            liPa = get_special_paths(di)
            for pa in liPa:
                print(pa)

    if todir:
        for di in args:
            liPa = get_special_paths(di)
            copy_to(liPa, todir)

    if tozip:
        for di in args:
            liPa = get_special_paths(di)
            zip_to(liPa,tozip)

    return

if __name__ == "__main__":
    main()
