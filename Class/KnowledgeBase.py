import glob
import os
import jsonpickle  # pip install jsonpickle
import json

import pandas as pd

from Class import *
from Class.Device import Device
from Class.Match import Match
from Class.Object import Object
import Class
from Class.Port import Port


class KnowledgeBase():
    def __init__(self, matchList : [Match]=[Match], outPortList: [Port]=[Port], inPortList: [Port]=[Port]):
        self.matchList = matchList
        self.outPortList = outPortList
        self.inPortList = inPortList

    def learn_folder(self,path2folder='..\excel\learn/220-母线&线路-第一套合并单元&第一套合并单元'):
        for filename in glob.iglob(path2folder + '**/*.xls', recursive=True):
            if filename.endswith(".xls") or filename.endswith(".csv"):
                self.learn_excel(filename)
            else:
                continue

    def learn_excel(self,path2excel='..\excel\learn/井门.xls'):
        sheet = pd.ExcelFile(path2excel).parse('已配置')
        try:
            for row in sheet.iterrows():
                outPort = Port(row[1]['开出端子描述'], row[1]['开出端子引用'] )
                inPort = Port(row[1]['开入端子描述'], row[1]['开入端子引用'] )
                match = Match(outPort, inPort)
                self.matchList.append(match)
        except RuntimeError:
            print(row[1])
        print(dir(self.matchList))

    def load_excel(self,path2excel='..\excel\learn/井门.xls',sheetName = '所有发送'):
        sheet = pd.ExcelFile(path2excel).parse(sheetName)
        try:
            for row in sheet.iterrows():
                outPort = Port(row[1]['开出端子描述'], row[1]['开出端子引用'] )
                self.outPortList.append(outPort)
        except RuntimeError:
            print(row[1])
        print(dir(self.outPortList))

    def load_excel(self,path2excel='..\excel\learn/井门.xls',sheetName = '所有发送', title = '开出'):
        sheet = pd.ExcelFile(path2excel).parse(sheetName)
        try:
            for row in sheet.iterrows():
                port = Port(row[1][title+'端子描述'], row[1][title+'端子引用'] )
                self.portList.append(port)
        except RuntimeError:
            print(row[1])
        print(dir(self.portList))

def transform(multilevelDict):

    return {str(key).replace("\n", ""):
                (transform(value)
                 if isinstance(value, dict)
                 else value
                 )
            for key, value in
            multilevelDict.items()
            }



kb = KnowledgeBase()
kb.learn_folder()
