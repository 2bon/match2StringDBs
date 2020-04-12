from Class.Object import Object


class Port(Object):
    chinese_name = '端子'

    def __init__(self, deviceName, num, description: str, reference):
        self.deviceName = deviceName
        if 'Goose' in num:
            if 'sv' in num:
                #print(num)
                raise RuntimeError('Goose + sv can not co-exist')
            else:
                self.isGoose = True
        else:
            self.isGoose = False
        #print(self.isGoose)
        if 'Out' in num:
            if 'in' in num:
                raise RuntimeError('Out + in can not co-exist')
            else:
                self.isOut = True
        else:
            self.isOut = False
        self.num = num
        self.description = description
        self.reference = reference
