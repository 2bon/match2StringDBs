from Class import Port
from Class.Object import Object


class Device(Object):
    chinese_name = '设备'
    def __init__(self, isIn: bool, name: str, Port: Port):
        self.isIn = isIn
        self.name = name
        self.Port = Port