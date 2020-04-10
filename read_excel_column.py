import pandas as pd
def read_excel_column(path,sheet,column):
    df = pd.ExcelFile(path).parse(sheet)[column]
    data = pd.read_excel (r'test/井门.xls', sheet_name='已配置')
    df = pd.DataFrame(data, columns= ['开出端子描述'])
    print (df)
    return df
def read_done(path,column):
    read_excel_column(path,'已配置',column)

def read_done_out_device_name(path):
    read_done(path,'开出设备名称')
def read_done_out_port(path):
    read_done(path,'开出端子号')
def read_done_out_describe(path):
    read_done(path,'开出端子描述')
def read_done_out_ref(path):
    read_done(path,'开出端子引用')

def read_done_in_device_name(path):
    read_done(path,'开入设备名称')
def read_done_in_port(path):
    read_done(path,'开入端子号')
def read_done_in_describe(path):
    read_done(path,'开入端子描述')
def read_done_in_ref(path):
    read_done(path,'开入端子引用')

