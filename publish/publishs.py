# 发布功能的主流程点击事件
from public import element
import time

class releas:
    def __init__(self,driver):
        self.driver = driver

    def release(self):
        self.driver.find_element_by_id('com.dealuck.cyy:id/ib_flash').click()
        time.sleep(2)     # 闪光灯
        print('点击了闪光灯，查看手机闪光灯是否有打开')

        self.driver.find_element_by_id('com.dealuck.cyy:id/ib_timer').click()
        time.sleep(3)     # 点击延时拍摄
        print('点击了延时拍摄，查看手机是否有效果')

        self.driver.find_element_by_id('com.dealuck.cyy:id/ib_flip').click()
        time.sleep(3)      # 翻转镜头
        print('查看手机镜头是否有转换')

        for i in range(4):
            self.driver.find_element_by_id('com.dealuck.cyy:id/fl_left').click()
            time.sleep(1)     # 比例
            print('查看手机的比例是否有切换')
            i += 1

        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_right').click()
        time.sleep(3)    # 美颜
        pub1 = element.validate_id(self.driver,'com.dealuck.cyy:id/fl_flag')
        if 'OK' == pub1:
            print('pub1执行成功------%s' % pub1)
        else:
            print('pub1执行失败------%s' % pub1)

        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_beauty').click()
        time.sleep(3)  # 美颜
        for i in range(6):
            i += 1
            self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[%s]' % i).click()
            print('第---%s-次' % i)
            time.sleep(1)

        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_filter').click()
        time.sleep(3)    # 滤镜
        for m in range(5):
            m += 1
            self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[%s]' % m).click()
            print('第---%s-次' % m)
            time.sleep(1)

        self.driver.find_element_by_id('com.dealuck.cyy:id/ib_flip').click()
        time.sleep(3)  # 翻转镜头
        print('查看手机镜头是否有转换')

        self.driver.find_element_by_id('com.dealuck.cyy:id/ib_timer').click()
        time.sleep(3)  # 点击延时拍摄
        print('点击了延时拍摄，查看手机是否有效果')

        self.driver.find_element_by_id('com.dealuck.cyy:id/btn_record').click()
        time.sleep(20)  # 拍摄按钮
        self.driver.find_element_by_id('com.dealuck.cyy:id/btn_record').click()
        time.sleep(3)     # 停止拍摄

        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_left').click()
        time.sleep(3)    # 预备删除这段视频
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_right').click()
        time.sleep(20)    # 完成

        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
        time.sleep(3)    # 返回
        self.driver.find_element_by_id('com.dealuck.cyy:id/fl_left').click()
        time.sleep(3)     # 删除

        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.TextView[1]').click()
        time.sleep(3)  # 相册
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]').click()
        time.sleep(3)    # 选中一个

        for k in range(3):
            k += 1
            self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.TextView[%s]' % k).click()
            time.sleep(1)    # 底部导航

        for j in range(4):
            self.driver.find_element_by_id('com.dealuck.cyy:id/fl_left').click()
            time.sleep(1)     # 比例
            print('查看手机的比例是否有切换')
            j += 1

        self.driver.find_element_by_id('com.dealuck.cyy:id/btn_record').click()
        time.sleep(4)     # 拍摄照片

        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back').click()
        time.sleep(3)    # 返回

        self.driver.find_element_by_id('com.dealuck.cyy:id/btn_record').click()
        time.sleep(4)  # 拍摄照片

        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_next').click()
        time.sleep(3)    # 下一步
        print('当前停留在发布页面')

        '''当前停留在发布页面'''

        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_close').click()
        time.sleep(3)    # 退出
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_cancel').click()
        time.sleep(3)     # 取消

        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_draft').click()
        time.sleep(3)   # 存草稿
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_cancel').click()
        time.sleep(3)    # 取消

        pub2 = self.driver.find_element_by_id('com.dealuck.cyy:id/et_message').text
        print('文本为空的默认文案----------%s' % pub2)

        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_delete').click()
        time.sleep(3)    # 图片中的X 删除照片
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_ok').click()
        time.sleep(3)    # 只有一张照片的时候，会提示知道拉
        pub3 = self.driver.find_element_by_id('com.dealuck.cyy:id/tv_ok').text
        print('只有一张照片的时候----------%s' % pub3)     # 只有一张的情况下
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_cancel').click()
        time.sleep(3)    # 多张的时候会提示是否需要删除     取消
        self.driver.find_element_by_id('com.dealuck.cyy:id/iv_delete').click()
        time.sleep(3)  # 图片中的X 删除照片
        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_ok').click()
        time.sleep(3)   # 确定删除

        # self.driver.find_element_by_id('com.dealuck.cyy:id/iv_cover').click()
        # time.sleep(3)    # 点击图片 全屏    没法返回，现在不能获取页面中图片的位置


        self.driver.find_element_by_id('com.dealuck.cyy:id/ib_add').click()
        time.sleep(3)     # 添加照片，调取相册

        self.driver.find_element_by_id('com.dealuck.cyy:id/ll_topic').click()
        time.sleep(3)    # 话题标签

        self.driver.find_element_by_id('com.dealuck.cyy:id/ll_goods').click()
        time.sleep(3)   # 商品标签

        self.driver.find_element_by_id('com.dealuck.cyy:id/rl_breed').click()
        time.sleep(3)   # 品种标签

        self.driver.find_element_by_id('com.dealuck.cyy:id/ll_location').click()
        time.sleep(3)   # 地址标签

        self.driver.find_element_by_id('com.dealuck.cyy:id/tv_publish').click()
        time.sleep(3)  # 发布









