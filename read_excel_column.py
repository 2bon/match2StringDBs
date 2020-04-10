import pandas as pd
def read_excel_column(path,sheet,column):
    df = pd.ExcelFile(path).parse(sheet)[column]
    data = pd.read_excel (r'test/井门.xls', sheet_name='已配置')
    df = pd.DataFrame(data, columns= ['开出端子描述'])
    print (df)
    return df
def read_done(path,column):
    read_excel_column(path,'已配置',column)

def read_done_out(path, columnTail):
    read_done(path,'开出' + columnTail)
def read_done_outDeviceName(path):
    read_done_out(path,'设备名称')
def read_done_outPortNum(path):
    read_done_out(path,'端子号')
def read_done_outDescribe(path):
    read_done_out(path,'端子描述')
def read_done_outRef(path):
    read_done_out(path,'端子引用')
def read_done_in(path, columnTail):
    read_done(path,'开入' + columnTail)
def read_done_inDeviceName(path):
    read_done_in(path,'设备名称')
def read_done_inPortNum(path):
    read_done_in(path,'端子号')
def read_done_inDescribe(path):
    read_done_in(path,'端子描述')
def read_done_inRef(path):
    read_done_in(path,'端子引用')

