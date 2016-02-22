# coding: utf-8


class Telefones():

    quantidade_digitos = 10

    def __init__(self, numero):
        self.numero = numero

    def _verificar_tamanho(self):
        if len(self.numero) == self.quantidade_digitos and \
                    self.numero.isdigit():
            return True
        else:
            return False

    def _verificar_ddd(self):
        numero_ddd = self.numero[0:2]
        if numero_ddd[0] != "0":
            return True
        else:
            return False

    def ddd(self):
        return self.numero[0:2]

    def get_numero(self):
        return self.numero[2:]


class TelefonesFixos(Telefones):

    def _validar_como_fixo(self):
        if self.get_numero()[0] in \
                ['2', '3', '4', '5']:
            return True
        else:
            return False

    def validar(self):

        digitos_fornecidos = \
            self._verificar_tamanho()

        verificacao_ddd = self._verificar_ddd()

        validar_fixo = self._validar_como_fixo()

        if digitos_fornecidos is True and verificacao_ddd is True and \
                validar_fixo is True:
            return True
        else:
            return False


class Celulares(Telefones):

    def _verificar_tamanho(self):

        if len(self.numero) in [
            self.quantidade_digitos, (self.quantidade_digitos + 1)] and \
                self.numero.isdigit():
            return True
        else:
            return False

    def _validar_como_celular(self):

        if self.get_numero()[0] == '9':
            return True
        else:
            return False

    def validar(self):

        digitos_fornecidos = \
            self._verificar_tamanho()

        verificacao_ddd = self._verificar_ddd()

        validar_celular = self._validar_como_celular()

        if digitos_fornecidos is True and verificacao_ddd is True and \
                validar_celular is True:
            return True
        else:
            return False
