from flask import Flask, request
import sqlite3
app = Flask(__name__)

@app.route("/escolas", methods= ['GET'])
def getEscolas():
    conn = sqlite3.connect('escola.db')

    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM tb_escola;
    """)
    for linha in cursor.fetchall():
        print(linha)

    conn.close()
    return("Executado")

@app.route("/escolas/<int:id>", methods=['GET'])
def getEscolasByID(id):
    conn = sqlite3.connect('escola.db')

    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM tb_escola where id = ?;
    """, (id, ))

    for linha in cursor.fetchall():
        print(linha)

    conn.close()
    return("Executado", 200)

@app.route("/escola", methods=['POST'])
def setEscola():

    print ('cadastrando a Escola')

    nome = request.form['nome']
    logradouro = request.form['logradouro']
    cidade = request.form['cidade']

    conn = sqlite3.connect('escola.db')

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO tb_escola(nome, logradouro, cidade)
        VALUES(?,?,?);

    """, (nome, logradouro, cidade))

    conn.commit()
    conn.close()

    return('CADASTRADO COM SUCESSO', 200)



@app.route("/alunos", methods=['GET'])
def getAlunos():

    conn = sqlite3.connect('escola.db')

    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM tb_aluno;
    """)

    for linha in cursor.fetchall():
        print(linha)
    conn.close()
    return ("Executado", 200)

@app.route("/alunos/<int:id>", methods=['GET'])
def getAlunosByID(id):

    conn = sqlite3.connect('escola.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM tb_aluno where id=?;
    """, (id, ))

    for linha in cursor.fetchall():
        print(linha)

    conn.close()
    return("Executado", 200)

@app.route("/aluno", methods=['POST'])
def setAluno():

    print ('cadastrando o aluno')

    nome = request.form['nome']
    matricula = request.form['matricula']
    cpf = request.form['cpf']
    nascimento = request.form['nascimento']

    conn = sqlite3.connect('escola.db')

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO tb_aluno(nome, matricula, cpf, nascimento)
        VALUES(?,?,?,?);

    """, (nome, matricula, cpf, nascimento))

    conn.commit()
    conn.close()
    return('CADASTRADO COM SUCESSO', 200)



@app.route("/cursos", methods=['GET'])
def getCursos():
    conn = sqlite3.connect('escola.db')

    cursor = conn.cursor()

    cursor.execute("""
        SELECT* FROM tb_curso;
    """)
    for linha in cursor.fetchall():
        print(linha)
    conn.close()
    return ("Executado", 200)

@app.route("/cursos/<int:id>", methods=['GET'])
def getCursosByID(id):
    conn = sqlite3.connect('escola.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM tb_curso where id=?;
    """, (id, ))

    for linha in cursor.fetchall():
        print(linha)

    conn.close()
    return("Executado", 200)

@app.route("/curso", methods=['POST'])
def setCurso():

    nome = request.form['nome']
    turno = request.form['turno']

    conn = sqlite3.connect('escola.db')
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tb_curso (nome, turno) values(?,?);
    """, (nome, turno, ))

    conn.commit()
    conn.close()

    return('CADASTRADO COM SUCESSO', 200)



@app.route("/turmas", methods=['GET'])
def getTurmas():
    conn = sqlite3.connect('escola.db')

    cursor = conn.cursor()

    cursor.execute("""
        SELECT* FROM tb_turma;
    """)
    for linha in cursor.fetchall():
        print(linha)
    conn.close()
    return ("Executado", 200)


@app.route("/turmas/<int:id>", methods=['GET'])
def getTurmasByID(id):
    conn = sqlite3.connect('escola.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM tb_turma where id=?;

    """, (id, ))

    for linha in cursor.fetchall():
        print(linha)

    conn.close()
    return("Executado", 200)


@app.route("/turma", methods=['POST'])
def setTurma():

    nome = request.form['nome']
    curso = request.form['curso']

    conn = sqlite3.connect('escola.db')
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO tb_turma (nome, curso) VALUES (?,?);

    """, (nome, curso, ))

    conn.commit()
    conn.close()
    return('CADASTRADO COM SUCESSO', 200)



@app.route("/disciplinas", methods=['GET'])
def getDisciplinas():
    conn = sqlite3.connect('escola.db')

    cursor = conn.cursor()

    cursor.execute("""
        SELECT* FROM tb_disciplina;
    """)
    for linha in cursor.fetchall():
        print(linha)
    conn.close()
    return ("Executado", 200)

@app.route("/disciplinas/<int:id>", methods=['GET'])
def getDisciplinasByID(id):
    conn = sqlite3.connect('escola.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM tb_disciplina where id=?;

    """, (id, ))

    for linha in cursor.fetchall():
        print(linha)

    conn.close()
    return("Executado", 200)


@app.route("/disciplina", methods=['POST'])
def setDisciplina():

    nome = request.form['nome']

    conn = sqlite3.connect('escola.db')
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO tb_disciplina (nome) VALUES (?);

    """, (nome, ))

    conn.commit()
    conn.close()
    return('CADASTRADO COM SUCESSO', 200)


if(__name__ == '__main__'):
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
