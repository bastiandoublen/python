def myfunc():
  x = 300
  print(x)

myfunc()

def myouterfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myouterfunc()
