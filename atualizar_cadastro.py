def atualizar_cadastro(lista_cadastro):
    print(lista_cadastro)
    
    while True:
        try:
            pergunta = input('Deseja atualizar o cadastro de qual cliente? ')
        
        except ValueError:
                print('ERRO,nesta aba só é permitido números inteiros\nDigite novamente')

        if pergunta.isnumeric() == True:
            pergunta_int = int(pergunta)
            break
        
    # Verificar se o cliente está na lista
    cliente_encontrado = None
    for cliente in lista_cadastro:
        if pergunta_int == cliente['CPF']:
            cliente_encontrado = cliente
            break
    
    if not cliente_encontrado:
        print('Cliente não encontrado.')
        return lista_cadastro
    
    print('Selecione uma das opções abaixo:\n[1]Atualizar Nome\n[2]Atualizar Idade\n[3]Atualizar CPF\n[4]Atualizar Contato')
    atualizacao = input()
    
    if atualizacao == '1':
        novo_nome = input('Para qual nome deseja atualizar? ')
        cliente_encontrado['NOME'] = novo_nome
        print('Atualização realizada com sucesso!')
    
    elif atualizacao == '2':
        nova_idade = input('Para qual idade deseja atualizar? ')
        cliente_encontrado['IDADE'] = nova_idade
        print('Atualização realizada com sucesso!')
    
    # elif atualizacao == '3':
    #     novo_cpf = input('Digite o novo CPF: ')
    #     cliente_encontrado['CPF'] = novo_cpf
    #     print('Atualização realizada com sucesso!')
    
    elif atualizacao == '4':
        novo_contato = input('Digite o novo contato: ')
        cliente_encontrado['CONTATO'] = novo_contato
        print('Atualização realizada com sucesso!')
    
    else:
        print('Opção inválida.')
    
    print('Lista atualizada de cadastros:', lista_cadastro)

    return lista_cadastro
