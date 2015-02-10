#Rename
#Main Program Flow Code Here.....
import sys
import argparse

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
    
    print( 'all args: ', sys.argv )
    print( 'argparse: ', args )
    print( 'args.verbose = ', args.verbose )
    print( 'args.interactive = ', args.interactive )
    print( 'args.lowercase = ', args.lowercase )
    print( 'args.uppercase = ', args.uppercase )
    print( 'args.trim = ', args.trim )
    print( 'args.replace = ', args.replace )
    print( 'args.countstring = ', args.countstring )
    print( 'filenames = ', args.filenames )
    
    
    return

















if (__name__ == '__main__'):
    Process()

