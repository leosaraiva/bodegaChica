def main():

    bodega = {}

    def cadastrarCliente():
        nome = str(input("Digite o nome do cliente: ")).upper()
        dividaValor = float(input("Digite o valor devido: R$"))
        telefoneNumero = str(input("Digite o telefone: "))
        enderecoInfo = str(input("Digite o endereço: ")).capitalize()
        bodega.update({nome: {'Deve: ': dividaValor, 'Telefone: ': telefoneNumero, 'Endereço: ': enderecoInfo}})

    def mostrarCliente():
        print("Lista dos caloteiros: ")
        for k, v in bodega.items():
            print(f"{k} - {v}")
       # print("teste de lista")
       # print(bodega)

    def removerCliente():
        busca = str(input("Digite nome a retirar: ")).upper()
        if busca in bodega.keys():
            print(f"{busca.capitalize()} pagou a bodega!")
            bodega.pop(busca)

    def procurarCliente():
        busca = str(input("Digite nome a buscar: ")).upper()
        if busca in bodega.keys():
            print(f"{busca.capitalize()} está devendo!")

        else:
            print(f"{busca.capitalize()} não está devendo.")

    def alterarNome(dado):
        novoNome = str(input("Digite o novo nome da pessoa: ")).upper()
        bodega[dado] = novoNome

    def alterarValor(dado):
        novoValor = float(input("Digite o novo valor do fiado: R$"))
        if novoValor <= 0:
            bodega.pop(dado)
        else:
            bodega[dado]['Deve: '] = novoValor

    def alterarTelefone(dado):
        novoTelefone = str(input("Digite o novo telefone: "))
        bodega[dado]['Telefone: '] = novoTelefone

    def alterarEndereco(dado):
        novoEndereco = str(input("Digite o novo endereço: "))
        bodega[dado]['Endereço: '] = novoEndereco

    def menuAlterar():
        while True:
            submenu = str(input(
                "O que deseja fazer? \n(1) listar caloteiro(a)s / (2) alterar nome / (3) alterar valor / "
                "(4) alterar telefone / (5) alterar endereço / (6) sair\n"))
            if submenu == "1":
                mostrarCliente()
            elif submenu == "2":
                dado = str(input("Diga o nome do(a) caloteiro(a): ")).upper()
                alterarNome(dado)
            elif submenu == "3":
                dado = str(input("Diga o nome do(a) caloteiro(a): ")).upper()
                alterarValor(dado)
            elif submenu == "4":
                dado = str(input("Diga o nome do(a) caloteiro(a): ")).upper()
                alterarTelefone(dado)
            elif submenu == "5":
                dado = str(input("Diga o nome do(a) caloteiro(a): ")).upper()
                alterarEndereco(dado)
            elif submenu == "6":
                break
            else:
                print("Digite um valor válido!\n")

    print("=== Bodega da Dona Chica ===\n Lista dos caloteiros\n ")
    while True:
        menu = str(input("O que deseja fazer? (1) cadastrar / (2) procurar / (3) alterar / (4) remover / (5) sair: \n"))
        if menu == "1":
            cadastrarCliente()
        elif menu == "2":
            procurarCliente()
        elif menu == "3":
            menuAlterar()
        elif menu == "4":
            removerCliente()
        elif menu == "5":
            print("Valeu aí por comprar na bodega.")
            break
        else:
            print("Digite um valor válido!\n")


main()
