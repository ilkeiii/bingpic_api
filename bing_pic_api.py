import requests
import xml.etree.ElementTree as ET
from flask import Flask, redirect

# api链接
bing_pic_url = "http://cn.bing.com/HPImageArchive.aspx?idx=0&n=1"
# 默认返回图片
default_return_pic_1920 = "https://www.bing.com/th?id=OHR.IcebergAntarctica_ZH-CN2053356825_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp"
default_return_pic_1080 = "https://www.bing.com/th?id=OHR.IcebergAntarctica_ZH-CN2053356825_1080x1920.jpg&rf=LaDigue_1080x1920.jpg&pid=hp"
default_return_pic_1366 = "https://www.bing.com/th?id=OHR.IcebergAntarctica_ZH-CN2053356825_1366x768.jpg&rf=LaDigue_1366x768.jpg&pid=hp"

# 创建一个Flask应用
app = Flask(__name__)

@app.route("/")
def get_url_default():
    return redirect("https://www.bing.com", code=301)

@app.route("/1920")
def get_url_1920():
    bing_pic_url_get = requests.get(bing_pic_url)
    if bing_pic_url_get.status_code == 200:
        # 将返回的内容转换为ElementTree对象
        root = ET.fromstring(bing_pic_url_get.text)
        # 找到第一个image标签下的url标签
        url = root.find("image/url")
        # 如果找到了url标签，获取它的文本内容
        if url is not None:
            url_value = "http://www.bing.com"+url.text
            return redirect(url_value,code=302)
        else:
            # 如果没有找到url标签，返回一个默认壁纸
            return redirect(default_return_pic_1920,code=302)
    else:
        # 如果请求失败，返回一个默认壁纸
        return redirect(default_return_pic_1920,code=302)

@app.route("/1080")
def get_url_1080():
    bing_pic_url_get = requests.get(bing_pic_url)
    if bing_pic_url_get.status_code == 200:
        # 将返回的内容转换为ElementTree对象
        root = ET.fromstring(bing_pic_url_get.text)
        # 找到第一个image标签下的url标签
        url = root.find("image/url")
        # 如果找到了url标签，获取它的文本内容
        if url is not None:
            url.text = url.text.replace("1920x1080", "1080x1920")
            url_value = "http://www.bing.com"+url.text
            return redirect(url_value,code=302)
        else:
            # 如果没有找到url标签，返回一个默认壁纸
            return redirect(default_return_pic_1080,code=302)
    else:
        # 如果请求失败，返回一个默认壁纸
        return redirect(default_return_pic_1080,code=302)

@app.route("/1366")
def get_url_1366():
    bing_pic_url_get = requests.get(bing_pic_url)
    if bing_pic_url_get.status_code == 200:
        # 将返回的内容转换为ElementTree对象
        root = ET.fromstring(bing_pic_url_get.text)
        # 找到第一个image标签下的url标签
        url = root.find("image/url")
        # 如果找到了url标签，获取它的文本内容
        if url is not None:
            url.text = url.text.replace("1920x1080", "1366x768")
            url_value = "http://www.bing.com"+url.text
            return redirect(url_value,code=302)
        else:
            # 如果没有找到url标签，返回一个默认壁纸
            return redirect(default_return_pic_1366,code=302)
    else:
        # 如果请求失败，返回一个默认壁纸
        return redirect(default_return_pic_1366,code=302)

app.run(port=8080,host="0.0.0.0")