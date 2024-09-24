def main():
    menu = f"""
    {"SEJA BEM-VINDO".center(20, "#")}

    DIGITE A OPERAÇÃO QUE DESEJA REALIZAR

    1 - SACAR

    2 - DEPOSITAR

    3 - EXTRATO

    4 - CADASTRAR USUARIO

    5 - NOVA CONTA

    6 - LISTAR CONTAS

    0 - SAIR
    
"""

    SAQUES_POR_DIA = 0
    AGENCIA = "0001"

    historico= []
    saldo = 0
    limite = 500
    usuarios = []
    contas = []

    while True:
        opcao = input(menu)

        if opcao == "1":
            sacar(saldo, historico, SAQUES_POR_DIA, limite)
    
        elif opcao == "2":
            depositar(saldo, historico)

        elif opcao == "3":
            extrato(saldo, historico)

        elif opcao == "4":
            novo_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = nova_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
            
        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            break

def sacar(saldo, historico, SAQUES_POR_DIA, limite):
    if SAQUES_POR_DIA > 3:
        print("\n \n LIMITE DE SAQUES ATINGIDOS")     
    else:
        valor = input("DIGITE O VALOR QUE DESEJA SACAR:")
        if saldo < float(valor):
            print("\n \n SALDO INSUFICIENTE \n")
        else:
            if float(valor) <= limite:
                saldo -= float(valor)
                SAQUES_POR_DIA += 1
                historico.append(f"SAQUE: R${valor}")
                
def depositar(saldo, historico):
    

    valor = input("DIGITE O VALOR A SER DEPOSITADO: ")
    saldo += float(valor)
    historico.append(f"DEPOSITO: R${valor}")

def extrato(saldo, historico):
    extrato = ""

    for item in historico:
        extrato += f"{item}\n"

    print(f"""SALDO ATUAL R${saldo}
{"EXTRATO".center(20,"#")}
{extrato}""")

def novo_usuario(usuarios):
    cpf = input("DIGITE SEU CPF:")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Já existe um usuário com esse CPF!")
        return
    
    nome = input("DIGITE SEU NOME COMPLETO: ")
    data_nascimento = input("DIGITE SUA DATA DE NASCIMENTO: ")
    endereco = input("DIGITE SEU ENDEREÇO: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("USUARIO CADASTRADO COM SUCESSO!")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def nova_conta(AGENCIA, numero_conta, usuarios):
    cpf = input("DIGITE SEU CPF:")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("CONTA CRIADA COM SUCESSO!")
        return{"agencia": AGENCIA, "numero_conta":numero_conta, "usuario":usuario}
    
    print("USUARIO NÃO ENCONTRADO.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            AGENCIA:\t{conta["agencia"]}
            C/C: \t{conta["numero_conta"]}
            TITULAR:\t{conta["usuario"]["nome"]}
        """
        print ("="*100)
        print (linha)


main()