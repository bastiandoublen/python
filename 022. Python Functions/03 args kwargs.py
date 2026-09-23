def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

def my_function_kwargs(**kid):
  print("His last name is " + kid["lname"])

my_function_kwargs(fname = "Tobias", lname = "Refsnes")
