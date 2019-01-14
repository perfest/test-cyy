# 元素滑动事件 获取界面大小
def getSize(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)


# 屏幕向上滑动
def swipeUp(driver,t):
    l = getSize()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.75)
    y2 = int(l[1] * 0.25)
    driver.swipe(x1, y1, x1, y2, t)

# 屏幕向下滑动
def swipeDown(driver,t):
    l = getSize()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.25)
    y2 = int(l[1] * 0.6)
    driver.swipe(x1, y1, x1, y2, t)

# 屏幕向左滑动
def swipLeft(driver,t):
    l = getSize()
    x1 = int(l[0] * 0.7)
    y1 = int(l[1] * 0.5)
    x2 = int(l[1] * 0.3)
    driver.swipe(x1, y1, x1, x2, t)

# 屏幕向右滑动
def swipRight(driver,t):
    l = getSize()
    x1 = int(l[0] * 0.3)
    y1 = int(l[1] * 0.5)
    x2 = int(l[1] * 0.7)
    driver.swipe(x1, y1, x1, x2, t)


# 坐标定位事件

def elementclick(driver,w,h):
   l=getSize()
   xx = w / l[0]
   yy = h / l[1]
   x1=int(l[0]*xx)
   y1=int(l[1]*yy)
   driver.tap([(x1,y1)])

# 返回我的页面
def rtclick(driver,w,h):
    l = getSize()
    xx = w / l[0]
    yy = h / l[1]
    x1 = int(l[0] * xx)
    y1 = int(l[1] * yy)
    driver.tap([(x1, y1)])

# 分享
def shareclick(driver,w,h):
    l = getSize()
    xx = w / l[0]
    yy = h / l[1]
    x1 = int(l[0] * xx)
    y1 = int(l[1] * yy)
    driver.tap([(x1, y1)])

# 页面中的 X
def xclick(driver, w, h):
    l = getSize()
    xx = w / l[0]
    yy = h / l[1]
    x1 = int(l[0] * xx)
    y1 = int(l[1] * yy)
    driver.tap([(x1, y1)])



