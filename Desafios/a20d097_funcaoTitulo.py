def titulo(conteudo):
    tamanho_conteudo = len(conteudo)
    print('~' * (tamanho_conteudo + 4))
    print(f'  {conteudo}')
    print('~' * (tamanho_conteudo + 4))


tituloInformado = str(input('Texto para o título: '))
titulo(tituloInformado)
