# 这段代码就是，我们的推特机器人，帮我们自动发帖
import tweepy as tp
import time
import os

# twitter api 账户信息，在这里申请API key 。
# https://developer.twitter.com/en/account/get-started

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

# 登陆账户 account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)


# 循环郭文贵文件夹里面的照片，然后把照片发出去。
os.chdir('郭文贵')

for guo_image in os.listdir('.'):
    api.update_with_media(guo_image,'这个是机器人发的，我在揭露五毛的剂量！')
    time.sleep(3)