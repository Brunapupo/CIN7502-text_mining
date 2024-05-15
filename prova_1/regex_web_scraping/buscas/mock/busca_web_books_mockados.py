import contractions
import re

html_mockado = "./mock_html.html"
with open(html_mockado, "r", encoding="utf-8") as file:
    mock = file.read()

# 01 - Título de todos os livros da Página.
regex_titulo = r'<h3><a .*? title="(.*?)">'
match_titulo = re.findall(regex_titulo, mock, re.DOTALL)
print("01 - Título de todos os livros da Página. \n")
for titulo in match_titulo:
    print(titulo)
print(
    "____________________________________________________________________________________\n"
)

# 02 - Tokenização aplicado nos títulos dos livros e caracteres convertidos pra minúsculas.
regex_token_titulo = r'<h3><a .*? title="(.*?)">'
match_token_titulo = re.findall(regex_token_titulo, mock, re.DOTALL)
print(
    "02 - Tokenização aplicado nos títulos dos livros e caracteres convertidos pra minúsculas: \n"
)
print(
    "A tokenização divide os títulos dos livros em tokens, ou seja, unidades menores, facilitando\na análise textual. Ao converter os títulos para minúsculas, reduzimos a variabilidade\n do texto, melhorando a uniformidade para processos de análise em processamento de linguagem natural.\n"
)
for token in match_token_titulo:
    tokenizacao = token.lower()
    tokenizacao = tokenizacao.replace(" ", "\n")
    print(tokenizacao)
print(
    "____________________________________________________________________________________\n"
)

# 03 - Preço dos livros da Página.
regex_preco_livro = r"£(\d+\.\d{2})"
match_preco_livro = re.findall(regex_preco_livro, mock, re.DOTALL)
print("03 - Preço dos livros da Página: \n")
for preco_livro in match_preco_livro:
    print(preco_livro)
print(
    "____________________________________________________________________________________\n"
)

# 04 - Limpeza Substituição de ponto por vírgula nos preços dos livros da página:
regex_preco_livro = r"£(\d+\.\d{2})"
match_preco_livro = re.findall(regex_preco_livro, mock, re.DOTALL)
print(
    "04 - Limpeza Substituição de ponto por vírgula nos preços dos livros da página: \n"
)
for preco in match_preco_livro:
    preco_modificado = preco.replace(".", ",")
    print(preco_modificado)
print(
    "____________________________________________________________________________________\n"
)

# 05 - Livros com preço de até 20 libras.
regex_preco_20_libras = r"£(0(\.\d{2})?|1\d\.\d{2}|20\.00)"
match_preco_20_libras = re.findall(regex_preco_20_libras, mock, re.DOTALL)
print("05 - Livros com preço de até 20 libras: \n")
for preco_20_libras in match_preco_20_libras:
    if isinstance(preco_20_libras, tuple):
        print("".join(preco_20_libras))
    else:
        print(preco_20_libras)
print(
    "____________________________________________________________________________________\n"
)

# 06 - Busca Todos os Títulos do Menu.
regex_menu = (
    r'<a href="catalogue/category/books/[^/]+/index\.html">\s*([^<\s].*?)\s*</a>'
)
match_menu = re.findall(regex_menu, mock, re.DOTALL)
print("Busca 06 - Todos os Títulos do Menu: \n")
for menu in match_menu:
    print(menu)
print(
    "____________________________________________________________________________________\n"
)

# 07 - Tokenização aplicado nos títulos do menu para caracteres maiusculos.
regex_menu_token = r'<h3><a .*? title="(.*?)">'
match_menu_token = re.findall(regex_menu_token, mock, re.DOTALL)
print("07 - Tokenização aplicado nos títulos do menu: \n")
print(
    "*** Novamente aplico a tokenização nos títulos do menu, desta vez convertendo o texto em\nunidades menores chamadas tokens e alterando para MAIÚSCULAS. Isso contribui para a análise\ndos dados textuais, permitindo a Contagem de Frequência e facilitando a análise. ***\n"
)
for menu_token in match_menu_token:
    tokenizacao_menu = menu_token.upper()
    tokenizacao_menu = tokenizacao_menu.replace(" ", "\n")
    print(tokenizacao_menu)
print(
    "____________________________________________________________________________________\n"
)

# 08 - Contrações são a fusão de duas palavras em uma, facilitando a fala ou escrita.
# Este processo pode incluir a remoção de letras e espaços, transformando duas palavras independentes em uma única palavra contraída.
regex_titulo_contractions = r'<h3><a .*? title="(.*?)">'
match_titulo_contractions = re.findall(regex_titulo_contractions, mock, re.DOTALL)
largura_coluna = 95
print("08 - Títulos de todos os livros da página com contrações expandidas: \n")
print(
    "*** Contrações são a fusão de duas palavras em uma, facilitando a fala ou escrita. \nEste processo pode incluir a remoção de letras e espaços, transformando duas\npalavras independentes em uma única palavra contraída. ***\n"
)
print("-" * 150)
print(
    f"{'Título Original'.ljust(largura_coluna)}|{'Título com Contrações Expandidas'.ljust(largura_coluna)}"
)
print("-" * 150)
 # tabela
for titulo_contractions in match_titulo_contractions:
    # Aplicando a expansão de contrações no título
    titulo_expandido = contractions.fix(titulo_contractions)
    print(
        f"{titulo_contractions.ljust(largura_coluna)}|{titulo_expandido.ljust(largura_coluna)}"
    )

print(
    "\nEssas modificações contribuem para a normalização e a análise de texto na mineração de texto."
)
print(
    "____________________________________________________________________________________\n"
)