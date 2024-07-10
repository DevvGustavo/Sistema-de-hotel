def reserva_quarto(lista_cadastro, lista_bloco_a, lista_bloco_b, lista_bloco_c):
    
    from cadastro_usuario import cadastrar_clientes
    cadastro = {}
    pergunta = input('Cliente novo[1] ou ja existente[2]? ')
    # caso cadastro não exista
    if pergunta == '1':
        cadastrar_clientes(lista_cadastro)
    
    # caso cadastro já exista
    elif pergunta == '2':
        busca = int(input('Digite o CPF do usuário: '))
        for busca_cpf in lista_cadastro:

            if busca == busca_cpf['CPF']:
                print(busca_cpf)
                cadastro = busca_cpf

        qual_quarto = input('Qual será o quarto reservado? ').upper()
        qual_bloco = input('Qual será o bloco reservado? ').upper()

        cadastro['QUARTO'] = qual_quarto
        cadastro['BLOCO'] = qual_bloco

        if qual_bloco == 'A':
            lista_bloco_a.append(cadastro)

        elif qual_bloco == 'B':
            lista_bloco_b.append(cadastro)

        elif qual_bloco == 'C':
            lista_bloco_c.append(cadastro)

    return lista_bloco_a, lista_bloco_b, lista_bloco_c
