import os


# funcao para dar entrada no parque, tendo como param a variavel parqueque faz a ligacao a lista
def entrada(parque):
    # iteração pelo numero de filas
    for i in range(filas):
        # iteracao pelo numero de lugares
        for j in range(lugares):
            # condicao para avaliar se está vazio, caso esteja...
            if (parque[i][j] == 0):
                # ... ocupamos o lugar
                parque[i][j] = 1
                # print para informar a posição ocupada pelo user
                print("O lugar está ocupado: fila{0}, lugar{1}." .format(i + 1, j + 1))
                # devolvemos o estado do parque
                return parque
    # na condicao de o parque estar cheio informamos o user
    print("O parque está cheio.")
    return parque


# funcao de saida do parque
def saida(parque):
    # estrutura try except para avaliarmos as condicoes dos lugares e filas atraves do input
    try:
        saidaFila = int(input('Qual é a fila que quer sair: '))
        saidaLugar = int(input('Qual é o lugar que quer sair: '))
        # se os valores inseridos forem maiores do que as filas ou lugares deverá apresentar um erro
        if saidaFila > filas:
            raise ValueError()
        if saidaLugar > lugares:
            raise ValueError()
    
    # excepcao para o caso de os valores inseridos nao serem validos
    except :
        print('O lugar ou fila inseridos não são válidos!')
        
    # estrutura de condicao para verificar se o lugar esta ocupado
    else:
        if [saidaFila-1][saidaLugar-1] == 0:
            print('O lugar não está ocupado')
        else:
            parque[saidaFila-1][saidaLugar-1] = 0
            print("O lugar foi desocupado") 
    return parque
            
            


def estado(parque):
    # variaveis para contagem de lugares livres e ocupados
    livres = 0
    ocupados = 0
    
    # ciclos iterativos para percorrermos as posições e sabermos o respectivo valor
    for i in range(filas):
        for j in range(lugares):
            # estrutura de condição para perceber se as linhas e as colunas tem ou não vaga
            if (parque[i][j] == 0):
                # incrementação da variavel de contagem por o parque ter vaga
                livres += 1
            else:
                # incrementação da variavel de contagem por o parque não ter vaga
                ocupados += 1
    
    # prints das informações do parque ter
    print('\tEstado do Parque:')
    print("\t\tO parque contém {0} lugares livres." .format(livres))
    print('\t\tO parque contém {0} lugares ocupados.' .format(ocupados))
    print("")



def criar_parque():
    # lista vazia para dar início a criação do parque
    lista = []
    # ciclo iterativo para as filas do parque
    for i in range(filas):
        # acrescentamos campos vazios para mais tarde acrescentar
        lista.append([])
        # ciclo iterativo para os lugares do parque
        for j in range(lugares):
            # acrescentamos a uma linha a cada coluna
            lista[i].append(0)
    return lista


filas = 3
lugares = 5
parque = criar_parque()


# Menu
# Iniciação do menu

# condição vazia por não sabermos a resposta
opcao = " "

# ciclo while para corrermos a estrutura repetitiva enquanto a opcao selcionada nao for 0, porque 0 implica sair do programa
while opcao != "0":
    os.system('clear')
    print("\tMenu")
    print("\tInsira as opções do Menu: ")
    print("1 - Entrada de veículo")
    print("2 - Saída de veículo")
    print("3 - Estado do Parque")
    print("0 - Sair")
    opcao = input('Insira uma das opções: ')
    if opcao == "1":
        entrada(parque)
    elif opcao == "2":
        saida(parque)
    elif opcao == "3":
        estado(parque)    
    input()



