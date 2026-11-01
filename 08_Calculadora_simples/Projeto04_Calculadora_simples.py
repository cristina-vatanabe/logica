# Contexto
# Você já escreveu programas que cumprimentam pessoas, montam listas e contam até 1000. 
# Agora é hora de reunir o que aprendeu e criar algo que as pessoas realmente usam no dia a dia: uma calculadora.

# O desafio vai além de fazer contas. Uma boa calculadora também precisa reagir bem quando algo não faz sentido, 
# como dividir por zero ou pedir uma operação que ela não conhece.

# O que o programa deve fazer
# Pedir ao usuário, com a função input(), três informações, uma de cada vez e nesta ordem:

# Ordem	Informação	Valores aceitos
# 1	Primeiro número	Qualquer número, inteiro ou decimal
# 2	Segundo número	Qualquer número, inteiro ou decimal
# 3	Operador	+ (soma), - (subtração), * (multiplicação) ou / (divisão)
# Realizar a operação escolhida entre os dois números.

# Exibir o resultado na tela.

# O que o programa deve exibir
# Situação	Saída esperada
# O operador é válido e a conta pode ser feita	O valor do resultado, sem nenhum texto antes ou depois
# Divisão em que o segundo número é zero	Não é possível dividir por zero
# O operador informado não é um dos quatro aceitos	Operador inválido
# Detalhes importantes:

# Números decimais usam ponto, como em 2.5.
# Nos casos de erro, o programa não deve exibir nenhum resultado.
# A forma de escrever o valor é livre. O que importa é que ele esteja correto. Por exemplo, 10 e 10.0 são aceitos, e 3.33 e 3.3333333333333335 também.
# O resultado (ou a mensagem de erro) deve ser a última coisa exibida pelo programa, em uma única linha.
# Sugestão (opcional): deixe a saída mais parecida com a de uma calculadora de verdade. Mostre os resultados inteiros sem casa decimal (10 em vez de 10.0). 
# Se quiser ir além, limite também os decimais a 2 casas (3.33 em vez de 3.3333333333333335). 
# Isso não é obrigatório, mas deixa o resultado mais agradável de ler. Os exemplos abaixo mostram a saída da solução de referência, que mostra os inteiros sem casa decimal, mas não limita os decimais.

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador: + (soma) | - (subtração) | * (multiplicação) | / (divisão): ")

if operador == "+":
    print(n1+n2)

elif operador == "-":
      print(n1-n2)
 
elif operador == "*":
      print(n1*n2)

elif operador == "/":
      if n2 == 0:
           print("Não é possível dividir por zero")
      else: print(n1/n2) 

else:
     print("Operador inválido")







