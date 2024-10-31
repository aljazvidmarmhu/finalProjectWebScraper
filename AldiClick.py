from Libraries import *
class AldiClick(OpenPage):
    def __init__(self, url):
        super().__init__(url)

    def clickThrough(self):
        try:
            # Wait for the dropdown to be present

            cookieBtn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'onetrust-accept-btn-handler')))
            cookieBtn.click()
            time.sleep(2)
            button = self.driver.find_element(By.CSS_SELECTOR, '.select-merchant-feature-bar__service-address')
            self.driver.execute_script("arguments[0].click();", button)
            time.sleep(2)
            continue_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test="change-merchant-alert_btn-confirm"]'))
            )
            continue_button.click()
            zip_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "merchant-zip-code-input"))
            )
            zip_input.clear()  # Clear any pre-existing text if needed
            zip_input.send_keys("28787")
            select_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "service-selector-search-dialog__store-select-btn"))
            )
            select_button.click()
            self.driver.get("https://new.aldi.us/weekly-specials/weekly-ads")
        
        except Exception as e:
            print("Error Clickin Through:", e)

    def getProductDetails(self, products):
        try:
            items = self.driver.find_elements(By.CLASS_NAME, 'p-grid-item')
            # Wait for the products to load
            for item in items:
             # Extract the image link
                image_element = item.find_element(By.CSS_SELECTOR, 'img')
                image_link = image_element.get_attribute('src')
    
            # Extract the name
                name_element = item.find_element(By.CSS_SELECTOR, 'div[data-qa-automation="prod-title"] span')
                name = name_element.text.strip()
    
            # Extract the price
                price_element = item.find_element(By.CSS_SELECTOR, '.p-savings-badge__text')
                price = price_element.text.strip()
                products.append({
                    'productName': name,
                    'price': price,
                    'imageURL': image_link,   
                    'store' : "Aldi"
                })
            
            return products

        except Exception as e:
            print("Error retrieving product details:", e)
            return []
        
if __name__ == '__main__':
    url = "https://new.aldi.us"
    products = []
    clickTh = AldiClick(url)
    clickTh.openPage()
    clickTh.clickThrough()
    products = clickTh.getProductDetails(products)
    print(products)
    