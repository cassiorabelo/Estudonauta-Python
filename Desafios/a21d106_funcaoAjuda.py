cores = ['\033[m',         # 0 - limpa a formatação
         '\033[30;41m',    # 1 - texto preto / fundo vermelho
         '\033[30;44m',    # 2 - texto preto / fundo azul
         '\033[30;45m',    # 3 - texto preto / fundo magenta
         '\033[7m']        # 4 - texto preto / fundo branco


fundoMagenta = '\033[45m'
textoPreto = '\033[30m'
limpaFormatacao = '\033[m'


def titulo(texto, cor=0):
    tamanho_texto = len(texto)
    print(cores[cor], end='')
    print('-' * (tamanho_texto + 4))
    print(f'  {texto}')
    print('-' * (tamanho_texto + 4))
    print(cores[0], end='')


def conteudo(comando):
    titulo(f'Acessando o manual do comando \'{comandoSolicitado}\'', 2)
    print(cores[4], end='')
    print(help(comando))
    print(cores[0])


while True:
    titulo('SISTEMA DE AJUDA', 3)
    comandoSolicitado = str(input('Digite a função ou biblioteca para ajuda ou SAIR: ')).strip().lower()
    print()
    if comandoSolicitado == 'sair':
        break
    conteudo(comandoSolicitado)
titulo('Até logo!', 1)
