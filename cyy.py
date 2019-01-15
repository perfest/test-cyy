from appium import webdriver
import time

from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}  # 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'LE67A06190312448'
# app信息    微信
desired_caps['appPackage'] = 'com.tencent.mm'
desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'

# desired_caps["unicodeKeyboard"] = True
# desired_caps["resetKeyboard"] = True
desired_caps["noReset"] = "True"#不初始化手机app信息（类似不清楚缓存）

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(3)
print('微信启动成功')

driver.close_app()

# 跳转首页需要点击滑动页面
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)

#屏幕向左滑动
def swipLeft(t):
   l=getSize()
   x1=int(l[0]*0.75)
   y1=int(l[1]*0.35)
   x2=int(l[0]*0.05)
   driver.swipe(x1,y1,x2,y1,t)
swipLeft(1000)
time.sleep(2)
swipLeft(1000)

time.sleep(2)

# 开启宠优优app
# 坐标获取当前需要点击的元素
x = driver.get_window_size()['width']     #获取屏幕的宽度，x的最大值
y = driver.get_window_size()['height']    #获取屏幕的高度，y的最大值

print(x,-----y)

a1 = 418/x
b1 = 820/y
driver.tap([(a1*x, b1*y)])

time.sleep(2)
# 点击关注
# driver.find_element_by_xpath("//*[contains(@text,'关注'))]")
x = driver.get_window_size()['width']     #获取屏幕的宽度，x的最大值
y = driver.get_window_size()['height']    #获取屏幕的高度，y的最大值
a1 = 329/x
b1 = 1831/y
driver.tap([(a1*x, b1*y)])

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


# 点击二维码
driver.find_element_by_id('com.dealuck.cyy:id/iv_qr_code').click()
time.sleep(1)
def saveclick():  # 550/1340
    l = getSize()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.7)
    driver.tap([(x1, y1)])
saveclick()
time.sleep(1)

# 设置 845/158
def stclick():
    l = getSize()
    x = int(l[0]*0.78)
    y = int(l[1]*0.08)
    driver.tap([(x,y)])
stclick()
time.sleep(1)

# 返回我的页面 70/160
def rtclick():
    l = getSize()
    x = int(l[0]*0.06)
    y = int(l[1] *0.08)
    driver.tap([(x,y)])
rtclick()
time.sleep(1)

# 分享 1010/162
def shareclick():
    l = getSize()
    x = int(l[0] * 0.93)
    y = int(l[1] * 0.08)
    driver.tap([(x,y)])
shareclick()
time.sleep(1)


# 点x返回我的页面  1020/1187
def xclick():
    l = getSize()
    x = int(l[0] * 0.94)
    y = int(l[1] * 0.61)
    driver.tap([(x, y)])
xclick()
time.sleep(1)

# 点击用户昵称
# 点击取消返回我的页面
from public import element
element.elementclick(driver,192,371)
time.sleep(1)
element.elementclick(driver,100,160)
time.sleep(1)

# 点击认证可以，返回我的页面
element.elementclick(driver,200,465)
time.sleep(1)
element.elementclick(driver,100,160)
time.sleep(1)

# 点击用户头像进入个人资料编辑页面
element.elementclick(driver,930,400)
time.sleep(1)
# 获取当前页面上的所有input输入框
# 编辑资料sendkeys发送数据
# 点击完成 保存编辑内容
element.elementclick(driver,1010,162)
time.sleep(1)

# 点击关注 获取关注列表
# 使用上拉滑动更新列表
# 点击返回，回到我的页面
element.elementclick(driver,77,900)
time.sleep(1)
element.swipeUp(driver,1000)
time.sleep(1)
element.swipeDown(driver,1000)
driver.find_element_by_id('com.dealuck.cyy:id/iv_left').click()
time.sleep(1)

# 点击粉丝获取粉丝列表
# 上拉滑动更新列表
# 点击返回，回到我的页面
element.elementclick(driver,280,900)
time.sleep(1)
element.swipeUp(driver,1000)
time.sleep(1)
element.swipeDown(driver,1000)
time.sleep(1)
driver.find_element_by_id('com.dealuck.cyy:id/iv_left').click()
time.sleep(1)

# 点击获赞 获取被赞数量
# 点击确认 返回我的页面
element.elementclick(driver,470,890)
time.sleep(1)
driver.find_element_by_id('com.dealuck.cyy:id/tv_ok').click()
time.sleep(1)

# 点击宠物卡，跳转宠物卡页面，
# 向左滑动 if 页面中是否存在“添加宠物”存在 点击添加，不存在继续向右滑动 选择编辑 逻辑和添加一样
# 点击添加宠物 编辑宠物资料
# 获取input输入框 填入宠物名称，
# 点击添加宠物头像，选择宠物头像
# 选择宠物的性别
# 选择宠物的品种
# 选择宠物的出生日期
# 选择是否绝育
# 选择宠物的性格
# 点击提交资料




# 点击赞过 获取赞过的列表  上拉刷新列表的类容，下拉返回
element.elementclick(driver,555,1050)
time.sleep(1)
element.swipeUp(driver,1000)
time.sleep(1)
element.swipeDown(driver,1000)
time.sleep(1)




# 点击收藏获取收藏的列表，选择收藏类目
# 点击话题/音乐/内容 获取相应的列表信息，并上拉刷新，下拉返回
element.elementclick(driver,900,1050)
time.sleep(1)
# 点击收藏下的内容，音乐，和话题
element.elementclick(driver,540,1180)
time.sleep(1)
element.swipeUp(driver,1000)
time.sleep(1)
element.swipeDown(driver,1000)
time.sleep(1)
element.elementclick(driver,780,1180)
time.sleep(5)

# 发布流程
from publish import publishs
publishs.release(driver)





driver.quit()





