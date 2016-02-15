# coding: utf-8

# Nesse código são estudados algumas questões como:
#     * List comprehensions
#     * A estrutura de dados quicksort
#     * Recursividade


# RESUMO
# Como funciona o Quicksort?
# Escolhe-se um pivô, normalmente a primeira posição, embora não seja uma regra.
# Verifica-se então quem é igual ao pivô, quem são os menores que o pivô, e quem
# são os maiores que o pivô. Posiciona-se os menores a esquerda, os iguais ao
# meio e os maiores a direita. Depois disso esse mesmo processo acontece
# apenas com os menores, e apenas com os maiores, ordenando assim a lista toda.


def quicksort(lista):

    if len(lista) <= 1:
        return lista

    pivo = lista[0]
    # list comprehensions
    iguais = [x for x in lista if x == pivo]
    # Pode-se ler algo como: Para todo x, pertencente ao conjunto lista, onde
    # x é igual ao pivô... List comprehensions nos aproxima da
    # linguagem matemática
    menores = [x for x in lista if x < pivo]
    maiores = [x for x in lista if x > pivo]
    # Uso da estrutura de dados Recursividade. Essa função chama ela mesma por
    # mais duas vezes, sendo seu parâmetro de entrada, o próprio retorno da
    # chamada anterior.
    return quicksort(menores) + iguais + quicksort(maiores)

if __name__ == "__main__":
    numeros = [7, 78, 77, 87, 6, 5, 22, -13, 43, 243, 56, 73, 57]
    print quicksort(numeros)
