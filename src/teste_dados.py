def getlines(arquivo, linha_inicio, quatidade_linha, encoding='utf8'):
    """-> Permite buscar em um arquivo de texto gigante de até mais de 20gb sem exceder a memoria ram,
    e armazenar uma certa quantidade de dados #por linhas em forma de uma lista.
    
    arquivo(str) = diretório onde o arquivo se encontra

    linha_inicio(int) = o numero da linha onde vai iniciar a captura de dados.
    
    quantidade_linha(int) = quantidade de dados por linha que vai ser capturado após o linha_inicio.
    
    encoding(str) = codificação ex: 'utf8' etc.
    
    return(list) = [dados] """

    resultado = list()
    print('Procurando linha...')
    with open(arquivo, encoding=encoding) as dicionario:
        flag = False
        end_line = linha_inicio + (quatidade_linha - 1)
        for i, line in enumerate(dicionario):
            if i == linha_inicio:
                print('Capturando linhas, aguarde...')
                flag = True
            if flag:
                resultado.append(line.strip())
                if i == end_line:
                    print('Captura concluida.')
                    return resultado


def escrever_dados(arquivo, lista_dados, encoding='utf8'):
    """ Escreve dados em um novo arquivo de texto
    
    arquivo(str) = diretório onde o arquivo se encontra
    
    lista_dados(list) = lista que será colocada no arquivo
    
    encoding(str) = codificação ex: 'utf8' etc."""

    from tqdm import tqdm
    from time import sleep

    try:
        with open(arquivo, 'a', encoding=encoding) as f_obj:
            for d in tqdm(lista_dados, 'Escrevendo Dados', unit='lines', colour='green'):
                f_obj.write(d + '\n')      
    except FileNotFoundError:
        print(f'Arquivo ({arquivo}) não encontrado, criando arquivo...')
        sleep(1.5)
        print(f'Arquivo ({arquivo}) criado com sucesso!')
        with open(arquivo, 'w', encoding='utf8') as f_obj:
            for d in tqdm(lista_dados, 'Escrevendo Dados', unit='lines', colour='green'):
                f_obj.write(d + '\n')


def count_lines(arquivo, numb_linhas=0, encoding='utf8'):
    """ faz contagem de linhas de um arquivo """

    from tqdm import tqdm

    with open(arquivo, encoding=encoding) as dicionario:
        count = numb_linhas
        if count > 0:
            print(f'Adicionado contagem de linhas manual, numero de linhas: {count}')
            return count
        else:
            for i, line in tqdm(enumerate(dicionario), 'Captando linhas', unit='lines'):
                count += 1
            print(f'O arquivo possui {count} linhas.')
            return count


def data_filter(data_list, totchar_numb=8):
    """ - filtra palavras por numero de caracteres -
    data_list(list) = recebe lista que deseja filtrar
    
    totchar_numb(int) = numero minimo de caracteres
    
    return = retorna lista(list) com o resultado """
    
    from tqdm import tqdm

    result = list()
    text = f'Filtrando palavras com {totchar_numb} caracteres'
    for data in tqdm(data_list, text, colour='red'):
        c = 0
        for d in data:
            c += 1
        if c < totchar_numb:
            None
        else:
            result.append(data)
    return result


# - programa principal -
from tqdm import tqdm

arquivo = r"C:\Games\parrot\dicionarios\Nova pasta (2)\Top2Billion-probable-v2.txt"

dado = 10000000
n = count_lines(arquivo, 1973218846, 'ansi')
n1 = 113 * 10000000
vezes = 197 - 111

for c in tqdm(range(vezes), 'Progresso Geral', unit='packets', colour='cyan'):
    if n == 0:
        break
    resultado = getlines(arquivo, n1, dado, 'ansi')
    filtrado = data_filter(resultado, 8)
    escrever_dados('resultado_sup_2.txt', filtrado)
    resultado.clear
    filtrado.clear
    n -= dado
    n1 += dado

print('fim')
