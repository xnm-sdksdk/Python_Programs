# lista para dias da semana
dias_semana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']


def diaSemana(maior_visitas):
    maior = max(maior_visitas)
    pos = maior_visitas.index(maior)
    dia = dias_semana[pos]
    return dia




# lista para o maior numero de visitantes
maior_visitas = []

for i in range(len(dias_semana)):
    verdade = False
    while not verdade:
        try:
            visitantes = int(input('Visitantes no/a {0}: ' .format(dias_semana[i])))
            maior_visitas.append(visitantes)
            if visitantes < 0 or  visitantes > 100:
                raise ValueError
        except ValueError:
            print('Valor inserido contém um erro!')
        else:
            verdade = True
            
            
        
            


afluencia = diaSemana(maior_visitas)
print('Dia da semana mais distante da média: ', afluencia)

input()