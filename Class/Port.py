from Class.Object import Object


class Port(Object):
    chinese_name = '端子'

    def __init__(self,isGoose: bool,isOut: bool,  num, description, reference):
        self.isGoose = isGoose
        self.isOut = isOut
        self.num = num
        self.description = description
        self.reference = reference
