from public import element
import time


# 信息中的点击事件
class msg:
    def __init__(self,driver,desired_caps):
        self.driver = driver
        self.desired_caps = desired_caps

    def msgclick(self):
        # 赞列表中的操作事件
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout[4]').click()
        time.sleep(2)
        msg1 = element.validate_id(driver=self.driver,value='com.dealuck.cyy:id/tv_title')
        if msg1 == 'OK':
            print('msg1执行成功 --------%s' % msg1)
        else:
            print('msg1执行失败 --------%s' % msg1)

        self.driver.find_element_by_id('com.dealuck.cyy:id/rl_belike').click()
        time.sleep(2)   # 点击赞
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
        time.sleep(2)    # 点击第三个用户头像，跳转他人主页

        '''
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_share').click()
        time.sleep(3)
        if 'b83ae0c0' == self.desired_caps['deviceName']:
            pass
        if 'LE67A06190312448' == self.desired_caps['deviceName']:
            time.sleep(2)    # 他人主页，点击分享，弹出分享渠道
            self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]').click()
            time.sleep(3)    # 点击微信渠道
            self.driver.find_element_by_id('com.tencent.mm:id/jb').click()
            time.sleep(2)    # 正常跳转，不做操作，直接返回

            self.driver.find_element_by_id('com.dealuck.cyy:id/fl_share').click()
            time.sleep(2)  # 点击他人主页的分享
            self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]').click()
            time.sleep(2)    # 跳转朋友圈
            self.driver.find_element_by_id('com.tencent.mm:id/jb').click()
            time.sleep(2)    # 不做任何操作，返回个人主页
            self.driver.find_element_by_id('com.dealuck.cyy:id/fl_share').click()
        time.sleep(2)     # 点击他人主页的分享
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[3]').click()
        time.sleep(2)     # 点击跳转qq
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout').click()
        time.sleep(2)   # 不做操作返回他人主页

        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_share').click()
        time.sleep(2)  # 点击他人主页的分享
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[4]').click()
        time.sleep(2)   # 点击跳转qq空间
        self.driver.find_element_by_id('com.tencent.mobileqq:id/ivTitleBtnLeftButton').click()
        time.sleep(2)
        '''
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_share').click()
        time.sleep(2)  # 点击他人主页的分享
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]').click()
        time.sleep(2)   # 点击跳转复制连接

        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_share').click()
        time.sleep(2)  # 点击他人主页的分享
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]').click()
        time.sleep(2)    # 点击跳转二维码
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_close').click()
        time.sleep(2)

        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_share').click()
        time.sleep(2)  # 点击他人主页的分享
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]').click()
        time.sleep(2)  # 点击跳转二维码 保存本地
        self.driver.find_element_by_id('com.dealuck.cyy:id/ll_save').click()
        time.sleep(2)
        print('他人主页分享页点击完毕，现在停留在他人主页')

        self.driver.find_element_by_id('com.dealuck.cyy:id/ll_focus').click()
        time.sleep(2)    # 他人主页的关注按钮
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.ImageView').click()
        time.sleep(2)    # 点击头像跳转至他人主页
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_back').click()
        time.sleep(2)    # 点击返回至他人关注页

        # self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView').click()
        # time.sleep(2)    # 点击关注
        text_name = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView').text
        if text_name=='关注':          # text 这个方法不能加括号
            self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView').click()
            time.sleep(2)
        else:
            self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView').click()
            time.sleep(2)
            self.driver.find_element_by_id('com.dealuck.cyy:id/tv_cancel').click()
            time.sleep(2)   # 点击取消

        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_left').click()
        time.sleep(2)    # 点击返回他人主页

        self.driver.find_element_by_id('com.dealuck.cyy:id/ll_fans').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.ImageView').click()
        time.sleep(2)   # 点击用户头像跳转他人主页
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_back').click()
        time.sleep(2)   # 返回至他的粉丝列表页
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_left').click()
        time.sleep(2)    # 返回 至他人主页

        text_name2 = self.driver.find_element_by_id('com.dealuck.cyy:id/tv_follow').text
        time.sleep(2)       # 这里他人主页。点击关注这个位置需要做修改
        if text_name2=='关注':
            self.driver.find_element_by_id('com.dealuck.cyy:id/btn_follow').click()
            time.sleep(2)
        else:
            self.driver.find_element_by_id('com.dealuck.cyy:id/btn_follow').click()
            time.sleep(2)
            self.driver.find_element_by_id('com.dealuck.cyy:id/tv_cancel').click()
            time.sleep(2)

        # self.driver.find_element_by_id('com.dealuck.cyy:id/iv_left').click()
        # time.sleep(2)     # 返回他人主页
        # print('他人粉丝页点击完毕')
        self.driver.find_element_by_id('com.dealuck.cyy:id/ll_like').click()
        time.sleep(2)   # 他人主页的获赞按钮
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_ok').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.dealuck.cyy:id/multi_header_view').click()
        time.sleep(2)   # 他人主页的宠物卡片按钮
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_close').click()
        time.sleep(2)

        # follws=self.driver.find_elements_by_calss_name('android.widget.ImageView')
        # for i in range(2):
        #     follws[i].click()
        #     time.sleep(2)
        # print('作品列表页，点赞第一个和第二个')

        # 一下实现作品详情页，的广度图
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.TextView[1]').click()
        time.sleep(2)   # 他人主页作品列表点击
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.ImageView[2]').click()
        time.sleep(2)   # 点击作品列表第一个ugc
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
        time.sleep(2)   # 从作品详情页返回至个人主页
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.ImageView[2]').click()
        time.sleep(2)


        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_header').click()
        time.sleep(2)    # 点击头像跳转至他人主页
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_back').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.dealuck.cyy:id/ll_user').click()
        time.sleep(2)      # 跳转用户个人主页
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_back').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_more').click()
        time.sleep(2)   # 点击更多
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_cancel').click()
        time.sleep(2)   # 点击取消
        self.driver.swipe(300,1000,300,400,3000)    # 向上滑动  持续3秒
        time.sleep(2)
        # 需要注意的是这里点击的ugc详情页话题，可能有些ugc上没有话题品种地址之类的标签
        # self.driver.find_element_by_id('com.dealuck.cyy:id/ll_topic').click()
        # time.sleep(2)    # 滑动以后点击话题进入详情页   话题页，上部是一整个view  无法获取返回按钮

        # self.driver.find_element_by_id('com.dealuck.cyy:id/ll_tags').click()
        # time.sleep(2)   # 点击品种  现在品种页，无法获取页面上的返回按钮

        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_summary').click()
        time.sleep(2)    # 点击全文
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_summary').click()
        time.sleep(2)  # 再次点击全文，收起全文展示

        self.driver.find_element_by_id('com.dealuck.cyy:id/rl_comment').send_keys(u"7654321")
        time.sleep(2)    # 点击页面输入框
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_send').click()
        time.sleep(2)   # 发送

        self.driver.find_element_by_id('com.dealuck.cyy:id/ll_comment').click()
        time.sleep(2)   # 点击评论
        '''这里的send_keys需要在做校验'''
        # self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]').click()
        # time.sleep(2)   # 对第一条评论点赞
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.FrameLayout').click()
        time.sleep(2)   # 点击第一条评论的用户头像
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_back').click()
        time.sleep(2)   # 返回

        # self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout').click()
        # time.sleep(2)   # 点击评论内的输入框
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView').click()
        time.sleep(2)   # 评论内部点击‘发送’同样调起评论输入框
        self.driver.find_element_by_id('com.dealuck.cyy:id/et_comment').send_keys(u'1234567')
        time.sleep(2)
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_send').click()
        time.sleep(2)    # 发送

        # self.driver.find_element_by_id('com.dealuck.cyy:id/ll_like').click()
        # time.sleep(2)     # 点赞或取消点赞
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_comment_close').click()
        time.sleep(2)     # 点击X返回至作品详情列表页

        self.driver.find_element_by_id('com.dealuck.cyy:id/ll_share').click()
        time.sleep(2)     # 点击分享弹框
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_cancel').click()
        time.sleep(2)   # 取消
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
        time.sleep(2)  # 返回
        ''' 这里没有返回'''

        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.TextView[2]').click()
        time.sleep(2)   # 他人主页，赞过列表点击
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout').click()
        time.sleep(2)   # 赞过列表下第一个作品详情

        # 节点
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_header').click()
        time.sleep(2)  # 点击头像跳转至他人主页
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_back').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.dealuck.cyy:id/ll_user').click()
        time.sleep(2)  # 跳转用户个人主页
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_back').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_more').click()
        time.sleep(2)  # 点击更多
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_cancel').click()
        time.sleep(2)  # 点击取消
        self.driver.swipe(300, 1000, 300, 400, 3000)  # 向上滑动  持续3秒
        time.sleep(2)
        # 需要注意的是这里点击的ugc详情页话题，可能有些ugc上没有话题品种地址之类的标签
        # self.driver.find_element_by_id('com.dealuck.cyy:id/ll_topic').click()
        # time.sleep(2)    # 滑动以后点击话题进入详情页   话题页，上部是一整个view  无法获取返回按钮

        # self.driver.find_element_by_id('com.dealuck.cyy:id/ll_tags').click()
        # time.sleep(2)   # 点击品种  现在品种页，无法获取页面上的返回按钮

        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_summary').click()
        time.sleep(2)  # 点击全文
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_summary').click()
        time.sleep(2)  # 再次点击全文，收起全文展示

        self.driver.find_element_by_id('com.dealuck.cyy:id/rl_comment').send_keys(u'000')
        time.sleep(2)  # 点击页面输入框

        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_send').click()
        time.sleep(2)  # 发送

        self.driver.find_element_by_id('com.dealuck.cyy:id/ll_comment').click()
        time.sleep(2)  # 点击评论

        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView').click()
        time.sleep(2)  # 评论内部点击‘发送’同样调起评论输入框
        self.driver.find_element_by_id('com.dealuck.cyy:id/et_comment').send_keys(u'999')
        time.sleep(2)
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_send').click()
        time.sleep(2)  # 发送

        # self.driver.find_element_by_id('com.dealuck.cyy:id/ll_like').click()
        # time.sleep(2)  # 点赞或取消点赞
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_comment_close').click()
        time.sleep(2)  # 点击X返回至作品详情列表页

        self.driver.find_element_by_id('com.dealuck.cyy:id/ll_share').click()
        time.sleep(2)  # 点击分享弹框
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_cancel').click()
        time.sleep(2)  # 取消
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
        time.sleep(2)  # 返回

        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_back').click()
        time.sleep(2)  # 他人主页，的返回按钮

        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.ImageView[2]').click()
        time.sleep(2)  # 点击作品image跳转 ugc详情页
        element.swipeUp(driver=self.driver, t=5000)
        time.sleep(2)
        for i in range(10):
            if 'OK' == element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/rl_comment'):
                break
            else:
                element.swipeDown(driver=self.driver, t=3000)
                time.sleep(3)
                print('当前是第 --%d--循环' % i)
        time.sleep(2)
        self.driver.find_element_by_id('com.dealuck.cyy:id/rl_comment').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.dealuck.cyy:id/et_comment').send_keys(u'666')
        time.sleep(2)
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_send').click()
        time.sleep(2)  # 发布评论
        self.driver.find_element_by_id('com.dealuck.cyy:id/ll_comment').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.dealuck.cyy:id/et_comment').send_keys(u'111')
        time.sleep(2)
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_send').click()
        time.sleep(2)  # 点击评论，发送评论

        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[2]').click()
        time.sleep(2)  # 点赞/取消点赞
        self.driver.find_element_by_id('com.dealuck.cyy:id/ll_share').click()
        time.sleep(2)  # 分享
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_cancel').click()
        time.sleep(2)  # 取消
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout/android.widget.LinearLayout[2]').click()
        time.sleep(2)  # 评论点赞
        msg2 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/ll_replay')
        if msg2 == 'OK':
            self.driver.find_element_by_id('com.dealuck.cyy:id/ll_replay').click()  # 点击重播按钮
            print('让视频播放一会儿 msg2执行成功 ------ %s' % msg2)
            time.sleep(10)
        else:
            print('界面上没有重播按钮不做操作')

        msg3 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/ll_title_user')
        if msg3 == 'OK':
            print('msg3执行成功，顶部昵称显示----------%s ' % msg3)
        else:
            print('msg3 执行失败----------------%s ' % msg3)

        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
        time.sleep(2)  # 返回至赞列表下
        msg4 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_bar_title')
        if msg4 == 'OK':
            print('msg4执行成功----------%s ' % msg4)
        else:
            print('msg4执行失败----------%s ' % msg4)

        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_bar_left').click()
        time.sleep(2)  # 返回消息主页
        msg5 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_sys_title')
        if msg5 == 'OK':
            print('msg5执行成功----------%s ' % msg5)
        else:
            print('msg5执行失败----------%s ' % msg5)
        print('当前停留在消息主页')

        self.driver.find_element_by_id('com.dealuck.cyy:id/rl_fans').click()
        time.sleep(2)  # 点粉丝     对次列表只做 跳转他人用户主页，和关注/取消关注
        msg6 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_title')
        if msg6 == 'OK':
            print('msg6执行成功----------%s ' % msg6)
        else:
            print('msg6执行失败----------%s ' % msg6)

        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.ImageView').click()
        time.sleep(2)  # 头像
        msg7 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/fl_share')
        if msg7 == 'OK':
            print('msg7执行成功----------%s ' % msg7)
        else:
            print('msg7执行失败----------%s ' % msg7)

        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_back').click()
        time.sleep(2)
        msg8 = self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView').text
        if msg8 == '关注':
            self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView').click()
            time.sleep(2)
            msg9 = self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView').text
            if msg9 == '已关注' or '互关注':
                print('msg9 执行成功---------%s' % msg9)
            else:
                print('msg9执行失败')
        else:
            self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView').click()
            time.sleep(2)
            msg10 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_ok')
            if msg10 == 'OK':
                print('msg10执行成功----------%s' % msg10)
            else:
                print('msg10执行失败----------%s' % msg10)
            self.driver.find_element_by_id('com.dealuck.cyy:id/tv_cancel').click()
            time.sleep(2)  # 点击取消
            self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView').click()
            time.sleep(2)
            self.driver.find_element_by_id('com.dealuck.cyy:id/tv_ok').click()
            time.sleep(2)  # 对当前用户 取消关注

        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_left').click()
        time.sleep(2)  # 返回至消息主页

        self.driver.find_element_by_id('com.dealuck.cyy:id/rl_comment').click()
        time.sleep(2)  # 点击评论
        msg11 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_bar_title')
        if msg11 == 'OK':
            print('msg11执行成功--------%s' % msg11)
        else:
            print('msg11执行失败--------%s' % msg11)

        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
        time.sleep(2)  # 点击第一条评论的头像
        msg14 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/title_container')
        if 'OK' == msg14:
            print('msg14执行成功----------%s' % msg14)
        else:
            print('msg14执行失败----------%s' % msg14)
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_back').click()
        time.sleep(2)  # 返回至评论列表页

        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.ImageView[2]').click()
        time.sleep(2)  # 点击评论的详情
        for i in range(10):
            msg15 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/load_more_load_end_view')
            if 'OK' == msg15:
                print('msg15执行成功----------%s' % msg15)
                break
            else:
                element.swipeUp(driver=self.driver, t=3000)
                time.sleep(3)
                print('msg15第 --%d 执行失败----------%s' % (i, msg15))
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
        time.sleep(2)  # 返回至评论列表页
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_bar_left').click()
        time.sleep(2)  # 返回消息主页

        print('当前停留在消息列表页下的评论列表页')

        self.driver.find_element_by_id('com.dealuck.cyy:id/rl_helper').click()
        time.sleep(2)  # 点通知消息
        msg12 = element.validate_xpath(driver=self.driver,
                                       value='/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[1]')
        if msg12 == 'OK':
            print('msg12执行成功--------%s' % msg12)
        else:
            print('msg12执行失败--------%s' % msg12)

        '''
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_cover').click()
        time.sleep(2)  # 点击推送的ugc
        msg13 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/ll_like')
        if 'OK' == msg13:
            print('msg13执行成功-----------%s' % msg13)
        else:
            print('msg13执行失败-----------%s' % msg13)

        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
        time.sleep(2)  # 返回通知消息页
        element.swipeUp(driver=self.driver, t=5000)
        element.swipeUp(driver=self.driver, t=5000)
        element.swipeUp(driver=self.driver, t=5000)
        element.swipeDown(driver=self.driver, t=5000)
        '''
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_left').click()
        time.sleep(2)  # 返回消息主页

        print('消息页点击测试执行完毕')




