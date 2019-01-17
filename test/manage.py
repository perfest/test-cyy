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

'''我的滑动事件'''
# TouchAction(driver)
# .press(x=508, y=465)
# .move_to(x=-26, y=880)
# .release()

# driver.press(x=508, y=465).move_to(x=-26, y=880)
time.sleep(2)
'''点击二维码事件'''
driver.tap([(683, 154)])
time.sleep(1)
driver.tap([(542, 1592)])
time.sleep(1)
driver.tap([(696, 154)])
time.sleep(1)
driver.tap([(542, 1345)])
time.sleep(1)
'''设置 账户安全'''
driver.tap([(841, 158)])
time.sleep(1)
driver.tap([(81, 175)])
time.sleep(1)
driver.tap([(841, 158)])
time.sleep(1)
driver.tap([(201, 312)])
time.sleep(1)
driver.tap([(721, 307)])
time.sleep(1)
driver.tap([(77, 184)])
time.sleep(1)
driver.tap([(77, 175)])
time.sleep(1)
'''通用设置'''
driver.tap([(154, 461)])
time.sleep(1)
driver.tap([(982, 307)])
time.sleep(1)
driver.tap([(982, 307)])
time.sleep(1)
driver.tap([(77, 175)])
time.sleep(1)
'''意见反馈'''
driver.tap([(196, 623)])
time.sleep(1)
driver.tap([(81, 188)])
time.sleep(1)
'''关于'''
driver.tap([(171, 768)])
time.sleep(1)
driver.tap([(166, 764)])
time.sleep(1)
driver.tap([(81, 188)])
time.sleep(1)
driver.tap([(213, 918)])
time.sleep(1)
driver.tap([(81, 188)])
time.sleep(1)
driver.tap([(171, 1071)])
time.sleep(1)
driver.tap([(90, 184)])
time.sleep(1)
driver.tap([(90, 188)])
time.sleep(3)

'''编辑资料，点击头像，昵称，取消，完成，关注，粉丝，获赞，宠物卡，作品，赞过，收藏，内容，话题，音乐'''
# 编辑资料，点击头像，昵称，取消，完成，
# TouchAction(driver).tap([(111, 363)])
# TouchAction(driver).tap([(120, 171)])
# TouchAction(driver).tap([(926, 414)])
# TouchAction(driver).tap([(546, 1234)])
# TouchAction(driver).tap([(670, 1545)])
# TouchAction(driver).tap([(978, 1311)])
# TouchAction(driver).tap([(990, 158)])
#
# # 获取关注列表 上拉下拉刷新
# TouchAction(driver).tap([(73, 1003)])
# TouchAction(driver)
# .press(x=534, y=359)
# .move_to(x=-30, y=887)
# .release()
#
# TouchAction(driver)
# .press(x=461, y=1481)
# .move_to(x=77, y=-926)
# .release()
#
# TouchAction(driver).tap([(124, 406)])
# TouchAction(driver).tap([(85, 188)])
# TouchAction(driver).tap([(376, 363)])
# TouchAction(driver).tap([(77, 179)])
# TouchAction(driver).tap([(77, 188)])
#
#
# # 粉丝列表页刷新和点击用户昵称和头像点击关注不关注
# TouchAction(driver).tap([(350, 990)])
# TouchAction(driver).tap([(120, 363)])
# TouchAction(driver).tap([(68, 179)])
# TouchAction(driver).tap([(452, 337)])
# TouchAction(driver).tap([(81, 188)])
# TouchAction(driver).tap([(918, 367)])
# TouchAction(driver).tap([(918, 359)])
# TouchAction(driver).tap([(218, 1135)])
# TouchAction(driver).tap([(918, 359)])
# TouchAction(driver).tap([(849, 1127)])
# TouchAction(driver).tap([(81, 184)])
#
# # 点击获赞和确定
# TouchAction(driver).tap([(653, 982)])
# TouchAction(driver).tap([(512, 1268)])
#
#
# # 宠物卡片 删除操作
# TouchAction(driver).tap([(926, 982)])
# TouchAction(driver).tap([(841, 282)])
# TouchAction(driver)
# .press(x=474, y=1486)
# .move_to(x=0, y=-662)
# .release()
#
# TouchAction(driver).tap([(226, 1737)])
# TouchAction(driver).tap([(218, 1140)])
# TouchAction(driver).tap([(239, 1725)])
# TouchAction(driver).tap([(845, 1127)])
#
#
# # 修改宠物资料
# TouchAction(driver).tap([(751, 986)])
# TouchAction(driver).tap([(815, 282)])
# TouchAction(driver).tap([(444, 884)])
# TouchAction(driver).tap([(333, 1332)])
# TouchAction(driver)
# .press(x=452, y=1392)
# .move_to(x=47, y=-735)
# .release()
#
# TouchAction(driver).tap([(525, 1725)])
#
#
# # 赞过的上拉刷新操作
# TouchAction(driver).tap([(525, 1148)])
# TouchAction(driver)
# .press(x=517, y=1494)
# .move_to(x=0, y=-1106)
# .release()
#
# TouchAction(driver)
# .press(x=521, y=1541)
# .move_to(x=13, y=-1110)
# .release()
#
# TouchAction(driver)
# .press(x=512, y=1622)
# .move_to(x=30, y=-1161)
# .release()
#
#
# # 我的话题，音乐，作品的点击音乐的深度点击
# TouchAction(driver).tap([(179, 1148)])
# TouchAction(driver).tap([(901, 1144)])
# TouchAction(driver).tap([(546, 1268)])
# TouchAction(driver).tap([(773, 1276)])
# TouchAction(driver).tap([(461, 1456)])
# TouchAction(driver).tap([(999, 162)])
# TouchAction(driver).tap([(1007, 1503)])
# TouchAction(driver).tap([(867, 162)])
# TouchAction(driver).tap([(858, 149)])
# # 点击播放音乐按钮
# TouchAction(driver).tap([(175, 418)])
# TouchAction(driver).tap([(171, 418)])
#
# # 点击参与挑起相机 返回
# TouchAction(driver).tap([(546, 1763)])
# TouchAction(driver).tap([(68, 243)])
#
# # 返回进入话题页
# TouchAction(driver).tap([(81, 184)])
# TouchAction(driver).tap([(534, 1272)])
# TouchAction(driver).tap([(461, 1404)])
#
# # 话题参与
# TouchAction(driver).tap([(529, 1767)])
# TouchAction(driver).tap([(73, 252)])
#
# # 点击收藏
# TouchAction(driver).tap([(529, 1767)])
# TouchAction(driver).tap([(73, 252)])
# TouchAction(driver).tap([(871, 158)])
# TouchAction(driver).tap([(858, 154)])
# TouchAction(driver).tap([(1003, 158)])
# TouchAction(driver).tap([(1025, 1498)])
# TouchAction(driver).tap([(81, 192)])
#
# TouchAction(driver).tap([(290, 1276)])
# TouchAction(driver).tap([(303, 1575)])
# TouchAction(driver).tap([(77, 188)])
# TouchAction(driver).tap([(768, 1537)])
# TouchAction(driver).tap([(77, 184)])
# TouchAction(driver).tap([(158, 1153)])
# TouchAction(driver).tap([(286, 1473)])
# TouchAction(driver).tap([(81, 179)])
# TouchAction(driver).tap([(798, 1464)])
# TouchAction(driver).tap([(85, 192)])
#


driver.quit()


