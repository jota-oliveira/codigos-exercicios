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
        self.assertEqual(
            "Quantidade de dígitos.......Ok", cl.PrimeiraValidacao('5511709091')
            )

    def test_PrimeiraValidacao_Incorreta(self):
        # mais curto
        self.assertEqual(
            "Há mais ou menos dígitos que o necessário",
            cl.PrimeiraValidacao('123')
        )
        # maior que
        self.assertEqual(
            "Há mais ou menos dígitos que o necessário",
            cl.PrimeiraValidacao('1234567890111213')
        )
        # sintax inválida
        self.assertEqual(
            "Há mais ou menos dígitos que o necessário",
            cl.PrimeiraValidacao('dasd321FDSF21as')
        )

    def test_ValidacaoDDD_Correto(self):
        # Valem quaisquer dois dígitos
        cl.PrimeiraValidacao('4749444164')
        cl.DivisaoDDD()
        self.assertEqual("DDD.......Ok", cl.ValidacaoDDD())
        cl.PrimeiraValidacao('1134799091')
        cl.DivisaoDDD()
        self.assertEqual("DDD.......Ok", cl.ValidacaoDDD())

    def test_ValidacaoDDD_Incorreto(self):
        # Começando com 0
        cl.PrimeiraValidacao('0711709091')
        cl.DivisaoDDD()
        self.assertEqual("DDD inválido!", cl.ValidacaoDDD())

    def test_validacaoFixo(self):
        # Verifica se está na faixa [2-5]
        cl.PrimeiraValidacao('4723995530')
        cl.DivisaoDDD()
        # Iniciando com 2
        self.assertEqual("Número.......Ok", cl.ValidacaoFixo())
        cl.PrimeiraValidacao('4734496567')
        cl.DivisaoDDD()
        # Iniciando com 3
        self.assertEqual("Número.......Ok", cl.ValidacaoFixo())
        cl.PrimeiraValidacao('4744448774')
        cl.DivisaoDDD()
        # Iniciando com 4
        self.assertEqual("Número.......Ok", cl.ValidacaoFixo())
        cl.PrimeiraValidacao('4754537777')
        cl.DivisaoDDD()
        # Iniciando com 5
        self.assertEqual("Número.......Ok", cl.ValidacaoFixo())

    def test_validacaoNaoFixo(self):
        # Verifica se não está na faixa [2-5]
        cl.PrimeiraValidacao('4713995530')
        cl.DivisaoDDD()
        self.assertEqual(
            "Não é um número de telefonia fixa", cl.ValidacaoFixo()
        )

        cl.PrimeiraValidacao('4764496567')
        cl.DivisaoDDD()
        self.assertEqual(
            "Não é um número de telefonia fixa", cl.ValidacaoFixo()
        )

        cl.PrimeiraValidacao('4774448774')
        cl.DivisaoDDD()
        self.assertEqual(
            "Não é um número de telefonia fixa", cl.ValidacaoFixo()
        )

        cl.PrimeiraValidacao('4784537777')
        cl.DivisaoDDD()
        self.assertEqual(
            "Não é um número de telefonia fixa", cl.ValidacaoFixo()
        )

        cl.PrimeiraValidacao('4784537777')
        cl.DivisaoDDD()
        self.assertEqual(
            "Não é um número de telefonia fixa", cl.ValidacaoFixo()
        )


if __name__ == '__main__':
    unittest.main()
