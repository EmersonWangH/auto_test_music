# 网易云音乐自动化测试实现：
# 1、新建收藏夹--每日精选
# 2、将每日推荐的前三首歌曲收藏到每日精选
# 3、返回收藏夹查看添加的歌曲
# 4、删除歌单，防止影响下一轮测试
import time
from appium import webdriver
from selenium.webdriver.common.by import By

caps = {
    'platformName': 'Android',
    'platfromVersion': '10',
    'deviceName': 'MI_8',
    'appPackage': 'com.netease.cloudmusic',
    'appActivity': '.activity.LoadingActivity',
    'noReset': True,
    'newCommandTimeout': 3600,
    'automationName': 'UiAutomator2'
    }
driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
driver.implicitly_wait(10)

# 1、新建收藏夹--每日精选
# 点击我的
driver.find_element(By.XPATH, '//*[@text="我的"]').click()
# 等待2s进入页面，向上滑动屏幕，至歌单出现
time.sleep(2)
driver.swipe(400, 1400, 400, 1100)
# 点击‘+’ (此方法比较便捷，换另一种方法来学习，包含以下两步)
# driver.find_element(By.ID, 'com.netease.cloudmusic:id/create').click()
# 点击‘:’(定位到‘+’的后一位，following-sibling::元素class)
driver.find_element(By.XPATH, '//*[@resource-id="com.netease.cloudmusic:id/create"]/following-sibling::android.widget.ImageView').click()
# 点击创建新歌单，因为排在第一位，所以可以直接点击ID获得
driver.find_element(By.ID, 'com.netease.cloudmusic:id/bs_list_title').click()
# 输入歌单名称
driver.find_element(By.ID, 'com.netease.cloudmusic:id/etPlaylistName').send_keys('每日精选')
# 等待字符输入完，完成按钮可交互
time.sleep(1)
# 点击完成
driver.find_element(By.ID, 'com.netease.cloudmusic:id/tvCreatePlayListComplete').click()

# 2、将每日推荐的前三首歌曲收藏到每日精选
# 从收藏夹返回
# driver.find_element(By.CLASS_NAME, 'android.widget.ImageButton').click()\
# 有时候返回按钮无法点击，可以使用手机系统返回按钮，返回按钮 keycode = 4
time.sleep(1)
driver.keyevent(4)
# 进入发现
driver.find_element(By.XPATH, '//*[@text="发现"]').click()
# 进入每日推荐
driver.find_element(By.XPATH, '//*[@text="每日推荐"]').click()
time.sleep(1)
#获取前三首歌曲的操作菜单按钮，然后重复添加歌单过程
options = driver.find_elements(By.ID, 'com.netease.cloudmusic:id/actionBtn')[:3]
for option in options:
    # 点击“:”
    option.click()
    driver.find_element(By.XPATH, '//*[@text="收藏到歌单"]').click()
    driver.find_element(By.XPATH, '//*[@text="每日精选"]').click()
    time.sleep(1)

# 3、返回收藏夹查看添加的歌曲
driver.keyevent(4)
driver.find_element(By.XPATH, '//*[@text="我的"]').click()
time.sleep(2)
driver.swipe(400, 1400, 400, 1100)
driver.find_element(By.XPATH, '//*[@text="每日精选"]').click()
time.sleep(1)
songs = driver.find_elements(By.ID, 'com.netease.cloudmusic:id/songName')
print('每日精选歌单：')
for song in songs:
    print(song.text)

# 4、删除歌单，防止影响下一轮测试
time.sleep(1)
driver.keyevent(4)
# 进入歌单管理页面
driver.find_element(By.XPATH, '//*[@resource-id="com.netease.cloudmusic:id/create"]/following-sibling::android.widget.ImageView').click()
driver.find_element(By.XPATH, '//*[@text="歌单管理"]').click()
time.sleep(1)
# 勾选歌单，删除
driver.find_element(By.ID, 'com.netease.cloudmusic:id/checkBox').click()
# 能直接选到，但是我们学更复杂的
# driver.find_element(By.ID, 'com.netease.cloudmusic:id/bottomNav').click()
# 从父元素选子元素
time.sleep(1)
driver.find_element(By.XPATH, '//*[@resource-id="com.netease.cloudmusic:id/mainActivityRealContainer"]/android.widget.LinearLayout').click()
# 弹框点删除
driver.find_element(By.ID, 'com.netease.cloudmusic:id/buttonDefaultPositive').click()
time.sleep(5)

driver.quit()