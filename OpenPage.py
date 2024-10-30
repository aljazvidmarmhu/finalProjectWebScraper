from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import mysql.connector
from mysql.connector import Error

class OpenPage:
    def __init__(self, url):
        self.url = url
        self.options = Options()
        #self.options.add_argument('--headless')  # Run Firefox in headless mode
        # Initialize the Firefox WebDriver with specified options
        self.driver = webdriver.Firefox(options=self.options) # Update geckodriver path if needed
    
    def openPage(self):
        # Open the URL
        self.driver.get(self.url)
        
    def getTitle(self):
        # Return the page title
        return self.driver.title
    
    def quitDriver(self):
        # Close the browser
        self.driver.quit()

    def clickThrough(self): #has to be implemented in subclass 
        raise NotImplementedError

class PublixClick(OpenPage):
    def __init__(self, url):
        super().__init__(url)

    def clickThrough(self):
        try:
            # Wait for the dropdown to be present
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'SELECT_US_STATE')))
            
            # Locate the dropdown (select) element
            dropdown = self.driver.find_element(By.ID, 'SELECT_US_STATE')
            dropdown.click()  # Open the dropdown
            
            # Wait for the options to be present
            WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'option')))
            
            # Select the 'NC' option
            options = dropdown.find_elements(By.TAG_NAME, 'option')
            for option in options:
                if option.text == 'NC':
                    option.click()  # Click the NC option
                    break
            # Wait for the second dropdown to be present and select "Weaverville"
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'SELECT_CITY')))
            dropdown_city = self.driver.find_element(By.ID, 'SELECT_CITY')
            dropdown_city.click()
            options_city = dropdown_city.find_elements(By.TAG_NAME, 'option')
            for option in options_city:
                if option.text == 'Weaverville':
                    option.click()  # Click the Weaverville option
                    break
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'SELECT_STORE')))
            dropdown_store = self.driver.find_element(By.ID, 'SELECT_STORE')
            dropdown_store.click()
            options_store = dropdown_store.find_elements(By.TAG_NAME, 'option')
            for option in options_store:
                if option.get_attribute("value") == '180':  # Check for the value '180'
                    option.click()  # Click the option for "140 Weaver Blvd"
                    break
            continue_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, 'BUTTON_CONTINUE')))
            continue_button.click()
            
            self.driver.get("https://flyer.inglesads.com/noncard/ThisWeek/ReviewAllSpecials.jsp")

        except Exception as e:
            print("Error selecting option:", e)

    def getProductDetails(self):
        try:
            # Wait for the products to load
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'treport')))
            
            # Find all product offer blocks
            offer_blocks = self.driver.find_elements(By.CLASS_NAME, 'offerblock')
            products = []

            for block in offer_blocks:
                # Extract product image URL
                img_element = block.find_element(By.CLASS_NAME, 'prodimage')
                img_url = img_element.get_attribute('src')

                # Extract product name
                title_element = block.find_element(By.CLASS_NAME, 'title')
                product_name = title_element.text.strip()
                product_name = product_name.replace('\n', ' ').strip()
                # Extract product price
                price_element = block.find_element(By.CLASS_NAME, 'price')
                product_price = price_element.text.strip()
                product_price = product_price.replace('\n', ' ').strip()
    
                products.append({
                    'productName': product_name,
                    'price': product_price,
                    'imageURL': img_url
                })
            
            return products

        except Exception as e:
            print("Error retrieving product details:", e)
            return []

class StoreToDatabase:
    def __init__(self):
        self.databaseName = "finalProject"
        self.databaseTableName = "finalProjectTable"
        self.databasePassword = "finalProject2024!"
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
        INSERT INTO {self.databaseTableName} (productName, price, imageURL)
        VALUES (%s, %s, %s);
        """

        for product in products:
            data = (product['productName'], product['price'], product['imageURL'])
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

        
if __name__ == '__main__':
    url = "https://flyer.inglesads.com/noncard/ThisWeek/SelectStore.jsp?lm=1"
    clickTh = PublixClick(url) 
    clickTh.openPage()
    clickTh.clickThrough()
    productDetails = clickTh.getProductDetails()
    store_db = StoreToDatabase()
    stored_products = store_db.storeToDatabase(productDetails)
    print("Stored Products:", stored_products)
    store_db.closeConnection()
    clickTh.quitDriver()
