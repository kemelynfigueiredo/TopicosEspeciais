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

    conn = sqlite3.connect("ifpb.db")

    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM TB_ESCOLAS;
    """)

    escolas = []
    for linha in cursor.fetchall():

    	escola = {
    		"id_escola" : linha[0],
    		"nome" : linha[1],
    		"logradouro" : linha[2],
    		"cidade" : linha[3]
    	}

    	escolas.append(escola)

	conn.close()

	return (jsonify(escolas))

@app.route("/escolas/<int:id>", methods=['GET'])
def getEscolaByID(id):

    conn = sqlite3.connect('ifpb.db')

    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM TB_ESCOLAS WHERE ID_ESCOLA = ?;

    """, (id, ))


    linha = cursor.fetchone()
    escolas = []
    escola = {
    	"id_escola" : linha[0],
		"nome" : linha[1],
    	"logradouro" : linha[2],
    	"cidade" : linha[3]
    	}
    escolas.append(escola)

    conn.close()

    return (jsonify(escolas))

@app.route("/escola", methods=['POST'])
def setEscola():

    escola = request.get_json()
    nome = escola['nome']
    logradouro = escola['logradouro']
    cidade = escola['cidade']

    conn = sqlite3.connect('ifpb.db')

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO TB_ESCOLAS(NOME, LOGRADOURO, CIDADE)
        VALUES(?,?,?);

    """, (nome, logradouro, cidade, ))

    conn.commit()
    conn.close()

    id = cursor.lastrowid
    escola['id_escola'] = id

    return (jsonify(escola))

@app.route("/escolas/<int:id>", methods=['PUT'])
def updateEscola():

    escola = request.get_json()
    nome = escola['nome']
    logradouro = escola['logradouro']
    cidade = escola['cidade']

    cursor.execute("""

        SELECT * FROM TB_ESCOLAS WHERE ID_ESCOLA = ?;

    """(id,))

    data = cursor.fetchone()

    if data is not None:

        cursor.execute("""

            UPDATE TB_ESCOLAS SET NOME=?, LOGRADOURO=?, CIDADE=? WHERE ID_ESCOLA=?;

        """(nome, logradouro, cidade, id))

        conn.commit()

    else:

        cursor.execute("""

            INSERT INTO TB_ESCOLAS(NOME, LOGRADOURO, CIDADE)
            VALUES(?,?,?)

        """(nome, logradouro, cidade))

        conn.commit()
        id = cursor.lastrowid
        escola['id_escola']

    conn.close()

    return(jsonify(escola))

@app.route("/alunos", methods=['GET'])
def getAlunos():

    conn = sqlite3.connect('ifpb.db')

    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM TB_ALUNOS;

    """)

    alunos = []
    for linha in cursor.fetchall():
    	aluno = {
    		"id_aluno" : linha[0],
    		"nome" : linha[1],
    		"matricula" : linha[2],
    		"cpf" : linha[3],
    		"nascimento" : linha[4]
    	}
        alunos.append(aluno)

    conn.close()

    return (jsonify(alunos))

@app.route("/alunos/<int:id>", methods=['GET'])
def getAlunoByID(id):

    conn = sqlite3.connect('ifpb.db')

    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM TB_ALUNOS WHERE ID_ALUNO = ?;

    """, (id, ))

    linha = cursor.fetchone()
    alunos = []
    aluno = {
    	"id_aluno" : linha[0],
    	"nome" : linha[1],
    	"matricula" : linha[2],
    	"cpf" : linha[3],
    	"nascimento" : linha[4]
    	}
    alunos.append(aluno)

    conn.close()

    return (jsonify(alunos))

@app.route("/aluno", methods=['POST'])
def setAlunos():

    aluno = request.get_json()
    nome = aluno['nome']
    matricula = aluno['matricula']
    cpf = aluno['cpf']
    nascimento = aluno['nascimento']

    conn = sqlite3.connect('ifpb.db')

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO TB_ALUNOS(NOME, MATRICULA, CPF, NASCIMENTO)
        VALUES(?,?,?,?);

    """, (nome, matricula, cpf, nascimento, ))

    conn.commit()
    conn.close()

    id = cursor.lastrowid
    aluno['id_aluno'] = id

    return (jsonify(aluno))

@app.route("/alunos/<int:id>", methods=["PUT"])
def updateAluno():

	aluno = request.get_json()
	nome = aluno['nome']
	matricula = aluno['matricula']
	cpf = aluno['cpf']
	nascimento = aluno['nascimento']

	conn = sqlite3.connect('ifpb.db')
	cursor = conn.cursor()

	cursor.execute("""

		SELECT * FROM TB_ALUNOS WHERE ID_ALUNO = ?;

	"""(id,))

	data = cursor.fetchone()

	if data is not None:

		cursor.execute("""

			UPDATE TB_ALUNOS SET NOME = ?, MATRICULA = ?, CPF = ?, NASCIMENTO = ? WHERE ID_ALUNO = ?;
		"""(nome, matricula, cpf, nascimento, id))

		conn.commit()

	else:

		cursor.execute("""

			INSERT INTO TB_ALUNOS(NOME, MATRICULA, CPF, NASCIMENTO)
			VALUES(?,?,?,?)

		"""(nome, matricula, cpf, nascimento))

		conn.commit()
		id = cursor.lastrowid
		aluno['id_aluno'] = id

	conn.close()

	return jsonify(aluno)

@app.route("/cursos", methods=['GET'])
def getCursos():

    conn = sqlite3.connect('ifpb.db')

    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM TB_CURSOS;

    """)

    cursos = []
    for linha in cursor.fetchall():
    	curso = {
    		"id_curso" : linha [0],
    		"nome" : linha[1],
    		"turna" : linha[2]
    	}
        cursos.append(curso)

    conn.close()

    return (jsonify(cursos))

@app.route("/cursos/<int:id>", methods=['GET'])
def getCursoByID(id):

    conn = sqlite3.connect('ifpb.db')

    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM TB_CURSOS WHERE ID_CURSO = ?;

    """, (id, ))

    linha = cursor.fetchone()
    cursos = []
    curso = {
    	"id_curso" : linha [0],
    	"nome" : linha[1],
    	"turna" : linha[2]
    	}
    cursos.append(curso)

    conn.close()

    return (jsonify(cursos))

@app.route("/curso", methods=['POST'])
def setCursos():

    curso = request.get_json()
    nome = curso['nome']
    turno = curso['turno']

    conn = sqlite3.connect('ifpb.db')

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO TB_CURSOS(NOME, TURNO)
        VALUES(?, ?);

    """, (nome, turno, ))

    conn.commit()
    conn.close()

    id = cursor.lastrowid
    curso['ID_CURSO'] = id

    return (jsonify(curso))

@app.route("/cursos/<int:id>, methods=['PUT']")
def updateCurso():
    curso = request.get_json()
    nome = curso['nome']
    turno = curso['turno']
    conn = sqlite3.connect('ifpb.db')

    cursor = conn.cursor()

    cursor.execute("""
    	SELECT * FROM TB_CURSOS WHERE ID_CURSO = ?;
    """(id,))

    data = cursor.fetchone()

    if data is not None:
        cursor.execute("""
        	UPDATE TB_CURSOS SET NOME=?, TURNO=? WHERE ID_CURSO = ?;
        """(nome, turno, id))

        conn.commit()

    else:
        cursor.execute("""
        	INSERT INTO TB_CURSOS(NOME, TURNO) VALUES(?,?)
        """(nome, turno))
        conn.commit()
        id = cursor.lastrowid
        curso['id_curso'] = id

    conn.close()

    return jsonify()

@app.route("/turmas", methods=['GET'])
def getTurmas():

    conn = sqlite3.connect('ifpb.db')

    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM TB_TURMAS;

    """)

    turmas = []
    for linha in cursor.fetchall():
    	turma = {

    		"id_turma" : linha[0],
    		"nome" : linha[1],
    		"curso" : linha[2]

    	}
        turmas.append(turma)

    conn.close()

    return (jsonify(turmas))

@app.route("/turmas/<int:id>", methods=['GET'])
def getTurmaByID(id):

    conn = sqlite3.connect('ifpb.db')

    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM TB_TURMAS WHERE ID_TURMA = ?;

    """, (id, ))

    linha = cursor.fetchone()
    turmas = []
    turma = {

    	"id_turma" : linha[0],
    	"nome" : linha[1],
    	"curso" : linha[2]

    	}
    turmas.append(turma)

    conn.close()

    return (jsonify(turmas))

@app.route("/turma", methods=['POST'])
def setTurmas():


    turma = request.get_json()
    nome = turma['nome']
    curso = turma['curso']

    conn = sqlite3.connect('ifpb.db')

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO TB_TURMAS(NOME, CURSO)
        VALUES(?, ?);

    """, (nome, curso, ))

    conn.commit()
    conn.close()

    id = cursor.lastrowid
    turma['id_turma'] = id

    return (jsonify(turma))

@app.route("/turmas/<int:id>, methods=['PUT']")
def updateTurma():

    turma = request.get_json()

    nome = turma['nome']
    curso = turma['curso']

    conn = sqlite3.connect('ifpb.db')
    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM TB_TURMAS WHERE ID_TURMA = ?;

        """(id,))

    data = cursor.fetchone()

    if data is not None:

        cursor.execute("""
            UPDATE TB_TURMAS SET NOME=?, CURSO=? WHERE  = ?;
        """(nome, curso, id))

        conn.commit()

    else:

        cursor.execute("""

            INSERT INTO TB_TURMAS(NOME, CURSO)
            VALUES(?,?)

        """(nome, curso))

        conn.commit()

        id = cursor.lastrowid

        turma['id_turma'] = id

    conn.close()

    return jsonify()

@app.route("/disciplinas", methods=['GET'])
def getDisciplinas():

    conn = sqlite3.connect('ifpb.db')

    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM TB_DISCIPLINAS;

    """)

    disciplinas = []
    for linha in cursor.fetchall():
    	disciplina = {
    		"id_disciplina" : linha[0],
    		"nome" : linha[1]
    	}
        disciplinas.append(disciplina)

    conn.close()

    return(jsonify(disciplinas))

@app.route("/disciplinas/<int:id>", methods=['GET'])
def getDisciplinaByID(id):

    conn = sqlite3.connect('ifpb.db')

    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM TB_DISCIPLINAS WHERE ID_DISCIPLINA = ?;

    """, (id, ))

    linha = cursor.fetchone()
    disciplinas = []
    disciplina = {
    	"id_disciplina" : linha[0],
    	"nome" : linha[1]
    	}
    disciplinas.append(disciplina)

    conn.close()

    return(jsonify(disciplinas))

@app.route("/disciplina", methods=['POST'])
def setDisciplinas():

    disciplina = request.get_json()
    nome = disciplina['nome']

    conn = sqlite3.connect('ifpb.db')

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO TB_DISCIPLINAS(NOME)
        VALUES(?);

    """, (nome, ))

    conn.commit()
    conn.close()

    id = cursor.lastrowid
    disciplina['id_disciplina'] = id

    return (jsonify(disciplina))

@app.route("/disciplinas/<int:id>, methods=['PUT']")
def updateDisciplina():

    disciplina = request.get_json()
    nome = disciplina['nome']

    conn = sqlite3.connect('ifpb.db')
    cursor = conn.cursor()

    cursor.execute("""

        SELECT * FROM TB_DISCIPLINAS WHERE ID_DISCIPLINA = ?;

    """(id,))

    data = cursor.fetchone()

    if data is not None:

        cursor.execute("""

            UPDATE TB_DISCIPLINAS SET NOME=? WHERE ID_DISCIPLINA = ?;

        """(nome, ))

        conn.commit()

    else:

        cursor.execute("""

            INSERT INTO TB_DISCIPLINAS(NOME)
            VALUES(?)

        """(nome, ))

        conn.commit()
        id = cursor.lastrowid
        disciplina['id_disciplina'] = id

    conn.close()

    return jsonify()

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
