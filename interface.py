def linha(tam = 42):
    return '-' * tam

def titulo(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def ler_int(frase):
    try:
        valor = int(input(f'{frase}'))
    except (TypeError, ValueError):
        print('\033[31mERRO: Digite um número inteiro válido.\033[m')
    except (KeyboardInterrupt):
        print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
        return 0
    else:
        return valor


def menu(lista):
    titulo('MENU PRINCIPAL')
    i = 1
    for item in lista:
        print(f'\033[36m{i}\033[m - \033[34m{item}\033[m')
        i += 1
    print(linha())
    option = ler_int('\033[32mSua opção: \033[m')
    return option
