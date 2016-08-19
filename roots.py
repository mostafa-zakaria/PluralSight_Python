import sys

def sqrt(x):
    '''derives sqrt using Heron of Alexandria's method'''
    guess = x
    i = 0
    while guess * guess != x and  i < 20:
        guess = (guess + x / guess)/2.0
        i += 1
    return(guess)


def main(num):
    try:
        print(sqrt(int(num))) #convert argument to integer before attempting to derive sqrt
    except (TypeError, ValueError, ZeroDivisionError) as err:
        print("Cannnot Compute sqrt of value> {}".format(num, str(err), file=sys.stderr))


if __name__ == '__main__':
        main(sys.argv[1]) #Needs to be [1] because [0] refers to script name
