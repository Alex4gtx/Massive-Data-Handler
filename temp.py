import src.functions as fc
from tqdm import tqdm

arquivo = r"C:\Users\geova\OneDrive\Documentos\Alex\resultado_sup.txt"

tot_lines = fc.count_lines(arquivo, 991386048)
divx = 11
div_lines = tot_lines/divx
init_line = 0
qline = 20000000

# novos arquivos
fm = 0
for na in tqdm(range(divx)):
    narquivo = 'out_arq_' + str(fm) + '.txt'
    for n in range(5):
        captured = fc.getlines(arquivo, init_line, qline)
        fc.escrever_dados(narquivo, captured)
        captured.clear
        init_line += qline
    fm += 1
