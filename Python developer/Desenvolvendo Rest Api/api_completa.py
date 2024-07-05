from flask import Flask, jsonify,request
import json

app = Flask(__name__)

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
# Devolve,deleta,atualiza desenvolvedor pelo ID
@app.route("/dev/<int:id>/",methods = ["GET", "PUT","DELETE"])
def desenvolvedor(id):
    if request.method == "GET":
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f"Desenvolvedor de ID {id} não existe"
            response = {"status":"erro","mensagem":mensagem}
        except Exception:
            mensagem = "Erro desconhecido procure o ADMIN"
            response = {"status":"erro","mensagem":mensagem}
        return jsonify(response)
    
    elif request.method == "PUT": 
        dados = json.loads(request.data)
        desenvolvedores[id] =dados
        return jsonify(dados)
    elif request.method == "DELETE":
        desenvolvedores.pop(id)
        return jsonify({"status":"sucesso","mensagem":"Registro excluido"})

# Lista todos os desenvolvedor e permite registra um novo desenvolvedor
@app.route('/dev/',methods=['GET', 'POST'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados["id"] = posicao
        desenvolvedores.append(dados)
        return jsonify({"status":'sucesso',"menssagem":"Registro inserido"})
    elif request.method == "GET":
        return jsonify(desenvolvedores)
if __name__ == '__main__':
    app.run()