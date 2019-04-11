import time
from public import info



class test_demo:
    def __init__(self,driver,desired_caps):
        self.driver = driver
        self.desired_caps = desired_caps

    def demos(self):
        from public import element

        ind23 = element.validate_id(self.driver,'com.dealuck.cyy:id/iv_cover_play')
        if 'OK' == ind23:
            print('ind23是视频------%s' % ind23)
            self.driver.find_element_by_id('com.dealuck.cyy:id/iv_cover_play').click()
            time.sleep(3)   # 确保是视频
        else:

            while True:
                element.swipeUp(self.driver,2000)
                time.sleep(5)

                if 'OK' == element.validate_id(self.driver,'com.dealuck.cyy:id/iv_cover_play'):
                    self.driver.find_element_by_id('com.dealuck.cyy:id/iv_cover_play').click()
                    time.sleep(2)
                    break
                else:
                    pass
        ind17 = element.validate_id(self.driver,'com.dealuck.cyy:id/ll_bgm')
        if 'OK' == ind17:
            print('ind17当前页面有音乐存在----%s' % ind17)
            self.driver.find_element_by_id('com.dealuck.cyy:id/ll_bgm').click()
            time.sleep(3)  # 有音乐存在
            self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
            time.sleep(2)   # 返回  音乐详情后期在➕
        else:
            print('ind17当前页面没有音乐存在----%s' % ind17)

        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_more').click()
        time.sleep(3)  # 更多
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_cancel').click()
        time.sleep(2)   # 取消弹框

        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_header').click()
        time.sleep(3)     # 用户头像
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_back').click()
        time.sleep(3)    # 返回ugc详情页

        ind18 = element.validate_id(self.driver,'com.dealuck.cyy:id/tv_follow')
        if 'OK' == ind18:
            print('ind18当前ugc的作者未关注他，现在关注-------%s' % ind18)
            self.driver.find_element_by_id('com.dealuck.cyy:id/tv_follow').click()
            time.sleep(2)    # 未关注的关注按钮
        else:
            print('ind18当前ugc的作者已经关注，页面没有关注-----%s' % ind18)

        ind19 = element.validate_id(self.driver,'com.dealuck.cyy:id/ll_commodity')
        if 'OK' == ind19:
            print('ind19当前ugc有商品-------%s' % ind19)
            self.driver.find_element_by_id('com.dealuck.cyy:id/ll_commodity').click()
            time.sleep(2)  # 商品标签
            '''正文'''
        else:
            print('ind19当前ugc无商品-------%s' % ind19)

        # self.driver.find_element_by_id('com.dealuck.cyy:id/rl_comment').click()
        # time.sleep(2)    #  评论输入框

        self.driver.find_element_by_id('com.dealuck.cyy:id/ll_comment').click()
        time.sleep(3)  # 评论
        ind20 = element.validate_xpath(self.driver,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout/android.widget.LinearLayout[2]')
        if 'OK' == ind20:
            self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout/android.widget.LinearLayout[2]').click()
            time.sleep(3)   # 评论点赞
        else:
            pass
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_comment_close').click()
        time.sleep(3)  # 取消

        self.driver.find_element_by_id('com.dealuck.cyy:id/ll_like').click()
        time.sleep(2)    # 点赞

        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
        time.sleep(2)   # 返回

        ind21 = element.validate_id(self.driver, 'com.dealuck.cyy:id/tv_follow')
        # 校验当前ugc的作者是否是我关注的人
        if 'OK' == ind21:
            print('ind21当前ugc作者是我关注的用户-----%s' % ind21)
        else:
            print('ind21当前ugc作者不是我关注的用户---%s' % ind21)

        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.view.ViewGroup/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.view.ViewGroup/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click()
        time.sleep(3)  # 用户头像
        ind22 = element.validate_id(self.driver,'com.dealuck.cyy:id/magic_indicator')
        if 'OK' == ind22:
            print('ind22当前ugc作者是我关注的用户-----%s' % ind22)
        else:
            print('ind22当前ugc作者不是我关注的用户---%s' % ind22)
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_back').click()
        time.sleep(3)   # 返回

        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.view.ViewGroup/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.view.ViewGroup/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[2]').click()
        time.sleep(3)  # 点赞

