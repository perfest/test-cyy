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


# 点击我的  990/1840
def clickmy():
    l = getSize()
    x1 = int(l[0] * 0.91)
    y1 = int(l[1] * 0.95)
    driver.tap([(x1, y1)])
clickmy()


# 设置 845/158
# def stclick():
#     l = getSize()
#     x = int(l[0] * 0.78)
#     y = int(l[1] * 0.08)
#     driver.tap([(x, y)])
# stclick()
# time.sleep(1)
from public import element
'''设置功能'''
# element.elementclick(driver,845,158) # 点击设置
# time.sleep(1)
# element.elementclick(driver,70,160) # 返回我的页面
# time.sleep(1)
# element.elementclick(driver,845,158) # 点击设置
# time.sleep(1)

'''账户与安全'''
# element.elementclick(driver,'安全')
# element.elementclick(driver,'手机号')
# element.elementclick(driver,'获取验证码')
# element.elementclick(driver,'点击验证码，并输入')
# element.elementclick(driver,'点击确认')
# print('验证成功')
# element.elementclick(driver,'新手机号')
# element.elementclick(driver,'验证码，没输入手机号情况下不能获取验证码和点击确认')
# element.elementclick(driver,'点击获取验证码')
# element.elementclick(driver,'输入验证码')
# element.elementclick(driver,'点击确认')
# print("修改成功")

'''通用设置'''
# element.elementclick(driver,'通用设置')
# element.elementclick(driver,'非wifi是否自动播放')
# element.elementclick(driver,'返回')

'''意见反馈'''
# element.elementclick(driver,'意见反馈')
# element.elementclick(driver,'返回')

'''关于'''
# element.elementclick(driver,'关于')
# element.elementclick(driver,'用户协议')
# element.elementclick(driver,'返回')
# element.elementclick(driver,'隐私政策')
# element.elementclick(driver,'返回')
# element.elementclick(driver,'社区公约')
# element.elementclick(driver,'返回')

# driver.find_element_by_id().clear()

'''编辑资料'''
element.elementclick(driver, 192, 371)
time.sleep(1)
element.elementclick(driver,500,800)
time.sleep(2)
# driver.find_element_by_id('com.dealuck.cyy:id/et_name').send_keys('帅气')
# element.elementclick(driver,500,800).send_keys('帅气')
# time.sleep(3)
element.elementclick(driver,950,150)
time.sleep(2)
driver.quit()



