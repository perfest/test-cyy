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
print('编辑资料，点击头像，昵称，取消，完成，关注，粉丝，获赞，宠物卡，作品，赞过，收藏，内容，话题，音乐')
driver.tap([(111, 363)])
time.sleep(1)
driver.tap([(120, 171)])
time.sleep(1)
driver.tap([(926, 414)])
time.sleep(1)
driver.tap([(546, 1234)])
time.sleep(1)
driver.tap([(670, 1545)])
time.sleep(1)
driver.tap([(978, 1311)])
time.sleep(1)
driver.tap([(990, 158)])
time.sleep(3)
print('编辑资料，点击头像，昵称，取消，完成-----开始关注事件的点击操作')
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
driver.tap([(124, 406)])
time.sleep(1)
driver.tap([(85, 188)])
time.sleep(1)
driver.tap([(376, 363)])
time.sleep(1)
driver.tap([(77, 179)])
time.sleep(1)
driver.tap([(77, 188)])
time.sleep(3)
print('关注事件的点击操作完成，--------开始粉丝列表的点击事件操作')
#
#
# # 粉丝列表页刷新和点击用户昵称和头像点击关注不关注
driver.tap([(350, 990)])
time.sleep(1)
driver.tap([(120, 363)])
time.sleep(1)
driver.tap([(68, 179)])
time.sleep(1)
driver.tap([(452, 337)])
time.sleep(1)
driver.tap([(81, 188)])
time.sleep(1)
driver.tap([(918, 367)])
time.sleep(1)
driver.tap([(918, 359)])
time.sleep(1)
driver.tap([(218, 1135)])
time.sleep(1)
driver.tap([(918, 359)])
time.sleep(1)
driver.tap([(849, 1127)])
time.sleep(1)
driver.tap([(81, 184)])
time.sleep(3)
print('粉丝列表完毕，-----开始获赞的点击操作')
#
# # 点击获赞和确定
driver.tap([(653, 982)])
time.sleep(1)
driver.tap([(512, 1268)])
time.sleep(3)
#
print('获赞操作完毕---------开始宠物卡片的点击事件操作')
# # 宠物卡片 删除操作
driver.tap([(926, 982)])
time.sleep(1)
driver.tap([(841, 282)])
time.sleep(3)
# TouchAction(driver)
# .press(x=474, y=1486)
# .move_to(x=0, y=-662)
# .release()
from public import element
element.swipeUp(driver,1000)
time.sleep(2)

driver.tap([(226, 1737)])
time.sleep(1)
driver.tap([(218, 1140)])
time.sleep(1)
driver.tap([(239, 1725)])
time.sleep(1)
driver.tap([(845, 1127)])
time.sleep(3)
#
#
# # 修改宠物资料
driver.tap([(751, 986)])
time.sleep(1)
driver.tap([(815, 282)])
time.sleep(1)
driver.tap([(444, 884)])
time.sleep(1)
driver.tap([(333, 1332)])
time.sleep(3)
# TouchAction(driver)
# .press(x=452, y=1392)
# .move_to(x=47, y=-735)
# .release()
element.swipeUp(driver,1000)
time.sleep(2)
driver.tap([(525, 1725)])
time.sleep(2)

# # 赞过的上拉刷新操作
# TouchAction(driver).tap([(525, 1148)])
# TouchAction(driver)
# .press(x=517, y=1494)
# .move_to(x=0, y=-1106)
# .release()
element.swipeUp(driver,1000)
time.sleep(2)
# TouchAction(driver)
# .press(x=521, y=1541)
# .move_to(x=13, y=-1110)
# .release()
element.swipeUp(driver,1000)
time.sleep(2)
# TouchAction(driver)
# .press(x=512, y=1622)
# .move_to(x=30, y=-1161)
# .release()
element.swipeUp(driver,1000)
time.sleep(2)
element.swipeDown(driver,1000)
time.sleep(2)
element.swipeDown(driver,1000)
time.sleep(2)
element.swipeDown(driver,1000)
time.sleep(2)
print('宠物卡片操作完毕----------开始音乐的点击操作')
# # 我的话题，音乐，作品的点击音乐的深度点击
driver.tap([(179, 1148)])
time.sleep(1)
driver.tap([(901, 1144)])
time.sleep(1)
driver.tap([(546, 1268)])
time.sleep(1)
driver.tap([(773, 1276)])
time.sleep(1)
driver.tap([(461, 1456)])
time.sleep(1)
driver.tap([(999, 162)])
time.sleep(1)
driver.tap([(1007, 1503)])
time.sleep(1)
driver.tap([(867, 162)])
time.sleep(1)
driver.tap([(858, 149)])
time.sleep(3)
# # 点击播放音乐按钮
driver.tap([(175, 418)])
time.sleep(3)
driver.tap([(171, 418)])
time.sleep(3)
#
# # 点击参与挑起相机 返回
driver.tap([(546, 1763)])
time.sleep(3)
driver.tap([(68, 243)])
time.sleep(3)

print('音乐操作完毕----------开始话题的操作')
# # 返回进入话题页
driver.tap([(81, 184)])
time.sleep(1)
driver.tap([(534, 1272)])
time.sleep(1)
driver.tap([(461, 1404)])
time.sleep(3)
#
# # 话题参与
driver.tap([(529, 1767)])
time.sleep(3)
driver.tap([(73, 252)])
time.sleep(3)

print('话题操作完毕-------------开始收藏操作')
# # 点击收藏
driver.tap([(529, 1767)])
time.sleep(1)
driver.tap([(73, 252)])
time.sleep(1)
driver.tap([(871, 158)])
time.sleep(1)
driver.tap([(858, 154)])
time.sleep(1)
driver.tap([(1003, 158)])
time.sleep(1)
driver.tap([(1025, 1498)])
time.sleep(1)
driver.tap([(81, 192)])
time.sleep(1)

driver.tap([(290, 1276)])
time.sleep(1)
driver.tap([(303, 1575)])
time.sleep(1)
driver.tap([(77, 188)])
time.sleep(1)
driver.tap([(768, 1537)])
time.sleep(1)
driver.tap([(77, 184)])
time.sleep(1)
driver.tap([(158, 1153)])
time.sleep(1)
driver.tap([(286, 1473)])
time.sleep(1)
driver.tap([(81, 179)])
time.sleep(1)
driver.tap([(798, 1464)])
time.sleep(1)
driver.tap([(85, 192)])
time.sleep(3)
print('我的页面点击事件执行完毕')




# 简化主程序的代码
# from test import public_demo
# dr = public_demo.Mydemo(driver)
# dr.erweima()
# dr.sting()







driver.quit()


