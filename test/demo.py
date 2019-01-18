import time
from public import element
from appium import webdriver

desired_caps = {}  # 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'LE67A06190312448'
# app信息    微信
desired_caps['appPackage'] = 'com.tencent.mm'
desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'

# desired_caps["unicodeKeyboard"] = True
# desired_caps["resetKeyboard"] = True
desired_caps["noReset"] = "True"  # 不初始化手机app信息（类似不清楚缓存）

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(3)
print('微信启动成功')

driver.close_app()


# 跳转首页需要点击滑动页面
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)


# 屏幕向左滑动
def swipLeft(t):
    l = getSize()
    x1 = int(l[0] * 0.75)
    y1 = int(l[1] * 0.35)
    x2 = int(l[0] * 0.05)
    driver.swipe(x1, y1, x2, y1, t)


swipLeft(1000)
time.sleep(2)
swipLeft(1000)
time.sleep(2)




# 开启宠优优app
# 坐标获取当前需要点击的元素
x = driver.get_window_size()['width']  # 获取屏幕的宽度，x的最大值
y = driver.get_window_size()['height']  # 获取屏幕的高度，y的最大值

print(x, -----y)

a1 = 418 / x
b1 = 820 / y
driver.tap([(a1 * x, b1 * y)])
time.sleep(2)


# 点击我的  990/1840
def clickmy():
    l = getSize()
    x1 = int(l[0] * 0.91)
    y1 = int(l[1] * 0.95)
    driver.tap([(x1, y1)])
clickmy()

# print('点击二维码')
# driver.find_element(by.id('resource-id'),value='com.dealuck.cyy:id/iv_qr_code')
# print('点击完成')
# driver.press(x=240,y=600).wait(100).move_to(x=100,y=100).release().perform()
time.sleep(5)
driver.quit()



