import time


class Myclick:
    '''我的页面click事件'''
    def __init__(self,driver):
        self.driver = driver

    def erweima(self):
        # self.driver.find_element_by_id('com.dealuck.cyy:id/fl_qr_code').click()
        # time.sleep(2)
        # self.driver.find_element_xpath("//*[contains(@text,'保存到本地')]").click()
        # time.sleep(2)

        # 添加进入我的个人主页的操作事件

        self.driver.tap([(842, 131)])
        time.sleep(2)
        self.driver.tap([(66, 163)])
        time.sleep(2)
        self.driver.tap([(851, 113)])
        time.sleep(2)
        self.driver.tap([(992, 307)])
        time.sleep(2)
        self.driver.tap([(980, 307)])
        time.sleep(2)
        self.driver.tap([(892, 1409)])
        time.sleep(2)
        self.driver.tap([(347, 1393)])
        time.sleep(2)
        self.driver.tap([(310, 1315)])
        time.sleep(2)
        self.driver.tap([(354, 1343)])
        time.sleep(2)
        self.driver.tap([(235, 1268)])
        time.sleep(2)
        self.driver.tap([(244, 1330)])
        time.sleep(2)
        self.driver.tap([(501, 1002)])
        time.sleep(2)
        print('点击确认以后不修改手机号，返回我的账号')

        self.driver.tap([(59, 157)])
        time.sleep(2)
        self.driver.tap([(908, 607)])
        time.sleep(2)
        self.driver.tap([(63, 150)])
        time.sleep(2)
        print('点击跳转第三方微信，看是否能够跳转成功，返回我的账号')

        print('qq这里目前有问题')

        self.driver.tap([(72, 172)])
        time.sleep(2)
        self.driver.tap([(451, 463)])
        time.sleep(2)
        self.driver.tap([(949, 275)])
        time.sleep(2)
        self.driver.tap([(995, 279)])
        time.sleep(2)
        print('进入点击通知信息，确认能够点击，'
              '需要注意的是需要在信息页查看是否已经修改，页面不存在返回按钮，需要手动返回')
        time.sleep(10)

        self.driver.tap([(341, 657)])
        time.sleep(2)
        self.driver.tap([(936, 319)])
        time.sleep(2)
        self.driver.tap([(1014, 322)])
        time.sleep(2)
        self.driver.tap([(72, 166)])
        time.sleep(2)
        print('通用设置点击以后返回设置页面')

        print('意见反馈这里有问题，后续再看')

        self.driver.tap([(116, 933)])
        time.sleep(2)
        self.driver.tap([(961, 758)])
        time.sleep(2)
        self.driver.tap([(81, 163)])
        time.sleep(2)
        self.driver.tap([(222, 933)])
        time.sleep(2)
        self.driver.tap([(56, 160)])
        time.sleep(2)
        self.driver.tap([(989, 1083)])
        time.sleep(2)
        self.driver.tap([(69, 153)])
        time.sleep(2)
        print('检查更新点击无效')

        self.driver.tap([(75, 163)])
        time.sleep(2)
        self.driver.tap([(426, 1096)])
        time.sleep(2)
        self.driver.tap([(695, 1124)])
        time.sleep(2)
        self.driver.tap([(535, 1283)])
        time.sleep(2)
        self.driver.tap([(326, 1118)])
        time.sleep(2)
        self.driver.tap([(72, 175)])
        time.sleep(2)
        print('设置点击完成，返回我的个人主页,查看是否回到了个人主页')
        time.sleep(10)

        self.driver.tap([(974, 131)])
        time.sleep(2)
        self.driver.tap([(135, 1211)])
        time.sleep(2)
        self.driver.tap([(59, 144)])
        time.sleep(2)
        self.driver.tap([(1011, 144)])
        time.sleep(2)
        self.driver.tap([(388, 1199)])
        time.sleep(2)
        self.driver.tap([(66, 153)])
        time.sleep(2)
        self.driver.tap([(1005, 150)])
        time.sleep(2)
        self.driver.tap([(651, 1205)])
        time.sleep(2)
        self.driver.tap([(307, 1083)])
        time.sleep(2)
        self.driver.tap([(758, 1262)])
        time.sleep(2)
        self.driver.tap([(285, 1096)])   # 从qq返回个人主页
        time.sleep(2)
        self.driver.tap([(995, 141)])
        time.sleep(2)
        self.driver.tap([(895, 1205)])
        time.sleep(2)
        self.driver.tap([(122, 147)])
        time.sleep(2)
        self.driver.tap([(1005, 116)])
        time.sleep(2)
        self.driver.tap([(103, 1587)])
        time.sleep(2)
        self.driver.tap([(999, 135)])
        time.sleep(2)
        self.driver.tap([(394, 1571)])
        time.sleep(2)
        self.driver.tap([(535, 1581)])
        time.sleep(2)
        print('分享点击事件执行完毕')

        self.driver.tap([(160, 297)])
        time.sleep(2)
        self.driver.tap([(94, 163)])
        time.sleep(2)
        self.driver.tap([(914, 338)])
        time.sleep(2)
        self.driver.tap([(97, 166)])
        time.sleep(2)
        self.driver.tap([(898, 523)])
        time.sleep(2)
        print('点击编辑资料，这里不做操作，后面需要使用send_keys输入数据')
        self.driver.tap([(970, 150)])
        time.sleep(2)

        self.driver.tap([(91, 786)])
        time.sleep(2)
        self.driver.tap([(135, 789)])
        time.sleep(2)
        self.driver.tap([(1008, 160)])
        time.sleep(2)
        self.driver.tap([(160, 1205)])
        time.sleep(2)
        self.driver.tap([(56, 153)])
        time.sleep(2)
        self.driver.tap([(1008, 144)])
        time.sleep(2)
        self.driver.tap([(382, 1196)])
        time.sleep(2)
        self.driver.tap([(44, 138)])
        time.sleep(2)
        self.driver.tap([(999, 160)])
        time.sleep(2)
        self.driver.tap([(651, 1224)])
        time.sleep(2)
        self.driver.tap([(999, 144)])
        time.sleep(2)
        self.driver.tap([(1002, 163)])
        time.sleep(2)
        self.driver.tap([(917, 1202)])
        time.sleep(2)
        self.driver.tap([(135, 147)])
        time.sleep(2)
        self.driver.tap([(1011, 150)])
        time.sleep(2)
        self.driver.tap([(135, 1575)])
        time.sleep(2)
        self.driver.tap([(1011, 157)])
        time.sleep(2)
        self.driver.tap([(413, 1571)])
        time.sleep(2)
        self.driver.tap([(545, 1581)])
        time.sleep(2)
        print('他人主页，分享点击')

        self.driver.tap([(914, 570)])
        time.sleep(2)
        self.driver.tap([(301, 1130)])
        time.sleep(2)
        self.driver.tap([(898, 576)])
        time.sleep(2)
        self.driver.tap([(711, 1114)])
        time.sleep(2)
        self.driver.tap([(923, 563)])
        time.sleep(2)
        print('他人主页点击关注')


        self.driver.tap([(72, 873)])
        time.sleep(2)
        self.driver.tap([(63, 163)])
        time.sleep(2)
        self.driver.tap([(294, 877)])
        time.sleep(2)
        self.driver.tap([(69, 160)])
        time.sleep(2)
        self.driver.tap([(501, 870)])
        time.sleep(2)
        self.driver.tap([(513, 1271)])
        time.sleep(2)
        self.driver.tap([(742, 877)])
        time.sleep(2)
        self.driver.tap([(394, 1518)])
        time.sleep(2)
        self.driver.tap([(53, 160)])
        time.sleep(2)
        self.driver.tap([(742, 864)])
        time.sleep(2)
        self.driver.tap([(532, 1528)])
        time.sleep(2)
        self.driver.tap([(59, 150)])
        time.sleep(2)
        self.driver.tap([(798, 861)])
        time.sleep(2)
        self.driver.tap([(682, 1525)])
        time.sleep(2)
        self.driver.tap([(983, 144)])
        time.sleep(2)
        self.driver.tap([(936, 867)])
        time.sleep(2)
        self.driver.tap([(798, 1528)])
        time.sleep(2)
        self.driver.tap([(122, 147)])
        time.sleep(2)
        self.driver.tap([(548, 1662)])
        time.sleep(2)
        self.driver.tap([(801, 858)])
        time.sleep(2)
        self.driver.tap([(275, 1525)])
        time.sleep(2)
        print('他人主页，关注、粉丝、获赞及宠物的分享跳转点击事件')

        self.driver.tap([(801, 1039)])
        time.sleep(2)
        self.driver.tap([(266, 1033)])
        time.sleep(2)
        # TouchAction(driver)
        # .press(x=573, y=1762)
        # .move_to(x=-35, y=-1424)
        # .release()
        #
        # TouchAction(driver).tap([(801, 304)])
        # TouchAction(driver)
        # .press(x=563, y=1813)
        # .move_to(x=-3, y=-1359)
        # .release()
        #
        #
        # TouchAction(driver)
        # .press(x=535, y=1690)
        # .move_to(x=7, y=-1267)
        # .release()
        #
        # TouchAction(driver)
        # .press(x=532, y=507)
        # .move_to(x=3, y=952)
        # .release()
        #
        # TouchAction(driver)
        # .press(x=72, y=1362)
        # .move_to(x=883, y=-10)
        # .release()
        #
        # TouchAction(driver)
        # .press(x=1002, y=1399)
        # .move_to(x=-861, y=-22)
        # .release()
        print('他人主页的作品、赞过，上下滑动，左右滑动事件,暂时不做点赞和点击用户头像的操作，后面补充')

        # TouchAction(driver).tap([(69, 169)])
        # TouchAction(driver)
        # .press(x=463, y=1734)
        # .move_to(x=13, y=-1249)
        # .release()

        self.driver.tap([(63, 160)])
        print('返回个人主页')

        self.driver.tap([(291, 776)])
        time.sleep(2)
        self.driver.tap([(939, 335)])
        time.sleep(2)
        self.driver.tap([(939, 347)])
        time.sleep(2)
        self.driver.tap([(329, 1121)])
        time.sleep(2)
        self.driver.tap([(917, 329)])
        time.sleep(2)
        self.driver.tap([(767, 1105)])
        time.sleep(2)
        self.driver.tap([(313, 313)])
        time.sleep(2)
        self.driver.tap([(1002, 147)])
        time.sleep(2)
        self.driver.tap([(138, 1196)])
        time.sleep(2)
        self.driver.tap([(66, 163)])
        time.sleep(2)
        self.driver.tap([(1011, 153)])
        time.sleep(2)
        self.driver.tap([(394, 1205)])
        time.sleep(2)
        self.driver.tap([(66, 153)])
        time.sleep(2)
        self.driver.tap([(1017, 153)])
        time.sleep(2)
        self.driver.tap([(920, 1215)])
        time.sleep(2)
        self.driver.tap([(106, 144)])
        time.sleep(2)
        self.driver.tap([(999, 163)])
        time.sleep(2)
        self.driver.tap([(125, 1565)])
        time.sleep(2)
        self.driver.tap([(1014, 150)])
        time.sleep(2)
        self.driver.tap([(398, 1581)])
        time.sleep(2)
        self.driver.tap([(517, 1343)])
        time.sleep(2)
        self.driver.tap([(75, 830)])
        time.sleep(2)
        self.driver.tap([(78, 157)])
        time.sleep(2)
        self.driver.tap([(282, 836)])
        time.sleep(2)
        self.driver.tap([(69, 175)])
        time.sleep(2)
        self.driver.tap([(501, 836)])
        time.sleep(2)
        self.driver.tap([(548, 1265)])
        time.sleep(2)
        self.driver.tap([(811, 977)])
        time.sleep(2)
        self.driver.tap([(260, 983)])
        time.sleep(2)
        self.driver.tap([(905, 579)])
        time.sleep(2)
        self.driver.tap([(992, 560)])
        time.sleep(2)
        self.driver.tap([(714, 1127)])
        time.sleep(2)
        self.driver.tap([(85, 166)])
        time.sleep(2)
        self.driver.tap([(72, 160)])
        time.sleep(2)
        print('粉丝列表页到他人主页，返回我的个人主页')

        self.driver.tap([(504, 779)])
        time.sleep(2)
        self.driver.tap([(529, 1280)])
        time.sleep(2)
        self.driver.tap([(833, 786)])
        time.sleep(2)
        self.driver.tap([(401, 1528)])
        time.sleep(2)
        self.driver.tap([(50, 153)])
        time.sleep(2)
        self.driver.tap([(920, 783)])
        time.sleep(2)
        self.driver.tap([(542, 1531)])
        time.sleep(2)
        self.driver.tap([(72, 144)])
        time.sleep(2)
        self.driver.tap([(980, 786)])
        time.sleep(2)
        self.driver.tap([(679, 1534)])
        time.sleep(2)
        self.driver.tap([(961, 138)])
        time.sleep(2)
        self.driver.tap([(989, 776)])
        time.sleep(2)
        self.driver.tap([(811, 1531)])
        time.sleep(2)
        self.driver.tap([(91, 150)])
        time.sleep(2)
        self.driver.tap([(532, 1675)])
        time.sleep(2)
        self.driver.tap([(917, 783)])
        time.sleep(2)
        # TouchAction(driver)
        # .press(x=1052, y=977)
        # .move_to(x=-967, y=-50)
        # .release()
        #
        # TouchAction(driver)
        # .press(x=1030, y=983)
        # .move_to(x=-902, y=138)
        # .release()

        self.driver.tap([(845, 272)])
        time.sleep(2)
        self.driver.tap([(66, 160)])
        print('个人主页的宠物卡片点击滑动操作，后期添加添加输入，删除操作')

        # TouchAction(driver)
        # .press(x=862, y=1311)
        # .move_to(x=-690, y=6)
        # .release()
        #
        # TouchAction(driver)
        # .press(x=871, y=1264)
        # .move_to(x=-521, y=-3)
        # .release()
        #
        # TouchAction(driver)
        # .press(x=849, y=1352)
        # .move_to(x=-621, y=6)
        # .release()
        #
        # TouchAction(driver)
        # .press(x=852, y=1411)
        # .move_to(x=-571, y=-22)
        # .release()
        #
        # TouchAction(driver)
        # .press(x=190, y=1264)
        # .move_to(x=578, y=0)
        # .release()
        #
        # TouchAction(driver)
        # .press(x=137, y=1358)
        # .move_to(x=562, y=0)
        # .release()
        #
        # TouchAction(driver)
        # .press(x=247, y=1445)
        # .move_to(x=474, y=6)
        # .release()
        #
        # TouchAction(driver)
        # .press(x=315, y=1383)
        # .move_to(x=384, y=-10)
        # .release()

        self.driver.tap([(518, 918)])
        time.sleep(2)
        self.driver.tap([(899, 918)])
        time.sleep(2)
        self.driver.tap([(552, 1043)])
        time.sleep(2)
        self.driver.tap([(777, 1049)])
        time.sleep(2)
        self.driver.tap([(190, 915)])
        time.sleep(2)
        # TouchAction(driver)
        # .press(x=493, y=1620)
        # .move_to(x=3, y=-980)
        # .release()

        self.driver.tap([(531, 262)])
        print('个人主页，作品、赞过、收藏、滑动点击，执行完毕')