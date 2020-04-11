from Class.Object import Object


class Port(Object):
    def __init__(self, num, description, reference):
        self.num = num
        self.description = description
        self.reference = reference
