my_query = {"address": "Parkway 38"}
query_with_regex = {"address": {"$gt": "S"}}

print("Find query:", my_query)
print("Filter query:", query_with_regex)
