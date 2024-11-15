from Libraries import *

class WholeFoodsClick(OpenPage):
    def __init__(self, url):
        super().__init__(url)

    def clickThrough(self):
        try:
            self.driver.maximize_window()
            time.sleep(2)
            popUp = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'w-core-info__my-store')))
            closeBtn = popUp.find_element(By.CLASS_NAME, "w-link--text")
            closeBtn.click()
            try:
                self.driver.get("https://www.wholefoodsmarket.com/sales-flyer?store-id=10520")
                print("Page Title:", self.driver.title)
            except Exception as e:
                print("error getting title asheville page :", e)
        except Exception as e:
            print("Error Clickin Through:", e)

    def getProductDetails(self, products):
        try:
            print("in getproducts")
            items1 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'root')))
            print("root found ")
            items2 = items1.find_element(By.CLASS_NAME, 'w-full')
            print("full found")
            items3 = items2.find_element(By.CLASS_NAME, 'grid')
            print("grid found")
            time.sleep(2)
            items = items3.find_elements(By.CLASS_NAME, 'col-span-1')
            print("div found")
            # Wait for the products to load
            for item in items:
             # Extract the image link
                image_element = item.find_element(By.CSS_SELECTOR, 'div.relative img')
                image_link = image_element.get_attribute('src')
                print("link:" + image_link)
            # Extract the name
                name_element = item.find_element(By.CSS_SELECTOR, 'span.bds--heading-5')
                name = name_element.text.strip()
    
            # Extract the price
                try:
                    price_element = item.find_element(By.CSS_SELECTOR, 'span.bds--heading-4')
                    price = price_element.text.strip() + " with Prime"
                except Exception as e:
                    print("price not there or not valid")
                    price = "Price might vary"
                products.append({
                    'productName': name,
                    'price': price,
                    'imageURL': image_link,   
                    'store' : "WholeFoods"
                })
            
            return products

        except Exception as e:
            print("Error retrieving product details:", e)
            return []
        
if __name__ == '__main__':
    url = "https://www.wholefoodsmarket.com/stores/eastasheville?utm_source=google&utm_medium=organic&utm_campaign=listings"
    products = []
    clickTh = WholeFoodsClick(url)
    clickTh.openPage()
    clickTh.clickThrough()
    products = clickTh.getProductDetails(products)
    print(products)
    