# Contexto
# Na primeira calculadora, cada conta envolvia dois números. 
# Uma calculadora melhorada precisa ir além: somar ou multiplicar uma lista inteira de números e responder a perguntas simples sobre eles, como "este número é par?".
# Em vez de um programa único, você vai criar funções: pequenos blocos de código, cada um com uma tarefa bem definida, que podem ser usados quantas vezes você quiser. 
# É assim que calculadoras e programas de verdade são construídos.
# Importante: crie uma calculadora nova, do zero, em vez de atualizar a primeira que você criou. 
# Mas leve com você o que aprendeu sobre fluxo de controle, ordem das operações (BODMAS) e funções.

# Calcula o somatório dos números da lista 
def somarmultiplosnumeros(numeros):
    # Pega a lista inteira e soma tudo de uma vez
    return sum(numeros)

# Calcula a multiplicação dos números da lista 
def multiplicarmultiplosnumeros(numeros):
    resultado = 1
    for numero in numeros:
        resultado = resultado * numero
    return resultado

# Verifica se o número é inteiro
def ehinteiro(numero):
    return numero % 1 == 0

# Verifica se o número é inteiro e par
def ehpar(numero):
    
    return ehinteiro(numero) and (numero % 2 == 0)

# --- TESTANDO AS NOSSAS FUNÇÕES NO PRÓPRIO ARQUIVO ---
if __name__ == "__main__":
    print("Soma [5, 10, 15]:", somarmultiplosnumeros([5, 10, 15]))
    print("Soma [0.5, -4, 2]:", somarmultiplosnumeros([0.5, -4, 2]))
    
    print("Multiplicação [2, 5]:", multiplicarmultiplosnumeros([2, 5]))
    print("Multiplicação [-1, 3, 2.5]:", multiplicarmultiplosnumeros([-1, 3, 2.5]))
    
    print("8 ehpar?:", ehpar(8))
    print("5 ehpar?:", ehpar(5))
    print("2.5 ehpar?:", ehpar(2.5))
    
    print("10 ehinteiro?:", ehinteiro(10))
    print("-6 ehinteiro?:", ehinteiro(-6))
    print("4.2 ehinteiro?:", ehinteiro(4.2))