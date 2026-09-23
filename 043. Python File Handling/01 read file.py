f = open("demofile.txt", "r")
print(f.read())
f.close()

f = open("demofile.txt", "r")
print("First 5 chars:", f.read(5))
f.close()

f = open("demofile.txt", "r")
print("Line 1:", f.readline(), end="")
print("Line 2:", f.readline(), end="")
f.close()
