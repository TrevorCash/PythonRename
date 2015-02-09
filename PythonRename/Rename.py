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
    #TODO - Temporary shortcut for testing arguments
    sys.argv = ["-h", "-v"]




    #flags for for indicating whether currently in interactive/verbose mode
    verboseOutput = False;
    interactiveMode = False;

    #print out full argument list
    print("All Arguments: ", sys.argv)

    for arg in (sys.argv):
        arg = arg.lower();
        print("current argument process: " + arg);

        if(arg == ARG_PRINT_HELP[0]):
            print(HELP_STRING)



        elif(arg == ARG_VERBOSE_OUTPUT[0]):
            verboseOutput = True;


        elif(arg == ARG_INTERACTIVE_MODE[0]):
            interactiveMode = True;

        elif(arg == ARG_CONV_LOWERCASE[0]):
            Print("TODO");

        elif(arg == ARG_CONV_UPPERCASE[0]):
            Print("TODO");

        elif(arg == ARG_TRIM_CHARS[0]):
            Print("TODO");

        elif(arg == ARG_REPLACE_STRING[0]):
            Print("TODO");


    return

















if (__name__ == '__main__'):
    Process()

