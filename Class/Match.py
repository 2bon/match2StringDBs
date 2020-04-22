from Class import Port
from Class.Object import Object


class Match(Object):

    def __init__(self, outPort: Port, inPort: Port):
        self.outPort = outPort
        self.inPort = inPort

    def set_outPort(self, outPort: Port):
        self.outPort = outPort

    def set_inPort(self, inPort: Port):
        self.inPort = inPort
