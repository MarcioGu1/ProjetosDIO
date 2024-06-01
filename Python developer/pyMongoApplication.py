from pymongo import *
from pymongo import MongoClient
from datetime import *
from pprint import *
#Realizando a conexão com o banco de dados na nuvem
client = MongoClient("mongodb+srv://marciogel:9aH&11a6@cluster0.fypil5f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Acessando o banco de dados 'test'
db = client.test

# Acessando a coleção 'test_collection' dentro do banco de dados 'test'
collection = db.test_collection
print(collection)  # Exibe a referência para a coleção 'test_collection'

# Definindo o documento a ser inserido na coleção
post = {
    "author": "Marcio",  # Autor do post
    "text": "My first mongodb application based on python",  # Texto do post
    "tags": ["mongodb", "python3", "pymongo"],  # Tags associadas ao post
    "date": datetime.now(timezone.utc)  # Data e hora atual em UTC
}

# Preparando para submeter as informações na coleção 'posts'
posts = db.posts  # Referência para a coleção 'posts' dentro do banco de dados 'test'

# Inserindo o documento na coleção 'posts' e obtendo o ID do documento inserido
post_id = posts.insert_one(post).inserted_id
print("Inserted document ID:", post_id)  # Exibe o ID do documento inserido

# Listando todas as coleções no banco de dados 'test'
print("Collections in the database:", db.list_collection_names())  # Exibe os nomes das coleções no banco de dados
#realiza uma busca
pprint(db.posts.find_one())

#criando novos documentos
new_posts = [{
    "author": "Marcio",  # Autor do post
    "text": "Another post",  # Texto do post
    "tags": ["bulk", "post", "insert"],  # Tags associadas ao post
    "date": datetime.now(timezone.utc)  # Data e hora atual em UTC
    },
    {
    "author": "Renan",  # Autor do post
    "text": "Post de Renan. Novo post liberado",  # Texto do post
    "title": "Mongo is fun", #titulo do post
    "tags": ["mongodb", "python3", "pymongo"],  # Tags associadas ao post
    "date": datetime(2009,11,10,10,45)  # Data e hora atual em UTC
    }]

#inserindo os 2 post
result = posts.insert_many(new_posts)
print(result.inserted_ids)

#recuperação final
print("\n recuperação final Renan")
pprint(db.posts.find_one({"author":"Renan"}))
#----------------------------------------------------------------
#recuperando varios
print("Documentos presentes na coleção")
for post in posts.find():
    pprint(post)