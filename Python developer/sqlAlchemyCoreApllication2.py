from sqlalchemy import *
 

# conexão com banco de dados
engine = create_engine('postgresql+psycopg2://postgres:9aH&11a6@localhost:5432/postgres')

# Cria uma instância de MetaData
metadata_obj = MetaData()

# Define uma tabela
user = Table(
    'user',metadata_obj,
    Column('user_id',Integer,primary_key=True),
    Column('user_name',String(40),nullable=False),
    Column('email',String(60)),
    Column('nickname',String(50),nullable=False),
    extend_existing=True
)
# Define outra tabela ou redefine a mesma tabela com novas opções
user_prefs = Table(
    'user_prefs',metadata_obj,
    Column('pref_id',Integer,primary_key=True),
    Column('user_id',Integer,ForeignKey("user.user_id"),nullable=False),
    Column('pref_name',String(40),nullable=False),
    Column('pref_value',String(100)),
    extend_existing=True
)
# Lista todas as tabelas definidas no metadata_obj
for table in metadata_obj.sorted_tables:
    print(table)

print('\nInfo da tabela user')
print(user.primary_key)
print(user.constraints)

print('\nInfo da tabela user_prefs')
print(user_prefs.primary_key)
print(user_prefs.constraints)
#pega informações
print(f'\n{metadata_obj.info}')
#mostra um dicionário do esquema
print(f'\n{metadata_obj.tables}')

# Cria todas as tabelas
metadata_obj.create_all(engine)

# Cria outra instância de MetaData
metadata_bd_obj = MetaData()

# Define uma tabela
financial_info = Table(
    'financial_info',
    metadata_bd_obj,
    Column('id',Integer,primary_key=True),
    Column('value',String(100),nullable=False),
)
print('\nInfo da tabela Financial_info')
print(financial_info.primary_key)
print(financial_info.constraints)
# Cria todas as tabelas
metadata_bd_obj.create_all(engine)
"""
# Executa uma consulta simples na tabela com comandos SQL
with engine.connect()as connection:
    sql = text("select * from user_account")
    result = connection.execute(sql)
    # Imprime os resultados da consulta
    for row in result:
        print(row)
"""
#Introduzindo valores na tabela user
with engine.connect()as connection:
    sql = insert(user).values(user_id=1, user_name='marcio', email='marico@gmail.com', nickname='Ret')
    result = connection.execute(sql)
    connection.commit()