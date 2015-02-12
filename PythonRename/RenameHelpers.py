###############################################################################
# File: RenameHelpers.py
#
# Authors: Dylan Geyer, Trevor Cash
#
# Class: Programming Languages (CSC 461)
#
# Instructor: Dr. Weiss
#
# Description:  This file provides helper functions for all of the string
#               manipulations on the filenames. This functionhas file globbing,
#               as well as very basic Regular Expression implementation.
#
# Date: 2/12/15
#
###############################################################################

import sys
import glob
import re
import Rename


###############################################################################
# Name: GlobFilenames
#
# Description:  This function will look at each filename argument passed to the
#               program and send it into the globber to see if we can match it
#               to any other files that are named in the same pattern.
#
# Parameters: filenameList - List of each filename passed in from command line
#
# Returns:  newlist - list of all of the files found by globbing
###############################################################################
def GlobFilenames( filenamelist ):
    """Returns a list of filenames globbed from the few passed in."""
    newlist = [] #create a blank list to add to
    #iterate through each filename passed in
    for name in filenamelist:
        globedNames = glob.glob(name);
        if(len(globedNames) > 0):
            for singleGlob in globedNames:
                newlist.append(singleGlob) #glob the name so we can automatically get patterns

    return newlist

###############################################################################
# Name: GetNewFilename
#
# Description:  This function will determien what the new filename should be
#               depending on which argument flags were passed in. It looks at
#               at the arguments in order so a "-l -u" will set a filename to 
#               lowercase then uppercase. This function is relatively modular
#               as it calls a specific function to handle each different flag
#
# Parameters: filename - single filename to process against all arguments
#                 args - list of all of the command line flags and arguments
#
# Returns:  newFilename - processed filename according to argument flags
###############################################################################
def GetNewFilename( filename, args ):
    """Returns a modified filename based on command line arguments, and their order."""
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

###############################################################################
# Name: ToLower
#
# Description:  Uses the string class function to set all characters to lowercase
#
# Parameters: string - string object to be set to lowercase
#
# Returns:  string - a lowercase version of the string passed in
###############################################################################
def ToLower( string ):
    """Converts a filename to all lowercase, including extension."""
    return str.lower(string)

###############################################################################
# Name: ToUpper
#
# Description:  Uses the string class function to set all characters to uppercase
#
# Parameters: string - string object to be set to uppercase
#
# Returns:  string - an uppercase version of the string passed in
###############################################################################
def ToUpper( string):
    """Converts a filename to all uppercase, including extension."""
    return str.upper(string)

###############################################################################
# Name: TrimFilename
#
# Description:  This function will chop characters off the front/back of a
#               filename depending on the number passed in with the -t flag.
#               a positive number trims characters from front of filename while
#               a negative number trims characters from end of the filename.
#
# Parameters: newFilename - the original unprocessed filename
#                    args - contains all command line arguments (-t n)
#
# Returns:  newFilename - final trimmed version of the filename
###############################################################################
def TrimFilename(newFilename, args):
    """Removes characters from start/end of a filename."""
    if args.trim > 0:
        newFilename = newFilename[args.trim:]
    else:
        newFilename = newFilename[:args.trim]
    return newFilename

###############################################################################
# Name: ReplaceStrings
#
# Description:  This function uses the RegEx module to replace a pattern in the
#               filename with another pattern.
#
# Parameters: newFilename - unchanged filename to change
#                    args - command line args containing both patterns
#
# Returns:  newFilename - process filename containing replaced patterns
###############################################################################
def ReplaceStrings(newFilename, args):
    """Uses RE sub to replace one pattern in a filename with another."""
    firstArg = args.replace[0]
    secondArg = args.replace[1]

    pattern = firstArg

    newFilename = re.sub(pattern, secondArg, newFilename)

    return newFilename

###############################################################################
# Name: CountStrings
#
# Description:  Uses the RegEx module to replace all '#' characters with the
#               incrementing count. The count is stored in Rename.py so that
#               it can only be incremented when a filename write occurs and
#               the number is used. Im not sure this function works properly
#               because it will turn '##' into '1' instead of '01' but it
#               seems good enough.
#
# Parameters: newFilename - unchanged filename to change
#                    args - command line args containing the CountString with '#'s
#
# Returns:  string - processed filename with an incremented #
###############################################################################
def CountStrings(newFilename, args):
    """Uses RE sub to replace '#' with an increasing counter."""
    Cstring = args.countstring
    #dont make any changes if there are no #'s to replace in the CountString
    if re.search(r'#+') == False:
        print('Improperly formatted CountString (No \'#\' characters)')
        return newFilename
        
    #replace how every many '#' appear in a row with the increment number
    newFilename = re.sub(r'#+', str(Rename.CountIncrementer), Cstring)
    return newFilename

