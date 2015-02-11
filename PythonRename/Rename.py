#Rename
#Main Program Flow Code Here.....
import sys
import argparse
import glob
import os
from RenameHelpers import *

#define argument strings
#touples (argstring, numinput args excpected)
ARG_PRINT_HELP = ("-h", 0)
ARG_VERBOSE_OUTPUT = ("-v", 0)
ARG_INTERACTIVE_MODE = ("-i", 0)
ARG_CONV_LOWERCASE = ("-l", 0)
ARG_CONV_UPPERCASE = ("-u", 0)
ARG_TRIM_CHARS = ("-t", 1)
ARG_REPLACE_STRING = ("r", 2)


#define help string
HELP_STRING = """ Rename Utility:\n
                  Authors: Dylan Geyer and Trevor Cash\n
                  Instructor: Dr. Weiss\n
                  Usage:\n


              """


def Process():
    parser = argparse.ArgumentParser("-h for help")
    
    parser.add_argument('-v', '--verbose', action = "store_true", help = "Verbose Output")
    parser.add_argument('-i', '--interactive', action = "store_true", help = "Interactive Mode confirms changes to each file")
    parser.add_argument('-l', '--lowercase', action = "store_true", help = "Set filename to lowercase")
    parser.add_argument('-u', '--uppercase', action = "store_true", help = "Set filename to uppercase")
    parser.add_argument('-t', '--trim', type = int, metavar = 'N', help = "n > 0: remove n characters from start of filename \n n < 0: remove n characters from end of filename")
    parser.add_argument('-r', '--replace', metavar = ('str1', 'str2'), type = str, nargs = 2, help = "replace all instances of str1 with str2")
    parser.add_argument('-n', '--countstring', type = str, metavar = "countstring#", help = "#'s in countstring become numbers; e.g., ## becomes 01, 02, ...")
    
    parser.add_argument('filenames', metavar = 'filenames', type = str, nargs = '+', help = "filenames to modify")
    
    args = parser.parse_args()
    
    sys.argv = sys.argv[1:len(sys.argv)] #chop off first argument, nobody cares about the filename
    
    #now put the list of all the filenames the user wanted into args.filenames
    args.filenames = GlobFilenames(args.filenames)
    
    #iterate through each filename and perform the operations in order
    for fname in args.filenames:
        newFilename = GetNewFilename(str(fname[0]), args) #cast fname to str because its a list of 1 string
        
        if args.interactive == True:
            #ask the user if they really want to change the file
            message = 'Would you like to change \'' + str(fname[0]) + '\' to \'' + newFilename + '\'? [y/n]'
            print(message, end = '')
            if(input() == 'y'):
                #rename the file
                os.rename(str(fname[0]), newFilename)
            else:
                #do not rename the file or do the verbose statement
                continue
        if args.verbose == True:
            #print out the previous and final filenames
            message = '\'' + str(fname[0]) + '\' -> \'' + newFilename + '\''
            print(message)
            
    return


    














if (__name__ == '__main__'):
    Process()

