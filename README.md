# Ep-2-2021
trabalho ep2 2021
oi
#Bibliotecas que serao utilizadas:
import random

#Funcoes a serem utilizadas:
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


    