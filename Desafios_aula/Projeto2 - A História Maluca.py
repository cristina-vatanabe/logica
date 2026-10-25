# Contexto:
# Mad Lib é um jogo de palavras. Uma pessoa pede ao grupo palavras soltas (um nome, um adjetivo, uma comida...) sem contar para que servem. 
# Depois, ela encaixa tudo nos espaços em branco de uma história pronta, e o resultado costuma ser bem engraçado.
# Neste projeto, o seu programa assume o papel de quem conduz o jogo.

Nome = input("Digite o nome: ")
Profissão = input("Digite a profissão: ")
Primeiro_Adjetivo = input("Digite o primeiro adjetivo: ")
Segundo_Adjetivo = input("Digite o segundo adjetivo: ")
Primeira_Comida = input("Digite a primeira comida: ")
Segunda_Comida = input("Digite a segunda comida: ")
Um_sentimento = input("Digite um sentimento: ")

print(f"{Nome} começou hoje o seu primeiro curso na Generation Brasil.\nEstá cursando a formação em {Profissão}.\nAchou a sua turma muito {Primeiro_Adjetivo} mas o instrutor era, no mínimo, {Segundo_Adjetivo}.\nNo almoço, comeu {Primeira_Comida} e {Segunda_Comida} enquanto revisava as suas anotações.\nAo final do dia, sente-se {Um_sentimento}, mas tem a determinação de concluir a jornada.")

