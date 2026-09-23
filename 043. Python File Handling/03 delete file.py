import os

with open("demofile_to_delete.txt", "w") as f:
  f.write("Temporary file content")

if os.path.exists("demofile_to_delete.txt"):
  os.remove("demofile_to_delete.txt")
  print("File deleted successfully.")
else:
  print("The file does not exist")
