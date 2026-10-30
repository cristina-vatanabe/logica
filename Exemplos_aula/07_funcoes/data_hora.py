
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
dias_semana = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", 
               "sexta-feira", "sábado", "domingo"]

# Função que mostra a data(padrão americano)
data = datetime.date(2024, 12, 21)

# A função print exibe o resultado da variável criada ou o texto que você quer que apareça na tela
print(data)

#Função para mostrar a data de hoje no padrão americano
hoje = datetime.date.today()
print(hoje)

# Mostra a data atual com a função "hoje" e depois converte no padrão do Brasil com o uso de ".strftime no modelo dia/mês/ano
print(hoje.strftime("%d/%m/%Y"))


print(f"São Paulo, {dias_semana[hoje.weekday()]}, {hoje.day} de {meses[hoje.month - 1]} de {hoje.year}")

print(f"2024 é Bissexto: {calendar.isleap(2024)}")

print(f"É o ultimo dia do mês? {calendar.monthrange(2026,10)[1]}")


