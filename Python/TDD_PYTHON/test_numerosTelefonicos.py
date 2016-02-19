# coding: utf-8
import unittest
from numerosTelefonicos import ValidaTelefonesFixos
cl = ValidaTelefonesFixos()


class TestNumerosTelefonicos(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_PrimeiraValidacao_Correta(self):
        # Devem haver no máximo 10 Dígitos, considerando DDD + Tipagem Fixo
        # + Número. ex: 55 xx [2-5] xxxxxxx
        self.assertEqual(True, cl.PrimeiraValidacao('5511709091'))

    def test_PrimeiraValidacao_Incorreta(self):
        # mais curto
        self.assertEqual(False, cl.PrimeiraValidacao('123'))
        # maior que
        self.assertEqual(False, cl.PrimeiraValidacao('1234567890111213'))
        # sintax inválida
        self.assertEqual(False, cl.PrimeiraValidacao('dasd321FDSF21as'))

    def test_ValidacaoDDD_Correto(self):
        # Valem quaisquer dois dígitos
        self.assertEqual(True, cl.ValidacaoDDD('55'))
        self.assertEqual(True, cl.ValidacaoDDD('47'))
        self.assertEqual(True, cl.ValidacaoDDD('11'))

    def test_ValidacaoDDD_Incorreto(self):
        # Mais curto que
        self.assertEqual(False, cl.ValidacaoDDD('1'))
        # Começando com 0
        self.assertEqual(False, cl.ValidacaoDDD('07'))
        # Maior que
        self.assertEqual(False, cl.ValidacaoDDD('112'))
        # Não são números
        self.assertEqual(False, cl.ValidacaoDDD('1E'))

    def test_validacaoFixo(self):
        # Verifica se está na faixa [2-5]
        self.assertEqual(True, cl.ValidacaoFixo('23995530'))
        self.assertEqual(True, cl.ValidacaoFixo('34496567'))
        self.assertEqual(True, cl.ValidacaoFixo('44448774'))
        self.assertEqual(True, cl.ValidacaoFixo('54537777'))

    def test_validacaoNaoFixo(self):
        # Verifica se não está na faixa [2-5]
        self.assertEqual(False, cl.ValidacaoFixo('13995530'))
        self.assertEqual(False, cl.ValidacaoFixo('64496567'))
        self.assertEqual(False, cl.ValidacaoFixo('74448774'))
        self.assertEqual(False, cl.ValidacaoFixo('84537777'))
        self.assertEqual(False, cl.ValidacaoFixo('84537777'))


if __name__ == '__main__':
    unittest.main()
