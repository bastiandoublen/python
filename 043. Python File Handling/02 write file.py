f = open("demofile2.txt", "a")
f.write("Now the file has more content!\n")
f.close()

f = open("demofile2.txt", "r")
print(f.read())
f.close()

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!\n")
f.close()
