import time
import requests
from selenium import webdriver
from PIL import Image
from io import BytesIO

# 你想打开的 url 地址
url = "https://unsplash.com"

# 用 Selenium 的 webdriver 去打开页面
driver = webdriver.Firefox()
driver.get(url)

# 滚动页面
driver.execute_script("window.scrollTo(0, 1000);")

# 等待5秒
time.sleep(5)

# 选择图片标签元素
image_elements = driver.find_elements_by_css_selector("img")

i = 0
for image_element in image_elements:
    image_url = image_element.get_attribute("src")
    if image_url:
        # 发送一个 HTTP 的 GET 请求，在响应里面获取并存储图片
        image_object = requests.get(image_url)
        image = Image.open(BytesIO(image_object.content))
        image.save("./images/image" + str(i) + "." + image.format, image.format)

        # 打印它们的 URL
        # print(image_url)

        i += 1
