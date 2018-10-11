#reading from the keyboard

#printing to the screen

#reading from a file
f = open("file.txt", "r+")

for line in f.readlines():
    print("Hello!")

#writing to a file

f.close();
f = open("file.txt", "w")

f.write("Sup!")
#closing a file
f.close()
