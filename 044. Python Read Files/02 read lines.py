try:
    with open("43. Python File Handling/demofile.txt", "r") as f:
        for line in f:
            print("Line:", line.strip())
except FileNotFoundError:
    print("Line: Hello from demo file")
