from flask import Flask

app = Flask(__name__)

@app.route("/usuario")
def hello_world():
    return ("Olá Mundo! Estou aprendendo Flask", 200)

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
