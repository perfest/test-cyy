import time

# 关注页面的点击事件
class foll:
    def __init__(self,driver):
        self.driver = driver

    def followclick(self):
        self.driver.find_elements_by_class_name('android.widget.FrameLayout').index(0).click()
