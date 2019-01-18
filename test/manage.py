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

'''我的滑动事件'''
# TouchAction(driver)
# .press(x=508, y=465)
# .move_to(x=-26, y=880)
# .release()

# driver.press(x=508, y=465).move_to(x=-26, y=880)
element.swipeDown(driver,1000)
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
driver.tap([(80,150)])
driver.tap([(80,150)])
time.sleep(3)
# 设置页面没有退出  需要修改

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




# # 获取关注列表   点击事件
driver.tap([(77, 990)])
time.sleep(1)
driver.tap([(73, 175)])
time.sleep(1)
driver.tap([(73, 990)])
time.sleep(1)
driver.tap([(162, 410)])
time.sleep(2)
driver.tap([(85, 184)])
time.sleep(1)
driver.tap([(918, 384)])
time.sleep(2)
driver.tap([(205, 1123)])
time.sleep(1)
driver.tap([(901, 393)])
time.sleep(2)
driver.tap([(862, 1135)])
time.sleep(1)
driver.tap([(73, 188)])
time.sleep(3)



print('关注事件的点击操作完成，--------开始粉丝列表的点击事件操作')
#
#
# # 粉丝列表页刷新和点击用户昵称和头像点击关注不关注
driver.tap([(286, 990)])
time.sleep(2)
driver.tap([(81, 184)])
time.sleep(1)
driver.tap([(282, 986)])
time.sleep(2)
driver.tap([(896, 359)])
time.sleep(2)
driver.tap([(914, 367)])
time.sleep(2)
driver.tap([(209, 1144)])
time.sleep(1)
driver.tap([(905, 359)])
time.sleep(2)
driver.tap([(849, 1123)])
time.sleep(1)
driver.tap([(81, 188)])
time.sleep(3)

print('粉丝列表完毕，-----开始获赞的点击操作')
#
# # 点击获赞和确定
driver.tap([(504, 986)])
time.sleep(1)
driver.tap([(521, 1259)])
time.sleep(3)
#
print('获赞操作完毕---------开始宠物卡片的点击事件操作')
# # 宠物卡片 删除操作
driver.tap([(914, 986)])
time.sleep(2)
driver.tap([(534, 1733)])
time.sleep(2)
driver.tap([(918, 973)])
time.sleep(1)
driver.tap([(841, 282)])
time.sleep(2)
from public import element
element.swipeUp(driver,1000)
time.sleep(1)
driver.tap([(487, 1733)])
time.sleep(3)


print('宠物卡片操作完毕----------开始音乐的点击操作')
# # 我的话题，音乐，作品的点击音乐的深度点击
driver.tap([(888, 1153)])
time.sleep(1)
driver.tap([(768, 1289)])
time.sleep(1)
driver.tap([(371, 1456)])
time.sleep(3)
driver.tap([(867, 166)])
time.sleep(1)
driver.tap([(149, 431)])
time.sleep(5)
driver.tap([(166, 435)])
time.sleep(1)
driver.tap([(854, 158)])
time.sleep(1)
driver.tap([(849, 162)])
time.sleep(1)
driver.tap([(999, 171)])
time.sleep(1)
driver.tap([(1016, 1498)])
time.sleep(1)
driver.tap([(555, 1772)])
time.sleep(5)
driver.tap([(73, 239)])
time.sleep(1)
driver.tap([(444, 1588)])
time.sleep(1)
driver.tap([(98, 1592)])
time.sleep(1)
driver.tap([(81, 184)])
time.sleep(1)
driver.tap([(77, 179)])
time.sleep(3)


print('音乐操作完毕----------开始话题的操作')
# # 返回进入话题页
driver.tap([(529, 1268)])
time.sleep(1)
driver.tap([(546, 1409)])
time.sleep(3)
driver.tap([(871, 158)])
time.sleep(1)
driver.tap([(854, 154)])
time.sleep(1)
driver.tap([(999, 149)])
time.sleep(1)
driver.tap([(1016, 1494)])
time.sleep(1)
driver.tap([(559, 1772)])
time.sleep(5)
driver.tap([(73, 239)])
time.sleep(1)
driver.tap([(295, 1200)])
time.sleep(5)
driver.tap([(77, 179)])
time.sleep(1)
driver.tap([(98, 1763)])
time.sleep(5)
driver.tap([(73, 179)])
time.sleep(1)
driver.tap([(68, 175)])
time.sleep(3)


print('话题操作完毕-------------开始点击')
driver.tap([(303, 1285)])
time.sleep(1)
driver.tap([(529, 1276)])
time.sleep(1)
driver.tap([(756, 1276)])
time.sleep(1)
driver.tap([(551, 1127)])
time.sleep(1)
driver.tap([(179, 1153)])
time.sleep(1)
driver.tap([(892, 1148)])
time.sleep(1)
driver.tap([(495, 999)])
time.sleep(1)
driver.tap([(529, 1259)])
time.sleep(1)
driver.tap([(277, 995)])
time.sleep(1)
driver.tap([(73, 188)])
time.sleep(1)
driver.tap([(73, 995)])
time.sleep(1)
driver.tap([(81, 175)])
time.sleep(1)
driver.tap([(837, 990)])
time.sleep(1)
driver.tap([(538, 1729)])
time.sleep(1)
driver.tap([(525, 1268)])
time.sleep(1)
driver.tap([(760, 1276)])
time.sleep(1)
driver.tap([(517, 1144)])
time.sleep(1)

print('我的页面点击事件执行完毕')

# 可以执行，在点击需要网络请求时，睡眠事件加长

driver.quit()


