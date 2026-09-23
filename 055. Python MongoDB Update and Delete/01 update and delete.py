my_query = {"address": "Valley 345"}
new_values = {"$set": {"address": "Canyon 123"}}
delete_query = {"address": "Mountain 21"}

print("Query to update:", my_query, "->", new_values)
print("Query to delete:", delete_query)
