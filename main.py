import sys
import os

from SimuladordeProcessos import *

def converte_entrada(entrada):
    entrada = entrada.replace("\n", "")
    entrada = entrada.split(" ")
    entrada = map(int, entrada)
    entrada = tuple(entrada)
    return entrada

def main():

    entrada = sys.stdin.readlines()
    processos = map(converte_entrada, entrada)

    simuladordeProcessos = SimuladordeProcessos()
    simuladordeProcessos_result = SimuladordeProcessos.execute(processos, 10)

    saida_simuladordeProcessos = "SimuladordeProcessos {0} {1} {2} {3} {4} {5} {6} {7} {8} {9} "
    saida_simuladordeProcessos = saida_simuladordeProcessos.format(simuladordeProcessos_result[0], simuladordeProcessos_result[1], simuladordeProcessos_result[2], simuladordeProcessos_result[3], simuladordeProcessos_result[4], simuladordeProcessos_result[5] simuladordeProcessos_result[6], simuladordeProcessos_result[7], simuladordeProcessos_result[8] simuladordeProcessos_result[9])

    saida ="{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n{7}\n{8}n\{9}"

    print(saida.format(saida_simuladordeProcessos))

    path = 'C:\\Users\\Usuario\\OneDrive\\Documentos'
    simuladordeProcessos = os.listdir(path)
    with open('resultadoProcesso.txt', 'w') as arquivo:
     arquivo.write("n".join(simuladordeProcessos))
     arquivo.write(f'\nTotal de arquivos {len(simuladordeProcessos)}')
       

     if __name__ == '__main__':
      main()
    



