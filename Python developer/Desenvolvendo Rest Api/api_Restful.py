from flask import Flask,request
from flask_restful import Resource,Api
import json

app = Flask(__name__)
api = Api(app)


desenvolvedores=[
    {
        "id":'0',
        "nome":"Marcio",
        "habilidade":["Python","Flask","Bd"]
    },
    {
        "id":'1',
        "nome":"Lucas",
        "habilidade":["Java","Python"]
    }
]
class Desenvolvedor(Resource):
    # Devolve,deleta,atualiza desenvolvedor pelo ID
    def get(self,id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f"Desenvolvedor de ID {id} não existe"
            response = {"status":"erro","mensagem":mensagem}
        except Exception:
            mensagem = "Erro desconhecido procure o ADMIN"
            response = {"status":"erro","mensagem":mensagem}
        return (response)
    def put(self,id):
        dados = json.loads(request.data)
        desenvolvedores[id] =dados
        return dados
    def delete(self,id):
        desenvolvedores.pop(id)
        return ({"status":"sucesso","mensagem":"Registro excluido"})
    
class LinstaDeDesenvolvedores(Resource):
    # Lista todos os desenvolvedor e permite registra um novo desenvolvedor

    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados["id"] = posicao
        desenvolvedores.append(dados)
        return {"status":'sucesso',"menssagem":"Registro inserido"}

# caminhos
api.add_resource(Desenvolvedor,'/dev/<int:id>/')
api.add_resource(LinstaDeDesenvolvedores,'/dev/')

#inicia a aplicação
if __name__ == '__main__':
    app.run()