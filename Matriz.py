

def iniciar_lista(lista):
    for i in range(3): # estrutura de repetição para criar o tamanho da matriz (linhas)
        lista.append([]) # acrescentar uma lista vazia para cada linha
        for j in range(3): # estrutura de repetição para criar o tamanho da matriz (colunas)
            num = int(input("Linha {0}, Coluna {1}: " .format(i + 1, j + 1))) # adiciona um a i e j devido aos valores começarem em 0 em python
            lista[i].append(num)
        
        
        
    for i in range(len(lista)):
        for j in range(len(lista)):
            print(lista[i][j], end =' ')
        print()
        
        
def matriz_transposta(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            print(lista[j][i], end =' ')
        print()
        
        
        
        
        
lista = []
iniciar_lista(lista)
print('')
matriz_transposta(lista)