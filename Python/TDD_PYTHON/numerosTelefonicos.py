# coding: utf-8


class ValidaTelefonesFixos():

    NUM = str
    DDD = str

    def __init__(self):
        self

    def PrimeiraValidacao(self, COMPLETO):
        if len(COMPLETO) == 10 and COMPLETO.isdigit():
            self.COMPLETO = COMPLETO
            return "Quantidade de dígitos.......Ok"
        else:
            return "Há mais ou menos dígitos que o necessário"

    def DivisaoDDD(self):
        self.DDD = self.COMPLETO[0:2]
        self.NUM = self.COMPLETO[2:10]
        return "Divisão de dígitos.......Ok"

    def ValidacaoDDD(self):
        if len(self.DDD) == 2 and self.DDD.isdigit() and self.DDD[0] != "0":
            return "DDD.......Ok"
        else:
            return "DDD inválido!"

    def ValidacaoFixo(self):
        if len(self.NUM) == 8 and self.NUM.isdigit() and self.NUM[0] in [
                '2', '3', '4', '5']:
            return "Número.......Ok"
        else:
            return "Não é um número de telefonia fixa"

    def getDDD(self):
        return self.DDD

cl = ValidaTelefonesFixos()
try:
    print cl.PrimeiraValidacao('4749444164')
    print cl.DivisaoDDD()
    print cl.ValidacaoDDD()
    print cl.ValidacaoFixo()
except:
    print "Operação Cancelada"
