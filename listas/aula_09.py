from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import contractions
import time
import re  # Importe o módulo re
import pandas as pd

# O webscraping, também conhecido como raspagem de dados da web, é uma técnica utilizada para extrair informações de páginas da internet.
# Selenium - literalmente abre um googleChrome para buscar as coisa que queremos
# Service é usado apra abrir uma instância do Chome WebDriver
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# 01 - Sinopse Dune.
url = "https://www.adorocinema.com/filmes/filme-133392/"
driver.get(url)
url_dune = driver.page_source
# 01 - Sinopse Dune.
regex_dune = r'<p class="bo-p">(.*?)</p>'
match_dune = re.findall(regex_dune, url_dune, re.DOTALL)
df = pd.DataFrame({"Sinopse": match_dune})
df.to_csv("sinopse_dune.txt", index=False, sep="\t")
print("01 - Sinopse Dune:\n")
for sinopse_dune in match_dune:
    print(sinopse_dune, " \n")
print(
    "____________________________________________________________________________________\n"
)
# 01 - Crítica Dune.
url = "https://www.adorocinema.com/filmes/filme-133392/criticas/espectadores/"
driver.get(url)
url_critica_dune = driver.page_source
# 01 - Crítica Dune.
regex_critica_dune = r'<div class="content-txt review-card-content">(.*?)</div>'
match_critica_dune = re.findall(regex_critica_dune, url_critica_dune, re.DOTALL)
df = pd.DataFrame({"Sinopse": match_critica_dune})
df.to_csv("sinopse_critica_dune.csv", index=False, sep="\t")
print("01 - Crítica Dune:\n")
for sinopse_critica_dune in match_critica_dune:
    print(sinopse_critica_dune, " \n")
print(
    "____________________________________________________________________________________\n"
)

# 02 - Sinopse Harry Potter.
url = "https://www.adorocinema.com/filmes/filme-46865/"
driver.get(url)
url_potter = driver.page_source
# 02 - Sinopse Harry Potter.
regex_potter = r'<p class="bo-p">(.*?)</p>'
match_potter = re.findall(regex_potter, url_potter, re.DOTALL)
df = pd.DataFrame({"Sinopse": match_potter})
df.to_csv("sinopse_potter.txt", index=False, sep="\t")
print("02 - Sinopse Harry Potter e o Prisioneiro de Azkaban:\n")
for sinopse_potter in match_potter:
    print(sinopse_potter, " \n")
print(
    "____________________________________________________________________________________\n"
)

# 03 - Crepusuculo.
url = "https://www.adorocinema.com/filmes/filme-131377/"
driver.get(url)
url_crepusculo = driver.page_source
# 03 - Sinopse Harry Potter.
regex_crepusculo = r'<p class="bo-p">(.*?)</p>'
match_crepusculo = re.findall(regex_crepusculo, url_crepusculo, re.DOTALL)
df = pd.DataFrame({"Sinopse": match_crepusculo})
df.to_csv("sinopse_crepusculo.txt", index=False, sep="\t")
print("03 - Sinopse Crepusculo:\n")
for sinopse_crepusculo in match_crepusculo:
    print(sinopse_crepusculo, " \n")
print(
    "____________________________________________________________________________________\n"
)

# 04 - Django
url = "https://www.adorocinema.com/filmes/filme-190918/"
driver.get(url)
url_django = driver.page_source
# 04 - Sinopse Django.
regex_django = r'<p class="bo-p">(.*?)</p>'
match_django = re.findall(regex_django, url_django, re.DOTALL)
df = pd.DataFrame({"Sinopse": match_django})
df.to_csv("sinopse_django.txt", index=False, sep="\t")
print("04 - Sinopse Django:\n")
for sinopse_django in match_django:
    print(sinopse_django, " \n")
print(
    "____________________________________________________________________________________\n"
)

# 05 - O Senhor dos Anéis - A Sociedade do Anel
url = "https://www.adorocinema.com/filmes/filme-27070/"
driver.get(url)
url_lord = driver.page_source
# 05 - O Senhor dos Anéis - A Sociedade do Anel
regex_lord = r'<p class="bo-p">(.*?)</p>'
match_lord = re.findall(regex_lord, url_lord, re.DOTALL)
df = pd.DataFrame({"Sinopse": match_lord})
df.to_csv("sinopse_o_senhor_dos_aneis.txt", index=False, sep="\t")
print("05 - Sinopse O Senhor dos Anéis - A Sociedade do Anel:\n")
for sinopse_lord in match_lord:
    print(sinopse_lord, " \n")
print(
    "____________________________________________________________________________________\n"
)
# Críticas dos usuários
# 05 - O Senhor dos Anéis - A Sociedade do Anel
url = "https://www.adorocinema.com/filmes/filme-27070/criticas/espectadores/"
driver.get(url)
url_critica_lord = driver.page_source
# 05 - O Senhor dos Anéis - A Sociedade do Anel
regex_critica_lord = r'<div class="content-txt review-card-content">(.*?)</div>'
match_critica_lord = re.findall(regex_critica_lord, url_critica_lord, re.DOTALL)
df = pd.DataFrame({"Sinopse": match_critica_lord})
df.to_csv("sinopse_o_senhor_dos_aneis.csv", index=False, sep="\t")
print("05 - Crítica O Senhor dos Anéis - A Sociedade do Anel:\n")
for sinopse_critica_lord in match_critica_lord:
    print(sinopse_critica_lord, " \n")
print(
    "____________________________________________________________________________________\n"
)

time.sleep(1000)
# Fecha o navegador
driver.quit()
# print(html_page)
