
mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

def pluviosidade(pluv):
    pluv.sort()
    pluv.reverse()
    for i in range(12):
        print(pluv[i])
    
    
    
def pluviosidade_v2(pluv):
    lista_ordenada = pluv.copy()
    lista_ordenada.sort(reverse = True)
    for i in range(12):
        position = pluv.index(lista_ordenada[i])
        print('\t', mes[position], '\t', lista_ordenada[position])
        pluv[position] = -1 
       
        
    

pluv = []

for i in range(12):
    valor = int(input('Pluviosidade no mês de {0} \t: ' .format(mes[i])))
    pluv.append(valor)
print("\n\n")


pluviosidade(pluv)
pluviosidade_v2(pluv)
input()