from appium import webdriver


desired_caps = {}   # 用来记录app的信息
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 常见的定位方式 使用位置坐标来定位时间最快 使用方法
# swip滑动事件
#
#   ⚠️从一个坐标位置滑动到另一个坐标位置,只能是两个点之间的滑动
#   方法：swipe(start_x, start_y, end_x, end_y, duration=None)
#   参数：
#       1.start_x：起点X轴坐标
#       2.start_y：起点Y轴坐标
#       3.end_x：  终点X轴坐标
#       4.end_y,： 终点Y轴坐标
#       5.duration： 滑动这个操作一共持续的时间长度，单位：ms



# scroll滑动事件
#
#   ⚠️ 从一个元素滑动到另一个元素，直到页面自动停止
#   方法：scroll(origin_el, destination_el)
#   参数：
#       1.origin_el：滑动开始的元素
#       2.destination_el：滑动结束的元素
#   业务场景：
#       1.进入设置页
#       2.模拟手指从存储菜单位置 到 WLAN菜单位置的上滑操作
#   代码实现：
#       # 定位到存储菜单栏
#       el1 = driver.find_element_by_xpath("//*[contains(@text,'存储')]")
#       # 定位到WLAN菜单栏
#       el2 = driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")
#       # 执行滑动操作
#       driver.scroll(el1,el2)



# drag拖拽事件
#   ⚠️ 从一个元素滑动到另一个元素,第二个元素替代第一个元素原本屏幕上的位置
#   方法：drag_and_drop(origin_el, destination_el)
#   参数：
#       1.origin_el：滑动开始的元素
#       2.destination_el：滑动结束的元素
#   业务场景：
#       1.进入设置页
#       2.模拟手指将存储菜单 滑动到 WLAN菜单栏位置
#   代码实现：
#       # 定位到存储菜单栏
#       el1 = driver.find_element_by_xpath("//*[contains(@text,'存储')]")
#       # 定位到WLAN菜单栏
#       el2 = driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")
#       # 执行滑动操作
#       driver.drag_and_drop(el1,el2)



# 应用置于后台事件
#   APP放置后台，模拟热启动
#   方法：background_app(seconds)
#   参数：
#       1.seconds:停留在后台的时间，单位：秒
#   业务场景：
#       1.进入设置页
#       2.将APP置于后台5s
#   代码实现：
#       driver.background_app(5)
#   效果：
#       app置于后台5s后，再次展示当前页面



# 显示等待，在一定的时间内 判断元素是否存在，如果存在返回定位对象，如果不存在直到超时时间到达，返回超时异常
# 方法:WebDriverWait(driver, timeout, poll_frequency).until(method)
#     参数：
#         1.driver：手机驱动对象
#         2.timeout：搜索超时时间
#         3.poll_frequency：每次搜索间隔时间，默认时间为0.5s
#         4.method：定位方法(匿名函数)
# 代码实现：
# from selenium.webdriver.support.wait import WebDriverWait  # 导入WebDriverWait类
#
# # 超时时间为30s，每隔1秒搜索一次元素是否存在，如果元素存在返回定位对象并退出
# search_button = WebDriverWait(driver, 30, 1).until(lambda x: x.find_elements_by_id(com.android.settings:id / search))
# search_button.click()
# # driver.quit()



#
# 等待操作
#
#   方法：wait(ms=0)
#   参数：
#       ms：暂停的毫秒数
#   业务场景:
#       1.进入设置
#       2.点击WLAN选项
#       3.长按WiredSSID选项5秒
#   代码实现：
#       # 点击WLAN
#       driver.find_element_by_xpath("//*[contains(@text,'WLAN')]").click()
#       # 定位到WiredSSID
#       el =driver.find_element_by_id("android:id/title")
#       # 通过元素定位方式长按元素
#       TouchAction(driver).press(el).wait(5000).perform()

      # TouchAction(driver).press(x=171,y=245).wait(5000).release().perform() ⚠️ 该方法未能完成长按操作，没有报任何错误


# 手指长按操作
#
#   模拟手机按下屏幕一段时间,按就要对应着离开.
#   方法：long_press(el=None, x=None, y=None, duration=1000)
#   参数：
#       1.element：被定位到的元素
#       2.x：通常会使用元素的X轴坐标
#       3.y：通常会使用元素的Y轴坐标
#       4.duration：持续时间，默认为1000ms
#   业务场景:
#       1.进入设置
#       2.点击WLAN选项
#       3.长按WiredSSID选项5秒
#   代码实现：
#       # 点击WLAN
#       driver.find_element_by_xpath("//*[contains(@text,'WLAN')]").click()
#       # 定位到WiredSSID
#       el =driver.find_element_by_id("android:id/title")
#       # 通过元素定位方式长按元素
#       TouchAction(driver).long_press(el,duration=5000).release().perform()
#
#       # 通过坐标方式长按元素，WLAN坐标:x=161,y=242
#       # TouchAction(driver).long_press(x=161,y=242).perform() #


# 手指移动操作
#   模拟手机的滑动操作
#   方法：move_to(el=None, x=None, y=None)
#   参数:
#       1.el:定位的元素
#       2.x:相对于前一个元素的X轴偏移量
#       3.y:相对于前一个元素的Y轴偏移量
#   业务场景1：
#       1.进入设置
#       2.向上滑动屏幕
#     代码实现：
#         # 定位到存储
#         el = driver.find_element_by_xpath("//*[contains(@text,'存储')]")
#         # 定位到更多
#         el1 = driver.find_element_by_xpath("//*[contains(@text,'更多')]")
#         # 元素方式滑动
#         TouchAction(driver).press(el).move_to(el1).release().perform()
#         # 坐标的方式滑动
#         # TouchAction(driver).press(x=240,y=600).wait(100).move_to(x=100,y=100).release().perform()



#
# 操作手机通知栏
#   打开手机的通知栏，可以获取通知栏的相关信息和元素操作
#   方法：open_notifications()
#   业务场景:
#       1.启动设置
#       2.打开通知栏
#   代码实现：
#       driver.open_notifications()

