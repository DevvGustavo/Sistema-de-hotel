import json

def salvar_arquivo(lista_cadastro):

    clientes = 'dados_dos_cliente'
    with open(clientes, 'w') as arquivo_de_clientes:
        json.dump(lista_cadastro, arquivo_de_clientes, indent = 4)

def ler_clientes(lista_cadastro):
    try:
        clientes = 'dados_dos_clientes'
        with open(clientes, 'r') as arquivo_cliente:
        
            lista_cadastro = json.load(arquivo_cliente)
    
    except FileNotFoundError:
        print('Arquivo não existente')

    except Exception as e:
        print(f'Error: {e}')

    finally:
        return lista_cadastro