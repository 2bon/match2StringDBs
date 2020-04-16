import glob
import os
import jsonpickle # pip install jsonpickle
import json

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
        for filename in glob.iglob(path2folder + '**/*.xls', recursive=True):
            if filename.endswith(".xls") or filename.endswith(".csv"):
                KnowledgeBase.learn_excel(filename)
            else:
                continue

    def learn_excel(path2excel='..\excel\learn/井门.xls'):
        sheet = pd.ExcelFile(path2excel).parse('已配置')
        print(path2excel)
        for row in sheet.iterrows():
            try:
                outPort = Port( row[1]['开出端子描述'], row[1]['开出端子引用'],row[1]['开出设备名称'], row[1]['开出端子号'])
                inPort = Port( row[1]['开入端子描述'], row[1]['开入端子引用'],row[1]['开入设备名称'],row[1]['开入端子号'],)
                match = Match(outPort, inPort)
                print(vars(inPort))
                print(vars(outPort))
                serialized = jsonpickle.encode(match)
                print(json.dumps(json.loads(serialized), indent=4) )
                KnowledgeBase.matchList.append(match)
            except RuntimeError:
                print(row[1])
        print(dir(KnowledgeBase.matchList))


def read_excel_column(path: str, sheet: str, column: str) -> list:
    """

    :rtype: list
    """
    df = pd.ExcelFile(path).parse(sheet)[column]
    print(df)
    return df


KnowledgeBase.learn_excel()
