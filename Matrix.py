from Class import Port
from Class.Object import Object
import pandas as pd


class Matrix(Object):

    def __init__(self, row: [], column: []):
        self.row = row
        self.column = column
        self = pd.DataFrame

    def set_row(self, row: []):
        self.row = row

    def set_column(self, column: []):
        self.column = column
