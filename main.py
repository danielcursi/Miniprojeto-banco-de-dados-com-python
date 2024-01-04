from conexao import conectar_banco, fechar_conexao

conexao, cursor = conectar_banco()

def cadastra_aluno(matricula, nome, np1=0, np2=0, np3=0, np4=0):
    comando = f'INSERT INTO notas(matricula, nome, np1, np2, np3, np4) VALUES ({matricula}, "{nome}", {np1}, {np2}, {np3}, {np4})'
    cursor.execute(comando)
    conexao.commit()
    
def inputs():
    matricula = int(input("Informe matricula (7digitos): "))
    nome = input("nome: ")
    np1 = input("Nota1: ")
    np2 = input("Nota2: ")
    np3 = input("Nota3: ")
    np4 = input("Nota4: ")
    
    if matricula == validar_matricula(matricula):
        print("Matricula já cadastrada")
    else:
        cadastra_aluno(matricula, nome, np1, np2, np3, np4)
    
def validar_matricula(matricula):
    comando = 'SELECT * FROM notas'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    valor = 0
    for i in range(len(resultado)):
        if matricula == resultado[i][0]:
            valor = (resultado[i][0])
            break;
    return valor

def media():
    divisor = int(input("Por quanto deseja dividir?: "))
    comando = 'SELECT * FROM notas'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    for i in range(len(resultado)):
        media = (resultado[i][2] + resultado[i][3] + resultado[i][4] + resultado[i][5]) / divisor
        matricula = resultado[i][0]
        comando = f'UPDATE notas SET media = {media} WHERE matricula = {matricula}'
        cursor.execute(comando)
    print("Médias atualizadas!")
 
def atualizar_cadastro():
    matricula = int(input("Informe a matricula: "))
    if matricula == validar_matricula(matricula):
        print("Matricula encontrada!")
        print(f"{matricula} - {nome_aluno(matricula)}")
        print("1 - Matricula\n2 - Nome\n3 - Notas\n4 - média")
        opcao = input("Digite a opção desejada: ")
        if opcao == '1':
            atualizar_matricula(matricula)
        elif opcao == '2':
            atualizar_nome(matricula)
        elif opcao == '3':
            atualizar_nota(matricula)
        
    else:
        print("Matricula não encontrada!")
 
def nome_aluno(matricula):
     comando = f'SELECT * FROM notas WHERE matricula = {matricula}'
     cursor.execute(comando)
     resultado = cursor.fetchall()
     for i in range(len(resultado)):
        return resultado[i][1]

def atualizar_matricula(matricula):
    nova_matricula = int(input("Nova matricula: "))
    if nova_matricula == validar_matricula(matricula):
        print("Matricula já existe!")
    else:
        comando = f'UPDATE notas SET matricula = {nova_matricula} WHERE matricula = {matricula}'
        cursor.execute(comando)
        print("Matricula atualizada!")

def atualizar_nome(matricula):
    novo_nome = input("Informe o novo nome: ")
    comando = f'UPDATE notas SET nome = "{novo_nome}" WHERE matricula = {matricula}'
    cursor.execute(comando)
    print("Nome atualizado!")
    
def atualizar_nota(matricula):
    semestre = input("Informe o semestre: ")
    if int(semestre) > 4:
        print("Semestre nao existente!")
    else:
        np = "np" + semestre
        nova_nota = input("Informe a nota: ")
        comando = f'UPDATE notas SET {np} = {nova_nota} WHERE matricula = {matricula}'
        cursor.execute(comando)
        print("Nota atualizada!")
        atualizar_media = input("Deseja atualizar todas as médias?: s/n: ")
        if atualizar_media == 's' or 'S':
            media()
        else:
            print("Programa finalizado!")


def banco_notas():
    comando = 'SELECT * FROM notas'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    for i in range(len(resultado)):
        print(f"matricula: {resultado[i][0]}, nome: {resultado[i][1]}, np1: {resultado[i][2]}, np2: {resultado[i][3]}, np3: {resultado[i][4]}, np4: {resultado[i][5]}, média: {resultado[i][6]}")
        
def banco_por_aluno():
    matricula = int(input("Informe a matricula: "))
    if matricula == validar_matricula(matricula):
        comando = f'SELECT * FROM notas WHERE matricula = {matricula}'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        for i in range(len(resultado)):
            print(f"matricula: {resultado[i][0]}, nome: {resultado[i][1]}, np1: {resultado[i][2]}, np2: {resultado[i][3]}, np3: {resultado[i][4]}, np4: {resultado[i][5]}, média: {resultado[i][6]}")
            
opcao = ''

while opcao != '6':
    print("1 - Novo aluno\n2 - Atualizar médias\n3 - Atualizar campos\n4 - visualizar tudo\n5 - visualizar por matricula\n6 - Sair")
    opcao = input("Opção: ")
    if opcao == "1":
        inputs()
    elif opcao == "2":
        media()
    elif opcao == "3":
        atualizar_cadastro()
    elif opcao == "4":
        banco_notas()
    elif opcao == "5":
        banco_por_aluno()
    elif opcao == "6":
        print("Saindo...")
        print("Cessão encerrada!")
    else:
        print("Opção não encontrada!")


fechar_conexao(conexao, cursor)