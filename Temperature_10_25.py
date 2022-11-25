import random
from datetime import datetime
import time

def saveFile(linha):
    
    # abrir o ficheiro em modo append, se não existir o ficheiro é criado
    fileCreate = open("temperature.txt", 'a')
    # escrita no ficheiro com o param passado
    fileCreate.write(linha)
    # close do file para não crashar o programa
    fileCreate.close()



print("\t\tData   \t\t   Hora  \tTemperatura")
print("\t\t-----------------------------------------")

# param para definir o principio de funcionamento do ciclo while
end = False
# ciclo while iterativo que vai correr enquanto a condição acima for Falsa
while not end:
    # gerar numeros aleatorios entre 10 e 25
    temperature = random.randint(10,25)
    data = datetime.now().date()
    hora = datetime.now().time().strftime("%H-%M-%S")
    print("\t\t", data , "\t", hora , "\t", temperature )
    linha = str(data) + ";" + str(hora) + ";" + str(temperature) + "\n"
    saveFile(linha)
    time.sleep(1)
    


