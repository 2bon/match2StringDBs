import glob

import pandas as pd

import Matrix
from Class.Match import Match
from Class.Port import Port


class KnowledgeBase():
    def __init__(self, matchList: [Match] = [Match], outPortList: [Port] = [Port], inPortList: [Port] = [Port]):
        self.matchList = matchList
        self.portListDict = {str: [Port]}
        self.portDict = {str: Port}
        self.matrixDict = {str: Matrix}  # in,out,match

    def learn_folder(self, path2folder='..\excel\learn/220-母线&线路-第一套合并单元&第一套合并单元'):
        for filename in glob.iglob(path2folder + '**/*.xls', recursive=True):
            if filename.endswith(".xls") or filename.endswith(".csv"):
                self.learn_excel(filename)
            else:
                continue

    def learn_excel(self, path2excel):
        sheet = pd.ExcelFile(path2excel).parse('已配置')
        try:
            for row in sheet.iterrows():
                outPort = Port(row[1]['开出端子描述'], row[1]['开出端子引用'])
                inPort = Port(row[1]['开入端子描述'], row[1]['开入端子引用'])
                match = Match(outPort, inPort)
                self.matchList.append(match)
                matrix = self.matrixDict.get('开出', Matrix)
                key = row[1]['开出端子描述'] + row[1]['开出端子引用']
                port = matrix.get(key)
        except RuntimeError:
            print(row[1])
        print(dir(self.matchList))

    def load_excel(self, path2excel='..\excel\learn/220-母线&线路-第一套合并单元&第一套合并单元/赤厝.xls', sheetName='所有发送', title='开出'):
        sheet = pd.ExcelFile(path2excel).parse(sheetName)
        key: str = path2excel + sheetName + title
        portList = self.portListDict.get(key, [Port])
        try:
            for row in sheet.iterrows():
                port = Port(row[1][title + '端子描述'], row[1][title + '端子引用'])
                portList.append(port)
                key2 = row[1][title + '端子描述'] + title + row[1][title + '端子引用']
                self.portDict[key2] = port
                matrix = self.matrixDict.get(title, Matrix)
                if sheetName == '已配置':
                    port = matrix.get(key2,{object: float})
            self.portListDict[key] = portList
        except RuntimeError:
            print(row[1])
        print(dir(portList))

    def load_test(self, path2excel='..\excel\learn/220-母线&线路-第一套合并单元&第一套合并单元/赤厝.xls'):
        self.load_excel(path2excel, sheetName='所有发送', title='开出')
        self.load_excel(path2excel, sheetName='所有接收', title='开入')


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
kb.load_test()
