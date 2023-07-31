import _datetime
name = input("What's your name?: ")

if name == "":
    print("You forgot to enter your name!")
else:
    print("Hello {}! The date and time is {} ".format(name, _datetime.datetime.today()))
