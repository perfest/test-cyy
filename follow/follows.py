import time

# 关注页面的点击事件
def followclick(driver):
    '''点击关注页面，跳转到关注详情列表
    1.用户的头像昵称
    2.是否被关注
    3.更多按钮
    4.ugc封面上的宠物，话题，音乐
    5.关注icon，评论，分享，收藏
    6.主评论输入框
    7.上拉加载新的ugc
    '''
    from public import element
    element.elementclick(driver,300,1880)
    time.sleep(3)
    element.swipeDown(driver, 1000)
    time.sleep(2)
    element.swipeUp(driver, 1000)  # 滑动事件
    time.sleep(1)
    element.swipeDown(driver, 1000)  # 下拉滑动事件
    time.sleep(1)








