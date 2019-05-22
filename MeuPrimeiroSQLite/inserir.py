import sqlite3

samira = sqlite3.connect('shallownowschool.db')

cursor = samira.cursor()

valores = [('José','Rus Costa Meriz','2003-12-01', '201813710022')]

cursor.executemany("""
    INSERT INTO tb_estudante (nome, endereco, nascimento, matricula)
    VALUES (?,?,?,?);

""",valores)
samira.commit()
print("Inserido com sucesso")
samira.close()
