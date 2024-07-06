from flask import *
from flask_restful import *
from models import Pessoas
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
api = Api(app)

# conexão com banco de dados
engine = create_engine('postgresql+psycopg2://postgres:9aH&11a6@localhost:5432/postgres')

class Pessoa(Resource):
    def get (self,nome):
        try:
            with Session(engine) as session:
                pessoa = session.query(Pessoas).filter_by(nome=nome).first()
                if pessoa:
                    response = {
                        "nome": pessoa.nome,
                        "idade": pessoa.idade,
                        "id": pessoa.id
                    }
                    return response
                else:
                    return jsonify({"mensagem": "Pessoa não encontrada"})
        except SQLAlchemyError as e:
            return {"mensagem": "Erro ao acessar o banco de dados", "error": str(e)}
    
    def post (self,nome):
        with Session(engine) as session:
            pessoa = session.query(Pessoas).filter_by(nome=nome).first()
            dados = request.json
        
            if 'nome' in dados:
                pessoa.nome = dados['nome']
            if 'idade' in dados:
                pessoa.idade = dados['idade']
            session.add(pessoa)
            session.commit()
            response = {
                "id" : pessoa.id, 
                "nome" : pessoa.nome,
                "idade" : pessoa.idade        
            }
            return response
    
    def deletar(self,nome):
        with Session(engine) as session:
            pessoa = session.query(Pessoas).filter_by(nome=nome).first()
            menssagem = f"Pessoa {pessoa.nome} excluida com sucesso."
            session.delete(pessoa)
            session.commit()
            return {f"status": "sucesso", "mensagem":menssagem}
        
class ListaPessoas(Resource):
    def get(self):
        with Session(engine) as session:
            pessoa = session.query(Pessoas).all()
            response = [{'id':i.id,'nome':i.nome,'idade':i.idade} for i in pessoa]
            return response
    
    def post(self):
        with Session(engine) as session:
            dados = request.json
            pessoa = Pessoas(nome = dados['nome'],idade = dados['idade'])
            session.add(pessoa)
            session.commit()
            response = {
                'id':pessoa.id,
                'nome':pessoa.nome,
                'idade':pessoa.idade
            }
            return response

#caminhos
#caminho referente a comando da class Pessoa
api.add_resource(Pessoa,'/pessoa/<string:nome>/')
#caminho referente a comando da class ListaPessoas
api.add_resource(ListaPessoas,'/pessoa/')