import time
from public import info
from public import element
from publish import publishs



class test_demo:
    def __init__(self,driver,desired_caps):
        self.driver = driver
        self.desired_caps = desired_caps

    def demos(self):

        # 单视频（非沉静式）
        '''
        处理单ugc的逻辑，需要区分视频和图文
        :return:
        '''
        # self.inf = info.infos(self.driver)

        # 图文  非评论入口
        # info33 = element.validate_id(self.driver,'com.dealuck.cyy:id/load_more_load_end_view')    # 只有评论页进来才会默认展示评论
        # if 'OK' == info33:
        #     print('info33执行成功------%s' % info33)
        # else:
        #     print('info33执行失败------%s' % info33)
        #
        # element.swipeDown(self.driver,2000)
        # time.sleep(3)
        # element.swipeDown(self.driver, 2000)
        # time.sleep(3)
        # element.swipeDown(self.driver, 2000)
        # time.sleep(3)

    #     info31 = element.validate_id(self.driver, 'com.dealuck.cyy:id/tv_num')    # 图片只有一张
    #     if 'OK' == info31:
    #         print('info31执行成功------%s' % info31)
    #         # 单张
    #
    #
    #
    #     else:
    #         print('info31执行失败------%s' % info31)
    #         # 多张
    #
    #
    #
    # def clicks(self):
    #     info36 = element.validate_id(self.driver, 'com.dealuck.cyy:id/ll_title_user')  # title
    #     if 'OK' == info36:
    #         print('info36执行成功--------%s' % info36)
    #     else:
    #         print('info36执行失败--------%s' % info36)
    #
    #     info37 = element.validate_id(self.driver, 'com.dealuck.cyy:id/ll_tags')
    #     if 'OK' == info37:
    #         print('info37-页面存在品种标签-----实现点击' % info37)
    #         self.inf.breedinfo()  # 品种详情页点击
    #     else:
    #         pass
    #
    #     info38 = element.validate_id(self.driver, 'com.dealuck.cyy:id/ll_topic')
    #     if 'OK' == info38:
    #         print('info38-页面存在话题标签------实现点击' % info38)
    #         self.inf.picinfo()  # 话题详情页点击
    #
    #     info39 = element.validate_id(self.driver, 'com.dealuck.cyy:id/ll_bgm')
    #     if 'OK' == info39:
    #         print('info39-页面存在音乐标签------实现点击' % info39)
    #         self.inf.mc()     # 音乐详情点击
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #     self.driver.find_element_by_id('com.dealuck.cyy:id/iv_back')      # 返回进入的一级页面
    #
    #     self.driver.find_element_by_id('com.dealuck.cyy:id/ll_title_user')    # title
    #
    #     self.driver.find_element_by_id('com.dealuck.cyy:id/iv_more')     # 更多，弹框分享渠道
    #
    #     self.driver.find_element_by_id('com.dealuck.cyy:id/ll_tags')     # 品种标签 跳转品种详情页
    #
    #     self.driver.find_element_by_id('com.dealuck.cyy:id/ll_topic')     # 话题标签
    #
    #     self.driver.find_element_by_id('com.dealuck.cyy:id/ll_address')    # 地址标签
    #
    #     self.driver.find_element_by_id('com.dealuck.cyy:id/ll_bgm')     # 音乐是否标签
    #
    #     '''商品暂时不做校验'''
    #
    #     self.driver.find_element_by_id('com.dealuck.cyy:id/rl_comment')    # 说点儿什么输入框
    #
    #     self.driver.find_element_by_id('com.dealuck.cyy:id/ll_comment')   # 评论
    #
    #     self.driver.find_element_by_id('com.dealuck.cyy:id/ll_share')    # 分享
    #
    #     self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[2]')
    #     # 点赞
    #
    #     self.driver.find_element_by_id('com.dealuck.cyy:id/tv_comment_title')      # 评论的title    用正则 提出字符串中的数字，对上划做判断
    #
    #
    #
    #     import re
    #     info34 = self.driver.find_element_by_id('com.dealuck.cyy:id/tv_comment_title').text
    #     info35 = re.findall(r'\d+',info34)
    #     if int(info35[0]) < 3:
    #         for i in range(3):
    #             element.swipeDown(self.driver,2000)
    #             time.sleep(3)
    #             i += 1       # 翻页到顶部 查看页面上的元素
    #     else:
    #         for j in range(int(info35[0]) // 3):
    #             element.swipeUp(self.driver,2000)
    #             time.sleep(3)
    #             j += 1     # 查看评论的内容
    #


        cy = info.infos(self.driver)
        cy.mc()

















