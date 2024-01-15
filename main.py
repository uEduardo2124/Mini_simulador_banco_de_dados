from time import sleep
from arquivo import *

arq = 'documento.txt'

if not existe_arquivo(arq):
    criar_arquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])

    if resposta == 1:
        ler_arquivo(arq)
    elif resposta == 2:
        titulo('NOVO CADASTRO')
        nome = str(input('Nome:  '))
        idade = ler_int('Idade: ')
        cadastro(arq, nome, idade)
    elif resposta == 3:
        titulo('Saindo do sistema. Até logo!')
        break
    else:
        print('\033[31mERRO: Digite uma opção válida!\033[m')
    sleep(0.5)
