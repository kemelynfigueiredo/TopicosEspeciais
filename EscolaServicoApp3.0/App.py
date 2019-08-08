from flask import Flask, request, jsonify
import sqlite3
import logging
from flask_json_schema import JsonSchema

app = Flask(__name__)
schema = JsonSchema(app)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler = logging.FileHandler("escolaAPP.log")
handler.setFormatter(formatter)
logger = app.logger
logger.addHandler(handler)
logger.setLevel(logging.INFO)

endereco_schema = {
    'required' : ['logradouro', 'complemento','bairro', 'cep', 'numero']
    'properties':{
    'logradouro'{'type':'string'}
    'complemento'{'type':'string'}
    'bairro' {'type':'string'}
    'cep'{'type':'string'}
    "numero"{'type':"string"}
    }
}

campus_schema = {

    'required':['sigla','cidade']
    'properties':{
    'sigla'{'type':'string'}
    'cidade'{'type':'string'}
    }
}

escola_schema = {
    'required': ['nome', 'fk_id_endereco', 'fk_id_campus']
    'properties':{
    'nome'{'type':string}
    'fk_id_endereco'{'type':'int'}
    'fk_id_campus'{'type':'int'}
    }
}

turno_schema = {
    'required': ['nome']
    'properties':{
    'nome'{'type':'string'}
    }
}

curso_schema = {
    'required':['nome', 'fk_id_turno']
    'properties':{
    'nome'{'type':'string'}
    'fk_id_turno'{'type':'int'}
    }
}

aluno_schema = {
    'required':['nome','matricula', 'cpf', 'nascimento', 'fk_id_endereco','fk_id_curso']
    'properties':{
    'nome'{'type':'string'}
    'matricula'{'type':'string'}
    'cpf'{'type':'string'}
    'nascimento'{'type':'string'}
    'fk_id_endereco'{'type':'int'}
    'fk_id_curso'{'type':'int'}
    }
}

turma_schema = {
    'required': ['nome','fk_id_curso']
    'properties':{
    'nome'{'type':'string'}
    'fk_id_curso'{'type':'int'}
    }
}

professor_schema ={
    'required': ['nome','fk_id_endereco']
    'properties':{
    'nome':{'type':'string'}
    'fk_id_endereco'{'type':'int'}
    }
}

disciplina_schema = {
    'required':['nome','fk_id_endereco']
    'properties':{
    'nome':{'type':'string'}
    'fk_id_endereco'{'type':'int'}
    }
}

@app.route("/enderecos", method = ['GET'])
def getEndereco():

    logger.info("Listando endereços.")

    conn = sqlite3.connect('EscolaApp_versao2.db')
    cursor = conn.cursor()

    cursor.execute("""
            select * from tb_endereco;
    """)
    enderecos = []

    for linha in cursor.fetchall():

        enderecos.append(dict_factory(linha, cursor))

    conn.close()

    return (jsonify(enderecos))

def

    def dict_factory(linha, cursor):
    dicionario = {}
    for idx, col in enumerate(cursor.description):
        dicionario[col[0]] = linha[idx]
    return dicionario

    if(__name__ == '__main__'):
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
