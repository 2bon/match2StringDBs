import os

import pandas as pd

from Class import *
from Class.Device import Device
from Class.Match import Match
from Class.Object import Object
import Class
from Class.Port import Port


class KnowledgeBase():
    matchList = [Match]

    def learn_folder(path2folder='..\excel\learn/'):
        for filename in os.listdir(path2folder):
            if filename.endswith(".xls") or filename.endswith(".csv"):
                KnowledgeBase.learn_excel(path2folder + filename)
            else:
                continue

    def learn_excel(path2excel='..\excel\learn/井门.xls'):
        sheet = pd.ExcelFile(path2excel).parse('已配置')
        for row in sheet.iterrows():
            try:
                outPort = Port(row[1]['开出设备名称'], row[1]['开出端子号'], row[1]['开出端子描述'], row[1]['开出端子引用'])
                inPort = Port(row[1]['开入设备名称'], row[1]['开入端子号'], 0, row[1]['开入端子引用'])
                match = Match(outPort, inPort)
                KnowledgeBase.matchList.append(match)
            except RuntimeError:
                print(row[1])
        print((KnowledgeBase.matchList))


def read_excel_column(path: str, sheet: str, column: str) -> list:
    """

    :rtype: list
    """
    df = pd.ExcelFile(path).parse(sheet)[column]
    print(df)
    return df


KnowledgeBase.learn_folder()
