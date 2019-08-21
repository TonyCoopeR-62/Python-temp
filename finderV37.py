#coding: utf8
import stat
import sys
import os
import string
import subprocess

try:
    pattern = input('Input search template:\n')
    commandString = ("Where " + pattern)
    commandOutput = subprocess.getoutput(commandString)
    findResults = str.split(commandOutput, "\n")
    print("Files:")
    print(commandOutput)
    print("================================")
    for file in findResults:
        mode=stat.S_IMODE(os.lstat(file)[stat.ST_MODE])
        print("\nPermissions for file ", file, ":")
        for level in "USR ", "GRP ", "OTH":
            for perm in "R ", "W ", "X ":
               if mode & getattr(stat,"S_I "+perm+level):
                   print (level, " has ", perm, " access")
               else:
                   print (level, " has no ", perm, " access")
except:
    print("Возникла проблема! Проверьте сообщение выше.")