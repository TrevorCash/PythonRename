"""############################################################################
# File: Rename.py
#
# Authors: Dylan Geyer, Trevor Cash
#
# Class: Programming Languages (CSC 461)
#
# Instructor: Dr. Weiss
#
# Description:  This file acts as the main() for our pyton file renaming prog.
#               This file handles the command-line argument parsing and then
#               calls its helper functions to do string manipulations on each
#               filename. Once a filename has been processed it is renamed.
#
# Command-Line Arguments: -v - Verbose, prints previous and new filenames
#                         -i - Interactive, aks user for permission each file
#                         -h - Help, displays an in depth argument explanation
#                         -l - Lowercase, convert filenames to lowercase
#                         -u - Uppercase, convert filenames to uppercase
#                         -t n - Trim, cut off characters from front/back
#                                of a filename.
#                         -r "str1" "str2" - Replace, replaces a pattern in
#                             str1 with a pattern in str2
#                         -n "CountString#" - Countstring, change all the
#                             filenames to "CountString#" but number them in
#                             increasing order for every name changed
#
# Date: 2/12/14
#
############################################################################"""
import sys
import argparse
import glob
import os
import os.path
from RenameHelpers import *

CountIncrementer = 0


"""############################################################################
# Name: Process
#
# Description:  Acts as main() and parses all of the command line arguments.
#               Calls a GetNewFilename function to figure out the new filename
#               based on the command line arguments it parsed earlier. It then
#               either asks the user if its ok to write the file or does it
#               without asking (depending on passed in arguments).
#
# Parameters: none
#
# Returns:    none
############################################################################"""
def Process():
    """Acts as the main function and handles command-line argument parsing, file re-naming."""
    parser = argparse.ArgumentParser("-h for help")

    parser.add_argument('-v', '--verbose', action = "store_true", help = "Verbose Output")
    parser.add_argument('-i', '--interactive', action = "store_true", help = "Interactive Mode confirms changes to each file")
    parser.add_argument('-l', '--lowercase', action = "store_true", help = "Set filename to lowercase")
    parser.add_argument('-u', '--uppercase', action = "store_true", help = "Set filename to uppercase")
    parser.add_argument('-t', '--trim', type = int, metavar = 'N', help = "n > 0: remove n characters from start of filename \n n < 0: remove n characters from end of filename")
    parser.add_argument('-r', '--replace', metavar = ('str1', 'str2'), type = str, nargs = 2, help = "replace all instances of str1 with str2")
    parser.add_argument('-n', '--countstring', type = str, metavar = "countstring#", help = "#'s in countstring become numbers; e.g., ## becomes 01, 02, ...")

    parser.add_argument('filenames', metavar="filenames", type = str, nargs = '*', help = "filenames to modify")



    args = parser.parse_args();

    sys.argv = sys.argv[1:len(sys.argv)] #chop off first argument, nobody cares about the filename

    #now put the list of all the filenames the user wanted into args.filenames

    #if the user did not supply any file names, assume he want to alter all in the current dir
    if len(args.filenames) <= 0:
        for potentialFile in os.listdir(os.getcwd()):
            if os.path.isfile(potentialFile):
                args.filenames += [potentialFile]
    else:
               args.filenames += GlobFilenames(args.filenames)


    #remove duplicate filenames in the list
    args.filenames = list(set(args.filenames))

    #iterate through each filename and perform the operations in order
    for fname in args.filenames:
        #make sure file exists before changing its name
        if os.path.isfile(fname) == False:
            continue

        newFilename = GetNewFilename(fname, args) #cast fname to str because its a list of 1 string

        if args.interactive == True:
            #ask the user if they really want to change the file
            message = 'Would you like to change \'' + fname + '\' to \'' + newFilename + '\'? [y/n]'
            print(message, end = '')
            if(input() == 'y'):
                #rename the file
                os.rename(fname, newFilename)
                Rename.CountIncrementer = Rename.CountIncrementer + 1
            else:
                #do not rename the file or do the verbose statement
                continue
        else:
             #rename the file
             os.rename(fname, newFilename)
             Rename.CountIncrementer = Rename.CountIncrementer + 1

        if args.verbose == True:
            #print out the previous and final filenames
            message = '\'' + fname + '\' -> \'' + newFilename + '\''
            print(message)

    return

















if (__name__ == '__main__'):
    Process()

