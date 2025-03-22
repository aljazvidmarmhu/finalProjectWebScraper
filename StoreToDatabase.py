from Libraries import *

class StoreToDatabase:
    def __init__(self):
        self.databaseName = "<your_database_name>"  # Replace with your actual database name
        self.databaseTableName = "<your_table_name>"  # Replace with your actual table name
        self.databasePassword = "<your_password>"  # Replace with your actual database password
        self.connection = self.createConnection()
    def createConnection(self):
        """Create a database connection."""
        try:
            connection = mysql.connector.connect(
                host='localhost',  # Change if needed
                user='root',  # Your MySQL username
                password=self.databasePassword,
                database=self.databaseName
            )
            if connection.is_connected():
                print("Connection to MySQL DB successful")
                return connection
        except Error as e:
            print(f"Error: '{e}'")

    def storeToDatabase(self, products):
        self.clearTable()  
        cursor = self.connection.cursor()

        insert_query = f"""
        INSERT INTO {self.databaseTableName} (productName, price, imageURL, store)
        VALUES (%s, %s, %s, %s);
        """

        for product in products:
            data = (product['productName'], product['price'], product['imageURL'], product['store'])
            cursor.execute(insert_query, data)

        self.connection.commit()  # Commit the transaction
        cursor.close()
        return products
    
    def clearTable(self):
        """Delete all existing records from the table."""
        cursor = self.connection.cursor()
        delete_query = f"DELETE FROM {self.databaseTableName};"
        cursor.execute(delete_query)
        self.connection.commit()  # Commit the transaction
        cursor.close()

    def closeConnection(self):
        """Close the database connection."""
        if self.connection.is_connected():
            self.connection.close()
            print("MySQL connection is closed")