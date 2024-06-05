"""
Esse trabalho tem o objetivo de usar a biblioteca pymongo para criar tabelas
e consultar dados de um banco de dados Mongo DB

"""

# Importando Bibliotecas

from pymongo import *
from pymongo import MongoClient
from datetime import *
from pprint import *

#Realizando a conexão com o banco de dados na nuvem
banco_de_dados = MongoClient("mongodb+srv://marciogel:9aH&11a6@cluster0.fypil5f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Acessando o banco de dados 'banco'
data_base = banco_de_dados.banco

# Acessando a coleção 'contas' dentro do banco de dados 'banco'
collection = data_base.contas
print(collection)  # Exibe a referência para a coleção 'test_collection'

# Definindo o documento a ser inserido na coleção
post = {
    "author": "Marcio",  # Autor do post
    "cpf": "658.851.658-44",  # Cpf cliente
    "conta": 10646231845, # Número da conta
    "tipo":"Corrente", # Tipo de conta
    "tags": ["Corrente", "658.851.658-44", "Marcio"],  # Tags associadas ao post
    "date": datetime.now(timezone.utc)  # Data e hora atual em UTC
}

# Preparando para submeter as informações na coleção 'posts'
posts = data_base.posts  # Referência para a coleção 'posts' dentro do banco de dados 'test'

# Inserindo o documento na coleção 'posts' e obtendo o ID do documento inserido
post_id = posts.insert_one(post).inserted_id
print("Inserted document ID:", post_id)  # Exibe o ID do documento inserido

# Listando todas as coleções no banco de dados 'test'
print("Collections in the database:", data_base.list_collection_names())  # Exibe os nomes das coleções no banco de dados
#realiza uma busca
pprint(data_base.posts.find_one())

#criando novos documentos
new_posts = [{
    "author": "Ana Cristina",  # Autor do post
    "cpf"   :"243.831.268-02",  # Cpf cliente
    "conta" : 10952231845, # Número da conta
    "tipo"  :"Poupança", # Tipo de conta
    "tags"  : ["Poupança", "Ana Cristina", "243.831.268-02"],  # Tags associadas ao post
    "date"  : datetime.now(timezone.utc)  # Data e hora atual em UTC
    },
    {
    "author": "Renan",  # Autor do post
    "cpf"   :"239.769.354-12",  # Cpf cliente
    "conta" :109632731845, # Número da conta
    "tipo":"Poupança", # Tipo de conta
    "tags": ["Renan", "239.769.354-12", "Poupança"],  # Tags associadas ao post
    "date": datetime(2009,11,10,10,45)  # Data e hora atual em UTC
    }]

#inserindo os 2 post
result = posts.insert_many(new_posts)
print(result.inserted_ids)

#recuperação final
print("\n recuperação final Renan")
pprint(data_base.posts.find_one({"author":"Renan"}))
#----------------------------------------------------------------
#recuperando varios
print("Documentos presentes na coleção")
for post in posts.find():
    pprint(post)