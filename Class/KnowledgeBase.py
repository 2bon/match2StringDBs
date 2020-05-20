import glob

import pandas as pd
import time
from pandas import DataFrame
from strsimpy.levenshtein import Levenshtein

from Class.Match import Match
from Class.Port import Port


class KnowledgeBase():
    sheetNameList = ['开出', '开入', '匹配']
    typeList = ['描述', '引用']
    levenshtein = Levenshtein()

    def __init__(self, matchList: [Match] = [Match], outPortList: [] = [], inPortList: [] = []):
        self.matchList = matchList
        self.portListDict = {str: []}
        self.portDict = {str: Port}
        self.dfDict = {}
        for sheetName in self.sheetNameList:
            for type in self.typeList:
                self.dfDict[sheetName + type] = DataFrame()  # in,out,match

    def learn_folder(self, path2folder='..\excel\learn/220-母线&线路-第一套合并单元&第一套合并单元'):
        for filename in glob.iglob(path2folder + '**/*.xls', recursive=True):
            if filename.endswith(".xls") or filename.endswith(".csv"):
                self.learn_excel(filename)
            else:
                continue

    def learn_excel(self, path2excel):
        for type in self.typeList:
            for inOut in ['开出', '开入']:
                self.load_excel(path2excel, sheetName='已配置', inOut=inOut, type=type)

        sheet = pd.ExcelFile(path2excel).parse('已配置')
        try:
            for row in sheet.iterrows():
                outPort = Port(row[1]['开出端子描述'], row[1]['开出端子引用'])
                inPort = Port(row[1]['开入端子描述'], row[1]['开入端子引用'])
                match = Match(outPort, inPort)
                self.matchList.append(match)
                for type in self.typeList:
                    df2 = self.dfDict.get('匹配' + type, DataFrame())
                    dfKey = row[1]['开出端子' + type] + '匹配' + row[1]['开入端子' + type]
                    if dfKey not in df2:
                        df2[dfKey] = df2.get(dfKey)
                    self.dfDict['匹配' + type] = df2
        except RuntimeError:
            print(row[1])

    def load_excel(self, path2excel='..\excel\learn/220-母线&线路-第一套合并单元&第一套合并单元/赤厝.xls',
                   sheetName='所有发送', inOut='开出', type='描述'):
        sheet = pd.ExcelFile(path2excel).parse(sheetName)
        key: str = path2excel + sheetName + inOut
        portList = self.portListDict.get(key, [])
        try:
            for row in sheet.iterrows():
                port = Port(row[1][inOut + '端子描述'], row[1][inOut + '端子引用'])
                portList.append(port)
                key2 = row[1][inOut + '端子' + type]
                self.portDict[key2] = port
                dfName = inOut + type
                global df2
                df2 = self.dfDict.get(dfName, DataFrame())
                if sheetName == '已配置':
                    df2[key2] = df2.get(key2)
                else:  # new
                    if key2 not in df2.index:
                        df2 = df2.reindex(df2.index.tolist() + [key2])
                        for done in df2:
                            similarity = self.levenshtein.distance(done, key2)
                            df2[done][key2] = similarity
                            if similarity < 0.3:
                                print(done + "like" + key2)
                self.dfDict[dfName] = df2
            self.portListDict[key] = portList
        except RuntimeError:
            print(row[1])

    def load_test(self, path2excel='..\excel\learn/220-母线&线路-第一套合并单元&第一套合并单元/赤厝.xls'):
        for type in self.typeList:
            self.load_excel(path2excel, sheetName='所有发送', inOut='开出', type=type)
            self.load_excel(path2excel, sheetName='所有接收', inOut='开入', type=type)
            key = '匹配' + type
            df = self.dfDict.get(key, DataFrame())
            for outPort in self.portListDict[path2excel + '所有发送' + '开出']:
                for inPort in self.portListDict[path2excel + '所有接收' + '开入']:
                    if type == '描述':
                        key2 = outPort.description + '匹配' + inPort.description
                    else:
                        key2 = outPort.reference + '匹配' + inPort.reference
                    if key2 not in df.index:
                        df = df.reindex(df.index.tolist() + [key2])
                        for done in df:
                            df[done][key2] = self.levenshtein.distance(done, key2)
                    self.dfDict[key] = df

    def main(self, path2excel='..\excel\learn/220-母线&线路-第一套合并单元&第一套合并单元/KnowledgeBase.xlsx'):
        # for sheetName in self.sheetNameList:
        #     self.dfDict[sheetName] = pd.ExcelFile(path2excel).parse(sheetName)  # load history
        start_time = time.time()

        # self.learn_folder()
        self.learn_excel('..\excel\learn/220-母线&线路-第一套合并单元&第一套合并单元/赤厝.xls')
        self.load_test()
        with pd.ExcelWriter(path2excel) as writer:
            for key, df in self.dfDict.items():
                print(key, df)
                df.to_excel(writer, sheet_name=key)
        print("--- %s m ---" % ((time.time() - start_time) / 60))

    def transform(self, multilevelDict):
        return {str(key).replace("\n", ""):
                    (self.transform(value)
                     if isinstance(value, dict)
                     else value
                     )
                for key, value in
                multilevelDict.items()
                }


kb = KnowledgeBase()
kb.main()
