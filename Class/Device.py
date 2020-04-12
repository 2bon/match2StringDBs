from Class import Port
from Class.Object import Object


class Device(Object):
    chinese_name = '设备'

    def __init__(self, isOut: bool, name: str, Port: Port, str):
        self.str = str

        self.isOut = isOut
        self.name = name
        self.Port = Port
