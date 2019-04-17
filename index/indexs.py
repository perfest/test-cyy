import time
from public import element
from public import info

# 首页点击事件
class indexclick:
    # 首页点击事件
    def __init__(self,driver,desired_caps):
        self.driver = driver
        self.desired_caps = desired_caps

    def indclick(self):
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]').click()
        time.sleep(3)   # 首页
        ind1 = element.validate_id(self.driver,'com.dealuck.cyy:id/ll_top')
        if 'OK' == ind1:
            print('ind1执行成功-------%s' % ind1)
        else:
            print('ind1执行失败-------%s' % ind1)

        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_scan').click()
        time.sleep(3)   # 扫一扫
        inde = info.infos(self.driver)
        inde.syis()

        self.driver.find_element_by_id('com.dealuck.cyy:id/rl_search').click()
        time.sleep(3)     # 搜索
        inde.es()

        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.view.ViewGroup/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.view.ViewGroup/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click()
        time.sleep(3)  # 用户头像
        ind22 = element.validate_id(self.driver, 'com.dealuck.cyy:id/magic_indicator')
        if 'OK' == ind22:
            print('ind22当前ugc作者是我关注的用户-----%s' % ind22)
        else:
            print('ind22当前ugc作者不是我关注的用户---%s' % ind22)
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_back').click()
        time.sleep(3)  # 返回

        if 'LE67A06190312448' == self.desired_caps['deviceName']:
            if 'OK' == element.validate_xpath(self.driver,
                                              '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.view.ViewGroup/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.view.ViewGroup/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[2]'):
                self.driver.find_element_by_xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.view.ViewGroup/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.view.ViewGroup/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[2]').click()
                time.sleep(3)  # 点赞
            else:
                pass
        elif 'b83ae0c0' == self.desired_caps['deviceName']:
            if 'OK' == element.validate_xpath(self.driver,
                                              '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.view.ViewGroup/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.view.ViewGroup/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout[2]'):
                self.driver.find_element_by_xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.view.ViewGroup/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.view.ViewGroup/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout[2]').click()
                time.sleep(2)  # 正序点击tab
            else:
                pass

        c = 1
        while c < 2:
            for i in range(1, 8):
                if 'LE67A06190312448' == self.desired_caps['deviceName']:
                    self.driver.find_element_by_xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.TextView[%d]' % i).click()

                    time.sleep(2)  # 正序点击tab
                    print('当前点击第 %s 个' % i)
                elif 'b83ae0c0' == self.desired_caps['deviceName']:
                    self.driver.find_element_by_xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.TextView[%d]' % i).click()
                    time.sleep(2)  # 正序点击tab
                    print('当前点击第 %s 个' % i)
            d = 6
            for m in range(1, 5):
                if 'LE67A06190312448' == self.desired_caps['deviceName']:
                    self.driver.find_element_by_xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.TextView[%d]' % (
                            d - m)).click()
                    time.sleep(2)  # 倒序点击tab
                    print('当前点击第 %s 个' % m)
                elif 'b83ae0c0' == self.desired_caps['deviceName']:
                    self.driver.find_element_by_xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.TextView[%d]' % (
                            d - m)).click()
                    time.sleep(2)  # 倒序点击tab
                    print('当前点击第 %s 个' % m)
            c += 1
        inde.validate_ugc()  # 校验确保是视频

        ind17 = element.validate_id(self.driver, 'com.dealuck.cyy:id/ll_bgm')
        if 'OK' == ind17:
            print('ind17当前页面有音乐存在----%s' % ind17)
            self.driver.find_element_by_id('com.dealuck.cyy:id/ll_bgm').click()
            time.sleep(3)  # 有音乐存在
            self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
            time.sleep(2)  # 返回  音乐详情后期在➕
        else:
            print('ind17当前页面没有音乐存在----%s' % ind17)

        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_more').click()
        time.sleep(3)  # 更多
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_cancel').click()
        time.sleep(2)  # 取消弹框

        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_header').click()
        time.sleep(3)  # 用户头像
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_back').click()
        time.sleep(3)  # 返回ugc详情页

        ind18 = element.validate_id(self.driver, 'com.dealuck.cyy:id/tv_follow')
        if 'OK' == ind18:
            print('ind18当前ugc的作者未关注他，现在关注-------%s' % ind18)
            self.driver.find_element_by_id('com.dealuck.cyy:id/tv_follow').click()
            time.sleep(2)  # 未关注的关注按钮
        else:
            print('ind18当前ugc的作者已经关注，页面没有关注-----%s' % ind18)

        ind19 = element.validate_id(self.driver, 'com.dealuck.cyy:id/ll_commodity')
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
        ind20 = element.validate_xpath(self.driver,
                                       '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout/android.widget.LinearLayout[2]')
        if 'OK' == ind20:
            self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout/android.widget.LinearLayout[2]').click()
            time.sleep(3)  # 评论点赞
        else:
            pass
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_comment_close').click()
        time.sleep(3)  # 取消

        self.driver.find_element_by_id('com.dealuck.cyy:id/ll_like').click()
        time.sleep(2)  # 点赞

        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
        time.sleep(2)  # 返回

        ind21 = element.validate_id(self.driver, 'com.dealuck.cyy:id/tv_follow')
        # 校验当前ugc的作者是否是我关注的人
        if 'OK' == ind21:
            print('ind21当前ugc作者是我关注的用户-----%s' % ind21)
        else:
            print('ind21当前ugc作者不是我关注的用户---%s' % ind21)

        print('当前还是停留在首页')




