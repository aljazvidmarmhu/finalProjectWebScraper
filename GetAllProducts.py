from Libraries import *
from PublixClick import PublixClick
from WholeFoodsClick import WholeFoodsClick
class GetAllProducts():
    def __init__(self):
        self.urlIngles = "https://flyer.inglesads.com/noncard/ThisWeek/SelectStore.jsp?lm=1"
        self.urlWholeFoods = "https://www.wholefoodsmarket.com/stores/eastasheville?utm_source=google&utm_medium=organic&utm_campaign=listings"
        self.urlPublix = "https://www.publix.com/savings/select-store?merch=1_hp_viz_nav_weeklyad&redirect=%2Fsavings%2Fweekly-ad%3Fmerch%3D1_hp_viz_nav_weeklyad"
        self.products = []
    def getAllProducts(self):
        clickTh = InglesClick(self.urlIngles) 
        clickTh.openPage()
        clickTh.clickThrough()
        self.products = clickTh.getProductDetails(self.products)
        clickTh.quitDriver()
        clickTh1 = PublixClick(self.urlPublix)
        clickTh1.openPage()
        clickTh1.clickThrough()
        self.products = clickTh1.getProductDetails(self.products)
        clickTh1.quitDriver()
        clickTh2 = WholeFoodsClick(self.urlWholeFoods) 
        clickTh2.openPage()
        clickTh2.clickThrough()
        self.products = clickTh2.getProductDetails(self.products)
        clickTh2.quitDriver()
        return self.products