import random

#Funcao para criar baralho:
def cria_baralho():
    faces = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    naipes = ['♠','♥','♦','♣']
    baralho = []
    i=0
    while i < len(faces):
        item = faces[i]
        j=0
        while j < len(naipes):
            naipe = naipes[j]
            carta = item + naipe
            baralho.append(carta)
            j+=1
        i+=1
    return baralho

#Embaralhar as cartas do baralho:
def embaralha_baralho(baralho):
    embaralhado=[]
    while len(embaralhado) < len(baralho):
        carta = random.choice(baralho)
        if carta not in embaralhado:
            embaralhado.append(carta)
    return embaralhado

#Funcao para colorir o baralho:
def colore_carta(carta):
    naipe = extrai_naipe(carta)
    carta_colorida = ''
    if naipe == '♠':
        carta_colorida  = '\033[34m' + carta + '\033[0m'
    elif naipe == '♥':
        carta_colorida  = '\033[31m' + carta + '\033[0m'
    elif naipe == '♦':
        carta_colorida  = '\033[32m' + carta + '\033[0m'
    elif naipe == '♣':
        carta_colorida  = '\033[33m' + carta + '\033[0m'
        
    return carta_colorida

#Funcao para extrair naipe da carta   
def extrai_naipe(carta):
    return carta[-1]

#Funcao para extrair VALOR da carta:
def extrai_valor(carta):
    return carta[ :-1]

#Funcao para listagem dos movimentos possiveis:
def lista_movimentos_possiveis(list1,i):
    lista=[]
    j=0
    while j < len(list1):
        item=str(list1[j])
        lista.append(item)
        j+=1

    lista_mov = []
    if i < 3:
        if i == 0:
            return lista_mov
        elif i == 1:
            if extrai_valor(lista[1]) == extrai_valor(lista[0]) or extrai_naipe(lista[1]) == extrai_naipe(lista[0]):
                lista_mov.append(1)
            return lista_mov
        elif i == 2:
            if extrai_valor(lista[1]) == extrai_valor(lista[2]) or extrai_naipe(lista[1]) == extrai_naipe(lista[2]):
                lista_mov.append(1)
            return lista_mov
    else:
        if extrai_valor(lista[i]) == extrai_valor(lista[i-1]) or extrai_naipe(lista[i]) == extrai_naipe(lista[i-1]):
            lista_mov.append(1)
        if extrai_valor(lista[i]) == extrai_valor(lista[i-3]) or extrai_naipe(lista[i]) == extrai_naipe(lista[i-3]):
            lista_mov.append(3)
        
        return lista_mov

#Funcao para verificar se existem movimentos possiveis:
def verifica_movimentos_possiveis(list1):
    lista=[]
    j=0
    while j < len(list1):
        item=str(list1[j])
        lista.append(item)
        j+=1
    
    tamanho = len(lista)
    i=0
    lista_mov = []
    while i < tamanho:
        if i < 3 :
            if i == 0:
                lista_mov = []
            elif i == 1:
                if extrai_valor(lista[1]) == extrai_valor(lista[0]) or extrai_naipe(lista[1]) == extrai_naipe(lista[0]):
                    lista_mov.append(1)
            elif i == 2:
                if extrai_valor(lista[1]) == extrai_valor(lista[2]) or extrai_naipe(lista[1]) == extrai_naipe(lista[2]):
                    lista_mov.append(1)
        else:
            if extrai_valor(lista[i]) == extrai_valor(lista[i-1]) or extrai_naipe(lista[i]) == extrai_naipe(lista[i-1]):
                lista_mov.append(1)
            if extrai_valor(lista[i]) == extrai_valor(lista[i-3]) or extrai_naipe(lista[i]) == extrai_naipe(lista[i-3]):
                lista_mov.append(3)
        
        i+=1

    return lista_mov

#Funcao para empilhar a carta:
def empilha(lista,origem,destino):
    if origem < 3:
        lista.pop(destino)
        return lista
    else:
        if destino == origem - 1:
            lista.pop(destino)
            
        else:
            i = origem
            lista[destino] = lista[i]
            lista.pop(origem)
        
        return lista
