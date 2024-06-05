from pymongo import *
from pymongo import MongoClient
from datetime import *
from pprint import *

#Realizando a conexão com o banco de dados na nuvem
client = MongoClient("mongodb+srv://marciogel:9aH&11a6@cluster0.fypil5f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Acessando o banco de dados 'banco'
data_base = client.banco
posts = data_base.posts
#recuperação de files
for post in posts.find():
    pprint(post)

#mostra quantos documentos foram dicionados
print(posts.count_documents({}))
print(posts.count_documents({"author":"Marcio"}))
print(posts.count_documents({"tags":"Poupança"}))

#recuperando many files de maneira ordenada
for post in posts.find({}).sort("date"):
    pprint(post)

# definindo indice,para otimmizar buscas
result = data_base.profiles.create_index([('author')], unique = True)

# mostra todos os index
print(sorted(list(data_base.profiles.index_information())))

user_profiles = [
    {'user_id' : 264,'name':'Thor'},
    {'user_id' : 325,'name':'Rocket'}
    ]

result = data_base.profile_user.insert_many(user_profiles)

#Colções armazenadas
colecao = data_base.list_collection_names()
for x in colecao:
    print(x)

#removendo documentos
""" db["posts"].drop()
    db["profile_user"].drop()
    db["profiles"].drop()
    #deleta um documento especifico
    #posts.delete_one({"author":"Marcio})
    """

#acessando bd
data_base["posts"]

client.drop_database('banco')