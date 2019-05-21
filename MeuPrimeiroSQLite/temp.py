import sqlite3

samira = sqlite3.connect('shallownowschool.db')

cursor = samira.cursor()

cursor.execute("""
    INSERT INTO td_estudante(nome, endereco, nascimento, matricula)
    VALUES ('Maria da Conceição', 'Rua da Paz', '1902-12-12', 20161382596);

""")
samira.commit()
print("Inserido com sucesso.")
samira.close()
