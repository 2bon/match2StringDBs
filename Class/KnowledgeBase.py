import pandas as pd

from Class import *
from Class.Device import Device
from Class.Object import Object
import Class
from Class.Port import Port


class KnowledgeBase():
    matchList = []

    def learn(path='../test/井门.xls'):
        sheet = pd.ExcelFile(path).parse('已配置')
        for row in sheet.iterrows():
            outPort = Port(row[1]['开出端子号'], row[1]['开出端子描述'], row[1]['开出端子引用'])
            # print(vars(outPort))
            outDevice = Device(row[1]['开出设备名称'], [outPort])
            print(vars(outDevice))


def read_excel_column(path: str, sheet: str, column: str) -> list:
    """

    :rtype: list
    """
    df = pd.ExcelFile(path).parse(sheet)[column]
    print(df)
    return df


KnowledgeBase.learn()
