import os

with open("delete_me.txt", "w") as f:
    f.write("Temp content")

if os.path.exists("delete_me.txt"):
    os.remove("delete_me.txt")
    print("delete_me.txt successfully removed.")
else:
    print("The file does not exist.")
