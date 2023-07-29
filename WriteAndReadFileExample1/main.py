names = ["Bill Gates", "Elon Musk", "Mark zuckerberg"]
File_write = open("names.txt", "w")
File_read = open("names.txt", "r")

for name in names:
    File_write.write(name + '\n')
File_write.close()

for line in File_read:
    print(line)


