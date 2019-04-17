import time
from public import element
from public import info


# 关注页面的点击事件
class topic_top:
    def __init__(self,driver,desired_caps):
        self.desired_caps = desired_caps
        self.driver = driver

    def topic_topic(self):
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]').click()
        time.sleep(2)  # 点击话题
        pic1 = element.validate_xpath(driver=self.driver,
                                      value='/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout')
        if 'OK' == pic1:
            print('pic1执行成功---------%s ' % pic1)
        else:
            print('pic1执行失败---------%s ' % pic1)

        self.driver.find_element_by_id('com.dealuck.cyy:id/rl_search').click()
        time.sleep(2)  # 搜索
        pic2 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_cancel')
        if 'OK' == pic2:
            print('pic2执行成功---------%s ' % pic2)
        else:
            print('pic2执行失败---------%s ' % pic2)

        self.driver.find_element_by_id('com.dealuck.cyy:id/rl_hot_keyword').click()
        time.sleep(2)  # 热门搜索
        pic3 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/iv_bg')
        if 'OK' == pic3:
            print('pic3执行成功---------%s ' % pic3)
        else:
            print('pic3执行失败---------%s ' % pic3)
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
        time.sleep(2)  # 返回搜索页面

        self.driver.find_element_by_id('com.dealuck.cyy:id/rl_hot_keyword').click()
        time.sleep(2)  # 搜索
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]').click()
        time.sleep(2)  # 点击热搜榜排名第一的热词
        for i in range(1, 5):
            self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.TextView[%d]' % i).click()
            time.sleep(2)  # 点击搜索页的tab
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.TextView[1]').click()
        time.sleep(2)  # 点击综合
        if 'OK' == element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/rl_ugc'):
            self.driver.find_element_by_id('com.dealuck.cyy:id/rl_ugc').click()
            time.sleep(2)  # 点击内容，进入内容tab下
            self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').click()
            time.sleep(8)  # 点击内容tab下的第一个ugc
            self.driver.find_element_by_id('com.dealuck.cyy:id/iv_more').click()
            time.sleep(2)  # 点击更多，弹框提示分享渠道
            pic5 = element.validate_xpath(driver=self.driver,
                                          value='/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]')
            if 'OK' == pic5:
                print('pic5执行成功--------%s' % pic5)
            else:
                print('pic5执行失败--------%s' % pic5)
            self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]').click()
            time.sleep(2)  # 收藏
            self.driver.find_element_by_id('com.dealuck.cyy:id/iv_more').click()
            time.sleep(2)  # 点击更多，弹框提示分享渠道
            self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[3]').click()
            time.sleep(2)  # 下载视频
            pic6 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/rl_tips')
            if 'OK' == pic6:
                print('pic6执行成功--------%s' % pic6)
            else:
                print('pic6执行失败--------%s' % pic6)
            time.sleep(8)
            self.driver.find_element_by_id('com.dealuck.cyy:id/iv_more').click()
            time.sleep(2)  # 点击更多，弹框提示分享渠道
            self.driver.find_element_by_xpath(
                '	/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[4]').click()
            time.sleep(2)  # 举报
            pic7 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_title')
            time.sleep(2)
            if 'OK' == pic7:
                print('pic7执行成功--------%s' % pic7)
            else:
                print('pic7执行失败--------%s' % pic7)
            self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RadioButton').click()
            time.sleep(2)  # 选中选项
            self.driver.find_element_by_id('com.dealuck.cyy:id/tv_submit').click()
            time.sleep(2)  # 提交举报

            if 'OK' == element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_follow'):
                self.driver.find_element_by_id('com.dealuck.cyy:id/tv_follow').click()
                time.sleep(2)
            else:
                pass

            self.driver.find_element_by_id('com.dealuck.cyy:id/fl_header').click()
            time.sleep(2)  # 点击用户头像跳转他人主页
            pic8 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/title_container')
            if 'OK' == pic8:
                print('pic8执行成功--------%s' % pic8)
            else:
                print('pic8执行失败--------%s' % pic8)
            self.driver.find_element_by_id('com.dealuck.cyy:id/fl_back').click()
            time.sleep(2)  # 返回视频页

            pic30 = element.validate_id(self.driver, 'com.dealuck.cyy:id/fl_article')
            if 'OK' == pic30:
                self.driver.find_element_by_id('com.dealuck.cyy:id/fl_article').click()
                time.sleep(2)  # 点击正文跳转
            else:
                self.driver.find_element_by_id('com.dealuck.cyy:id/ll_commodity').click()
                time.sleep(2)  # 收起商品展示
                self.driver.find_element_by_id('com.dealuck.cyy:id/fl_article').click()
                time.sleep(2)  # 点击正文跳转
            pic9 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/ll_title_user')
            if 'OK' == pic9:
                print('pic9执行成功--------%s' % pic9)
            else:
                print('pic9执行失败--------%s' % pic9)
            self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
            time.sleep(2)  # 返回视频页

            self.driver.find_element_by_id('com.dealuck.cyy:id/ll_like').click()
            time.sleep(2)  # 点赞
            '''分享变成微信/朋友圈，后面再处理'''
            self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
            time.sleep(2)  # 返回搜索主页
        elif 'OK' == element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/rl_topic'):
            self.driver.find_element_by_id('com.dealuck.cyy:id/rl_topic').click()
            time.sleep(2)  # 点击话题，进入话题tab下
        elif 'OK' == element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/rl_user'):
            self.driver.find_element_by_id('com.dealuck.cyy:id/rl_user').click()
            time.sleep(2)  # 点击用户，进入用户tab下
        else:
            print('热搜词没有内容不合理----------')

        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_clear').click()
        time.sleep(2)  # 清除输入框的内容
        pic4 = self.driver.find_element_by_id('com.dealuck.cyy:id/tv_content').text
        if '呆萌' != pic4:
            print('pic4执行成功--------%s ' % pic4)
        else:
            print('pic4执行失败--------%s ' % pic4)
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_history_clear').click()
        time.sleep(2)  # 清除历史数据
        pic10 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_history_clear')
        if 'OK' != pic10:
            print('pic10执行成功---------%s' % pic10)
        else:
            print('pic10执行失败---------%s' % pic10)
        self.driver.find_element_by_id('com.dealuck.cyy:id/ll_title').click()
        time.sleep(2)  # 话题详情页
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_more').click()
        time.sleep(2)  # 话题分享
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout').click()
        time.sleep(2)  # 收藏
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_more').click()
        time.sleep(2)  # 话题分享
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_cancel').click()
        time.sleep(2)  # 取消弹框

        self.driver.find_element_by_id('com.dealuck.cyy:id/ll_join').click()
        time.sleep(2)  # 话题参与发布
        pic11 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/btn_record')
        if 'OK' == pic11:
            print('pic11执行成功---------%s' % pic11)
        else:
            print('pic11执行失败---------%s' % pic11)
        self.driver.find_element_by_id('com.dealuck.cyy:id/ib_close').click()
        time.sleep(2)  # 返回话题主页

        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]').click()
        time.sleep(2)  # 话题页，第一个ugc
        pic12 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_title')
        if 'OK' == pic12:
            print('pic12执行成功---------%s' % pic12)
        else:
            print('pic12执行失败---------%s' % pic12)

        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
        time.sleep(2)  # 返回话题主页

        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.ImageView').click()
        time.sleep(2)  # 用户头像
        pic13 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/magic_indicator')
        if 'OK' == pic13:
            print('pic13执行成功---------%s' % pic13)
        else:
            print('pic13执行失败---------%s' % pic13)
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_back').click()
        time.sleep(2)  # 返回话题

        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[2]').click()
        time.sleep(2)  # 话题主页点赞

        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
        time.sleep(2)  # 返回搜索页

        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_cancel').click()
        time.sleep(3)   # 返回至话题广场页

        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_scan').click()
        time.sleep(2)  # 扫一扫
        pic14 = element.validate_id(driver=self.driver,value='com.dealuck.cyy:id/tv_title')
        if 'OK' == pic14:
            print('pic14执行成功--------%s' % pic14)
        else:
            print('pic14执行失败--------%s' % pic14)
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_my_code').click()
        time.sleep(3)   # 我的二维码
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_close').click()
        time.sleep(2)    # X掉
        pic15 = element.validate_id(driver=self.driver,value='com.dealuck.cyy:id/fl_close')
        if 'NG' == pic15:
            print('pic15执行成功--------%s' % pic15)
        else:
            print('pic15执行失败--------%s' % pic15)
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_right').click()
        time.sleep(3)    # 相册
        pic16 = element.validate_id(driver=self.driver,value='com.dealuck.cyy:id/tv_des')
        if 'NG' == pic16:
            print('pic16执行成功--------%s' % pic16)
        else:
            print('pic16执行失败--------%s' % pic16)
        self.driver.find_element_by_id('com.dealuck.cyy:id/btn_back').click()
        time.sleep(3)    # 返回扫一扫
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_left').click()
        time.sleep(3)    # 返回至话题广场

        self.driver.find_element_by_id('com.dealuck.cyy:id/ll_more').click()
        time.sleep(2)  # 热门品种更多
        pic17 = element.validate_id(driver=self.driver,value='com.dealuck.cyy:id/tv_title')
        if 'OK' == pic17:
            print('pic17执行成功--------%s' % pic17)
        else:
            print('pic17执行失败--------%s' % pic17)

        a = 1
        while a <= 3:
            for i in range(1,4):
                self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.TextView[%d]' % i).click()
                time.sleep(2)  # 循环点击tab
                print('点击第 %s 个tab' % i)
            a += 1

        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout').click()
        time.sleep(3)    # 点击喜欢进入 品种详情页

        '''品种详情页'''
        pic18 = element.validate_id(driver=self.driver,value='com.dealuck.cyy:id/tv_big_title')
        if 'OK' == pic18:
            print('pic18执行成功--------%s' % pic18)
        else:
            print('pic18执行失败--------%s' % pic18)
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_more').click()
        time.sleep(3)    # 分享
        pic19 = element.validate_id(driver=self.driver,value='com.dealuck.cyy:id/rcv1')
        if 'OK' == pic19:
            print('pic19执行成功--------%s' % pic19)
        else:
            print('pic19执行失败--------%s' % pic19)
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_cancel').click()
        time.sleep(2)   # 取消

        b = 1
        while b <= 3:
            for i in range(1,4):
                self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.TextView[%d]' % i).click()
                time.sleep(3)   # 循环品种详情页的tab
                print('点击第 %s 个tab' % i)
            b += 1
            self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.TextView[1]').click()
            time.sleep(3)  # 点击动态

        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').click()
        time.sleep(2)   # 点击第一个ugc
        pic20 = element.validate_id(driver=self.driver,value='com.dealuck.cyy:id/tv_title')
        if 'OK' == pic20:
            print('pic20执行成功--------%s' % pic20)
        else:
            print('pic20执行失败--------%s' % pic20)
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
        time.sleep(3)   # 返回品种详情
        if 'OK' != element.validate_xpath(self.driver,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]'):
            element.swipeUp(driver=self.driver, t=2000)
            time.sleep(3)
            self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click()
            time.sleep(3)    # 点击用户头像
        else:
            self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click()
            time.sleep(3)    # 点击头像
        pic21 = element.validate_id(driver=self.driver,value='com.dealuck.cyy:id/ll_user_name')
        if 'OK' == pic21:
            print('pic21执行成功--------%s' % pic21)
        else:
            print('pic21执行失败--------%s' % pic21)
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_back').click()
        time.sleep(2)   # 返回品种详情
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[2]').click()
        time.sleep(3)     # 点赞

        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.TextView[3]').click()
        time.sleep(3)   # 点人气榜

        pic22 = element.validate_xpath(self.driver,value='/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout')
        if 'OK' == pic22:
            print('pic22该品种有上榜者-------%s' % pic22)
            self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout/android.widget.RelativeLayout').click()
            time.sleep(3)   # 点金牌区域 进入个人首页
            pic23 = element.validate_id(driver=self.driver,value='com.dealuck.cyy:id/ll_user_name')
            if 'OK' == pic23:
                print('pic23执行成功--------%s' % pic23)
            else:
                print('pic23执行失败--------%s' % pic23)
            self.driver.find_element_by_id('com.dealuck.cyy:id/fl_back').click()
            time.sleep(2)   # 返回品种主页
            self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]').click()
            time.sleep(3)   # 第一个ugc
            self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
            time.sleep(2)    # 返回
        else:
            print('pic21该品种没有上榜者--------%s' % pic21)


        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
        time.sleep(3)   # 返回热门品种主页

        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]').click()
        time.sleep(3)     # 点击第一个ugc，进入详情页
        pic24 = element.validate_id(self.driver,'com.dealuck.cyy:id/tv_title')
        if 'OK' == pic24:
            print('pic24执行成功--------%s' % pic24)
        else:
            print('pic24执行失败--------%s' % pic24)
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
        time.sleep(2)  # 返回

        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_left').click()
        time.sleep(3)   # 返回话题广场页

        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]').click()
        time.sleep(2)  # 第一个热门品种

        inf = info.infos(driver=self.driver)
        inf.breedinfo()

        self.driver.find_element_by_xpath(
            '	/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout').click()
        time.sleep(2)  # 话题广场的第一个话题
        pic25 = element.validate_id(self.driver, 'com.dealuck.cyy:id/tv_detail')
        if 'OK' == pic25:
            print('pic25执行成功---------%s' % pic25)
        else:
            print('pic25执行失败---------%s' % pic25)
        print('当前话题的介绍是-----%s' % self.driver.find_element_by_id('com.dealuck.cyy:id/tv_detail').text)

        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_more').click()
        time.sleep(2)  # 分享
        pic27 = element.validate_xpath(self.driver, 'com.dealuck.cyy:id/share2')
        if 'OK' == pic27:
            print('pic27执行成功---------%s' % pic27)
        else:
            print('pic27执行失败---------%s' % pic27)
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout').click()
        time.sleep(3)  # 收藏

        self.driver.find_element_by_id('com.dealuck.cyy:id/ll_join').click()
        time.sleep(3)  # 参与发布
        pic28 = element.validate_id(self.driver, 'com.dealuck.cyy:id/fl_left')
        if 'OK' == pic28:
            print('pic28执行成功---------%s' % pic28)
        else:
            print('pic28执行失败---------%s' % pic28)
        self.driver.find_element_by_id('com.dealuck.cyy:id/ib_close').click()
        time.sleep(3)  # 返回话题详情页

        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]').click()
        time.sleep(3)  # 点击第一个ugc
        pic29 = element.validate_id(self.driver, 'com.dealuck.cyy:id/tv_title')
        if 'OK' == pic29:
            print('pic29执行成功---------%s' % pic29)
        else:
            print('pic29执行失败---------%s' % pic29)
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
        time.sleep(3)  # 返回话题详情

        element.swipeUp(self.driver, 2000)
        time.sleep(3)
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click()
        time.sleep(3)  # 点击头像进入个人主页
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_back').click()
        time.sleep(3)  # 返回话题详情页

        # self.driver.find_element_by_xpath(
        #     '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[2]').click()
        # time.sleep(3)  # 页面点赞

        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
        time.sleep(2)  # 返回



        '''之后加上滑动效果'''

