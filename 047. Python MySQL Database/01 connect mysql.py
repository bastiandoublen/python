try:
    import mysql.connector
    print("mysql-connector is available.")
except ImportError:
    print("MySQL connector module demo (run: pip install mysql-connector-python)")
