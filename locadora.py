from operacoesbd import *

conexao = criarConexao("localhost", "root", "senha", "locadora")

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
            inserirfilme = input("Digite o nome do filme: ")
            dados = [inserirfilme]
            comandofilme = "INSERT INTO filmes (nome) VALUES (%s)"
            if len(listarBancoDados(conexao, "SELECT * FROM filmes WHERE nome = %s", dados)) > 0:
                print("Filme já cadastrado")
            else:
                insertNoBancoDados(conexao, comandofilme, dados)
                print("Filme cadastrado com sucesso")   
    elif opcao == 2: 
        filme = input("Digite o nome do filme que deseja alugar: ")
        dados = [filme]
        if len(listarBancoDados(conexao, "SELECT * FROM filmes WHERE nome = %s", dados)) == 0:
            print("Filme não cadastrado")
            break
        else:
            comandoinserir = "INSERT INTO alugados (nome) VALUES (%s)"
            insertNoBancoDados(conexao, comandoinserir, dados)
            comandoexcluir = "DELETE FROM filmes WHERE nome = %s"
            excluirBancoDados(conexao, comandoexcluir, dados)  
            print("Filme alugado com sucesso")
    elif opcao == 3:
        filme = input("Digite o nome do filme para devolver: ")
        dados = [filme]
        if len(listarBancoDados(conexao, "SELECT * FROM alugados WHERE nome = %s", dados)) == 0:
            print("Filme não alugado")
            break
        else:
            comandoinserir = "INSERT INTO filmes (nome) VALUES (%s)"
            insertNoBancoDados(conexao, comandoinserir, dados)
            comandoexcluir = "DELETE FROM alugados WHERE nome = %s"
            excluirBancoDados(conexao, comandoexcluir, dados)
            print("Filme devolvido com sucesso")
        
    elif opcao == 4:
                listarfilmes = "SELECT * FROM filmes"
                listagem = listarBancoDados(conexao, listarfilmes)
                if len(listagem) == 0:
                    print("Não há filmes cadastrados")
                else:       
                    print("lista de filmes")
                    contagem = 0
                    for filme in listagem:
                        contagem += 1
                        print(contagem, filme[0])
    elif opcao == 5:
        listaralugados = "SELECT * FROM alugados"
        listagem = listarBancoDados(conexao, listaralugados)
        if len(listagem) == 0:
            print("Não há filmes alugados")
        else:
            print("lista de filmes alugados")
            contagem = 0
            for filme in listagem:
                contagem += 1
                print(filme[0])
    elif opcao == 6:
        print("Saindo...")
        encerrarConexao(conexao)
    else:
        print("Opção inválida")
