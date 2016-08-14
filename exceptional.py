'''very basic module used to test out exceptions in Pythin'''
import sys #used to output via standard system communication


def convert(s): #function to convert a string into an integer
    try: #traditional "Try-Catch" type block
        return(int(s))
    except (ValueError, TypeError) as err: #catch ValueError and TypeError
        print("Conversion Error: {}".format(str(err), file=sys.stderr)) #Prints the error tp standard communication channel
    raise #raise exception to parent function
