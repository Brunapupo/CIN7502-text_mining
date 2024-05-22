import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import spacy
import os
from collections import Counter

# Baixar os recursos necessários do NLTK
nltk.download("stopwords")
nltk.download("punkt")

# Carregar o modelo de português do SpaCy
nlp = spacy.load("pt_core_news_sm")

# Definir as stopwords em português
stop_words = set(stopwords.words("portuguese"))


# Função para remover stopwords de uma sentença
def remove_stopwords(text):
    word_tokens = word_tokenize(text)
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
    return " ".join(filtered_sentence)


# Função para obter a lista de verbos no infinitivo e advérbios
def get_verbs_adverbs(tokens):
    doc = nlp(tokens)
    verbs_infinitive = [token.text for token in doc if token.pos_ == "VERB"]
    adverbs = [token.text for token in doc if token.pos_ == "ADV"]
    return verbs_infinitive, adverbs


# Caminho do arquivo de entrada e saída
input_file_path = "listas/lista_10/_sinopses-todos.txt"
output_verbs_path = "listas/lista_10/_sinopses_verbs_infinitive.txt"
output_adverbs_path = "listas/lista_10/_sinopses_adverbs.txt"

# Verificar se o arquivo de entrada existe
if not os.path.exists(input_file_path):
    print(f"Erro: O arquivo {input_file_path} não foi encontrado.")
else:
    # Ler o arquivo inteiro
    with open(input_file_path, "r", encoding="utf-8") as file:
        text = file.read()

    # Remover stopwords do texto
    text_no_stopwords = remove_stopwords(text)

    # Obter verbos no infinitivo e advérbios
    verbs_infinitive, adverbs = get_verbs_adverbs(text_no_stopwords)

    # Contar a frequência dos verbos e advérbios
    verbs_infinitive_count = Counter(verbs_infinitive)
    adverbs_count = Counter(adverbs)

    # Obter os 30 mais comuns, preenchendo com "N/A" se houver menos de 30
    most_common_verbs_infinitive = verbs_infinitive_count.most_common(30)
    most_common_adverbs = adverbs_count.most_common(30)

    # Preencher com "N/A" se houver menos de 30
    if len(most_common_verbs_infinitive) < 30:
        most_common_verbs_infinitive += [("N/A", 0)] * (
            30 - len(most_common_verbs_infinitive)
        )
    if len(most_common_adverbs) < 30:
        most_common_adverbs += [("N/A", 0)] * (30 - len(most_common_adverbs))

    # Salvar os resultados em arquivos
    with open(output_verbs_path, "w", encoding="utf-8") as file:
        file.write("Token\t:\tTag\n")
        file.write("---------------------------------------------\n")
        for token, count in most_common_verbs_infinitive:
            file.write(f"{token}\t:\tVERB\n")

    with open(output_adverbs_path, "w", encoding="utf-8") as file:
        file.write("Token\t:\tTag\n")
        file.write("---------------------------------------------\n")
        for token, count in most_common_adverbs:
            file.write(f"{token}\t:\tADV\n")

    print("Dicionários de termos gerados com sucesso.")
