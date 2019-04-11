import time
from public import element


class infos():
    def __init__(self, driver):
        self.driver = driver

    def breedinfo(self):
        pic18 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_big_title')
        if 'OK' == pic18:
            print('pic18执行成功--------%s' % pic18)
        else:
            print('pic18执行失败--------%s' % pic18)
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_more').click()
        time.sleep(3)  # 分享
        pic19 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/rcv1')
        if 'OK' == pic19:
            print('pic19执行成功--------%s' % pic19)
        else:
            print('pic19执行失败--------%s' % pic19)
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_cancel').click()
        time.sleep(2)  # 取消

        b = 1
        while b <= 3:
            for i in range(1, 4):
                self.driver.find_element_by_xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.TextView[%d]' % i).click()
                time.sleep(3)  # 循环品种详情页的tab
                print('点击第 %s 个tab' % i)
            b += 1
            self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.TextView[1]').click()
            time.sleep(3)  # 点击动态

        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').click()
        time.sleep(2)  # 点击第一个ugc
        pic20 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_title')
        if 'OK' == pic20:
            print('pic20执行成功--------%s' % pic20)
        else:
            print('pic20执行失败--------%s' % pic20)
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
        time.sleep(3)  # 返回品种详情

        if 'OK' != element.validate_xpath(self.driver,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]'):
            element.swipeUp(driver=self.driver,t=2000)
            time.sleep(3)
            self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click()
            time.sleep(3)    # 点击用户头像
        else:
            self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click()
            time.sleep(3)    # 点击头像
        pic21 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/ll_user_name')
        if 'OK' == pic21:
            print('pic21执行成功--------%s' % pic21)
        else:
            print('pic21执行失败--------%s' % pic21)
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_back').click()
        time.sleep(2)  # 返回品种详情
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[2]').click()
        time.sleep(3)  # 点赞

        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.TextView[3]').click()
        time.sleep(3)  # 点人气榜

        pic22 = element.validate_xpath(self.driver,
                                       value='/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout')
        if 'OK' == pic22:
            print('pic22该品种有上榜者-------%s' % pic22)
            self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout/android.widget.RelativeLayout').click()
            time.sleep(3)  # 点金牌区域 进入个人首页
            pic23 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/ll_user_name')
            if 'OK' == pic23:
                print('pic23执行成功--------%s' % pic23)
            else:
                print('pic23执行失败--------%s' % pic23)
            self.driver.find_element_by_id('com.dealuck.cyy:id/fl_back').click()
            time.sleep(2)  # 返回品种主页
            self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]').click()
            time.sleep(3)  # 第一个ugc
            self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
            time.sleep(2)  # 返回
            self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
            time.sleep(3)  # 返回上一级进入的页面
        else:
            print('pic21该品种没有上榜者--------%s' % pic21)

    def picinfo(self):
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

        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[2]').click()
        time.sleep(3)  # 页面点赞

        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
        time.sleep(2)  # 返回

    def es(self):
        ind5 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_cancel')
        if 'OK' == ind5:
            print('ind5执行成功---------%s ' % ind5)
        else:
            print('ind5执行失败---------%s ' % ind5)

        self.driver.find_element_by_id('com.dealuck.cyy:id/rl_hot_keyword').click()
        time.sleep(2)  # 热门搜索
        ind6 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/iv_bg')
        if 'OK' == ind6:
            print('ind6执行成功---------%s ' % ind6)
        else:
            print('ind6执行失败---------%s ' % ind6)
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
            ind7 = element.validate_xpath(driver=self.driver,
                                          value='/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]')
            if 'OK' == ind7:
                print('ind7执行成功--------%s' % ind7)
            else:
                print('ind7执行失败--------%s' % ind7)
            self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]').click()
            time.sleep(2)  # 收藏
            self.driver.find_element_by_id('com.dealuck.cyy:id/iv_more').click()
            time.sleep(2)  # 点击更多，弹框提示分享渠道
            self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[3]').click()
            time.sleep(2)  # 下载视频
            ind8 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/rl_tips')
            if 'OK' == ind8:
                print('ind8执行成功--------%s' % ind8)
            else:
                print('ind8执行失败--------%s' % ind8)
            time.sleep(8)
            self.driver.find_element_by_id('com.dealuck.cyy:id/iv_more').click()
            time.sleep(2)  # 点击更多，弹框提示分享渠道
            self.driver.find_element_by_xpath(
                '	/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[4]').click()
            time.sleep(2)  # 举报
            ind9 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_title')
            time.sleep(2)
            if 'OK' == ind9:
                print('ind9执行成功--------%s' % ind9)
            else:
                print('ind9执行失败--------%s' % ind9)
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
            ind10 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/title_container')
            if 'OK' == ind10:
                print('ind10执行成功--------%s' % ind10)
            else:
                print('ind10执行失败--------%s' % ind10)
            self.driver.find_element_by_id('com.dealuck.cyy:id/fl_back').click()
            time.sleep(2)  # 返回视频页

            ind17 = element.validate_id(self.driver, 'com.dealuck.cyy:id/fl_article')
            if 'OK' == ind17:
                self.driver.find_element_by_id('com.dealuck.cyy:id/fl_article').click()
                time.sleep(2)  # 点击正文跳转
            else:
                self.driver.find_element_by_id('com.dealuck.cyy:id/ll_commodity').click()
                time.sleep(2)  # 收起商品展示
                self.driver.find_element_by_id('com.dealuck.cyy:id/fl_article').click()
                time.sleep(2)  # 点击正文跳转

            ind11 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/ll_title_user')
            if 'OK' == ind11:
                print('ind11执行成功--------%s' % ind11)
            else:
                print('ind11执行失败--------%s' % ind11)
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
        ind12 = self.driver.find_element_by_id('com.dealuck.cyy:id/tv_content').text
        if '呆萌' != ind12:
            print('ind12执行成功--------%s ' % ind12)
        else:
            print('ind12执行失败--------%s ' % ind12)
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_history_clear').click()
        time.sleep(2)  # 清除历史数据
        ind13 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_history_clear')
        if 'OK' != ind13:
            print('ind13执行成功---------%s' % ind13)
        else:
            print('ind13执行失败---------%s' % ind13)
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
        ind14 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/btn_record')
        if 'OK' == ind14:
            print('ind14执行成功---------%s' % ind14)
        else:
            print('ind14执行失败---------%s' % ind14)
        self.driver.find_element_by_id('com.dealuck.cyy:id/ib_close').click()
        time.sleep(2)  # 返回话题主页

        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]').click()
        time.sleep(2)  # 话题页，第一个ugc
        ind15 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_title')
        if 'OK' == ind15:
            print('ind15执行成功---------%s' % ind15)
        else:
            print('ind15执行失败---------%s' % ind15)

        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
        time.sleep(2)  # 返回话题主页

        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.ImageView').click()
        time.sleep(2)  # 用户头像
        ind16 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/magic_indicator')
        if 'OK' == ind16:
            print('ind16执行成功---------%s' % ind16)
        else:
            print('ind16执行失败---------%s' % ind16)
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_back').click()
        time.sleep(2)  # 返回话题

        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[2]').click()
        time.sleep(2)  # 话题主页点赞

        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
        time.sleep(2)  # 返回搜索页
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_cancel').click()
        time.sleep(3)  # 返回到进入搜索的一级页面

    def syis(self):
        ind2 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_title')
        if 'OK' == ind2:
            print('ind2执行成功--------%s' % ind2)
        else:
            print('ind2执行失败--------%s' % ind2)
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_my_code').click()
        time.sleep(3)  # 我的二维码
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_close').click()
        time.sleep(2)  # X掉
        ind3 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/fl_close')
        if 'NG' == ind3:
            print('ind3执行成功--------%s' % ind3)
        else:
            print('ind3执行失败--------%s' % ind3)
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_right').click()
        time.sleep(3)  # 相册
        ind4 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_des')
        if 'OK' == ind4:
            print('ind4执行成功--------%s' % ind4)
        else:
            print('ind4执行失败--------%s' % ind4)
        self.driver.find_element_by_id('com.dealuck.cyy:id/btn_back').click()
        time.sleep(3)  # 返回扫一扫
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_left').click()
        time.sleep(2)  # 返回第一级

    def oneugc(self):
        ind17 = element.validate_id(self.driver, 'com.dealuck.cyy:id/ll_bgm')
        if 'OK' == ind17:
            print('ind17当前页面有音乐存在----%s' % ind17)
            self.driver.find_element_by_id('com.dealuck.cyy:id/ll_bgm').click()
            time.sleep(3)  # 有音乐存在
            self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
            time.sleep(2)  # 返回  音乐详情后期在➕
        else:
            pass

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

    def validate_ugc(self):
        ind23 = element.validate_id(self.driver, 'com.dealuck.cyy:id/iv_cover_play')
        if 'OK' == ind23:
            print('ind23是视频------%s' % ind23)
            self.driver.find_element_by_id('com.dealuck.cyy:id/iv_cover_play').click()
            time.sleep(3)  # 确保是视频
        else:
            while True:
                element.swipeUp(self.driver, 2000)
                time.sleep(5)

                if 'OK' == element.validate_id(self.driver, 'com.dealuck.cyy:id/iv_cover_play'):
                    self.driver.find_element_by_id('com.dealuck.cyy:id/iv_cover_play').click()
                    time.sleep(2)
                    break
                else:
                    pass
