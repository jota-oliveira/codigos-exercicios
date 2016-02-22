# coding: utf-8
import unittest
from numeros_telefonicos import Celulares


class TestCelurares(unittest.TestCase):

    def test_verificar_tamanho(self):
        # Devem haver no máximo 11 Dígitos, considerando DDD + Tipagem Móvel
        # + Número. ex: xx (9)[9|8|7] xxxxxxx

        # Testando corretos
        corretos = [
            '5511709091', '0987654321', '3812707241', '83912707241',
            '93912707241'
        ]

        for elemento in corretos:
            cl = Celulares(elemento)
            self.assertTrue(cl._verificar_tamanho())

        # Testando incorretos
        incorretos = [
            '123', '1234567890111213', 'dasd321FDSF21as', '738127072414'
        ]

        for elemento in incorretos:
            cl = Celulares(elemento)
            self.assertFalse(cl._verificar_tamanho())

    def test_verificar_ddd(self):
        # Valem quaisquer dois dígitos, que não comecem com 0

        # Testando corretos
        corretos = ['5511709091', '4712707241', '11939127072']
        for elemento in corretos:
            cl = Celulares(elemento)
            self.assertTrue(cl._verificar_ddd())

        # Testando incorretos
        cl = Celulares('0711709091')
        self.assertFalse(cl._verificar_ddd())

    def test_validar_como_celular(self):
        # Verifica se os números começam com 9
        corretos = [
            '4799887755', '4797887755', '11988737373',
            '85977101010', '85997121212'
        ]

        for elemento in corretos:
            cl = Celulares(elemento)
            self.assertTrue(cl._validar_como_celular())

        incorretos = [
            '4719887755', '4729887755', '4839887755', '4849887755',
            '4859887755', '8569887755', '8509887755', '8579887755',
            '2789887755', '27709887755', '27209887755', '27nadahaver',
            '85caracter', '4819carac7'
            ]

        for elemento in incorretos:
            cl = Celulares(elemento)
            self.assertFalse(cl._validar_como_celular())

    def test_ddd(self):
        # Verifica se retorna o ddd passado como instância da classe
        cl = Celulares('4799887755')
        self.assertEqual('47', cl.ddd())

    def test_get_numero(self):
        # Verifica se retorna o número passado como instância da classe
        cl = Celulares('4799887755')
        self.assertEqual('99887755', cl.get_numero())

    def test_validar(self):
        # Recebe um número e faz todas as verificações
        corretos = ['4794441641', '47912707241', '47997741641']

        for elemento in corretos:
            cl = Celulares(elemento)
            self.assertTrue(cl.validar())

        incorretos = [
            '0794441641', '314441641', '31dasjid', '47794441641', '47704441641'
        ]

        for elemento in incorretos:
            cl = Celulares(elemento)
            self.assertFalse(cl.validar())


if __name__ == '__main__':
    unittest.main()
