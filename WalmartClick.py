
#does not work properly

from Libraries import *

class WalmartClick(OpenPage):
    def __init__(self, url):
        super().__init__(url)

    def clickThrough(self):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="item-stack"]')))
            print("found all")
            element1 = element.find_element("id", "zaKlOMVogIdTrwN")
            
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
    url = "https://www.walmart.com/shop/deals/food?povid=FallSavings_Facet_Food"
    products = []
    clickTh = WalmartClick(url)
    clickTh.openPage()
    clickTh.clickThrough()
    products = clickTh.getProductDetails(products)
    print(products)
    