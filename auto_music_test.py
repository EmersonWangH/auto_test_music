# 网易云音乐自动化测试实现：
# 1、启动app
# 2、进入发现
# 3、点击每日推荐
# 4、显示前3首歌曲名称

# 导包
from appium import webdriver
from selenium.webdriver.common.by import By

# appium自动化相关配置，参数是固定的，可以从appium官网查找
caps = {
    # 被测APP平台   （iOS只能运行在Mac环境下，系统闭环）
    'platformName': 'Android',
    'platfromVersion': '10',
    'deviceName': 'MI_8',    # 随便写
    # 被测app信息查找方式：adb shell dumpsys activity recents | findstr intent
    # 被测app包名，代表被测app在设备上的地址
    'appPackage': 'com.netease.cloudmusic',
    # 被测app入口
    'appActivity': '.activity.LoadingActivity',
    # 禁止app在自动化后重置
    'noReset': True,
    # 设置命令超时时间
    'newCommandTimeout': 3600,
    # 指定驱动 UiAutomator2
    'automationName': 'UiAutomator2'
    }
# 启动被测app
driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
# 或 http://127.0.0.1:4723/wd/hub

# 加入隐式等待，如果当前界面没有出现目标元素，会一直等待知道超出设定时间
driver.implicitly_wait(10)

# 元素定位方法：ID、CLASS、content-desc
# xpath:   //元素类型(class值)[@属性 = "属性值"] ，元素类型可用*表示 ，如//*[@text="每日推荐"]

# 进入发现
driver.find_element(By.XPATH, '//*[@text="发现"]').click()
# 点击每日推荐
driver.find_element(By.XPATH, '//*[@text="每日推荐"]').click()
# 获取前三首歌曲名称
songs = driver.find_elements(By.ID, 'com.netease.cloudmusic:id/songName')[:3]
print('前三首歌曲是：')
for song in songs:
    print(song.text)

driver.quit()