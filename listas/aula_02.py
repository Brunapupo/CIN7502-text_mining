import re
caminho_do_arquivo_2 = '../database/cin7502_texto02.txt'
import re
caminho_do_arquivo_3 = '../database/cin7502_texto03.txt'
import re
caminho_do_arquivo_4 = '../database/cin7502_texto04.txt'
import re
caminho_do_arquivo_5 = '../database/cin7502_texto05.txt'
import re
caminho_do_arquivo_6 = '../database/cin7502_texto06.txt'
import re
caminho_do_arquivo_7 = '../database/cin7502_texto07.txt'


with open(caminho_do_arquivo_2, 'r', encoding='utf-8') as file:
    banco_2 = file.read()
with open(caminho_do_arquivo_3, 'r', encoding='utf-8') as file:
    banco_3 = file.read() 
with open(caminho_do_arquivo_4, 'r', encoding='utf-8') as file:
    banco_4 = file.read() 
with open(caminho_do_arquivo_5, 'r', encoding='utf-8') as file:
    banco_5 = file.read() 
with open(caminho_do_arquivo_6, 'r', encoding='utf-8') as file:
    banco_6 = file.read() 
with open(caminho_do_arquivo_7, 'r', encoding='utf-8') as file:
    banco_7 = file.read() 

# 1 - Escreva uma regex que capture as sete palavras da lista abaixo (com exatos 7 matchs)
regex_sete_palavras = r'\b\w+\b'
match_sete_palavras = re.findall(regex_sete_palavras, banco_2)
print('1. Escreva uma regex que capture as sete palavras da lista abaixo (com exatos 7 matchs): \n')
print('REGEX: \B\w+\B \n')
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
print('2. Escreva uma regex que capture especificicamente a sequência "viagra" e todas as variações existentes: \n')
print('REGEX: v[1i!][a@]gr[@a]\n')
if match_variacoes_viagra:
    for variacoes_viagra in match_variacoes_viagra:
        print(variacoes_viagra, end="\n")
else:
    print("Nenhum valor encontrado.")

print('------------------------------------------------------------------\n')

# 3 - Escreva uma regex específica que capture todos os possíveis formatos de ordem de serviço de determinada empresa.
regex_ordem_servico = r"(OS)(-|#|\s| )?(nn| nn)(-| |n)(n+.*)"
match_ordem_servico = re.findall(regex_ordem_servico, banco_4)
print('3. Escreva uma regex específica que capture todos os possíveis formatos de ordem de serviço de determinada empresa: \n')
print('REGEX: (OS)(-|#|\s| )?(nn| nn)(-| |n)(n+.*)\n')
if match_ordem_servico:
    for ordem_servico in match_ordem_servico:
        # Verificamos se a correspondência é uma tupla e fazemos join, ou simplesmente imprimimos a string
        if isinstance(ordem_servico, tuple):
            print(''.join(ordem_servico))
        else:
            print(ordem_servico)
else:
    print("Nenhum valor encontrado.")

print('------------------------------------------------------------------\n')

# 4 - Construa uma expressão regular específica que capture todos os valores monetários existentes no texto (marcados em amarelo).
regex_yellow_text = r"R\$\s?-?[0-9]+,[0-9]+|\d{1,3}(?:\.\d{3})*(?:,\d{2})?\sreais"
match_yellow_text = re.findall(regex_yellow_text, banco_5)
print('4. Construa uma expressão regular específica que capture todos os valores monetários existentes no texto (marcados em amarelo): \n')
print('R\$\s?-?[0-9]+,[0-9]+|\d{1,3}(?:\.\d{3})*(?:,\d{2})?\sreais\n')
if match_yellow_text:
    for yellow_text in match_yellow_text:
        # Verificamos se a correspondência é uma tupla e fazemos join, ou simplesmente imprimimos a string
        if isinstance(yellow_text, tuple):
            print(''.join(yellow_text))
        else:
            print(yellow_text)
else:
    print("Nenhum valor encontrado.")

print('------------------------------------------------------------------\n')

# 5 - Construa uma expressão regular específica que capture as linhas que começam por números e terminam com palavras.
regex_floripa = r"^[0-9]+\. \w+(?:\s\w+)*\s*$"
match_floripa = re.findall(regex_floripa, banco_6, re.MULTILINE)
print('5. Construa uma expressão regular específica que capture as linhas que começam por números e terminam com palavras: \n')
print('REGEX: ^[0-9]+\. \w+(?:\s\w+)*\s*$\n')
if match_floripa:
    for floripa in match_floripa:
        # Verificamos se a correspondência é uma tupla e fazemos join, ou simplesmente imprimimos a string
        if isinstance(floripa, tuple):
            print(''.join(floripa))
        else:
            print(floripa)
else:
    print("Nenhum valor encontrado.")

print('------------------------------------------------------------------\n')

# 6 - Construa uma expressão regular específica que capture todas as linhas que estão em azul e nenhuma das que estão em vermelho.
# importante: a regex precisa ter, no máximo, 13 caracteres.
regex_blue_lines = r"^[0-9]+\. \w+(?:\s\w+)*\s*$"
match_blue_lines = re.findall(regex_blue_lines, banco_7)
print('5. Construa uma expressão regular específica que capture as linhas que começam por números e terminam com palavras: \n')
print('REGEX: ^[0-9]+\. \w+(?:\s\w+)*\s*$\n')
if match_blue_lines:
    for blue_lines in match_blue_lines:
        # Verificamos se a correspondência é uma tupla e fazemos join, ou simplesmente imprimimos a string
        if isinstance(blue_lines, tuple):
            print(''.join(blue_lines))
        else:
            print(blue_lines)
else:
    print("Nenhum valor encontrado.")

print('------------------------------------------------------------------\n')