def cabecalho(msg):
    '''Só faz a digitação de linhas para deixar o cabeçalho bonito '''

    print(50 * '-')
    print(msg)
    print(50* '-')


def linha():
    ''' Mostra as linhas '''

    print(50 * '-')


def menu(opcoes):
    ''' Faz parte do menu principal '''

    print(opcoes)
    print(50 * '-')


def limpar():
    '''Limpa o terminal'''
    import os
    os.system('cls' if os.name == 'nt' else 'clear')