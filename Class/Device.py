from Class import Port
from Class.Object import Object


class Device(Object):
    chinese_name = '设备'

    def __init__(self, name: str, portList: [Port], str):
        self.str = str

        self.name = name
        self.portList = portList
