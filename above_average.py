
def aboveAverage(inteiros):
    media = sum(inteiros) / len(inteiros)       
    count = 0
    for i in range(len(inteiros)):
        if inteiros[i] > media:
            return count
    
    
        
inteiros = []
for i in range(10):
    num = int(input('Insira um numero: '))
    inteiros.append(num)
count = aboveAverage(inteiros)

print('Média: {0}' .format(count))
input()