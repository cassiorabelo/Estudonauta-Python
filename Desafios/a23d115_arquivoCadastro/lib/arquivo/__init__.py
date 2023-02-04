from Desafios.a23d115_arquivoCadastro.lib.interface import *
from time import sleep

def inicializar_arquivo():
    try:
        open('cadastros.txt', 'r')
    except FileNotFoundError:
        cadastros = open('cadastros.txt', 'a')
        cadastros.write('nome;idade')
        cadastros.close()
    except:
        print('\033[31mFalha na leitura ou criação do arquivo de cadastros.\033[m')


def menu():
    while True:
        sleep(1)
        titulo('Menu')
        print(f'\033[34m1\033[m Consultar cadastros')
        print(f'\033[34m2\033[m Novo cadastro')
        print(f'\033[34m3\033[m Sair do sistema')
        try:
            opcao = int(input('\nOpção: '))
        except (TypeError, ValueError):
            print('\033[31mOpção inválida\033[m')
            continue
        sleep(1)
        if opcao == 1:
            consultar_cadastros()
            continue
        elif opcao == 2:
            titulo('Novo cadastro')
            novo_cadastro()
            print('\033[32mCadastro realizado com sucesso!\033[m')
            continue
        elif opcao == 3:
            print(f'\n{" Fim ":-^50}')
            break
        print('\033[31mOpção inválida\033[m')


def consultar_cadastros():
    titulo('Pessoas cadastradas')
    try:
        consulta = open('cadastros.txt', 'r')
    except:
        print("\033[31mErro ao ler o arquivo.\033[m")
    else:
        for indice, cadastro in enumerate(consulta):
            dado = cadastro.split(';')
            if indice > 0:
                dado[1] = dado[1].replace('\n', '')
                print(f'  {dado[0]:<38}{dado[1]:>3} anos  ')
    finally:
        consulta.close()


def novo_cadastro():
    cadastros = open('cadastros.txt', 'a')
    nome = str(input('Nome: '))
    idade_validada = False
    idade = 0
    while not idade_validada:
        try:
            idade = int(input('Idade: '))
        except (TypeError, ValueError):
            print('\033[31mValor inválido. Por favor, digite um número inteiro.\033[m')
            continue
        idade_validada = True
    cadastros.write(f'\n{nome};{idade}')
    cadastros.close()
