
import pandas as pd
class Object(object):
    chinese_name = ''
    def __init__(self, value:str):
        self.value = value
    def __init__(self, strMapList):
        for key, value in strMapList:
            if self.chinese_name in key:
                self.value = value


