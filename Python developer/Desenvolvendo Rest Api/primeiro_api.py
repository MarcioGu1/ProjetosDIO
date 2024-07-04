from flask import * 

app = Flask(__name__)

@app.route("/")
def ola():
    return "first project "

if __name__ == "__main__":
    app.run() 
