# -*- coding: utf-8 -*-
import requests
from .exception import ChatBotError

key="b7505ed8dad24dc5942ebd5ae80dbd95"
url="http://www.tuling123.com/openapi/api"

def get_response(msg):
    try:
        data = {'key': key,'info': msg, 'userid':'my-robot',}
        req=requests.post(url,data=data).json()
        return req.get('text')
    except:
        raise ChatBotError("图灵机器人服务调用异常")