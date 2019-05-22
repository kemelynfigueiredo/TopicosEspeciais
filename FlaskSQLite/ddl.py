import sqlite3

conn = sqlite3.connect('escola.db')

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE tb_aluno(
        id_aluno integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome varchar(45) NOT NULL,
        matricula varchar(12) NOT NULL,
        cpf varchar (11) NOT NULL,
        nascimento date NOT NULL
    );
""")
print('Tabela tb_aluno foi criada')
cursor.execute("""
    CREATE TABLE tb_curso(
        id_curso integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome varchar(45) NOT NULL,
        turno varchar(1) NOT NULL
    );
""")
print('Tabela tb_curso foi criada')
cursor.execute("""
    CREATE TABLE tb_turma(
        id_turma integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        fk_id_curso integer NOT NULL
    );
""")
print('Tabela tb_turma foi criada')
print ("Tabelas criadas com sucesso.")
conn.close()
