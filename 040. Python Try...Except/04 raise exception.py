x = -1

if x < 0:
  try:
    raise Exception("Sorry, no numbers below zero")
  except Exception as e:
    print("Caught expected exception:", e)

x = "hello"

if not type(x) is int:
  try:
    raise TypeError("Only integers are allowed")
  except TypeError as e:
    print("Caught expected type error:", e)
