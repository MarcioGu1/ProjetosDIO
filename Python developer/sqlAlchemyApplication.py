from sqlalchemy import *
from sqlalchemy.orm import *

base = declarative_base()

class User(base):
    __tablename__= "user_account"
    # atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = relationship(
        "Address",back_populates="user",cascade = "all,delete-orphan"
    )
    def  __repr__(self):
        return "User (id = {self.id}, name = {self.name})"
class Address(base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email = Column(String(30),nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"))

    user = relationship("User",back_populates="address")

    def __repr__(self):
        return f"Address(id={self.id},email={self.email})"
    
# conexão com banco de dados
engine = create_engine('postgresql+psycopg2://postgres:9aH&11a6@localhost:5432/postgres')
#criando as classes como tabelas no banco de dados
base.metadata.create_all(engine)

#investiga o esquema de banco de dados
inspetor_engine = inspect(engine)
print(inspetor_engine.has_table("user_account"))
print(inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)

#adicionando itens no Bd
with Session(engine) as session:
    marcio = User (
    name = 'Marcio Guilherme',
    address = [Address(email = "marcioguilherme@gmail.com")]
    )

    lucas = User(
        name = 'Lucas',
        address = [Address(email = "lucas@gmail.com"),Address(email = "lucaswar@gmail.com")]
    )
    patrick = User( name = "Patrick")

    #Enviando para o banco de dados
    session.add_all([marcio,lucas,patrick])
    session.commit()
#--------------------------------------------------------------------------------------------------------
#Consultando itens 
stat = select(User).where(User.name.in_(["Lucas",'Marcio Guilherme']))
print("Recuperando usuários a partir de condição de filtragem")
for user in session.scalars(stat):
    print(f"id = {user.id}, name = {user.name}")

stat_address = select(Address).where(Address.user_id.in_([2]))
print("\nRecuperando os endereços de email a partir de condição de filtragem")
for address in session.scalars(stat_address):
    print(f"id = {address.id}, name = {address.email}")
#Execultando consultas Order by,join
stat_order = select(User).order_by(User.name.desc())
print("\nRecuperando os usuários de maneira decrescente apartir do nome")
for result in session.scalars(stat_order):
    print (f"id = {result.id}, name = {result.name}")
stat_join = select(User.name,Address.email).join_from(Address, User)
print("\nRecuperando os usuários atraves de um join apartir do nome")
for result in session.scalars(stat_join):
    print (result)
conexao = engine .connect()
results = conexao.execute(stat_join).fetchall()
print("\Execultando statement da conexão")
for result in results:
    print (result)
stat_count =select(func.count('*')).select_from(User)
print("\nTotal de instâncias em User")
for result in session.scalars(stat_count):
    print (result)