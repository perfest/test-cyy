import time

def release(driver):
    from public import element
    '''页面上的元素   
    闪光灯 resource-id     com.dealuck.cyy:id/ib_flash
    延时器 resource-id     com.dealuck.cyy:id/ib_timer
    前后镜 resource-id     com.dealuck.cyy:id/ib_flip
    返回键 。。。           com.dealuck.cyy:id/ib_close
    选音乐 。。。           com.dealuck.cyy:id/tv_bgm
    选比例 。。。             com.dealuck.cyy:id/iv_ratio
    录制按钮 。。。           com.dealuck.cyy:id/btn_record
    美颜 。。。。             com.dealuck.cyy:id/iv_filter
    相册，拍摄，拍照，使用坐标直接定位
    
    '''
    # driver.find_element_by_id('com.dealuck.cyy:id/ib_flash').click()
    # driver.find_element_by_id('com.dealuck.cyy:id/ib_timer').click()
    driver.find_element_by_id('com.dealuck.cyy:id/ib_flip').click()
    # driver.find_element_by_id('com.dealuck.cyy:id/tv_bgm').click()
    time.sleep(2)
    driver.find_element_by_id('com.dealuck.cyy:id/ib_flip').click()
    time.sleep(1)
    driver.find_element_by_id('com.dealuck.cyy:id/iv_ratio').click()
    time.sleep(1)
    # driver.find_element_by_id('com.dealuck.cyy:id/btn_record').click()
    driver.find_element_by_id('com.dealuck.cyy:id/iv_filter').click()
    time.sleep(1)
    driver.find_element_by_id('com.dealuck.cyy:id/ib_close').click()


