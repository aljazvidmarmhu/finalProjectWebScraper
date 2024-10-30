from Libraries import *

class GetAllProducts():
    def __init__(self):
        self.urlIngles = "https://flyer.inglesads.com/noncard/ThisWeek/SelectStore.jsp?lm=1"
        self.urlAldi = ""
        self.urlPublix = ""
        self.products = []
    def getAllProducts(self):
        clickTh = InglesClick(self.urlIngles) 
        clickTh.openPage()
        clickTh.clickThrough()
        self.products = clickTh.getProductDetailsIngles(self.products)
        clickTh.quitDriver()
        return self.products