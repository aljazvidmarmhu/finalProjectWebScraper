from Libraries import *

class PublixClick(OpenPage):
    def __init__(self, url):
        super().__init__(url)

    def clickThrough(self):
        try:
            # Wait for the dropdown to be present
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'search-input')))
            
            # Locate the dropdown (select) element
            textArea = self.driver.find_element(By.CLASS_NAME, 'search-input')
            textAreaField = textArea.find_element(By.NAME, 'search')
            textAreaField.send_keys("28787")
            button = textArea.find_element(By.CLASS_NAME, 'search-button')
            time.sleep(4)
            button.click()
            print(f"hrlllas")
            time.sleep(2)

            print("gewq")
            # Wait for the options to be present
            chooseStoreBtn = self.driver.find_element(By.ID, 'choose_1546')
            chooseStoreBtn.click()
            time.sleep(4)
            # Select the 'NC' option
           
            self.driver.get("https://www.publix.com/savings/weekly-ad/view-all")

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
                    'store' : "Publix"
                })
            
            return products

        except Exception as e:
            print("Error retrieving product details:", e)
            return []
        
if __name__ == '__main__':
    url = "https://www.publix.com/savings/select-store?merch=1_hp_viz_nav_weeklyad&redirect=%2Fsavings%2Fweekly-ad%3Fmerch%3D1_hp_viz_nav_weeklyad"
    products = []
    clickTh = PublixClick(url)
    clickTh.openPage()
    clickTh.clickThrough()
    products = clickTh.getProductDetails(products)
    print(products)
    