
import requests
from bs4 import BeautifulSoup as bs
import os

# website with images  你要的网址
url = 'https://www.google.com/search?q=%E9%83%AD%E6%96%87%E8%B4%B5&tbm=isch&source=lnt&tbs=isz:lt,islt:svga&sa=X&ved=0ahUKEwiU8b2V7q_eAhWQw4MKHQ22Ak0QpwUIIQ&biw=1920&bih=928&dpr=1'

# download page for parsing
page = requests.get(url)
soup = bs(page.text, 'html.parser')

# 找到搜有的图片
image_tags = soup.findAll('img')

# 创立文件夹用来储存图片
if not os.path.exists('郭文贵'):
    os.makedirs('郭文贵')

# move to new directory 移到新的文件夹
os.chdir('郭文贵')

# image file name variable 图片文件的名字
x = 0

# writing images
for image in image_tags:
    try:
        url = image['src']
        response = requests.get(url)
        if response.status_code == 200:
            with open('郭文贵-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1
    except:
        pass