"""
Este projeto tem o objetivo de usar a biblioteca sqlAlchemy para realizar
consultas, inserir valores e criar tabelas, tudo isso usando como Banco de
dados o Postgree e Mongodb

"""


#Importando Bibliotecas 

from sqlalchemy import *
from sqlalchemy.orm import *

#Declarando a base

base = declarative_base()

# Criando tabelas

class User(base):
    """
    Esta classe é responsavel por criar a tabela cliente onde 
    contem as informações do usuário como : Id, Nome, CPF, endereço

    """
    
    # Definindo nome da tabela
    
    __tablename__= "cliente"
    
    # atributos da tabela
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    cpf = Column(String)
    
    # Criando relação entre tabelas

    conta = relationship(
        "Bank",back_populates="user",
    )
    
    # Retorna informações da tabela

    def  __repr__(self):
        return "User (id = {self.id}, name = {self.name}, cpf = {self.cpf})"

class Bank(base):
    """
    Esta classe é responsavel por criar a tabela conta onde 
    contem as informações do usuário como : Id, Tipo, Número, 
    Id_cliente, Saldo.

    """
    
    # Definindo nome da tabela
    __tablename__ = "conta"
    
    # Atributos da tabela

    id = Column(Integer, primary_key=True)
    tipo = Column(String,nullable=False)
    num = Column(String , nullable= False)
    id_cliente = Column(Integer, ForeignKey("cliente.id"))
    saldo = Column(DECIMAL)

    user = relationship("User",back_populates="conta")

    # Retorna informações da tabela

    def __repr__(self):
        return "Bank(id={self.id}, tipo={self.tipo}, num={self.num},id={self.id_cliente}, saldo={self.saldo} )"


# Conexão com banco de dados

engine = create_engine('postgresql+psycopg2://postgres:9aH&11a6@localhost:5432/postgres')

# Criando as classes como tabelas no banco de dados

base.metadata.create_all(engine)

# Adicionando itens no Banco de dados Postgreesql

with Session(engine) as session:
   """ 
    #Depois da primeira iserção, deixar como comentario senão a toda exexução ira
    adicionar novamente os user

    marcio = User(
    name = 'Marcio Guilherme',
    cpf = '489.652.658-88',
    conta = [Bank(tipo= 'Corrente', num= '2651265', saldo = 554.86)]
    )

    marcelo = User(
    name = 'Marcelo',
    cpf = "167.051.437.61",
    conta = [Bank(tipo= 'Poupança', num= '2651265', saldo = 1856.86)]
    )

    ana = User(
    name = 'Ana Cristina',
    cpf = '165.568.987-02',
    conta = [Bank(tipo= 'Conjunta', num= '26512', saldo= 452)]
    )
    
    # Upload dos dados para o banco de dados
    
    session.add_all([marcio,marcelo,ana])
    session.commit() 
"""
#-----------------------------------------------------------------------------------------------------

# Investiga o esquema de banco de dados

inspetor_engine = inspect(engine)
print(inspetor_engine.has_table("clientes"))
print(inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)

# Consultando itens no banco de dados

# Consultando todos os usuários
stat = select(User).where(User.name.in_(["Marcelo",'Marcio Guilherme','Ana Cristina']))
print("Recuperando usuários a partir de condição de filtragem")
for user in session.scalars(stat):
    print(f"id = {user.id}, name = {user.name}, cpf = {user.cpf}")

# Consultando contas apartir do id_usuario

stat_bank = select(Bank).where(Bank.id_cliente.in_([5]))
print("\nRecuperando as contas a partir de condição de filtragem")
for conta in session.scalars(stat_bank):
    print(f"id={conta.id}, tipo={conta.tipo}, num={conta.num},id={conta.id_cliente}, saldo={conta.saldo}")


# Execultando consultas Order by,join

stat_order = select(User).order_by(User.name.desc())
print("\nRecuperando os usuários de maneira decrescente apartir do nome")
for result in session.scalars(stat_order):
    print (f"id = {result.id}, name = {result.name}")

# Executando consultas  atravez de join

stat_join = select(User.name,Bank.num).join_from(Bank, User)
print("\nRecuperando os usuários atraves de um join,apartir do nome")
for result in session.scalars(stat_join):
    print (result)

# Contando total de users

conexao = engine .connect()
results = conexao.execute(stat_join).fetchall()
print("\nExecultando statement da conexão")
for result in results:
    print (result)

stat_count =select(func.count('*')).select_from(User)
print("\nTotal de instâncias em User")
for result in session.scalars(stat_count):
    print (result)