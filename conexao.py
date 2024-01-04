import mysql.connector

def conectar_banco():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='uece',
    )
    cursor = conexao.cursor()
    return conexao, cursor

def fechar_conexao(conexao, cursor):
    cursor.close()
    conexao.close()

if __name__ == "__main__":
    conexao, cursor = conectar_banco()

    # Insira aqui o restante do seu código CRUD

    fechar_conexao(conexao, cursor)