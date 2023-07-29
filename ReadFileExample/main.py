import os
file = "list.txt"
path = os.getcwd() + '/' + file
f = open(path, "r")
buffer= []
for line in f:
    if line != "\n":
        buffer.append(line.replace("\n", ""))
print(buffer)