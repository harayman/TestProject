import sys
import telethon
from telethon import TelegramClient, sync, events


api_id = 489553
api_hash = '735d12b12937a3a959591a6d0da7c34b'
host_name = 'https://np8x.com'
members = ['page']
TOKEN = '685968806:AAG5gTQHIXJM8zr-Wga7Pn0v4A1S3eW-c9E'

# jenkins环境变量，在job中配置并传入python脚本
# report报告地址
report_path = None
# 下载地址 https://np8x.com/eightx/eightx.apk
down_link = None


# 发送报告链接到telegram

def send_link(link):
    bot = TelegramClient('notify_session', api_id, api_hash).start(bot_token=TOKEN)
    bot.send_message(-334899744, link)

def main():

    print('=========================')
    print(down_link)
    print('=========================')
    send_link(down_link)
    # target_link = copy_report()
    # send_link(target_link)

if __name__ == '__main__':
    if len(sys.argv) <= 0:
        print('please input the evn path')
    else:
        down_link = '下载地址：1）华为：https://np8x.com/test/huawei_1.0.apk 2）小米：https://np8x.com/test/xiaomi_1.0.apk'

        main()