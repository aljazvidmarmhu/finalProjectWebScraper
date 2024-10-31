from Libraries import *

class OpenPage:
    def __init__(self, url):
        self.url = url
        self.options = Options()
        self.options.set_preference("geo.prompt.testing", True)  # Enable location prompt testing
        self.options.set_preference("geo.prompt.testing.allow", True) 
        self.options.set_preference("geo.enabled", True)  # Disable geolocation
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

if __name__ == '__main__':
    url = "https://flyer.inglesads.com/noncard/ThisWeek/SelectStore.jsp?lm=1"
    page = OpenPage(url)
    page.openPage()
    print(page.getTitle())
    time.sleep(2)
    page.quitDriver()
    
