## Documentação do Script de Webscraping 📘

### Objetivo:
Este script é destinado ao webscraping de títulos e preços de livros do site [Books to Scrape](https://books.toscrape.com/). Utiliza Selenium para navegação e interação com a web e o módulo `re` (regular expressions) para a extração de informações específicas.

### Funcionalidades Implementadas:
- **Extração de Títulos dos Livros:** Captura os títulos de todos os livros na página principal.
- **Tokenização dos Títulos:** Converte os títulos para letras minúsculas e separa em palavras individuais.
- **Extração de Preços dos Livros:** Lista os preços dos livros, oferecendo uma visão geral dos valores.
- **Formatação de Preços:** Ajusta a formatação dos preços, substituindo ponto por vírgula.
- **Filtragem por Preço:** Seleciona livros com preço até 20 libras para fácil identificação.
- **Extração de Títulos do Menu:** Extrai os títulos das categorias de livros do menu lateral.
- **Tokenização dos Títulos do Menu:** Aplica tokenização nos títulos do menu, usando letras maiúsculas.

### Código:
```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import re

# Inicialização e configuração do Selenium WebDriver
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://books.toscrape.com/")
html_page = driver.page_source

# Extração e manipulação de dados omitidos para brevidade...

driver.quit()

### Instruções de Uso:
1. **Assegure-se de que o ChromeDriver esteja instalado e atualizado conforme a versão do seu navegador Chrome.**
2. **Instale as dependências necessárias, incluindo Selenium.**
3. **Execute o script em um ambiente compatível com Python e observe os resultados no terminal.**

### Considerações Finais:
Este script exemplifica o potencial do Selenium para webscraping e o uso de expressões regulares para a manipulação de strings em Python. **Sugestões para melhorias e expansões das funcionalidades são bem-vindas.**
