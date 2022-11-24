import os

def maior_faturacao(facturacao):
    # return devolve algo, index devolve a posição especificada neste caso o max da lista facturacao
    return meses[facturacao.index(max(facturacao))]





def menor_faturacao(facturacao):
    return meses[facturacao.index(min(facturacao))]




def media_faturacao(facturacao):
    # somar os valores dividir pelo comprimento dos meses
    return sum(facturacao) / len(meses)
 


#lista com os meses a iterar
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro','Novembro','Dezembro']
# lista com os valores a serem inseridos
facturacao = []

# Iterar pelos meses de modo a no print ser possível inserir os valores de cada mes
for i in range(len(meses)):    
    print('Facturação do mês {0} :  ' .format(meses[i])) # print para a consola de cada mês sucessivamente
    valores = int(input('' .format(facturacao))) # input dos valores da facturação
    facturacao.append(valores) # append na lista da facturacao os respectivos valores


# limpar o ecrã    
os.system('clear')
print('O Mês de maior facturação: ', maior_faturacao(facturacao))
print('O Mês de menor facturação: ', menor_faturacao(facturacao))
print('O valor médio de facturação: ', media_faturacao(facturacao))
input()




