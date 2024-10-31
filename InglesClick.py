from Libraries import *
class InglesClick(OpenPage):
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
            print("Error Clickin Through:", e)

    def getProductDetails(self, products):
        try:
            # Wait for the products to load
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'treport')))
            
            # Find all product offer blocks
            offer_blocks = self.driver.find_elements(By.CLASS_NAME, 'offerblock')

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
                    'imageURL': img_url,
                    'store' : "Ingles"
                })
            
            return products

        except Exception as e:
            print("Error retrieving product details:", e)
            return []