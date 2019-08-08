from flask import Flask, request, jsonify
import sqlite3
import logging

app = Flask(__name__)

# Logging
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler = logging.FileHandler("escolaAPP.log")
handler.setFormatter(formatter)
logger = app.logger
logger.addHandler(handler)
logger.setLevel(logging.INFO)



@app.route("/escolas", methods=['GET'])
def getEscolas():

    logger.info("Listando escolas.")

    conn = sqlite3.connect("escola.db")

    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM tb_escola;
    """)

    escolas = []
    for linha in cursor.fetchall():

        escolas.append(dict_factory(linha, cursor))

    conn.close()

    return (jsonify(escolas))

@app.route("/escolas/<int:id>", methods=['GET'])
def getEscolaByID(id):

    logger.info("Listando escolas pelo ID.")

    conn = sqlite3.connect('escola.db')

    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM tb_escola WHERE id_escola = ?;

    """, (id, ))


    linha = cursor.fetchone()
    escola = []
    escola.append(dict_factory(linha,cursor))

    conn.close()

    return (jsonify(escolaId))

@app.route("/escola", methods=['POST'])
def setEscola():

    logger.info("Buscando dados da escola.")

    escola = request.get_json()
    nome = escola['nome']
    logradouro = escola['logradouro']
    cidade = escola['cidade']

    conn = sqlite3.connect('escola.db')

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO tb_escola (nome, logradouro, cidade)
        VALUES(?,?,?);

    """, (nome, logradouro, cidade, ))

    conn.commit()
    conn.close()

    id = cursor.lastrowid
    escola['id_escola'] = id

    return (jsonify(escola))

@app.route("/escolas/<int:id>", methods=['PUT'])
def updateEscola():

    logger.info("Atualizando dados da escola.")

    escola = request.get_json()
    nome = escola['nome']
    logradouro = escola['logradouro']
    cidade = escola['cidade']

    cursor.execute("""

        SELECT * FROM tb_escola WHERE id_escola = ?;

    """(id,))

    data = cursor.fetchone()

    if data is not None:

        cursor.execute("""

            UPDATE tb_escola SET nome=?, logradouro=?, cidade=? WHERE id_escola=?;

        """(nome, logradouro, cidade, id))

        conn.commit()

    else:

        cursor.execute("""

            INSERT INTO tb_escola(nome, logradouro, cidade)
            VALUES(?,?,?)

        """(nome, logradouro, cidade))

        conn.commit()
        id = cursor.lastrowid
        escola['id_escola']

    conn.close()

    return(jsonify(escola))

@app.route("/alunos", methods=['GET'])
def getAlunos():

    logger.info("Listando alunos.")

    conn = sqlite3.connect('escola.db')

    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM tb_aluno;

    """)

    alunos = []
    for linha in cursor.fetchall():
        alunos.append(dict_factory(linha,cursor))

    conn.close()

    return (jsonify(alunos))

@app.route("/alunos/<int:id>", methods=['GET'])
def getAlunoByID(id):

    logger.info("Listando alunos pelo ID.")

    conn = sqlite3.connect('escola.db')

    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM tb_aluno WHERE id_aluno=?;

    """, (id, ))

    linha = cursor.fetchone()
    alunos = []
    alunos.append(dict_factory(linha,cursor))

    conn.close()

    return (jsonify(alunos))

@app.route("/aluno", methods=['POST'])
def setAlunos():

    logger.info("Buscando dados dos alunos.")

    aluno = request.get_json()
    nome = aluno['nome']
    matricula = aluno['matricula']
    cpf = aluno['cpf']
    nascimento = aluno['nascimento']

    conn = sqlite3.connect('escola.db')

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO tb_aluno(nome, matricula, cpf, nascimento)
        VALUES(?,?,?,?);

    """, (nome, matricula, cpf, nascimento, ))

    conn.commit()
    conn.close()

    id = cursor.lastrowid
    aluno['id_aluno'] = id

    return (jsonify(aluno))

@app.route("/alunos/<int:id>", methods=["PUT"])
def updateAluno():

    logger.info("Atualizando dados dos alunos.")

    aluno = request.get_json()
    nome = aluno['nome']
    matricula = aluno['matricula']
    cpf = aluno['cpf']
    nascimento = aluno['nascimento']

    conn = sqlite3.connect('escola.db')
    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM tb_aluno WHERE id_aluno=?;

    """(id,))

    data = cursor.fetchone()

    if data is not None:

        cursor.execute("""

            UPDATE tb_aluno SET nome = ?, matricula = ?, cpf = ?, nascimento = ? WHERE id_aluno = ?;

        """(nome, matricula, cpf, nascimento, id))

        conn.commit()

    else:

        cursor.execute("""

            INSERT INTO tb_aluno(nome, matricula, cpf, nascimento)
			VALUES(?,?,?,?)

        """(nome, matricula, cpf, nascimento))

        conn.commit()
        id = cursor.lastrowid
        aluno['id_aluno']= id

    conn.close()
    return (jsonify(aluno))


@app.route("/cursos", methods=['GET'])
def getCursos():

    logger.info("Listando cursos.")

    conn = sqlite3.connect('escola.db')

    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM tb_curso;

    """)

    cursos = []
    for linha in cursor.fetchall():
        cursos.append(curso)

    conn.close()

    return (jsonify(cursos))

@app.route("/cursos/<int:id>", methods=['GET'])
def getCursoByID(id):

    logger.info("Listando cursos pelo ID.")

    conn = sqlite3.connect('escola.db')
    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM tb_curso WHERE id_curso = ?;

    """, (id, ))

    linha = cursor.fetchone()
    cursos = []
    cursos.append(dict_factory(linha,cursor))

    conn.close()

    return (jsonify(cursos))

@app.route("/curso", methods=['POST'])
def setCursos():

    logger.info("Buscando dados dos cursos.")

    curso = request.get_json()
    nome = curso['nome']
    turno = curso['turno']

    conn = sqlite3.connect('escola.db')

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO tb_cursoS(nome, turno)
        VALUES(?, ?);

    """, (nome, turno, ))

    conn.commit()
    conn.close()

    id = cursor.lastrowid
    curso['id_curso'] = id

    return (jsonify(curso))

@app.route("/cursos/<int:id>, methods=['PUT']")
def updateCurso():

    logger.info("Atualizando dados dos cursos.")

    curso = request.get_json()
    nome = curso['nome']
    turno = curso['turno']

    conn = sqlite3.connect('escola.db')

    cursor = conn.cursor()

    cursor.execute("""
    	SELECT * FROM tb_curso WHERE id_curso = ?;
    """(id,))

    data = cursor.fetchone()

    if data is not None:
        cursor.execute("""
        	UPDATE tb_curso SET nome=?, turno=? WHERE id_curso = ?;
        """(nome, turno, id))

        conn.commit()

    else:
        cursor.execute("""
        	INSERT INTO tb_curso(nome, turno) VALUES(?,?)
        """(nome, turno))
        conn.commit()
        id = cursor.lastrowid
        curso['id_curso'] = id

    conn.close()

    return jsonify()

@app.route("/turmas", methods=['GET'])
def getTurmas():

    logger.info("Listando turmas.")

    conn = sqlite3.connect('escola.db')

    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM tb_turma;

    """)

    turmas = []
    for linha in cursor.fetchall():
        turmas.append(dict_factory(linha,cursor))

    conn.close()

    return (jsonify(turmas))

@app.route("/turmas/<int:id>", methods=['GET'])
def getTurmaByID(id):

    logger.info("Listando turmas pelo ID.")

    conn = sqlite3.connect('escola.db')

    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM tb_turma WHERE id_turma = ?;

    """, (id, ))

    linha = cursor.fetchone()
    turmas = []
    turmas.append(dict_factory(linha, cursor))

    conn.close()

    return (jsonify(turmas))

@app.route("/turma", methods=['POST'])
def setTurmas():

    logger.info("Buscando dados das turmas.")


    turma = request.get_json()
    nome = turma['nome']
    curso = turma['curso']

    conn = sqlite3.connect('escola.db')

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO tb_turma(nome, curso)
        VALUES(?, ?);

    """, (nome, curso, ))

    conn.commit()
    conn.close()

    id = cursor.lastrowid
    turma['id_turma'] = id

    return (jsonify(turma))

@app.route("/turmas/<int:id>, methods=['PUT']")
def updateTurma():

    logger.info("Atualizando dados das turmas.")

    turma = request.get_json()
    nome = turma['nome']
    curso = turma['curso']

    conn = sqlite3.connect('escola.db')
    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM tb_turma WHERE id_turma = ?;

        """(id,))

    data = cursor.fetchone()

    if data is not None:

        cursor.execute("""
            UPDATE tb_turma SET nome=?, curso=? WHERE  = ?;
        """(nome, curso, id))

        conn.commit()

    else:

        cursor.execute("""

            INSERT INTO tb_turma(nome, curso)
            VALUES(?,?)

        """(nome, curso))

        conn.commit()

        id = cursor.lastrowid

        turma['id_turma'] = id

    conn.close()

    return jsonify()

@app.route("/disciplinas", methods=['GET'])
def getDisciplinas():

    logger.info("Listando disciplinas.")

    conn = sqlite3.connect('escola.db')

    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM tb_disciplina;

    """)

    disciplinas = []
    for linha in cursor.fetchall():
        disciplinas.append(dict_factory(linha, cursor))

    conn.close()

    return(jsonify(disciplinas))

@app.route("/disciplinas/<int:id>", methods=['GET'])
def getDisciplinaByID(id):

    logger.info("Listando disciplinas pelo ID.")

    conn = sqlite3.connect('escola.db')

    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM tb_disciplina WHERE id_disciplina = ?;

    """, (id, ))

    linha = cursor.fetchone()
    disciplinas = []
    disciplinas.append(dict_factory(linha,cursor))

    conn.close()

    return(jsonify(disciplinas))

@app.route("/disciplina", methods=['POST'])
def setDisciplinas():

    logger.info("Buscando dados das disciplinas.")

    disciplina = request.get_json()
    nome = disciplina['nome']

    conn = sqlite3.connect('escola.db')

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO tb_disciplina(nome)
        VALUES(?);

    """, (nome, ))

    conn.commit()
    conn.close()

    id = cursor.lastrowid
    disciplina['id_disciplina'] = id

    return (jsonify(disciplina))

@app.route("/disciplinas/<int:id>, methods=['PUT']")
def updateDisciplina():

    logger.info("Atualizando dados das disciplinas.")

    disciplina = request.get_json()
    nome = disciplina['nome']

    conn = sqlite3.connect('escola.db')
    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM tb_disciplina WHERE id_disciplina = ?;

    """(id,))

    data = cursor.fetchone()

    if data is not None:

        cursor.execute("""

            UPDATE tb_disciplina SET nome=? WHERE id_disciplina = ?;

        """(nome, ))

        conn.commit()

    else:

        cursor.execute("""

            INSERT INTO tb_disciplina(nome)
            VALUES(?)

        """(nome, ))

        conn.commit()
        id = cursor.lastrowid
        disciplina['id_disciplina'] = id

    conn.close()

    return jsonify()


def dict_factory(linha, cursor):
    dicionario = {}
    for idx, col in enumerate(cursor.description):
        dicionario[col[0]] = linha[idx]
    return dicionario

@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
