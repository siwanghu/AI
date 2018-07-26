# -*- coding: utf-8 -*-

class TrainError(RuntimeError):
    def  __init__(self,args):
        self.args=args

class FileError(RuntimeError):
    def  __init__(self,args):
        self.args=args