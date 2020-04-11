from Class import Device
from Class.Object import Object


class Match(Object):

    def __init__(self, inDevice: Device, outDevice: Device, str):
        self.str = str

        self.inDevice = inDevice
        self.outDevice = outDevice
