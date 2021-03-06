import pandas as pd

print( pd.ExcelFile('test/井门.xls').parse('已配置')['开出端子号'])

def read_excel_column(path: str, sheet: str, column: str) -> list:
    """

    :rtype: list
    """
    df = pd.ExcelFile(path).parse(sheet)[column]
    print(df)
    return df


# read_excel_column('test/井门.xls','已配置','开出端子描述')
def read_done(path, column):
    read_excel_column(path, '已配置', column)

def read_done(path, column):
    read_excel_column(path, '已配置', column)


# read_done('test/井门.xls','开出端子描述')
def read_done_out(path, columnTail):
    read_done(path, '开出' + columnTail)


def read_done_outDeviceName(path):
    read_done_out(path, '设备名称')


def read_done_outPortNum(path):
    read_done_out(path, '端子号')


def read_done_outDescribe(path):
    read_done_out(path, '端子描述')


def read_done_outRef(path):
    read_done_out(path, '端子引用')


def read_done_in(path, columnTail):
    read_done(path, '开入' + columnTail)


def read_done_inDeviceName(path):
    read_done_in(path, '设备名称')


def read_done_inPortNum(path):
    read_done_in(path, '端子号')


def read_done_inDescribe(path):
    read_done_in(path, '端子描述')


def read_done_inRef(path):
    read_done_in(path, '端子引用')


#read_done_inRef('test/井门.xls')
