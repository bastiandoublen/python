create_table_sql = """
CREATE TABLE customers (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  address VARCHAR(255)
);
"""
print("SQL Definition:")
print(create_table_sql.strip())
