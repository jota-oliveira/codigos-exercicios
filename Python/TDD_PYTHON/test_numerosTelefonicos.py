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
        self.assertEqual(True, cl.PrimeiraValidacao(551170909))

    def test_PrimeiraValidacao_Incorreta(self):
        # mais curto
        self.assertEqual(False, cl.PrimeiraValidacao(123))
        # maior que
        self.assertEqual(False, cl.PrimeiraValidacao(1234567890111213))
        # sintax inválida
        self.assertEqual(False, cl.PrimeiraValidacao('dasd321FDSF21as'))

    def test_ValidacaoDDD_Correto(self):
        # Valem quaisquer dois dígitos
        self.assertEqual(True, cl.ValidacaoDDI(55))
        self.assertEqual(True, cl.ValidacaoDDI(47))
        self.assertEqual(True, cl.ValidacaoDDI(11))

    def test_ValidacaoDDD_Incorreto(self):
        # Mais curto que
        self.assertEqual(True, cl.ValidacaoDDI(1))
        # Começando com 0
        self.assertEqual(True, cl.ValidacaoDDI(07))
        # Maior que
        self.assertEqual(True, cl.ValidacaoDDI(112))
        # Não são números
        self.assertEqual(True, cl.ValidacaoDDI('11'))

    def test_validacaoFixo(self):
        # Verifica se está na faixa [2-5]
        self.assertEqual(True, cl.ValidacaoDDI(23995530))
        self.assertEqual(True, cl.ValidacaoDDI(34496567))
        self.assertEqual(True, cl.ValidacaoDDI(44448774))
        self.assertEqual(True, cl.ValidacaoDDI(54537777))

    def test_validacaoNaoFixo(self):
        # Verifica se não está na faixa [2-5]
        self.assertEqual(True, cl.ValidacaoDDI(13995530))
        self.assertEqual(True, cl.ValidacaoDDI(64496567))
        self.assertEqual(True, cl.ValidacaoDDI(74448774))
        self.assertEqual(True, cl.ValidacaoDDI(84537777))
        self.assertEqual(True, cl.ValidacaoDDI('84537777'))


if __name__ == '__main__':
    unittest.main()
