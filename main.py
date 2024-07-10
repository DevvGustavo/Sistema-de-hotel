from cadastro_usuario import cadastrar_clientes
from atualizar_cadastro import atualizar_cadastro
from buscar_cadastro import busca_cadastro
from menu import cabecalho, menu, limpar
from reservas import reserva_quarto
from listagem_hospedes import hospedes_hotel
from time import sleep

def main():
    
    lista_cadastro = []
    lista_bloco_a = []
    lista_bloco_b = []
    lista_bloco_c = []

    while True:
        
        usuario = input('Quem está acessando o sistema?\nA) Administrador B) Atendente\n').upper()

        while usuario not in 'AB':
            print('Opção inválida, escolha uma das opções mostradas.')
            usuario = input().upper()
            break
        
        while usuario in 'A':
            cabecalho('Área do administrador')
            menu('Selecione um das opções a baixo:\n[1]Verificar hóspedes que estão cadastrados\n[2]Cadastro de novos quartos\n[3]Excluir quartos\n[0]Retornar ao menu principal')
            escolha = input()
            limpar()

            while escolha not in '1230':
                print('Opção inválida, escolha uma das opções mostradas.')
                escolha = input()
            
            if escolha == '0':
                print('Retornando ao menu principal...')
                print('Salvando as informações...')
                sleep(1)
                break

            elif escolha == '1':
                limpar()
                cabecalho('Área dos hospedes cadastrados no sistema')

        while usuario in 'B':
            cabecalho('Área do atendente')
            menu('Selecione um das opções a baixo:\n[1]Novo cadastro\n[2]Atualizar Cadastro\n[3]Buscar Cadastro Único\n[4]Lista de Hóspedes\n[5]Reserva de Quarto\n[6]Cancelar Reserva\n[0]Retornar ao menu principal')
            escolha = input()
            limpar()

            while escolha not in '1234560':
                print('Opção inválida, escolha uma das opções mostradas.')
                escolha = input()

            if escolha == '0':
                limpar()
                print('Retornando ao menu principal...')
                print('Salvando as informações...')
                sleep(1)
                break

            elif escolha == '1':
                limpar()
                cabecalho('Área de cadastro')
                lista_cadastro, cadastro = cadastrar_clientes(lista_cadastro)

            elif escolha == '2':
                limpar()
                cabecalho('Área para atualizar cadastro')
                lista_cadastro = atualizar_cadastro(lista_cadastro)

            elif escolha == '3':
                limpar()
                cabecalho('Área para buscar cadastro')
                busca_cadastro(lista_cadastro)

            elif escolha == '4':
                limpar()
                cabecalho('Listagem de Hóspedes')
                hospedes_hotel(lista_cadastro)

            elif escolha == '5':
                limpar()
                cabecalho('Reserva de quarto')
                lista_bloco_a, lista_bloco_b, lista_bloco_c = reserva_quarto(lista_cadastro, lista_bloco_a, lista_bloco_b, lista_bloco_c)
                print(lista_bloco_a, lista_bloco_b, lista_bloco_c)

main()