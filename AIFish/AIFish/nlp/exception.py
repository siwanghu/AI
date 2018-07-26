# -*- coding: utf-8 -*-

class FileError(RuntimeError):
    def  __init__(self,args):
        self.args=args

class ChatBotError(RuntimeError):
    def  __init__(self,args):
        self.args=args
