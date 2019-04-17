import time
from public import element

class Myclick:
    '''我的页面click事件'''
    def __init__(self,driver,desired_caps):
        self.driver = driver
        self.desired_caps = desired_caps

    def Myindex(self):
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout[5]').click()
        time.sleep(2)  # 点击我的  乐视
        # self.driver.find_element_by_xpath(
        #     '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout[5]').click()
        # time.sleep(2)   # 华为
        my1 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/fl_qr_code')
        if 'OK' == my1:
            print('my1执行成功-------%s' % my1)
        else:
            print('my1执行失败-------%s' % my1)

        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_qr_code').click()
        time.sleep(2)  # 二维码
        my2 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/ll_save')
        if 'OK' == my2:
            print('my2执行成功-------%s' % my2)
        else:
            print('my2执行失败-------%s' % my2)

        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_close').click()
        time.sleep(2)
        my3 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/ll_save')
        if 'NG' == my3:
            print('my3执行成功-------%s' % my3)
        else:
            print('my3执行失败-------%s' % my3)

        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_setting').click()
        time.sleep(2)  # 点击设置
        my4 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_title')
        if 'OK' == my4:
            print('my4执行成功-------%s' % my4)
        else:
            print('my4执行失败-------%s' % my4)

        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_left').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_setting').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.dealuck.cyy:id/rl_safe').click()
        time.sleep(2)  # 账户与安全
        my5 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_title')
        if 'OK' == my5:
            print('my5执行成功-------%s' % my5)
        else:
            print('my5执行失败-------%s' % my5)

        self.driver.find_element_by_id('com.dealuck.cyy:id/rl_phone').click()
        time.sleep(2)  # 手机号码
        my6 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/btn_count')  # 验证码but
        if 'OK' == my6:
            print('my6执行成功-------%s' % my6)
        else:
            print('my6执行失败-------%s' % my6)
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_left').click()
        time.sleep(2)  # 返回我的账号

        if 'b83ae0c0' == self.desired_caps['deviceName']:       # 小米
            pass
        elif 'c6ab25900205' == self.desired_caps['deviceName']:      # 红米
            pass
        else:
            self.driver.find_element_by_id('com.dealuck.cyy:id/rl_wx').click()
            time.sleep(5)  # 微信绑定
            my7 = element.validate_id(driver=self.driver, value='com.tencent.mm:id/jl')
            if 'OK' == my7:
                print('my7执行成功-------%s' % my7)
            else:
                print('my7执行失败-------%s' % my7)

            if 'LE67A06190312448' == self.desired_caps['deviceName']:
                self.driver.find_element_by_id('com.tencent.mm:id/jb').click()
                time.sleep(2)  # 返回我的账号  乐视     #                 在小米中无法获取返回按钮
            else:
                self.driver.find_element_by_id('com.tencent.mm:id/ka').click()
                time.sleep(2)  # 返回我的账号  华为


        # self.driver.find_element_by_id('com.dealuck.cyy:id/rl_qq').click()
        # time.sleep(2)  # qq绑定
        # my8 = element.validate_id(driver=self.driver, value='com.tencent.mobileqq:id/ivTitleName')
        # if 'OK' == my8:
        #     print('my8执行成功-------%s' % my8)
        # else:
        #     print('my8执行失败-------%s' % my8)
        # self.driver.find_element_by_id('com.tencent.mobileqq:id/ivTitleBtnLeft').click()
        # time.sleep(2)  # 返回我的账户
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_left').click()
        time.sleep(2)  # 返回设置主页

        my9 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/rl_notification')
        # self.driver.find_element_by_id('com.dealuck.cyy:id/rl_notification').click()
        # time.sleep(2)    # 消息与通知  这里每个手机的显示效果不一样，不做点击处理
        if 'OK' == my9:
            print('my9执行成功------------%s' % self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.TextView').text)
        else:
            print('my9执行失败-----------%s' % my9)
        time.sleep(2)

        self.driver.find_element_by_id('com.dealuck.cyy:id/rl_setting').click()
        time.sleep(2)  # 通用设置
        if 'b83ae0c0' == self.desired_caps['deviceName']:
            pass
        else:
            my10 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_title')
            if 'OK' == my10:
                print('my10执行成功--------%s' % my10)
            else:
                print('my10执行失败--------%s' % my10)
            self.driver.find_element_by_id('com.dealuck.cyy:id/rb_auto_play').click()
            time.sleep(2)  # 点击开启/关闭，自动播放   每个手机的显示效果不一样，小米就没有

        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_left').click()
        time.sleep(2)  # 点击返回设置

        self.driver.find_element_by_id('com.dealuck.cyy:id/rl_opinion').click()
        time.sleep(2)  # 意见反馈
        my11 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_title')
        if 'OK' == my11:
            print('my11执行成功-------%s' % my11)
        else:
            print('my11执行失败-------%s' % my11)
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_left').click()
        time.sleep(2)  # 返回设置主页

        self.driver.find_element_by_id('com.dealuck.cyy:id/rl_about').click()
        time.sleep(2)  # 关于
        my12 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_title')
        if 'OK' == my12:
            print('my12执行成功------%s' % my12)
        else:
            print('my12执行失败------%s' % my12)
        print('当前版本是------%s' % self.driver.find_element_by_id('com.dealuck.cyy:id/tv_version').text)
        time.sleep(2)

        self.driver.find_element_by_id('com.dealuck.cyy:id/rl_protocol').click()
        time.sleep(2)  # 用户协议
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_left').click()
        time.sleep(2)

        self.driver.find_element_by_id('com.dealuck.cyy:id/rl_policy').click()
        time.sleep(2)  # 隐私政策
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_left').click()
        time.sleep(2)

        self.driver.find_element_by_id('com.dealuck.cyy:id/rl_convention').click()
        time.sleep(2)  # 社区公约
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_left').click()
        time.sleep(2)

        self.driver.find_element_by_id('com.dealuck.cyy:id/rl_check_version').click()
        time.sleep(2)  # 检查版本

        my13 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_build')
        if 'OK' == my13:
            print('my13执行成功--构建时间是--------%s' % self.driver.find_element_by_id('com.dealuck.cyy:id/tv_build').text)
        else:
            print('my13执行失败--------%s' % my13)
        time.sleep(2)

        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_left').click()
        time.sleep(2)   #  返回设置主页

        self.driver.find_element_by_id('com.dealuck.cyy:id/rl_cache').click()
        time.sleep(2)  # 清楚缓存
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_cancel').click()
        time.sleep(2)

        self.driver.find_element_by_id('com.dealuck.cyy:id/rl_quit').click()
        time.sleep(2)  # 退出登陆
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_cancel').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_left').click()
        time.sleep(2)  # 返回个人主页
        print('设置执行完毕')


        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_share').click()
        time.sleep(2)  # 点击分享    微信、朋友圈、qq、qq空间各手机的第三方id不一样
        my14 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/fl_close')
        if 'OK' == my14:
            print('my14执行成功----------%s' % my14)
        else:
            print('my14执行失败----------%s' % my14)

        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]').click()
        time.sleep(2)  # 复制连接
        my15 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/fl_close')
        if 'NG' == my15:
            print('my15执行成功----------%s' % my15)
        else:
            print('my15执行失败----------%s' % my15)

        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_share').click()
        time.sleep(2)  # 点击分享
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]').click()
        time.sleep(2)  # 二维码
        my16 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/root_view')
        if 'OK' == my16:
            print('my16执行成功----------%s' % my16)
        else:
            print('my16执行成功----------%s' % my16)
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_close').click()
        time.sleep(2)  # 取消二维码弹框
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_share').click()
        time.sleep(2)  # 点击分享
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_cancel').click()
        time.sleep(2)  # 取消分享弹框


        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_name').click()
        time.sleep(2)  # 点击昵称
        my17 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_title')
        if 'OK' == my17:
            print('my17执行成功----------%s' % my17)
        else:
            print('my17执行失败----------%s' % my17)

        self.driver.find_element_by_id('com.dealuck.cyy:id/et_name').send_keys(u'001')
        time.sleep(2)  # 昵称输入框
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_id_copy').click()
        time.sleep(2)  # 复制id
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_left').click()
        time.sleep(2)  # 返回个人主页
        my18 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/fl_qr_code')
        if 'OK' == my18:
            print('my18执行成功----------%s' % my18)
        else:
            print('my18执行失败----------%s' % my18)

        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_edit').click()
        time.sleep(2)  # 编辑资料
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_gender').click()
        time.sleep(2)  # 性别
        my19 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/dialog_bg_view2')
        if 'OK' == my19:
            print('my19执行成功----------%s' % my19)
        else:
            print('my19执行失败----------%s' % my19)

        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.RelativeLayout[2]').click()
        time.sleep(2)  # 选女性
        my20 = self.driver.find_element_by_id('com.dealuck.cyy:id/tv_gender').text
        if '女' == my20:
            print('my20执行成功----------%s' % my20)
        else:
            print('my20执行失败----------%s' % my20)

        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_birthday').click()
        time.sleep(2)  # 选日期
        my21 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/btnSubmit')
        if 'OK' == my21:
            print('my21执行成功----------%s' % my21)
        else:
            print('my21执行失败----------%s' % my21)
        self.driver.find_element_by_id('com.dealuck.cyy:id/btnSubmit').click()
        time.sleep(2)  # 确认日期

        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_address').click()
        time.sleep(2)  # 地区
        my22 = self.driver.find_element_by_id('com.dealuck.cyy:id/tv_title').text
        if '设置地区' == my22:
            print('my22执行成功----------%s' % my21)
        else:
            print('my22执行失败----------%s' % my21)
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_right').click()
        time.sleep(2)  # 地区，返回

        self.driver.find_element_by_id('com.dealuck.cyy:id/et_sign').send_keys(u'002')
        time.sleep(2)  # 签名
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_left').click()
        time.sleep(2)  # 返回个人主页

        self.driver.find_element_by_id('com.dealuck.cyy:id/civ_header').click()
        time.sleep(2)  # 点击用户头像
        my23 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_left')
        if 'OK' == my23:
            print('my23执行成功----------%s' % my23)
        else:
            print('my23执行失败----------%s' % my23)
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_left').click()
        time.sleep(2)  # 返回个人主页

        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_edit').click()
        time.sleep(2)  # 点击编辑资料
        my24 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_left')
        if 'OK' == my24:
            print('my24执行成功----------%s' % my24)
        else:
            print('my24执行失败----------%s' % my24)
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_left').click()
        time.sleep(2)  # 返回个人主页

        print('当前的用户介绍是-------%s ' % self.driver.find_element_by_id('com.dealuck.cyy:id/tv_intro').text)

        self.driver.find_element_by_id('com.dealuck.cyy:id/ll_focus').click()
        time.sleep(2)  # 点击关注
        my25 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_title')
        if 'OK' == my25:
            print('my25执行成功----------%s' % my25)
        else:
            print('my25执行失败----------%s' % my25)

        if '关注' == self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView').text:
            self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView').click()
        else:
            self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView').click()
            time.sleep(3)
            self.driver.find_element_by_id('com.dealuck.cyy:id/tv_cancel').click()
            time.sleep(2)
            self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView').click()
            time.sleep(3)
            self.driver.find_element_by_id('com.dealuck.cyy:id/tv_ok').click()
            time.sleep(2)  # 取消当前关注
            if '关注' == self.driver.find_element_by_xpath(
                    '	/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView').text:
                print('操作成功')
            else:
                print('操作失败')

        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.ImageView').click()
        time.sleep(2)  # 点击第一个头像跳转至用户主页
        my26 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/ll_like')
        if 'OK' == my26:
            print('my26执行成功----------%s' % my26)
        else:
            print('my26执行失败----------%s' % my26)
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_share').click()
        time.sleep(2)  # 分享
        my27 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_cancel')
        if 'OK' == my27:
            print('my27执行成功----------%s' % my27)
        else:
            print('my27执行失败----------%s' % my27)
        time.sleep(2)
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_cancel').click()
        time.sleep(2)  # 取消
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_back').click()
        time.sleep(2)  # 返回关注主页
        my28 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_title')
        if 'OK' == my28:
            print('my28执行成功----------%s' % my28)
        else:
            print('my28执行失败----------%s' % my28)
        time.sleep(2)
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_left').click()
        time.sleep(2)  # 返回个人主页

        self.driver.find_element_by_id('com.dealuck.cyy:id/ll_fans').click()
        time.sleep(2)  # 点击粉丝
        my29 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_title')
        if 'OK' == my29:
            print('my29执行成功----------%s' % my29)
        else:
            print('my29执行失败----------%s' % my29)
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.ImageView').click()
        time.sleep(2)  # 点击第一个头像 进入个人主页
        my31 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/iv_header')
        if 'OK' == my31:
            print('my31执行成功----------%s' % my31)
        else:
            print('my31执行失败----------%s' % my31)
        time.sleep(2)
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_back').click()
        time.sleep(2)  # 返回粉丝主页
        my32 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_title')
        if 'OK' == my32:
            print('my32执行成功----------%s' % my32)
        else:
            print('my32执行失败----------%s' % my32)

        if '关注' == self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView').text:
            self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView').click()
            if '关注' != element.validate_xpath(driver=self.driver,
                    value='/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView'):
                print('关注成功')
            else:
                print('关注失败')
        else:
            self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView').click()
            time.sleep(2)
            self.driver.find_element_by_id('com.dealuck.cyy:id/tv_cancel').click()
            time.sleep(2)
            self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView').click()
            time.sleep(2)
            self.driver.find_element_by_id('com.dealuck.cyy:id/tv_ok').click()
            time.sleep(2)  # 取消关注
            my30 = element.validate_xpath(driver=self.driver,
                                          value='/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView')
            if 'OK' == my30:
                print('my30执行成功----------%s' % my30)
            else:
                print('my30执行失败----------%s' % my30)
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_left').click()
        time.sleep(2)  # 返回个人主页

        self.driver.find_element_by_id('com.dealuck.cyy:id/ll_like').click()
        time.sleep(2)  # 点击获赞
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_ok').click()
        time.sleep(2)

        self.driver.find_element_by_id('com.dealuck.cyy:id/multi_header_view').click()
        time.sleep(2)  # 点击宠物卡片
        element.swipLeft(driver=self.driver, t=2000)
        time.sleep(2)  # 左滑
        element.swipRight(driver=self.driver, t=2000)
        time.sleep(2)  # 右滑
        my33 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/ll_edit')
        if 'OK' == my33:
            self.driver.find_element_by_id('com.dealuck.cyy:id/ll_edit').click()
            time.sleep(2)  # 编辑
            my34 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tag_layout')
            if 'OK' == my34:
                print('my34执行成功----------%s' % my34)
            else:
                print('my34执行失败----------%s' % my34)
            self.driver.find_element_by_id('com.dealuck.cyy:id/et_name').send_keys(u'003')
            time.sleep(2)  # 编辑昵称
            my35 = self.driver.find_element_by_id('com.dealuck.cyy:id/et_name').text
            if '003' == my35:
                print('my35执行成功----------%s' % my35)
            else:
                print('my35执行失败----------%s' % my35)
            self.driver.find_element_by_id('com.dealuck.cyy:id/ll_female').click()
            time.sleep(2)
            self.driver.find_element_by_id('com.dealuck.cyy:id/tv_type').click()
            time.sleep(2)  # 切换宠物品种
            my36 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_title')
            if 'OK' == my36:
                print('my36执行成功----------%s' % my36)
            else:
                print('my36执行失败----------%s' % my36)
            self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout').click()
            time.sleep(2)  # 获取全部品种
            my37 = element.validate_xpath(driver=self.driver,
                                          value='/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[1]')
            if 'OK' == my37:
                print('my37执行成功----------%s' % my37)
            else:
                print('my37执行失败----------%s' % my37)
            self.driver.find_element_by_id('com.dealuck.cyy:id/iv_left').click()
            time.sleep(2)  # 返回宠物品种
            self.driver.find_element_by_id('com.dealuck.cyy:id/iv_left').click()
            time.sleep(2)  # 返回宠物编辑页
            self.driver.find_element_by_id('com.dealuck.cyy:id/tv_birthday').click()
            time.sleep(2)  # 选择日期
            my38 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/timepicker')
            if 'OK' == my38:
                print('my38执行成功----------%s' % my38)
            else:
                print('my38执行失败----------%s' % my38)
            self.driver.find_element_by_id('com.dealuck.cyy:id/btnSubmit').click()
            time.sleep(2)  # 确认
            self.driver.find_element_by_id('com.dealuck.cyy:id/tv_jue_yu').click()
            time.sleep(2)  # 绝育
            self.driver.find_element_by_id('com.dealuck.cyy:id/tv_confirm').click()
            time.sleep(2)  # 提交资料
        else:
            print('my33执行失败-----这里开始做添加-----%s' % my33)
            self.driver.find_element_by_id('com.dealuck.cyy:id/iv_add').click()
            time.sleep(2)  # 添加宠物
            self.driver.find_element_by_id('com.dealuck.cyy:id/et_name').send_keys(u'004')
            time.sleep(2)  # 编辑昵称
            my39 = self.driver.find_element_by_id('com.dealuck.cyy:id/et_name').text
            if '004' == my39:
                print('my39执行成功----------%s' % my39)
            else:
                print('my39执行失败----------%s' % my39)
            self.driver.find_element_by_id('com.dealuck.cyy:id/ll_female').click()
            time.sleep(2)
            self.driver.find_element_by_id('com.dealuck.cyy:id/tv_type').click()
            time.sleep(2)  # 切换宠物品种
            my40 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/tv_title')
            if 'OK' == my40:
                print('my40执行成功----------%s' % my40)
            else:
                print('my40执行失败----------%s' % my40)
            self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout').click()
            time.sleep(2)  # 获取全部品种
            my41 = element.validate_xpath(driver=self.driver,
                                          value='/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[1]')
            if 'OK' == my41:
                print('my41执行成功----------%s' % my41)
            else:
                print('my41执行失败----------%s' % my41)
            self.driver.find_element_by_id('com.dealuck.cyy:id/iv_left').click()
            time.sleep(2)  # 返回宠物品种
            self.driver.find_element_by_id('com.dealuck.cyy:id/iv_left').click()
            time.sleep(2)  # 返回宠物编辑页
            self.driver.find_element_by_id('com.dealuck.cyy:id/tv_birthday').click()
            time.sleep(2)  # 选择日期
            my42 = element.validate_id(driver=self.driver, value='com.dealuck.cyy:id/timepicker')
            if 'OK' == my42:
                print('my42执行成功----------%s' % my42)
            else:
                print('my42执行失败----------%s' % my42)
            self.driver.find_element_by_id('com.dealuck.cyy:id/btnSubmit').click()
            time.sleep(2)  # 确认
            self.driver.find_element_by_id('com.dealuck.cyy:id/tv_jue_yu').click()
            time.sleep(2)  # 绝育
            self.driver.find_element_by_id('com.dealuck.cyy:id/tv_confirm').click()
            time.sleep(2)  # 提交资料

        self.driver.find_element_by_id('com.dealuck.cyy:id/multi_header_view').click()
        time.sleep(2)  # 点击宠物卡片
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_close').click()
        time.sleep(2)  # 取消关闭




