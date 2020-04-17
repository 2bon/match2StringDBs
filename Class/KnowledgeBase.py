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
        print(path2excel)
        try:
            for row in sheet.iterrows():
                outPort = Port(row[1]['开出端子描述'], row[1]['开出端子引用'] )
                inPort = Port(row[1]['开入端子描述'], row[1]['开入端子引用'] )
                match = Match(outPort, inPort)
                self.matchList.append(match)
        except RuntimeError:
            print(row[1])
        print(dir(self.matchList))


def transform(multilevelDict):

    return {str(key).replace("\n", ""):
                (transform(value)
                 if isinstance(value, dict)
                 else value
                 )
            for key, value in
            multilevelDict.items()
            }


def read_excel_column(path: str, sheet: str, column: str) -> list:
    """

    :rtype: list
    """
    df = pd.ExcelFile(path).parse(sheet)[column]
    print(df)
    return df

kb = KnowledgeBase()
kb.learn_folder()
