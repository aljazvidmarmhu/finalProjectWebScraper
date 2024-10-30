from Libraries import *

if __name__ == '__main__':
    productDetails = GetAllProducts().getAllProducts()
    store_db = StoreToDatabase()
    stored_products = store_db.storeToDatabase(productDetails)
    print("Stored Products:", stored_products)
    store_db.closeConnection()