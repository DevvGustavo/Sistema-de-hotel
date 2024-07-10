
def verificar_cpf(lista_cadastro, cliente):
    '''
    verificar se o cpf ja esta cadastrado
    '''

    for c in lista_cadastro:
        if c['CPF'] == cliente['CPF']:
            return True
        
    return False
        