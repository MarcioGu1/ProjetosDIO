from sqlalchemy import *
from sqlalchemy.orm import *

# conexão com banco de dados
engine = create_engine('postgresql+psycopg2://postgres:9aH&11a6@localhost:5432/postgres')

base = declarative_base()

class Pessoas(base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40))
    idade = Column(Integer)

    #representação do objetivo,quado pesquisado retorna o nome 
    def __repr__(self):
        return f'<nome = {self.nome}  idade = {self.idade} >'

class Usuarios(base):
    __tablename__= 'usuarios'
    id = Column(Integer, primary_key=True)
    login = Column(String(20),unique=True)
    senha = Column(String(20))

    def __repr__(self):
        return f"<Usuário: {self.login}>"
    def save(self):
         with Session(engine) as session:
             session.add(self)
             session.commit()
    def delete(self):
         with Session(engine) as session:
             # Deleta a pessoa
            session.delete(self)
            session.commit()

def init_db():
    #criando as classes como tabelas no banco de dados
    base.metadata.create_all(engine)

def inserir():
    while True:
        nome = input('Nome da pessoa: ')
        idade = int(input('Idade da pessoa: '))

    # Verifica se o usuário digitou 0 para ambos nome e idade
        if nome == '0' and idade == 0:
            print("Finalizando o programa.")
            break

    # Verificando se a idade é 0 ou nome é vazio
        if idade == 0 or nome == '':
            print("Nome não pode estar vazio e idade não pode ser 0.")
        else:
        # Inserindo dados no banco de dados
            with Session(engine) as session:
                dados = Pessoas(
                    nome=nome,
                    idade=idade
                )
                session.add(dados)
                session.commit()
                print(f"Sucesso! {dados} foram inseridos com sucesso.")

def consultar():
   with Session(engine) as session:
    tipo = int(input("""Qual tipo de consulta deseja realizar:
                 [ 1 ] Através do nome
                 [ 2 ] Através da idade
                 [ 3 ] Através do Id
                 [ 4 ] Através da atividade
                 tipo :  """))
    if tipo == 1 :
        nome = str(input("Digite o nome: "))
        stat = select(Pessoas).where(Pessoas.nome.in_([nome]))
        print("Recuperando usuários a partir de condição de filtragem")
        for user in session.scalars(stat):
            print(f"id = {user.id}, name = {user.nome}, idade = {user.idade}")    
    elif tipo == 2 :
        idade = int(input("Digite a idade: "))
        stat = select(Pessoas).where(Pessoas.idade.in_([idade]))
        print("Recuperando usuários a partir de condição de filtragem")
        for user in session.scalars(stat):
            print(f"id = {user.id}, name = {user.nome}, idade = {user.idade}")
    elif tipo == 3 :
        id = int(input("Digite o ID: "))
        stat = select(Pessoas).where(Pessoas.id.in_([id]))
        print("Recuperando usuários a partir de condição de filtragem")
        for user in session.scalars(stat):
            print(f"id = {user.id}, name = {user.nome}, idade = {user.idade}")
    elif tipo == 4 :
        pass
    else:
        print("Voce digitou uma opção invalida")

def atualizar(user_id,novo_nome = None,nova_idade=None):
    with Session(engine) as session:
        pessoa = session.query(Pessoas).filter(Pessoas.id == user_id).one_or_none()
        
        if pessoa is None:
            print("Pessoa não encontrada.")
            return
        
        if novo_nome is not None:
            pessoa.nome = novo_nome
        
        if nova_idade is not None:
            pessoa.idade = nova_idade

        session.commit()
        print(f"Sucesso! Informações de {pessoa.nome} foram atualizadas com sucesso.")
    
def deletar():
    pessoa_id = int(input("ID do usúario que deseja excluir : "))
    with Session(engine) as session:
        try:
            # Busca a pessoa pelo ID
            pessoa = session.query(Pessoas).filter(Pessoas.id == pessoa_id).one_or_none()

            if pessoa is None:
                print("Pessoa não encontrada.")
                return

            # Deleta a pessoa
            session.delete(pessoa)
            session.commit()
            print(f"Sucesso! Informações de {pessoa.nome} foram deletadas com sucesso.")

        except Exception:
            print("Erro: Nenhuma pessoa encontrada com o ID fornecido.")

def insere_usuario():
  login = input("digite seu login: ")
  senha = input ("Digite sua senha : ")
  usuario = Usuarios(login=login,senha=senha)
  usuario.save()


def consulta_users():
    with Session(engine) as session:
        usuarios = session.query.all()
        print(usuarios)

if __name__ == '__main__':
    init_db()
    #inserir()
    consultar()
    consulta_users()