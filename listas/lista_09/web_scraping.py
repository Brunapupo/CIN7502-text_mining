from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import re
import pandas as pd
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import unicodedata
import os
import nltk

nltk.download("punkt")
nltk.download("stopwords")

# O webscraping, também conhecido como raspagem de dados da web, é uma técnica utilizada para extrair informações de páginas da internet.
# Selenium - literalmente abre um googleChrome para buscar as coisa que queremos
# Service é usado para abrir uma instância do Chrome WebDriver
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


# Função para limpeza textual
def clean_text(text):
    # Remover tags HTML
    text = BeautifulSoup(text, "html.parser").get_text()
    # Remover pontuação
    text = text.translate(str.maketrans("", "", string.punctuation))
    # Remover acentuação
    text = (
        unicodedata.normalize("NFKD", text)
        .encode("ascii", "ignore")
        .decode("utf-8", "ignore")
    )
    # Remover números
    text = re.sub(r"\d+", "", text)
    return text


# Função para remover frases sem valor semântico
def remove_non_semantic(text):
    sentences = text.split(".")
    meaningful_sentences = [
        sentence.strip() for sentence in sentences if len(sentence.split()) > 4
    ]
    return " ".join(meaningful_sentences)


# Função para tokenização
def tokenize(text):
    return word_tokenize(text)


# Função para remoção de stopwords
def remove_stopwords(tokens):
    stop_words = set(stopwords.words("portuguese"))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    return filtered_tokens


# Função para normalização completa do texto
def normalize_text(text):
    text = clean_text(text)
    text = remove_non_semantic(text)
    tokens = tokenize(text)
    tokens = remove_stopwords(tokens)
    return " ".join(tokens)


output_dir = "arquivos"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Sinopse de Dune
print("Processando sinopse de Dune...")
url = "https://www.adorocinema.com/filmes/filme-133392/"
driver.get(url)
url_dune = driver.page_source
regex_dune = r'<p class="bo-p">(.*?)</p>'
match_dune = re.findall(regex_dune, url_dune, re.DOTALL)
print(f"Sinopses encontradas: {len(match_dune)}")
normalized_synopsis_dune = [normalize_text(synopsis) for synopsis in match_dune]
df = pd.DataFrame({"Sinopse": normalized_synopsis_dune})
sinopse_output_path = os.path.join(output_dir, "sinopse_dune_normalized.txt")
df.to_csv(sinopse_output_path, index=False, sep="\t")
print(f"Sinopse normalizada salva em: {sinopse_output_path}")
for sinopse_dune in normalized_synopsis_dune:
    print(sinopse_dune, " \n")
print(
    "____________________________________________________________________________________\n"
)
# Críticas de Dune
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
normalized_reviews_dune = [normalize_text(review) for review in todas_criticas_dune]
df = pd.DataFrame({"Crítica": normalized_reviews_dune})
df.to_csv(
    os.path.join(output_dir, "critica_dune_normalized.csv"), index=False, sep="\t"
)
for critica_dune in normalized_reviews_dune:
    print(critica_dune, " \n")
print(
    "____________________________________________________________________________________\n"
)

# Sinopse de Harry Potter
print("Processando sinopse de Harry Potter...")
url = "https://www.adorocinema.com/filmes/filme-46865/"
driver.get(url)
url_potter = driver.page_source
regex_potter = r'<p class="bo-p">(.*?)</p>'
match_potter = re.findall(regex_potter, url_potter, re.DOTALL)
normalized_synopsis_potter = [normalize_text(synopsis) for synopsis in match_potter]
df = pd.DataFrame({"Sinopse": normalized_synopsis_potter})
sinopse_output_path = os.path.join(output_dir, "sinopse_harrypotter_normalized.txt")
df.to_csv(sinopse_output_path, index=False, sep="\t")
for sinopse_potter in normalized_synopsis_potter:
    print(sinopse_potter, " \n")
print(
    "____________________________________________________________________________________\n"
)
# Críticas de Harry Potter
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
normalized_reviews_potter = [normalize_text(review) for review in todas_criticas_potter]
df = pd.DataFrame({"Crítica": normalized_reviews_potter})
df.to_csv(
    os.path.join(output_dir, "critica_harrypotter_normalized.csv"),
    index=False,
    sep="\t",
)
for critica_harrypotter in normalized_reviews_potter:
    print(critica_harrypotter, " \n")
print(
    "____________________________________________________________________________________\n"
)

# Sinopse de Crepúsculo
print("Processando sinopse de Crepúsculo...")
url = "https://www.adorocinema.com/filmes/filme-131377/"
driver.get(url)
url_crepusculo = driver.page_source
regex_crepusculo = r'<p class="bo-p">(.*?)</p>'
match_crepusculo = re.findall(regex_crepusculo, url_crepusculo, re.DOTALL)
print(f"Sinopses encontradas: {len(match_crepusculo)}")
normalized_synopsis_crepusculo = [
    normalize_text(synopsis) for synopsis in match_crepusculo
]
df = pd.DataFrame({"Sinopse": normalized_synopsis_crepusculo})
sinopse_output_path = os.path.join(output_dir, "sinopse_crepusculo_normalized.txt")
df.to_csv(sinopse_output_path, index=False, sep="\t")
print(f"Sinopse normalizada salva em: {sinopse_output_path}")
for sinopse_crepusculo in normalized_synopsis_crepusculo:
    print(sinopse_crepusculo, " \n")
print(
    "____________________________________________________________________________________\n"
)
# Críticas de Crepúsculo
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
normalized_reviews_crepusculo = [
    normalize_text(review) for review in todas_criticas_crepusculo
]
df = pd.DataFrame({"Crítica": normalized_reviews_crepusculo})
df.to_csv(
    os.path.join(output_dir, "critica_crepusculo_normalized.csv"),
    index=False,
    sep="\t",
)
for critica_crepusculo in normalized_reviews_crepusculo:
    print(critica_crepusculo, " \n")
print(
    "____________________________________________________________________________________\n"
)

# Sinopse de Django
print("Processando sinopse de Django...")
url = "https://www.adorocinema.com/filmes/filme-190918/"
driver.get(url)
url_django = driver.page_source
regex_django = r'<p class="bo-p">(.*?)</p>'
match_django = re.findall(regex_django, url_django, re.DOTALL)
print(f"Sinopses encontradas: {len(match_django)}")
normalized_synopsis_django = [normalize_text(synopsis) for synopsis in match_django]
df = pd.DataFrame({"Sinopse": normalized_synopsis_django})
sinopse_output_path = os.path.join(output_dir, "sinopse_django_normalized.txt")
df.to_csv(sinopse_output_path, index=False, sep="\t")
print(f"Sinopse normalizada salva em: {sinopse_output_path}")
for sinopse_django in normalized_synopsis_django:
    print(sinopse_django, " \n")
print(
    "____________________________________________________________________________________\n"
)
# Críticas de Django
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
normalized_reviews_django = [normalize_text(review) for review in todas_criticas_django]
df = pd.DataFrame({"Crítica": normalized_reviews_django})
df.to_csv(
    os.path.join(output_dir, "critica_django_normalized.csv"),
    index=False,
    sep="\t",
)
for critica_django in normalized_reviews_django:
    print(critica_django, " \n")
print(
    "____________________________________________________________________________________\n"
)

# Sinopse de O Senhor dos Anéis - A Sociedade do Anel
print("Processando sinopse de O Senhor dos Anéis - A Sociedade do Anel...")
url = "https://www.adorocinema.com/filmes/filme-27070/"
driver.get(url)
url_lord = driver.page_source
regex_lord = r'<p class="bo-p">(.*?)</p>'
match_lord = re.findall(regex_lord, url_lord, re.DOTALL)
print(f"Sinopses encontradas: {len(match_lord)}")
normalized_synopsis_lord = [normalize_text(synopsis) for synopsis in match_lord]
df = pd.DataFrame({"Sinopse": normalized_synopsis_lord})
sinopse_output_path = os.path.join(output_dir, "sinopse_lord_normalized.txt")
df.to_csv(sinopse_output_path, index=False, sep="\t")
print(f"Sinopse normalizada salva em: {sinopse_output_path}")
for sinopse_lord in normalized_synopsis_lord:
    print(sinopse_lord, " \n")
print(
    "____________________________________________________________________________________\n"
)
# Críticas de O Senhor dos Anéis - A Sociedade do Anel
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
normalized_reviews_lord = [normalize_text(review) for review in todas_criticas_lord]
df = pd.DataFrame({"Crítica": normalized_reviews_lord})
df.to_csv(
    os.path.join(output_dir, "critica_lord_normalized.csv"),
    index=False,
    sep="\t",
)
for critica_lord in normalized_reviews_lord:
    print(critica_lord, " \n")
print(
    "____________________________________________________________________________________\n"
)

time.sleep(1000)
# Fecha o navegador
driver.quit()
# print(html_page)
