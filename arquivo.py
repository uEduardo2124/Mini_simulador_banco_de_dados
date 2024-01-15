from interface import *


def existe_arquivo(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[31mOcorreu um erro ao criar o arquivo, tente novamente D:\033[m')
    else:
        print(f'O aquivo {nome} foi criado com sucesso!')


def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mOcorreu um erro ao ler o arquivo, tente novamente\033[m')
    else:
        titulo('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastro(arq, nome = 'desconhecido', idade = 0):
    try:
        a = open(arq, 'at')
    except:
        print('\033[31mOcorreu um erro na abertura do arquivo\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31mOcorreu um erro durante a escrita dos dados\033[m')
        else:
            print(f'Novo registro de {nome} com idade de {idade} anos adicionado com sucesso!')
            a.close()
