sql_where = "SELECT * FROM customers WHERE address LIKE '%way%'"
sql_order = "SELECT * FROM customers ORDER BY name DESC"
sql_limit = "SELECT * FROM customers LIMIT 5 OFFSET 2"

print("WHERE query:", sql_where)
print("ORDER BY query:", sql_order)
print("LIMIT query:", sql_limit)
