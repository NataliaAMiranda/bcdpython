import sqlite3

if __name__ == '__main__':
    print("OLá mundo")

    conexao = sqlite3.connect('lab05-ex01.sqlite')

    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM Pessoa")

    print(cursor.fetchall())

    pessoa = ('Juca',)
    cursor.execute("SELECT * FROM Pessoa where nome = ?", pessoa)
    for linha in cursor.fetchall():
        print("Id: {}\nNome: {}".format(linha[0], linha[1]))

    cursor.close()
    conexao.close()