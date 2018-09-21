# -*- coding:utf-8 -*-

import hashlib

#计算md5值 
class calmd5():
    def __init__(self):
        pass
    def getmd5(self,path):
        m = hashlib.md5()
        with open(path,'rb') as f:
            
            m.update(f.read())
            ret = m.hexdigest()
        return ret
    
