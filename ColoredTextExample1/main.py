import sys
try:
    from termcolor import colored
except ImportError:
    print('termcolor is not installed, Please install it with pip install termcolor')
    sys.exit(1)

print(colored("This text is red", "red"))
print(colored("This text is green", "green"))
print(colored("This text is blue\n", "blue"))

print(colored("This text is red with green background", "red", "on_green"))
print(colored("This text is green with red background", "green", "on_red"))
print(colored("This text is blue with white background", "blue", "on_white"))