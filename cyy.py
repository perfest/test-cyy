import time

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


# 点击关注
# driver.find_element_by_xpath("//*[contains(@text,'关注'))]")
x = driver.get_window_size()['width']  # 获取屏幕的宽度，x的最大值
y = driver.get_window_size()['height']  # 获取屏幕的高度，y的最大值
a1 = 329 / x
b1 = 1831 / y
driver.tap([(a1 * x, b1 * y)])

time.sleep(2)
driver.find_element_by_id('com.dealuck.cyy:id/editPhone').send_keys("13476299157")
time.sleep(2)
driver.find_element_by_id('com.dealuck.cyy:id/btnNextStep').click()
time.sleep(2)
driver.find_element_by_id('com.dealuck.cyy:id/et_code').send_keys("1111")
time.sleep(2)
# 点击登陆
driver.find_element_by_id('com.dealuck.cyy:id/btnLogin').click()

time.sleep(5)


# 点击我的  990/1840
def clickmy():
    l = getSize()
    x1 = int(l[0] * 0.91)
    y1 = int(l[1] * 0.95)
    driver.tap([(x1, y1)])
clickmy()


from my_index import my
dr = my.Myclick(driver)
dr.erweima()
dr.sting()
dr.ziliao()
dr.Slide()

'''跳转首页节奏上有问题设置页面还是没有退出'''
from index import indexs
dri = indexs.indexclick(driver)
dri.pbclick()

from information import message
driv = message.msg(driver)
driv.msgclick()



print('点击事件完成')
driver.quit()




