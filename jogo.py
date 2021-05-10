import bibliotecas

vitoria = True
loop = True 
#Loop para o jogo continuar rodando ate nao houver mais possibilidades de movimento
while loop:

    baralho = bibliotecas.cria_baralho()
    embaralhado = bibliotecas.embaralha_baralho(baralho)

    #Loop para o jogo continuar rodando ate o tamanho do baralho ser igual a 1
    while len(embaralhado) > 1:
        for i,carta in enumerate(embaralhado):
            print(f'{i + 1}. {bibliotecas.colore_carta(carta)}')

        movimentos_possiveis = bibliotecas.verifica_movimentos_possiveis(embaralhado)
        print('Quantidade de movimentos possiveis: {0}'.format(len(movimentos_possiveis)))
        
        if len(movimentos_possiveis) == 0 and len(embaralhado) > 1:
            vitoria = False
            break   
        
        carta= int(input(f'Escolha uma carta (Digite um numero de 1 a {len(embaralhado)}): ')) - 1        
        
        while carta >= len(embaralhado) or carta < 1:
            print('Numero invalido')
            carta= int(input(f'Escolha outra carta (Digite um numero de 1 a {len(embaralhado)}): ')) - 1

        lista_mov = []
        lista_mov = bibliotecas.lista_movimentos_possiveis(embaralhado,carta)
        destino = 0 
        
        while len(lista_mov) == 0:
            print('Essa carta nao pode ser movida')
            carta= int(input(f'Escolha outra carta (Digite um numero de 1 a {len(embaralhado)}): ')) - 1
            lista_mov = bibliotecas.lista_movimentos_possiveis(embaralhado,carta)
        
