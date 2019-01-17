import time


class Mydemo:
    '''我的页面click事件'''
    def __init__(self,driver):
        self.driver = driver

    def erweima(self):
        print('开始点击二维码事件')
        self.driver.tap([(683, 154)])
        time.sleep(1)
        self.driver.tap([(542, 1592)])
        time.sleep(1)
        self.driver.tap([(696, 154)])
        time.sleep(1)
        self.driver.tap([(542, 1345)])
        time.sleep(1)

    def sting(self):
        print('开始设置点击操作')
        self.driver.tap([(841, 158)])
        time.sleep(1)
        self.driver.tap([(81, 175)])
        time.sleep(1)
        self.driver.tap([(841, 158)])
        time.sleep(1)
        self.driver.tap([(201, 312)])
        time.sleep(1)
        self.driver.tap([(721, 307)])
        time.sleep(1)
        self.driver.tap([(77, 184)])
        time.sleep(1)
        self.driver.tap([(77, 175)])
        time.sleep(2)
        print('通用模块')
        self.driver.tap([(154, 461)])
        time.sleep(1)
        self.driver.tap([(982, 307)])
        time.sleep(1)
        self.driver.tap([(982, 307)])
        time.sleep(1)
        self.driver.tap([(77, 175)])
        time.sleep(1)
        print('意见模块')
        self.driver.tap([(196, 623)])
        time.sleep(1)
        self.driver.tap([(81, 188)])
        time.sleep(1)
        print('关于模块')
        self.driver.tap([(171, 768)])
        time.sleep(1)
        self.driver.tap([(166, 764)])
        time.sleep(1)
        self.driver.tap([(81, 188)])
        time.sleep(1)
        self.driver.tap([(213, 918)])
        time.sleep(1)
        self.driver.tap([(81, 188)])
        time.sleep(1)
        self.driver.tap([(171, 1071)])
        time.sleep(1)
        self.driver.tap([(90, 184)])
        time.sleep(1)
        self.driver.tap([(90, 188)])
        time.sleep(3)

    def ziliao(self):
        self.driver.tap([(111, 363)])
        time.sleep(1)
        self.driver.tap([(120, 171)])
        time.sleep(1)
        self.driver.tap([(926, 414)])
        time.sleep(1)
        self.driver.tap([(546, 1234)])
        time.sleep(1)
        self.driver.tap([(670, 1545)])
        time.sleep(1)
        self.driver.tap([(978, 1311)])
        time.sleep(1)
        self.driver.tap([(990, 158)])
        time.sleep(3)






