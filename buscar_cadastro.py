def busca_cadastro(lista_cadastro):
    
    busca = int(input('Digite o CPF do usuário: '))

    for busca_cpf in lista_cadastro:

        if busca == busca_cpf['CPF']:
            print(busca_cpf)
            