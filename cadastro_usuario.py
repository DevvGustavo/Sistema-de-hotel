from cpf_unico import verificar_cpf

def cadastrar_clientes(lista_cadastro):
    '''
    Cadastro do Cliente e sendo guardada na lista
    '''
    from reservas import reserva_quarto
    
    print('Se quiser retornar ao menu digite: sair')

    while True:
        
        try:    
            quantidade_de_usuarios = int(input('Digite quantos úsuarios serão cadastrados: '))
            break

        except ValueError:
            print('ERRO, não é possivel digitar nada além de números...')
        

    for c in range(quantidade_de_usuarios):
            
        cadastro = {}
        
        nome = input('Nome do Cliente: ').capitalize()
        if nome == 'Sair':
            print('retornando para o menu...')
            break

        idade = input('Idade do Cliente: ').capitalize()
        if idade == 'Sair':
            print('retornando para o menu...')
            break

        cpf = input('CPF do Cliente: ').capitalize()
        if cpf == 'Sair':
            print('retornando para o menu...')
            break

        contato = input('Contato do Cliente: ').capitalize()
        if contato == 'Sair':
            print('retornando para o menu...')
            break


        if idade.isnumeric() == True and cpf.isnumeric() == True and contato.isnumeric() == True:
            cpf_int = int(cpf)
            contato_int = int(contato)
            idade_int = int(idade)
        
        cadastro['NOME'] = nome
        cadastro['IDADE'] = idade_int
        cadastro['CPF'] = cpf_int
        cadastro['CONTATO'] = contato_int
        
        if verificar_cpf(lista_cadastro, cadastro) == False:
            lista_cadastro.append(cadastro)

        else:
            print('-------------------')

            print('usuario ja existente')
        

    return lista_cadastro, cadastro

