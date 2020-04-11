from Class.Object import Object


class Port(Object):
    chinese_name = '端子'

    def __init__(self, num, description, reference, str):
        self.str = str
        self.num = num
        self.description = description
        self.reference = reference
