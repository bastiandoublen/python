def my_function(x, /):
  print(x)

my_function(3)

def my_func(*, x):
  print(x)

my_func(x = 3)
