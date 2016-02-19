# coding: utf-8


class ValidaTelefones_Fixos():

    # DDI = int
    # DDD = int
    # NUM = int

    # def __init__(self, DDI, DDD, NUM):
        # self.DDI = DDI
        # self.DDD = DDD
        # self.NUM = NUM

    def validacaoDDI(self, DDI):
        if DDI == 55:
            return 'Brasil'
        elif DDI == 20:
            return 'Egito'
        elif DDI == 33:
            return 'França'
