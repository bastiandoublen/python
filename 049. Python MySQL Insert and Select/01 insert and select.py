sql_insert = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
sql_select = "SELECT * FROM customers WHERE address = 'Parkway 38'"

print("Insert Template:", sql_insert)
print("Insert Values:", val)
print("Select Query:", sql_select)
