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
urls_dune = [
    "https://www.adorocinema.com/filmes/filme-133392/criticas/espectadores/",
    "https://www.adorocinema.com/filmes/filme-133392/criticas/espectadores/?page=2",
    "https://www.adorocinema.com/filmes/filme-133392/criticas/espectadores/?page=3",
    "https://www.adorocinema.com/filmes/filme-133392/criticas/espectadores/?page=4",
    "https://www.adorocinema.com/filmes/filme-133392/criticas/espectadores/?page=5",
    "https://www.adorocinema.com/filmes/filme-133392/criticas/espectadores/?page=6",
    "https://www.adorocinema.com/filmes/filme-133392/criticas/espectadores/?page=7",
    "https://www.adorocinema.com/filmes/filme-133392/criticas/espectadores/?page=8",
    "https://www.adorocinema.com/filmes/filme-133392/criticas/espectadores/?page=9",
]
regex_critica_dune = r'<div class="content-txt review-card-content">(.*?)</div>'
todas_criticas_dune = []
for url in urls_dune:
    driver.get(url)
    page_source = driver.page_source
    match_critica = re.findall(regex_critica_dune, page_source, re.DOTALL)
    todas_criticas_dune.extend(match_critica)
df = pd.DataFrame({"Sinopse": todas_criticas_dune})
df.to_csv("sinopse_critica_dune.csv", index=False, sep="\t")
print("01 - Crítica Dune:\n")
for sinopse_critica_dune in todas_criticas_dune:
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
urls_potter = [
    "https://www.adorocinema.com/filmes/filme-46865/criticas/espectadores/",
    "https://www.adorocinema.com/filmes/filme-46865/criticas/espectadores/?page=2",
    "https://www.adorocinema.com/filmes/filme-46865/criticas/espectadores/?page=3",
    "https://www.adorocinema.com/filmes/filme-46865/criticas/espectadores/?page=4",
    "https://www.adorocinema.com/filmes/filme-46865/criticas/espectadores/?page=5",
    "https://www.adorocinema.com/filmes/filme-46865/criticas/espectadores/?page=6",
    "https://www.adorocinema.com/filmes/filme-46865/criticas/espectadores/?page=7",
    "https://www.adorocinema.com/filmes/filme-46865/criticas/espectadores/?page=8",
]
regex_critica_potter = r'<div class="content-txt review-card-content">(.*?)</div>'
todas_criticas_potter = []
for url_potter in urls_potter:
    driver.get(url_potter)
    page_source = driver.page_source
    match_critica = re.findall(regex_critica_potter, page_source, re.DOTALL)
    todas_criticas_potter.extend(match_critica)
df = pd.DataFrame({"Sinopse": todas_criticas_potter})
df.to_csv("sinopse_critica_potter.csv", index=False, sep="\t")
print("01 - Crítica Sinopse Harry Potter e o Prisioneiro de Azkaban:\n")
for sinopse_critica_potter in todas_criticas_potter:
    print(sinopse_critica_potter, " \n")
print(
    "____________________________________________________________________________________\n"
)

# 03 - Crepusuculo.
url = "https://www.adorocinema.com/filmes/filme-131377/"
driver.get(url)
url_crepusculo = driver.page_source
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
urls_crepusculo = [
    "https://www.adorocinema.com/filmes/filme-131377/criticas/espectadores/",
    "https://www.adorocinema.com/filmes/filme-131377/criticas/espectadores/?page=2",
    "https://www.adorocinema.com/filmes/filme-131377/criticas/espectadores/?page=3",
    "https://www.adorocinema.com/filmes/filme-131377/criticas/espectadores/?page=4",
    "https://www.adorocinema.com/filmes/filme-131377/criticas/espectadores/?page=5",
    "https://www.adorocinema.com/filmes/filme-131377/criticas/espectadores/?page=6",
    "https://www.adorocinema.com/filmes/filme-131377/criticas/espectadores/?page=7",
    "https://www.adorocinema.com/filmes/filme-131377/criticas/espectadores/?page=8",
    "https://www.adorocinema.com/filmes/filme-131377/criticas/espectadores/?page=9",
    "https://www.adorocinema.com/filmes/filme-131377/criticas/espectadores/?page=10",
]
regex_critica_crepusculo = r'<div class="content-txt review-card-content">(.*?)</div>'
todas_criticas_crepusculo = []
for url_crepusculo in urls_crepusculo:
    driver.get(url_crepusculo)
    page_source = driver.page_source
    match_critica = re.findall(regex_critica_crepusculo, page_source, re.DOTALL)
    todas_criticas_crepusculo.extend(match_critica)
df = pd.DataFrame({"Sinopse": todas_criticas_crepusculo})
df.to_csv("sinopse_critica_crepusculo.csv", index=False, sep="\t")
print("01 - Crítica Crepusculo:\n")
for sinopse_critica_crepusculo in todas_criticas_crepusculo:
    print(sinopse_critica_crepusculo, " \n")
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
# 01 - Crítica Django.
urls_django = [
    "https://www.adorocinema.com/filmes/filme-190918/criticas/espectadores/",
    "https://www.adorocinema.com/filmes/filme-190918/criticas/espectadores/?page=2",
    "https://www.adorocinema.com/filmes/filme-190918/criticas/espectadores/?page=3",
    "https://www.adorocinema.com/filmes/filme-190918/criticas/espectadores/?page=4",
    "https://www.adorocinema.com/filmes/filme-190918/criticas/espectadores/?page=5",
    "https://www.adorocinema.com/filmes/filme-190918/criticas/espectadores/?page=6",
    "https://www.adorocinema.com/filmes/filme-190918/criticas/espectadores/?page=7",
    "https://www.adorocinema.com/filmes/filme-190918/criticas/espectadores/?page=8",
    "https://www.adorocinema.com/filmes/filme-190918/criticas/espectadores/?page=9",
    "https://www.adorocinema.com/filmes/filme-190918/criticas/espectadores/?page=10",
]
regex_critica_django = r'<div class="content-txt review-card-content">(.*?)</div>'
todas_criticas_django = []
for url_django in urls_django:
    driver.get(url_django)
    page_source = driver.page_source
    match_critica = re.findall(regex_critica_django, page_source, re.DOTALL)
    todas_criticas_django.extend(match_critica)
df = pd.DataFrame({"Sinopse": todas_criticas_django})
df.to_csv("sinopse_critica_django.csv", index=False, sep="\t")
print("01 - Crítica Django:\n")
for sinopse_critica_django in todas_criticas_django:
    print(sinopse_critica_django, " \n")
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
urls_lords = [
    "https://www.adorocinema.com/filmes/filme-27070/criticas/espectadores/",
    "https://www.adorocinema.com/filmes/filme-27070/criticas/espectadores/?page=2",
    "https://www.adorocinema.com/filmes/filme-27070/criticas/espectadores/?page=3",
    "https://www.adorocinema.com/filmes/filme-27070/criticas/espectadores/?page=4",
    "https://www.adorocinema.com/filmes/filme-27070/criticas/espectadores/?page=5",
    "https://www.adorocinema.com/filmes/filme-27070/criticas/espectadores/?page=6",
    "https://www.adorocinema.com/filmes/filme-27070/criticas/espectadores/?page=7",
    "https://www.adorocinema.com/filmes/filme-27070/criticas/espectadores/?page=8",
    "https://www.adorocinema.com/filmes/filme-27070/criticas/espectadores/?page=9",
    "https://www.adorocinema.com/filmes/filme-27070/criticas/espectadores/?page=10",
]
regex_critica_lord = r'<div class="content-txt review-card-content">(.*?)</div>'
todas_criticas_lord = []
for url_lord in urls_lords:
    driver.get(url_lord)
    page_source = driver.page_source
    match_critica_lord = re.findall(regex_critica_lord, page_source, re.DOTALL)
    todas_criticas_lord.extend(match_critica_lord)
df = pd.DataFrame({"Sinopse": todas_criticas_lord})
df.to_csv("sinopse_critica_lord.csv", index=False, sep="\t")
print("05 - Crítica O Senhor dos Anéis - A Sociedade do Anel:\n")
for sinopse_critica_lord in todas_criticas_lord:
    print(sinopse_critica_lord, " \n")
print(
    "____________________________________________________________________________________\n"
)


time.sleep(1000)
# Fecha o navegador
driver.quit()
# print(html_page)
