print('Bem vindo ao controle de estoque de bicicletaria do Vinicius Alfonso')
# Função para cadastrar uma peça
def cadastrarPeca(codigo):
    print('Você selecinou a opção de Cadastrar peça')
    print(f'O codigo da peça é {contador}')
    nome = input("Nome da peça: ")
    fabricante = input("Fabricante da peça: ")
    valor = float(input("Valor da peça: "))
    peca = {"codigo": codigo, "nome": nome, "fabricante": fabricante, "valor": valor}
    return peca

# Função para consultar peças
def consultarPeca(pecas):
    print('Voce selecionou a opção de consultar peça')
    while True:
        print("\nOpções de consulta:")
        print("1. Consultar todas as peças")
        print("2. Consultar peças por código")
        print("3. Consultar peças por fabricante")
        print("4. Retornar")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            for peca in pecas:
                print(peca)
        elif opcao == 2:
            codigo = int(input("Digite o código da peça: "))
            for peca in pecas:
                if peca["codigo"] == codigo:
                    print(peca)
        elif opcao == 3:
            fabricante = input("Digite o nome do fabricante: ")
            for peca in pecas:
                if peca["fabricante"] == fabricante:
                    print(peca)
        elif opcao == 4:
            break
        else:
            print("Opção inválida.")

# Função para remover uma peça
def removerPeca(pecas):
    print('Voce selecionou a opção de Remover peça')
    codigo = int(input("Digite o código da peça que deseja remover: "))
    for i, peca in enumerate(pecas):
        if peca["codigo"] == codigo:
            del pecas[i]
            print("Peça removida.")
            return
    print("Peça não encontrada.")

# Programa principal
pecas = []
contador = 1

while True:
    print("\nMenu:")
    print("1. Cadastrar peça")
    print("2. Consultar peça")
    print("3. Remover peça")
    print("4. Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        peca = cadastrarPeca(contador)
        pecas.append(peca)
        contador += 1
        print("Peça cadastrada com sucesso.")
    elif opcao == 2:
        consultarPeca(pecas)
    elif opcao == 3:
        removerPeca(pecas)
    elif opcao == 4:
        break
    else:
        print("Opção inválida.")

