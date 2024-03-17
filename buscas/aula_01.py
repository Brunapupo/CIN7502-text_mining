import re
caminho_do_arquivo = '../database/cin7502_texto01.txt'

with open(caminho_do_arquivo, 'r', encoding='utf-8') as file:
    banco = file.read()

# 1 - Os valores monetários exclusivamente em reais do arquivo TXT
regex_valores_reais = r'R\$\s?\d{1,3}(?:\.\d{3})*(?:,\d{2})?'
match_valores_reais = re.findall(regex_valores_reais, banco)
print('1. Os valores monetários exclusivamente em reais do arquivo TXT:')
print()
if match_valores_reais:
    for valores_reais in match_valores_reais:
        print(valores_reais)
else:
    print("Nenhum valor encontrado.")

print('------------------------------------------------------------------\n')

# 2 - Os valores monetários exclusivamente em dólares do arquivo TXT
regex_valores_dolares = r'US\$\s?\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
match_valores_dolares = re.findall(regex_valores_dolares, banco)
print('2. Os valores monetários exclusivamente em reais do arquivo TXT:')
print()
if match_valores_reais:
    for valores_dolares in match_valores_dolares:
        print(valores_dolares)
else:
    print("Nenhum valor encontrado.")

print('------------------------------------------------------------------\n')

# 3 - Todos os valores monetários do arquivo TXT
regex_todos_os_valores = r'\$\s?\.?\d{1,3}[,.]\d{3}[,.]\d{2}'
match_todos_os_valores = re.findall(regex_todos_os_valores, banco)
print('3. Todos os valores monetários do arquivo TXT:')
print()
if match_todos_os_valores:
    for todos_os_valores in match_todos_os_valores:
        print(todos_os_valores)
else:
    print("Nenhum valor encontrado.")

print('------------------------------------------------------------------\n')

# 4 - Todos os dias de janeiro (no formato de datas do Brasil) do arquivo TXT
regex_dias_de_janeiro_brasil = r'\b(0[1-9]|[12][0-9]|3[01])/01/\d{4}(?!\s*US\$)'
match_dias_de_janeiro_brasil = re.findall(regex_dias_de_janeiro_brasil, banco)
print('4. Todos os dias de janeiro (no formato de datas do Brasil) do arquivo TXT:')
print()
if match_dias_de_janeiro_brasil:
    for dias_de_janeiro_brasil in match_dias_de_janeiro_brasil:
        print(dias_de_janeiro_brasil)
else:
    print("Nenhum valor encontrado.")

print('------------------------------------------------------------------\n')

# 5. Todos os dias de janeiro (no formato de datas do EUA) do arquivo TXT
regex_dias_de_janeiro_eua = r'\b(0[1-9]|[12][0-9]|3[01])/01/\d{4}(?=\s*US\$)'
match_dias_de_janeiro_eua = re.findall(regex_dias_de_janeiro_eua, banco)
print('5. Todos os dias de janeiro (no formato de datas do EUA) do arquivo TXT:')
print()
if match_dias_de_janeiro_eua:
    for dias_de_janeiro_eua in match_dias_de_janeiro_eua:
        print(dias_de_janeiro_eua)
else:
    print("Nenhum valor encontrado.")

print('------------------------------------------------------------------\n')

# 6. Todos os dias de janeiro de 2018 (no formato de datas do brasil) para busca genérica que leve em consideração os 31 dias do mês
regex_dias_de_janeiro_de_2018 = r'\b(0[1-9]|[12][0-9]|3[01])/01/2018(?!\s*US\$)'
match_dias_de_janeiro_de_2018 = re.findall(regex_dias_de_janeiro_de_2018, banco)
print('6. Todos os dias de janeiro de 2018 (no formato de datas do brasil)\npara busca genérica que leve em consideração os 31 dias do mês:')
print()
if match_dias_de_janeiro_de_2018:
    for dias_de_janeiro_de_2018 in match_dias_de_janeiro_de_2018:
        print(dias_de_janeiro_de_2018)
else:
   print("Nenhum valor encontrado.")

print('------------------------------------------------------------------\n')

# 7. Todos os dias de janeiro de 2018 (no formato de datas do EUA) para busca genérica que leve em consideração os 31 dias do mês
regex_dias_de_janeiro_de_2018_eua = r'\b01/(0[1-9]|[12][0-9]|3[01])/2018\b'
match_dias_de_janeiro_de_2018_eua = re.findall(regex_dias_de_janeiro_de_2018_eua, banco)
print('6. Todos os dias de janeiro de 2018 (no formato de datas do brasil)\npara busca genérica que leve em consideração os 31 dias do mês:')
print()
if match_dias_de_janeiro_de_2018_eua:
    for dias_de_janeiro_de_2018_eua in match_dias_de_janeiro_de_2018_eua:
        print(dias_de_janeiro_de_2018_eua)
else:
    print("Nenhum valor encontrado.")

print('------------------------------------------------------------------\n')

# 8. Só os dias pares de janeiro (formato do Brasil) do arquivo TXT
regex_dias_pares_brasil = r'\b([0-2][02468])/01/\d{4}\b(?!\s*US\$)'
match_dias_pares_brasil = re.findall(regex_dias_pares_brasil, banco)
print('8. Só os dias pares de janeiro (formato do Brasil) do arquivo TXT:')
print()
if match_dias_pares_brasil:
    for dias_pares_brasil in match_dias_pares_brasil:
        print(dias_pares_brasil)
else:
    print("Nenhum valor encontrado.")

print('------------------------------------------------------------------\n')

# 9. Só os dias pares de janeiro (formato do EUA) do arquivo TXT
regex_dias_pares_eua = r'\b01/([0-2][02468])/\d{4}\b(?=\s*US\$)'
match_dias_pares_eua = re.findall(regex_dias_pares_eua, banco)
print('9. Só os dias pares de janeiro (formato do EUA) do arquivo TXT:')
print()
if match_dias_pares_eua:
    for dias_pares_eua in match_dias_pares_eua:
        print(dias_pares_eua)
else:
    print("Nenhum valor encontrado.")

print('------------------------------------------------------------------\n')

# 10. Só os dias pares de janeiro (formato do Brasil), busca genérica, com exceção do dia 10
regex_dias_pares_brasil_ex10 = r'\b(02|04|06|08|12|14|16|18|20|22|24|26|28|30)/01/\d{4}\b(?!\s*US\$)'
match_dias_pares_brasil_ex10 = re.findall(regex_dias_pares_brasil_ex10, banco)
print('10. Só os dias pares de janeiro (formato do Brasil),/nbusca genérica, com exceção do dia 10:')
print()
if match_dias_pares_brasil_ex10:
    for dias_pares_brasil_ex10 in match_dias_pares_brasil_ex10:
        print(dias_pares_brasil_ex10)
else:
    print("Nenhum valor encontrado.")

print('------------------------------------------------------------------\n')