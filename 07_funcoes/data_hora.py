
# Biblioteca que fornece as funções clássicas de datas
import datetime

# Usado para complementar mais funções que a biblioteca datetime não oferece
import calendar

# Variável "meses" criada com uma lista contendo os meses do ano

meses = [
        "janeiro", 
        "fevereiro", 
        "março", 
        "abril", 
        "maio", 
        "junho",
        "julho", 
        "agosto", 
        "setembro", 
        "outubro", 
        "novembro", 
        "dezembro"
        ]

# Variável "dias_semana" criada com uma lista contendo os dias da semana
# A função weekday() usa índices de 0 (segunda-feira) a 6 (domingo).
dias_semana = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", 
               "sexta-feira", "sábado", "domingo"]

# Função que mostra a data(padrão americano)
data = datetime.date(2024, 12, 21)

# A função print exibe o resultado da variável criada ou o texto que você quer que apareça na tela
print(f"Data específica: {data}")

#Função para mostrar a data de hoje no padrão americano
hoje = datetime.date.today()
print(f"Data atual: {hoje}")

# Mostra a data atual com a função "hoje" e depois converte no padrão do Brasil com o uso de ".strftime no modelo dia/mês/ano
print(f"Data atual (formato brasileiro): {hoje.strftime('%d/%m/%Y')}")

# Combina o dia da semana, o dia do mês, o nome do mês e o ano.
print(f"São Paulo, {dias_semana[hoje.weekday()]}, {hoje.day} de {meses[hoje.month - 1]} de {hoje.year}")

# Verifica se 2024 é um ano bissexto.
print(f"2024 é Bissexto: {calendar.isleap(2024)}")


# monthrange(2026, 10) recebe o ano (2026) e o mês (10 = outubro);
# retorna o dia da semana do primeiro dia e a quantidade de dias do mês.
# O índice [1] seleciona a quantidade de dias, exibida pelo print.
print(f"É o ultimo dia do mês? {calendar.monthrange(2026,10)[1]}")


print(hoje.weekday())
print(hoje.day)
print(hoje.month - 1)


