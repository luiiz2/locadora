filmes = ["interestelar", "transformes", "vingadores", "carros"]
alugados = []
opcao = 0
while opcao != 6:
    print("1 - Adicionar filme")
    print("2 - alugar filme")
    print("3 - devolver filme")
    print("4 - Listar filmes")
    print("5 - Listar filmes alugados")
    print("6 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        filme = input("Digite o nome do filme: ")
        filmes.append(filme)
    elif opcao == 2:
        filme = input("Digite o nome do filme: ")
        alugados.append(filme)
        filmes.remove(filme)
    elif opcao == 3:
        filme = input("Digite o nome do filme para devolver: ")
    elif opcao == 4:
        for filme in filmes:
            print(filme)
    elif opcao == 5:
        for filme in alugados:
            print(filme)
    elif opcao == 6:
        print("Saindo...")
    else:
        print("Opção inválida")