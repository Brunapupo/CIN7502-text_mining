# Importações e inicializações
import re
import nltk
import heapq
import string
import collections

import numpy as np
import pandas as pd

from nltk import ngrams
from nltk import tokenize
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download("punkt")
nltk.download("stopwords")


# Leitura de arquivo do corpus e uniformização em minúsculas
def ler_corpus(nome_arquivo_corpus):
    with open(nome_arquivo_corpus, "r", encoding="utf-8") as arq_corpus:
        return arq_corpus.read().lower()
    return ""


# Leitura de arquivo de corpus tokenizado
def ler_corpus_tokenizado(nome_arquivo_corpus):
    with open(nome_arquivo_corpus, "r", encoding="utf-8") as arq_corpus:
        return arq_corpus.read().split()
    return ""


# Leitura de arquivo de stopwords
def ler_stopwords(nome_arquivo_stopwords):
    with open(nome_arquivo_stopwords, "r", encoding="utf-8") as arq_stopwords:
        return arq_stopwords.read().split()
    return ""


# Salvamento de arquivo não-tokenizado sem sufixo
def salvar_arquivo(nome_arquivo_saida, texto):
    with open(nome_arquivo_saida, "w", encoding="utf-8") as arq_saida:
        arq_saida.write(texto)


# Salvamento de arquivo tokenizado sem sufixo
def salvar_arquivo_tokenizado(nome_arquivo_saida, termos):
    with open(nome_arquivo_saida, "w", encoding="utf-8") as arq_saida:
        for termo in termos:
            arq_saida.write(termo + "\n")


# Salvamento de arquivo tokenizado com sufixo
def salvar_arquivo_sem_stopwords(nome_arquivo_saida, termos, sufixo):
    arquivo_saida = nome_arquivo_saida[: nome_arquivo_saida.rfind(".")] + sufixo
    salvar_arquivo_tokenizado(arquivo_saida, termos)


# Salvamento de arquivo não-tokenizado com sufixo
def salvar_arquivo_sem_pontuação(nome_arquivo_saida, termos, sufixo):
    arquivo_saida = nome_arquivo_saida[: nome_arquivo_saida.rfind(".")] + sufixo
    salvar_arquivo(arquivo_saida, termos)


# Aplicador de múltiplas regexes em corpora textuais
def aplicar_regexes_multiplos_arquivos(arquivos_corpora_entrada, regexes, sufixo):
    for corpus in arquivos_corpora_entrada:
        texto_entrada = ler_corpus(corpus)
        texto_saida = texto_entrada
        for par_regex in regexes:
            texto_saida = re.sub(
                par_regex[0], par_regex[1], texto_saida, flags=re.MULTILINE
            )
        arquivo_saida = corpus[: corpus.rfind(".")] + sufixo
        salvar_arquivo(arquivo_saida, texto_saida)


# Função de remoção de stopwords baseada em arquivo
def remover_stopwords(texto_corpus, texto_stopwords):
    texto_sem_stopwords = [
        termo for termo in texto_corpus if not termo in texto_stopwords
    ]
    return texto_sem_stopwords


# Função de retirada de pontuação com o pacote string
def retirar_pontuação(texto_corpus):
    regex = re.compile("[%s]" % re.escape(string.punctuation))
    texto_sem_pontuação = [regex.sub("", termo) for termo in texto_corpus]
    return "".join(texto_sem_pontuação)


# Função de retirada de pontuação com a função NLTK isalpha()
def retirar_pontuação_isalpha(texto_corpus):
    tokens = word_tokenize(texto_corpus)
    palavras_sem_pontuação = [palavra for palavra in tokens if palavra.isalpha()]
    return " ".join(palavras_sem_pontuação)


# Salvar arquivo de n-gramas com sufixo
def salvar_arquivo_ngramas(nome_arquivo, lista_termos, sufixo):
    arquivo_saida = nome_arquivo[: nome_arquivo.rfind(".")] + sufixo
    with open(arquivo_saida, "w", encoding="utf-8") as arq_saida:
        for termo in lista_termos:
            arq_saida.write(" ".join(map(str, termo)) + "\n")


# Funções Python para Bag of Words
def vetorizar(texto, termos_únicos):
    vetor = []
    for termo in termos_únicos:
        vetor.append(texto.count(termo))
    return vetor


def criar_conjunto_termos(texto):
    conjunto = set()
    return [termo for termo in texto if not (termo in conjunto or conjunto.add(termo))]


# Dicionário de Termos
def criar_dicionário_termos(texto, n_itens):
    dicionário_termos = {}
    contador = collections.Counter(texto)
    dt = dict(contador)
    total = 0
    for i in sorted(dt, key=dt.get, reverse=True):
        dicionário_termos[i] = dt[i]
        total += 1
        if total >= n_itens:
            break
    return dicionário_termos


# Normalização Textual

# Definir regexes para limpeza textual
regexes = [
    [r"<[^>]+>", ""],  # Remover tags HTML
    [r"[áâãäàÁÂÃÄÀ]", "a"],  # Remover acentos
    [r"[éêëèÉÊËÈ]", "e"],
    [r"[íîïìÍÎÏÌ]", "i"],
    [r"[óôõöòÓÔÕÖÒ]", "o"],
    [r"[úûüùÚÛÜÙ]", "u"],
    [r"[çÇ]", "c"],
    [r"[ñÑ]", "n"],
    [r"[^\w\s]", ""],  # Remover pontuação
]

# Arquivo de sinopse de entrada
arquivo_sinopse = "sinopse_crepusculo.txt"

# Aplicar regexes ao arquivo de sinopse
texto_entrada = ler_corpus(arquivo_sinopse)
texto_saida = texto_entrada

for par_regex in regexes:
    texto_saida = re.sub(par_regex[0], par_regex[1], texto_saida, flags=re.MULTILINE)

arquivo_saida = arquivo_sinopse[: arquivo_sinopse.rfind(".")] + "_limpo.txt"
salvar_arquivo(arquivo_saida, texto_saida)

# Tokenização
# Definir regex para tokenização
regexes = [[r"\s+", r"\n"]]

# Aplicar tokenização ao arquivo de sinopse limpo
texto_entrada = ler_corpus(arquivo_saida)
texto_saida = texto_entrada

for par_regex in regexes:
    texto_saida = re.sub(par_regex[0], par_regex[1], texto_saida, flags=re.MULTILINE)

arquivo_saida_tokenizado = arquivo_saida[: arquivo_saida.rfind(".")] + "_tokenizado.txt"
salvar_arquivo(arquivo_saida_tokenizado, texto_saida)

# Remoção de Stopwords
# Nome do arquivo de stopwords
nome_arquivo_stopwords = "stopwords_ampliado_pt.txt"

# Remover stopwords do arquivo de sinopse tokenizado
corpus = ler_corpus_tokenizado(arquivo_saida_tokenizado)
stopwords = ler_stopwords(nome_arquivo_stopwords)
texto_sem_stopwords = remover_stopwords(corpus, stopwords)
salvar_arquivo_sem_stopwords(
    arquivo_saida_tokenizado, texto_sem_stopwords, "_sem_stopwords.txt"
)

# Bag of Words (BoW)
# Arquivo de sinopse sem stopwords
arquivo_sinopse_sem_stopwords = (
    arquivo_saida_tokenizado[: arquivo_saida_tokenizado.rfind(".")]
    + "_sem_stopwords.txt"
)

# Gerar matriz BoW para a sinopse
corpus = ler_corpus_tokenizado(arquivo_sinopse_sem_stopwords)
stopwords = ler_stopwords(nome_arquivo_stopwords)
texto_sem_stopwords = remover_stopwords(corpus, stopwords)
conjunto = criar_conjunto_termos(texto_sem_stopwords)
vetor = vetorizar(texto_sem_stopwords, conjunto)

print("#" * 50)
print(f'Arquivo "{arquivo_sinopse_sem_stopwords}":')
print(
    f"20 primeiros termos do texto ({len(texto_sem_stopwords)} termos no total, {len(conjunto)} termos únicos):\n{texto_sem_stopwords[:20]}\n"
)
print(f"20 primeiros termos do vetor BoW:\n{vetor[:20]}\n\n")

# Cálculo do TF-IDF
# Arquivo de crítica sem stopwords
arquivo_critica_sem_stopwords = "sinopse_critica_crepusculo_sem_stopwords.txt"

# Gerar matriz TF-IDF para a crítica
corpus = ler_corpus(arquivo_critica_sem_stopwords)
lista_sentenças = corpus.split("\n")
stopwords_pt = ler_stopwords(nome_arquivo_stopwords)

# IDF não-suave
tf_idf_vec = TfidfVectorizer(
    use_idf=True, smooth_idf=False, ngram_range=(1, 1), stop_words=stopwords_pt
)
tf_idf_data = tf_idf_vec.fit_transform(lista_sentenças)

print("#" * 50)
print(f'Arquivo "{arquivo_critica_sem_stopwords}":')
tf_idf_df = pd.DataFrame(
    tf_idf_data.toarray(), columns=tf_idf_vec.get_feature_names_out()
)
print(f"Dataframe com o Cálculo do TF-IDF (Não-Suave):\n{tf_idf_df}\n\n")

# Geração de n-Gramas
# Gerar bigramas e trigramas
n = 2
bigramas = ngrams(corpus.split(), n)
salvar_arquivo_ngramas(arquivo_critica_sem_stopwords, bigramas, f"_ngramas-{n}.txt")

n = 3
trigramas = ngrams(corpus.split(), n)
salvar_arquivo_ngramas(arquivo_critica_sem_stopwords, trigramas, f"_ngramas-{n}.txt")

# Identificar os 10 bigramas e trigramas mais frequentes
bigramas_mais_frequentes = collections.Counter(bigramas).most_common(10)
trigramas_mais_frequentes = collections.Counter(trigramas).most_common(10)

print("10 Bigramas mais frequentes:")
for bigrama in bigramas_mais_frequentes:
    print(bigrama)

print("\n10 Trigramas mais frequentes:")
for trigrama in trigramas_mais_frequentes:
    print(trigrama)

# Dicionário de Termos
# Criar dicionário de termos para a sinopse
n_itens = 20  # Primeiros termos mais frequentes
dic_termos = criar_dicionário_termos(texto_sem_stopwords, n_itens)

print("#" * 50)
print(f'Arquivo "{arquivo_sinopse_sem_stopwords}"\n')
print(f"{n_itens} primeiros termos mais frequentes:")
for chave, valor in dic_termos.items():
    print(f"{chave} : {valor}")
else:
    print("\n")
