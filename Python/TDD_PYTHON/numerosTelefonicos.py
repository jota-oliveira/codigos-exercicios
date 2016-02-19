# coding: utf-8


class ValidaTelefonesFixos():

    NUM = str

    def __init__(self):
        pass

    def PrimeiraValidacao(self, COMPLETO):
        if len(COMPLETO) == 10 and COMPLETO.isdigit():
            return True
        else:
            return False

    def ValidacaoDDD(self, DDD):
        if len(DDD) == 2 and DDD.isdigit() and DDD[0] != "0":
            return True
        else:
            return False

    def ValidacaoFixo(self, NUM):
        if len(NUM) == 8 and NUM.isdigit() and NUM[0] in ['2', '3', '4', '5']:
            return True
        else:
            return False

cl = ValidaTelefonesFixos()
