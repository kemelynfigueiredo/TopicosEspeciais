import sqlite3

samira = sqlite3.connect('shallownowschool.db')

cursor = samira.cursor()

cursor.execute(
    CREATE TABLE tb_estudante(
       nome varchar(50) NOT NULL,
       endereco text NOT NULL,
       nascimento date NOT NULL,
       matricula varchar(12) NOT NULL
   );
)
"""
#cursor.execute("""
    #SELECT * from td_estudante;

#""")
#for linha in cursor.fetchall():
    #print(linha)
print('Tabela criada com sucesso.')

samira.close()
