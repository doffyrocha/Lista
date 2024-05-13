import sqlite3

def criar_tabela():
    conn = sqlite3.connect('lista_de_itens.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS'''

    )