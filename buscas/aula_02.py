import re
caminho_do_arquivo_2 = '../database/cin7502_texto02.txt'
import re
caminho_do_arquivo_3 = '../database/cin7502_texto03.txt'

with open(caminho_do_arquivo_2, 'r', encoding='utf-8') as file:
    banco_2 = file.read()
with open(caminho_do_arquivo_3, 'r', encoding='utf-8') as file:
    banco_3 = file.read() 

# 1 - Escreva uma regex que capture as sete palavras da lista abaixo (com exatos 7 matchs)
regex_sete_palavras = r'\b\w+\b'
match_sete_palavras = re.findall(regex_sete_palavras, banco_2)
print('1. Escreva uma regex que capture as sete palavras da lista abaixo (com exatos 7 matchs):')
print()
if match_sete_palavras:
    for sete_palavras in match_sete_palavras:
        print(sete_palavras, end="\n")
else:
    print("Nenhum valor encontrado.")

print('------------------------------------------------------------------\n')

# 2 - Escreva uma regex que capture especificicamente a sequência "viagra" e todas as variações existentes.
regex_variacoes_viagra_1 = r'v[1i!][a@]gr[@a]'
regex_variacoes_viagra_2 = r'v(i|!|1)(a|@)gr(a|@)'
regex_variacoes_viagra_3 = r'v.{5}'
match_variacoes_viagra = re.findall(regex_variacoes_viagra_1, banco_3)
print('2. Escreva uma regex que capture especificicamente a sequência "viagra" e todas as variações existentes: ')
print()
if match_variacoes_viagra:
    for variacoes_viagra in match_variacoes_viagra:
        print(variacoes_viagra, end="\n")
else:
    print("Nenhum valor encontrado.")

print('------------------------------------------------------------------\n')