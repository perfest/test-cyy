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


# lists = driver.find_element_by_name('推荐')
lists = driver.find_elements_by_class_name('android.widget.TextView')
# driver.find_elements_by_name()
# size = lists.size
# if size > 0 :
for i in lists:
    l = i.text
    print(l)

# # 点击我的事件
# from my_index import my
# dr = my.Myclick(driver)
# dr.erweima()
# dr.sting()
# dr.ziliao()
# time.sleep(3)

driver.tap([(960,1840)])
time.sleep(2)

# 点击页面的  设置   com.dealuck.cyy:id/iv_setting
# driver.find_element_by_id('com.dealuck.cyy:id/iv_setting').click()
# print('点击设置完成')
# time.sleep(3)


# 获取当前界面上的所有class为  android.widget.ImageView
ls = driver.find_elements_by_class_name('android.widget.ImageView')
print(ls)
print('---------------------------------------------------------------')
for i in ls:
    print(i.tag_name)

print('点击设置成功')




#
#

#
# # 点击到首页，然后滑动测试


# 首页点击事件需要优化
# from index import indexs
# dr = indexs.indexclick(driver)
# dr.pbclick()

# from follow import follows
# dr = follows.foll(driver)
# dr.followclick()

time.sleep(2)
driver.quit()




