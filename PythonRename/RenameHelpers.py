import sys
import glob
import argparse

def GlobFilenames( filenamelist ):
    newlist = [] #create a blank list to add to
    #iterate through each filename passed in
    for name in filenamelist:
        newlist.append(glob.glob(name)) #glob the name so we can automatically get patterns
    return newlist

def GetNewFilename( filename, args ):
    #string operations are done in the order they were entered
    # -l -n File## would lowercase the whole filename then do the countstring op
    for argument in sys.argv:
        if argument == '-l':
            #lowercase the filename
            filename = ToLower(filename)
        elif argument == '-u':
            #uppercase the filename
            filename = ToUpper(filename)
        elif argument == '-t':
            #trim characters from the filename
            filename = TrimFilename(filename, args)
        elif argument == '-r':
            #replace strings in the filename
            filename = ReplaceStrings(filename, args)
        elif argument == '-n':
            #rename file in sequence using countstring with #'s incrementing
            filename = CountStrings(filename, args)
        else:
            #no action is taking, this argument likely pairs with a command
            filename = filename
    return filename
    

def ToLower( string ):
    return str.lower(string)
    
def ToUpper( string):
    return str.upper(string)
    
def TrimFilename(newFilename, args):
    if args.trim > 0:
        newFilename = newFilename[args.trim:]
    else:
        newFilename = newFilename[:args.trim]
    return newFilename

def ReplaceStrings(newFilename, args):
    newFilename = '2'

def CountStrings(newFilename, args):
    newFilename = '3'

