import sys

try:
    if len(sys.argv) > 0:
        argument = sys.argv[1]
        print("You entered argument {}".format(argument))
except:
        print("Error: You forgot to enter an argument!")