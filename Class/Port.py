from Class.Object import Object


class Port(Object):
    chinese_name = '端子'

    def __init__(self, description: str, reference, deviceName=0, num=0):
        self.description = description
        self.reference = reference
        self.deviceName = deviceName
        num = str(num)
        if len(num)>0:
            if 'Goose' in num:
                if 'sv' in num:
                    #print(num)
                    raise RuntimeError('Goose + sv can not co-exist')
                else:
                    self.isGoose = True
            else:
                self.isGoose = False
            if 'Out' in num:
                if 'in' in num:
                    raise RuntimeError('Out + in can not co-exist')
                else:
                    self.isOut = True
            else:
                self.isOut = False
        self.num = num
