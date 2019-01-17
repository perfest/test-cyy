
import time
# 信息中的点击事件
def messageclick(driver):
    '''信息模块下的点击事件
    1.点赞，获取点赞的列表，可向上拉，加载更多
    2.粉丝，获取当前用户的粉丝
    3.评论，获取当前用户的评论或被评论
    4.系统消息
    5.系统公告
    '''
    # 1.点赞
    from public import element
    element.elementclick(driver,950,1850)
    time.sleep(1)
    element.elementclick(driver,200,400)
    time.sleep(1)
    # 向上拉动查看事件 次数自定义
    element.swipeUp(driver,1000)
    time.sleep(1)
    '''点击头像跳转个人主页位置
        点击热点区跳转到详情页面     评论详情页/作品详情页
        评论页下拉可以刷新
        判断有子评论，点击子评论区域可以跳转子评论主页
        点击评论内容调起键盘/回复输入框
        点赞评论  icon 高亮 ➕1
    '''
    element.swipeDown(driver,1000)
    time.sleep(1)
    element.elementclick(driver,100,350) # 用户头像
    time.sleep(1)
    element.elementclick(driver,35,180)
    time.sleep(1)
    element.elementclick(driver,300,330) # 用户昵称
    time.sleep(1)
    element.elementclick(driver,35,180)
    time.sleep(1)
    element.elementclick(driver,300,400) # 点赞了你的评论/作品
    time.sleep(1)
    element.elementclick(driver,35,180)
    time.sleep(1)
    element.elementclick(driver,1000,350) # 热点区，跳转评论/作品详情页
    time.sleep(1)
    element.elementclick(driver,35,180)
    time.sleep(3)


