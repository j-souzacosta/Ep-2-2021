vitoria = True
loop = True 
#Loop para o jogo continuar rodando ate nao houver mais possibilidades de movimento
while loop:

    baralho = cria_baralho()
    embaralhado = embaralha_baralho(baralho)

    #Loop para o jogo continuar rodando ate o tamanho do baralho ser igual a 1
    while len(embaralhado) > 1:
        for i,carta in enumerate(embaralhado):
            print(f'{i + 1}. {colore_carta(carta)}')

        movimentos_possiveis = verifica_movimentos_possiveis(embaralhado)
        print('Quantidade de movimentos possiveis: {0}'.format(len(movimentos_possiveis)))
        