
import pandas as pd
class Object(object):
    chinese_name = '物质'
    def __init__(self, str):
        self.str = str

    def read_excel_column(path: str, sheet: str, column: str) -> list:
        """

        :rtype: list
        """
        df = pd.ExcelFile(path).parse(sheet)[column]
        print(df)
        return df