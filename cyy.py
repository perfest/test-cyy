import time

from appium import webdriver

'''
android  这个在个手机中是通用的，需要考虑的是，在不同的手机中，微信qq有分身的。需要做区分
消息，赞列表下，第一个不能自己本人
'''
start_time = time.time()

desired_caps = {}  # 设备信息
desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '6.0'
# desired_caps['deviceName'] = 'LE67A06190312448'     # 乐视
# desired_caps['platformVersion'] = '9'
# desired_caps['deviceName'] = 'UYT7N17A05000497'      # 华为 9.0
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'b83ae0c0'       # 小米
# desired_caps['platformVersion'] = '8.1'
# desired_caps['deviceName'] = 'M7BBB18A03150918'      # 华为 8.1
# desired_caps['platformVersion'] = '8.1'
# desired_caps['deviceName'] = 'c6ab25900205'      # 红米
# app信息    微信i
desired_caps['appPackage'] = 'com.tencent.mm'
desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'

# desired_caps["resetKeyboard"] = True
# desired_caps["unicodeKeyboard"] = True          # 频闭手机的自带输入法，调用appium的输入法。出现乱码，加u“你好”

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
print(getSize())

swipLeft(1000)
time.sleep(2)
swipLeft(1000)
time.sleep(2)

time.sleep(10)


# 点击关注
# driver.find_element_by_xpath("//*[contains(@text,'关注'))]")
x = driver.get_window_size()['width']  # 获取屏幕的宽度，x的最大值
y = driver.get_window_size()['height']  # 获取屏幕的高度，y的最大值
a1 = 329 / x
b1 = 1831 / y

time.sleep(10)



# from information import demo
# driv = demo.test_demo(driver,desired_caps)
# driv.demos()

from my_index import my
dr = my.Myclick(driver,desired_caps)
dr.Myindex()

from information import message
drive = message.msg(driver,desired_caps)
drive.msgclick()

from topic import topics
dri = topics.topic_top(driver,desired_caps)
dri.topic_topic()

from index import indexs
driv = indexs.indexclick(driver)
driv.indclick()


end_time = time.time()
cont_time = end_time - start_time
print('页面点击耗时 ------%f' % cont_time)
driver.quit()








'''
在单个view中，如果长度超过了当前屏幕的宽度，
当前列表的会重新加载12345，不会紧跟之前结束的6789这样
'''





'''

driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout[5]').click()

time.sleep(2)
driver.find_element_by_id('com.dealuck.cyy:id/editPhone').send_keys("13666666666")
time.sleep(2)
driver.find_element_by_id('com.dealuck.cyy:id/btnNextStep').click()
time.sleep(2)
driver.find_element_by_id('com.dealuck.cyy:id/et_code').send_keys("11111")
time.sleep(2)
# 点击登陆
driver.find_element_by_id('com.dealuck.cyy:id/btnLogin').click()
time.sleep(5)

print('------------------------ok-------------------------')

# 信息模块点击事件
from information import message
driv = message.msg(driver)
driv.msgclick()

end_time = time.time()
cont_time = end_time - start_time
print('消息页点击耗时 ------%f' % cont_time)

# 我的模块点击事件
from my_index import my
dr = my.Myclick(driver)
dr.Myindex()

# 跳转首页节奏上有问题设置页面还是没有退出
# from index import indexs
# dri = indexs.indexclick(driver)
# dri.pbclick()

print('点击事件完成')
driver.quit()



'''
