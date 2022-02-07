import functions as fc
from mainclass import DataHandler
from tqdm import tqdm

# - programa principal -
arquivo = r"C:\Games\parrot\dicionarios\Nova pasta (2)\Top2Billion-probable-v2.txt"

dado = 10000000
n = fc.count_lines(arquivo, 1973218846, 'ansi')
n1 = 113 * 10000000
vezes = 197 - 111

for c in tqdm(range(vezes), 'Progresso Geral', unit='packets', colour='cyan'):
    if n == 0:
        break
    resultado = fc.getlines(arquivo, n1, dado, 'ansi')
    filtrado = fc.data_filter(resultado, 8)
    fc.escrever_dados('resultado_sup_2.txt', filtrado)
    resultado.clear
    filtrado.clear
    n -= dado
    n1 += dado

print('fim')

# - input -
# arquivo
# codec

# - output -
# arquivo
# codec

# - options -
# numero de linhas
dh = DataHandler()
dh.input_parameter(arquivo, 'utf8')
print(dh.in_arquivo)