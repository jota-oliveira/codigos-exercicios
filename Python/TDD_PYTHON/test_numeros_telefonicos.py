# coding: utf-8
import unittest
from numeros_telefonicos import TelefonesFixos


class TestTelefonesFixos(unittest.TestCase):

    def test_verificar_quantidade_digitos_fornecidos(self):
        # Devem haver no máximo 10 Dígitos, considerando DDD + Tipagem Fixo
        # + Número. ex: xx [2-5] xxxxxxx

        # Testando corretos
        corretos = ['5534441112', '0934445577', '3829921313']
        for elemento in corretos:
            cl = TelefonesFixos(elemento)
            self.assertTrue(cl._verificar_tamanho())

        # Testando incorretos
        # Menor que; Maior que; Com caracteres
        incorretos = ['123', '1234567890111213', 'dasd321FDSF21as']
        for elemento in incorretos:
            cl = TelefonesFixos(elemento)
            self.assertFalse(cl._verificar_tamanho())

    def test_verificar_ddd(self):
        # Valem quaisquer dois dígitos, que não comecem com 0
        # Considera-se que caracteres são excluídos com a verificação acima

        # Testando corretos
        corretos = ['5534441641', '4734445544', '1134440091']
        for elemento in corretos:
            cl = TelefonesFixos(elemento)
            self.assertTrue(cl._verificar_ddd())

        # Testando incorretos
        # A única chance de falha é caso aplique-se o número 0
        cl = TelefonesFixos('0734441515')
        self.assertFalse(cl._verificar_ddd())

    def test_validar_como_fixo(self):
        # Verifica se está na faixa [2-5]

        # Telefones nas Faixas 2,3,4 e 5
        corretos = ['4723995530', '1134496567', '8544448774', '8554537777']
        for elemento in corretos:
            cl = TelefonesFixos(elemento)
            self.assertTrue(cl._validar_como_fixo())

        # Telefones fora das Faixas 2,3,4 e 5
        incorretos = ['1113995530', '1464496567', '4574448774', '4884537777']
        for elemento in incorretos:
            cl = TelefonesFixos(elemento)
            self.assertFalse(cl._validar_como_fixo())

    def test_ddd(self):
        # Verifica se retorna o ddd passado como instância da classe
        cl = TelefonesFixos('4734441515')
        self.assertEqual('47', cl.ddd())

    def test_get_numero(self):
        # Verifica se retorna o número passado como instância da classe
        cl = TelefonesFixos('4734441515')
        self.assertEqual('34441515', cl.get_numero())

    def test_validar(self):
        # Verifica se o método validar está funcionando como meio de chamar
        # o método privado validar_como_fixo
        cl = TelefonesFixos('4734441515')
        self.assertTrue(cl.validar())

        incorretos = ['314441641', '31dasjid']
        for elemento in incorretos:
            cl = TelefonesFixos(elemento)
            self.assertFalse(cl.validar())


if __name__ == '__main__':
    unittest.main()
