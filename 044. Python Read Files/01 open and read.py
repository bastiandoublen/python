try:
    with open("43. Python File Handling/demofile.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Sample content: Hello! Welcome to W3Schools Python Tutorial.")
