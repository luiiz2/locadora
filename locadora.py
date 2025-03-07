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
        while True:
            filme = input("Digite o nome do filme: ")
            while filme in filmes:
                print("Filme já cadastrado")
                filme = input("Digite o nome do filme: ")
            filmes.append(filme)
            print("Filme adicionado com sucesso")
            continuar = input("Deseja adicionar outro filme? (s/n) ")
            if continuar == "n":
                break
    elif opcao == 2:
        filme = input("Digite o nome do filme: ")
        tentativa = 0
        while filme not in filmes:
            print("Filme não cadastrado")
            tentativa += 1
            filme = input("Digite o nome do filme: ")
            if tentativa > 3:
                print("Número de tentativas excedido")
                break
        else:
            alugados.append(filme)
            filmes.remove(filme)
            print("Filme alugado com sucesso")
    elif opcao == 3:
        filme = input("Digite o nome do filme para devolver: ")
        while filme not in alugados:
            print("Filme não alugado")
            filme = input("Digite novamente o nome do filme para devolver: ")
            tentativa += 1
            if tentativa > 3:
                print("Número de tentativas excedido")
                break
        else:
            alugados.remove(filme)
            filmes.append(filme)
            print("Filme devolvido com sucesso")
    elif opcao == 4:
        for filme in filmes:
            if len(filmes) == 0:
                print("Não há filmes cadastrados")
            else:
                print(filme)
    elif opcao == 5:
        for filme in alugados:
            if len(alugados) == 0:
                print("Não há filmes alugados")
            else:
                print(filme)
    elif opcao == 6:
        print("Saindo...")
    else:
        print("Opção inválida")
