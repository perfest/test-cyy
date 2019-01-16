import time

# 首页点击事件
def indexclick(driver):
    from public import element
    element.elementclick(driver,115,1836)  # 点击首页
    print('开始首页点击滑动事件')
    list = [(100,200),(250,200),(450,200),(620,200),(770,200),(930,200)]
    for i in list:
        element.elementclick(driver,i[0],i[1])
        time.sleep(2)
        element.swipeUp(driver, 1000)  # 滑动事件
        time.sleep(1)
        element.swipeDown(driver,1000)  # 下拉滑动事件
        time.sleep(1)
    ''' 点击搜索框 send_keys
        添加滑动事件，左右和上下滑动   点击取消返回首页  
    '''

    print('马上点击搜索框')
    element.elementclick(driver,450,320)
    # driver.find_element_by_name('踩奶大作战').send_kesy('一百万')
    time.sleep(3)
    element.elementclick(driver,985,150)
    time.sleep(1)
    print('开始左右滑动事件')
    for i in range(5):
        element.swipLeft(driver,1000)
        time.sleep(1)

    for s in range(5):
        element.swipRight(driver,1000)
        time.sleep(1)
    print('首页完成点击滑动事件')

