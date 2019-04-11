import time
# 元素滑动事件 获取界面大小
def getSize(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)


# 屏幕向上滑动
def swipeUp(driver,t):
    l = getSize(driver)
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.75)
    y2 = int(l[1] * 0.25)
    driver.swipe(x1, y1, x1, y2, t)

# 屏幕向下滑动
def swipeDown(driver,t):
    l = getSize(driver)
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.25)
    y2 = int(l[1] * 0.7)
    driver.swipe(x1, y1, x1, y2, t)

# 屏幕向左滑动
def swipLeft(driver,t):
    l = getSize(driver)
    x1 = int(l[0] * 0.7)
    y1 = int(l[1] * 0.5)
    x2 = int(l[1] * 0.05)
    driver.swipe(x1, y1, x1, x2, t)

# 屏幕向右滑动
def swipRight(driver,t):
    l = getSize(driver)
    x1 = int(l[0] * 0.05)
    y1 = int(l[1] * 0.5)
    x2 = int(l[1] * 0.7)
    driver.swipe(x1, y1, x1, x2, t)


# 坐标定位事件
def elementclick(driver,w,h):
   l=getSize(driver)
   xx = w / l[0]
   yy = h / l[1]
   x1=int(l[0]*xx)
   y1=int(l[1]*yy)
   driver.tap([(x1,y1)])


# 滑动事件
def swipe_up(driver):
    swipeUp(driver,1000)
    time.sleep(3)
    swipeDown(driver,1000)
    time.sleep(3)
    swipeDown(driver, 1000)
    time.sleep(3)
    swipeDown(driver, 1000)
    time.sleep(3)
    swipeUp(driver, 1000)
    time.sleep(3)
    swipeUp(driver, 1000)
    time.sleep(3)
    swipeUp(driver, 1000)
    time.sleep(3)

def validate_id(driver, value):
    ls = driver.find_elements_by_id(value)
    if 0 == len(ls):
        return 'NG'
    else:
        return 'OK'

def validate_class(driver, value):
    ll = driver.find_elements_by_calss_name(value)
    if 0 == len(ll):
        return 'NG'
    else:
        return 'OK'

def validate_xpath(driver, value):
    xp = driver.find_elements_by_xpath(value)
    if 0 == len(xp):
        return 'NG'
    else:
        return 'OK'


'''
1、消息，单视频详情页
2、消息，单图文详情页
3、图文视频混合页
4、图文详情列表页
5、沉浸式详情页
6、品种详情页
'''

