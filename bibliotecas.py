import random

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

baralho = cria_baralho()
embaralhado=[]
while len(embaralhado) < len(baralho):
    carta = random.choice(baralho)
    if carta not in embaralhado:
        embaralhado.append(carta)


#Funcao para colorir o baralho:
def colore_baralho(baralho):
    i=0
    tamanho=len(baralho)
    baralho_color=[]
    while i < tamanho:
        item = baralho[i]
        teste = extrai_naipe(item)
        valor=0
        if teste == '♠':
            valor = '\033[34m' + item + '\033[0m'
        elif teste == '♥':
            valor = '\033[31m' + item + '\033[0m'
        elif teste == '♦':
            valor = '\033[32m' + item + '\033[0m'
        elif teste == '♣':
            valor = '\033[33m' + item + '\033[0m'

        baralho_color.append(valor)
        i+=1
        
    return baralho_color
