import time
from public import element
import re


class infos():
    def __init__(self, driver):
        self.driver = driver

    # 品种详情
    def breedinfo(self):
        info1 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_big_title')
        if 'OK' == info1:
            print('info1执行成功--------%s' % info1)
        else:
            print('info1执行失败--------%s' % info1)
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_more').click()
        time.sleep(3)  # 分享
        info2 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/rcv1')
        if 'OK' == info2:
            print('info2执行成功--------%s' % info2)
        else:
            print('info2执行失败--------%s' % info2)
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
        info3 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_title')
        if 'OK' == info3:
            print('info3执行成功--------%s' % info3)
        else:
            print('info3执行失败--------%s' % info3)
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
        info4 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/ll_user_name')
        if 'OK' == info4:
            print('info4执行成功--------%s' % info4)
        else:
            print('info4执行失败--------%s' % info4)
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_back').click()
        time.sleep(2)  # 返回品种详情
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[2]').click()
        time.sleep(3)  # 点赞

        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.TextView[3]').click()
        time.sleep(3)  # 点人气榜

        info5 = element.validate_xpath(self.driver,
                                       value='/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout')
        if 'OK' == info5:
            print('info5该品种有上榜者-------%s' % info5)
            self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout/android.widget.RelativeLayout').click()
            time.sleep(3)  # 点金牌区域 进入个人首页
            info6 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/ll_user_name')
            if 'OK' == info6:
                print('info6执行成功--------%s' % info6)
            else:
                print('info6执行失败--------%s' % info6)
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
            print('info5该品种没有上榜者--------%s' % info5)

    # 话题详情
    def picinfo(self):
        info7 = element.validate_id(self.driver, 'com.dealuck.cyy:id/tv_detail')
        if 'OK' == info7:
            print('info7执行成功---------%s' % info7)
        else:
            print('info7执行失败---------%s' % info7)
        print('当前话题的介绍是-----%s' % self.driver.find_element_by_id('com.dealuck.cyy:id/tv_detail').text)

        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_more').click()
        time.sleep(2)  # 分享
        info8 = element.validate_xpath(self.driver, 'com.dealuck.cyy:id/share2')
        if 'OK' == info8:
            print('info8执行成功---------%s' % info8)
        else:
            print('info8执行失败---------%s' % info8)
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout').click()
        time.sleep(3)  # 收藏

        self.driver.find_element_by_id('com.dealuck.cyy:id/ll_join').click()
        time.sleep(3)  # 参与发布
        info9 = element.validate_id(self.driver, 'com.dealuck.cyy:id/fl_left')
        if 'OK' == info9:
            print('info9执行成功---------%s' % info9)
        else:
            print('info9执行失败---------%s' % info9)
        self.driver.find_element_by_id('com.dealuck.cyy:id/ib_close').click()
        time.sleep(3)  # 返回话题详情页

        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]').click()
        time.sleep(3)  # 点击第一个ugc
        info10 = element.validate_id(self.driver, 'com.dealuck.cyy:id/tv_title')
        if 'OK' == info10:
            print('info10执行成功---------%s' % info10)
        else:
            print('info10执行失败---------%s' % info10)
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
        info11 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_cancel')
        if 'OK' == info11:
            print('info11执行成功---------%s ' % info11)
        else:
            print('info11执行失败---------%s ' % info11)

        self.driver.find_element_by_id('com.dealuck.cyy:id/rl_hot_keyword').click()
        time.sleep(2)  # 热门搜索
        info12 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/iv_bg')
        if 'OK' == info12:
            print('info12执行成功---------%s ' % info12)
        else:
            print('info12执行失败---------%s ' % info12)
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
            info13 = element.validate_xpath(driver=self.driver,
                                          value='/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]')
            if 'OK' == info13:
                print('info13执行成功--------%s' % info13)
            else:
                print('info13执行失败--------%s' % info13)
            self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]').click()
            time.sleep(2)  # 收藏
            self.driver.find_element_by_id('com.dealuck.cyy:id/iv_more').click()
            time.sleep(2)  # 点击更多，弹框提示分享渠道
            self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[3]').click()
            time.sleep(2)  # 下载视频
            info14 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/rl_tips')
            if 'OK' == info14:
                print('info14执行成功--------%s' % info14)
            else:
                print('info14执行失败--------%s' % info14)
            time.sleep(8)
            self.driver.find_element_by_id('com.dealuck.cyy:id/iv_more').click()
            time.sleep(2)  # 点击更多，弹框提示分享渠道
            self.driver.find_element_by_xpath(
                '	/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[4]').click()
            time.sleep(2)  # 举报
            info15 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_title')
            time.sleep(2)
            if 'OK' == info15:
                print('info15执行成功--------%s' % info15)
            else:
                print('info15执行失败--------%s' % info15)
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

            info16 = element.validate_id(self.driver, 'com.dealuck.cyy:id/fl_article')
            if 'OK' == info16:
                self.driver.find_element_by_id('com.dealuck.cyy:id/fl_article').click()
                time.sleep(2)  # 点击正文跳转
            else:
                self.driver.find_element_by_id('com.dealuck.cyy:id/ll_commodity').click()
                time.sleep(2)  # 收起商品展示
                self.driver.find_element_by_id('com.dealuck.cyy:id/fl_article').click()
                time.sleep(2)  # 点击正文跳转

            info17 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/ll_title_user')
            if 'OK' == info17:
                print('info17执行成功--------%s' % info17)
            else:
                print('info17执行失败--------%s' % info17)
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
        info18 = self.driver.find_element_by_id('com.dealuck.cyy:id/tv_content').text
        if '呆萌' != info18:
            print('info18执行成功--------%s ' % info18)
        else:
            print('info18执行失败--------%s ' % info18)
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_history_clear').click()
        time.sleep(2)  # 清除历史数据
        info19 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_history_clear')
        if 'OK' != info19:
            print('info19执行成功---------%s' % info19)
        else:
            print('info19执行失败---------%s' % info19)
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
        info20 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/btn_record')
        if 'OK' == info20:
            print('info20执行成功---------%s' % info20)
        else:
            print('info20执行失败---------%s' % info20)
        self.driver.find_element_by_id('com.dealuck.cyy:id/ib_close').click()
        time.sleep(2)  # 返回话题主页

        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]').click()
        time.sleep(2)  # 话题页，第一个ugc
        info21 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_title')
        if 'OK' == info21:
            print('info21执行成功---------%s' % info21)
        else:
            print('info21执行失败---------%s' % info21)

        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
        time.sleep(2)  # 返回话题主页

        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.ImageView').click()
        time.sleep(2)  # 用户头像
        info22 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/magic_indicator')
        if 'OK' == info22:
            print('info22执行成功---------%s' % info22)
        else:
            print('info22执行失败---------%s' % info22)
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_back').click()
        time.sleep(2)  # 返回话题

        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[2]').click()
        time.sleep(2)  # 话题主页点赞

        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
        time.sleep(2)  # 返回搜索页
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_cancel').click()
        time.sleep(3)  # 返回到进入搜索的一级页面

    # 扫一扫
    def syis(self):
        info23 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_title')
        if 'OK' == info23:
            print('info23执行成功--------%s' % info23)
        else:
            print('info23执行失败--------%s' % info23)
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_my_code').click()
        time.sleep(3)  # 我的二维码
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_close').click()
        time.sleep(2)  # X掉
        info24 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/fl_close')
        if 'NG' == info24:
            print('info24执行成功--------%s' % info24)
        else:
            print('info24执行失败--------%s' % info24)
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_right').click()
        time.sleep(3)  # 相册
        info25 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_des')
        if 'OK' == info25:
            print('info25执行成功--------%s' % info25)
        else:
            print('info25执行失败--------%s' % info25)
        self.driver.find_element_by_id('com.dealuck.cyy:id/btn_back').click()
        time.sleep(3)  # 返回扫一扫
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_left').click()
        time.sleep(2)  # 返回第一级

    # 单视频（沉静式）
    def oneugc(self):
        info26 = element.validate_id(self.driver, 'com.dealuck.cyy:id/ll_bgm')
        if 'OK' == info26:
            print('info26当前页面有音乐存在----%s' % info26)
            self.driver.find_element_by_id('com.dealuck.cyy:id/ll_bgm').click()
            time.sleep(3)  # 有音乐存在
            self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
            time.sleep(2)  # 返回  音乐详情后期在➕
        else:
            print('info26当前页面没有音乐存在----%s' % info26)

        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_more').click()
        time.sleep(3)  # 更多
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_cancel').click()
        time.sleep(2)  # 取消弹框

        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_header').click()
        time.sleep(3)  # 用户头像
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_back').click()
        time.sleep(3)  # 返回ugc详情页

        info27 = element.validate_id(self.driver, 'com.dealuck.cyy:id/tv_follow')
        if 'OK' == info27:
            print('info27当前ugc的作者未关注他，现在关注-------%s' % info27)
            self.driver.find_element_by_id('com.dealuck.cyy:id/tv_follow').click()
            time.sleep(2)  # 未关注的关注按钮
        else:
            print('info27当前ugc的作者已经关注，页面没有关注-----%s' % info27)

        info28 = element.validate_id(self.driver, 'com.dealuck.cyy:id/ll_commodity')
        if 'OK' == info28:
            print('info28当前ugc有商品-------%s' % info28)
            self.driver.find_element_by_id('com.dealuck.cyy:id/ll_commodity').click()
            time.sleep(2)  # 商品标签
            '''正文'''
        else:
            print('info28当前ugc无商品-------%s' % info28)

        # self.driver.find_element_by_id('com.dealuck.cyy:id/rl_comment').click()
        # time.sleep(2)    #  评论输入框

        self.driver.find_element_by_id('com.dealuck.cyy:id/ll_comment').click()
        time.sleep(3)  # 评论
        info29 = element.validate_xpath(self.driver,
                                       '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout/android.widget.LinearLayout[2]')
        if 'OK' == info29:
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

    # 校验是否是视频
    def validate_ugc(self):
        info30 = element.validate_id(self.driver, 'com.dealuck.cyy:id/iv_cover_play')
        if 'OK' == info30:
            print('info30是视频------%s' % info30)
            self.driver.find_element_by_id('com.dealuck.cyy:id/iv_cover_play').click()
            time.sleep(3)  # 确保是视频
            '''需要添加不是视频对图片的处理方式'''
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

    # 图文视频混合详情
    def ugc_list(self):
        '''
        是否多张照片、是否是视频、是否是单张图片
        消息页的单视频，单图文、沉浸式的单视频默认展开是显示评论内容，需要单独梳理
        :return:
        '''

    # 图文列表列
    def ugc_png_list(self):
        '''
        处理图片列表页的逻辑
        :return:
        '''

    # 单视频（非沉静式）
    def ugc(self):
        '''
        处理单ugc的逻辑，需要区分视频和图文
        :return:
        '''

    # 单图文
    def ugc_png(self):
        pass

    def validate_ugcs(self):
        info31 = element.validate_id(self.driver,'com.dealuck.cyy:id/tv_num')       # 校验图片的张数元素
        info32 = element.validate_id(self.driver,'com.dealuck.cyy:id/iv_full')      # 校验视频的全屏元素
        if 'OK' == info31:
            print('info31是多张图片------%s' % info31)
        elif 'OK' == info32:
            print('info32是视频----------%s' % info32)
        else:
            print('info31是单张图片------%s' % info31)

    def addres(self):
        '''地址点击返回  第三方界面，每个手机的元素不一样不做点击'''


    def mc(self):
        '''音乐详情点击'''
        info33 = element.validate_id(self.driver, 'com.dealuck.cyy:id/rl_cover')   # 音乐播放按钮
        if 'OK' == info33:
            print('info33执行成功-------%s' % info33)
        else:
            print('info33执行失败-------%s' % info33)
        print('当前音乐的名字是----------%s' % self.driver.find_element_by_id('com.dealuck.cyy:id/tv_big_title').text)

        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_favorite').click()
        time.sleep(3)    # 收藏
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_share').click()
        time.sleep(3)    # 分享
        info34 = element.validate_id(self.driver,'com.dealuck.cyy:id/tv_cancel')
        if 'OK' == info34:
            print('info34执行成功-------%s' % info34)
        else:
            print('info34执行失败-------%s' % info34)
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_cancel').click()
        time.sleep(2)     # 取消

        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_play_status').click()
        time.sleep(10)     # 让音乐播放一会儿

        info35 = self.driver.find_element_by_id('com.dealuck.cyy:id/tv_video_no').text  # 校验音乐中是否存在作品
        if int(info35) > 0:
            print('当前音乐中作品数为----------%s' % info35)
            info35 = self.driver.find_element_by_id('com.dealuck.cyy:id/tv_big_title').text
            info36 = re.findall(r'原声',info35)
            if [] == info36:
                '''非原创'''
                info38 = element.validate_xpath(self.driver,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]')
                if 'OK' == info38:
                    print('非原创音乐视频---------%s' % info38)
                else:
                    print('非原创音乐图片---------%s' % info38)
                self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]').click()
                time.sleep(3)   # 点击第一个ugc

                self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
                time.sleep(3)   # 返回
                self.driver.find_element_by_xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]').click()
                time.sleep(3)  # 点击用户头像
                self.driver.find_element_by_id('com.dealuck.cyy:id/fl_back').click()
                time.sleep(3)   # 返回
                '''点赞这里是有参与的按钮会覆盖不好判断，暂时不做操作事件'''
            else:
                '''原创作品'''
                info37 = element.validate_id(self.driver,'com.dealuck.cyy:id/iv_cover_play')
                if 'OK' == info37:
                    print('原创音乐视频---------%s' % info37)
                else:
                    print('原创音乐图片---------%s' % info37)
                self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]').click()
                time.sleep(3)
                self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
                time.sleep(3)  # 返回
                self.driver.find_element_by_id('com.dealuck.cyy:id/ll_profile').click()
                time.sleep(3)  # 点击用户头像
                self.driver.find_element_by_id('com.dealuck.cyy:id/fl_back').click()
                time.sleep(3)  # 返回
        else:
            print('当前音乐中作品数为----------%s' % info35)
            info36 = self.driver.find_element_by_id('com.dealuck.cyy:id/tv_state').text
            print('存在空白页----------%s' % info36)

        self.driver.find_element_by_id('com.dealuck.cyy:id/ll_join').click()
        time.sleep(3)    # 参与
        '''这是调用发布功能'''
        from publish import publishs
        pub = publishs.releas(self.driver)
        pub.release()

        # self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
        # time.sleep(3)  # 返回

        print('执行完毕')
