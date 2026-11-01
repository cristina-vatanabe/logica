# Importa as cores e o código de redefinição usados para fazer a formatação do design do menu
from cores import *

# Variável criada para guardar as tarefas digitadas pelo usuário em uma lista
tarefas = []

# Função criada para exibir as opções do Menu para o usuário
# Obs: RESET serve para ele não "colorir" tudo pela frente
def menu():
    print(f"\n" + FRENTE_AMARELO + "___MENU___" + RESET)
    print("1- Adicionar Tarefa")
    print("2- Listar Tarefa")
    print("3- Remover Tarefa")
    print("4- Sair")

# Função para adicionar uma nova tarefa na lista
def adicionarTarefa():
        tarefa = input("Digite o nome da tarefas: ")
        tarefas.append(tarefa)
        print("Tarefa Adicionada")

# Função para exibir os itens da lista ou informar se está vazia
def listarTarefas():
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada")
        else:
            for numero, tarefa in enumerate(tarefas, start=1):
                print(numero, "-", tarefa)

# Função para visualizar qual tarefa será retirada da lista, caso o usuário escolha essa opção        
def removerTarefa():
    listarTarefas()

    if len(tarefas) > 0:
      # A escolha é convertida para inteiro para permitir validar o número.  
      numero = int(input("Digite o número da tarefa a remover: "))

     # As posições de uma lista Python começam em 0, mas a numeração apresentada ao usuário começa em 1. Subtrair 1 converte a escolha
     # para o índice correspondente: por exemplo, a tarefa 1 está no índice 0.
     # Pop remove essa tarefa da lista e retorna o valor removido. 
     # Esta comparação encadeada verifica se o número escolhido está entre 1 e a quantidade de tarefas, incluindo os dois limites. 
     # É equivalente a (1 <= numero) and (numero <= len(tarefas)); assim, só aceita uma tarefa que realmente existe na lista.

    if 1 <= numero <= len(tarefas):
         tarefas.pop(numero - 1)
         print("Tarefa removida!")
    else:
         print("Número inválido")

# Inicializa a opção como texto vazio para iniciar o laço do menu.
opcao = ""

# Continua exibindo o menu até o usuário escolher a opção "4"
while opcao != "4":
    menu()
    # input sempre retorna o que foi digitado como texto.
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
         adicionarTarefa()
    elif opcao == "2":
         listarTarefas()
    elif opcao == "3":
         removerTarefa()
    elif opcao == "4":
    # Esta condição compara texto com número; a opção "4" não entra aqui. 
      print("Até logo!")
    else:
      print("Opção inválida!")   