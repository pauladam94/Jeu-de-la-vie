
# coding: utf8

import pygame as py
from random import randint
#from C:/Users/marin/Documents/Perso/Python/GENERAL/Couleur import *
py.init()

NOIR        = (0,0,0)
BLANC       = (255,255,255)
VERT        = (0,255,0)
ROUGE       = (255,0,0)
GRIS        = (60,60,60)
MARRON      = (173,79,9)
### def des variables :
# def couleur de fonc
C_FOND = BLANC

# variable à définir en fonction du choix
LARGUEUR = 600
# nombre de carré : max 200 sans lag
NBCARRE = 300
# en miliseconde
speed = 10

CARRE = LARGUEUR/NBCARRE

# pourcentage de foret
pforet = 65

def affichage1(window,terre):
    for i in range(len(terre)):
        for j in range(len(terre)):
            if terre[i][j] == 1 :
                py.draw.rect(window, NOIR, [CARRE*j,CARRE*i, CARRE,CARRE])
            elif terre[i][j] == 0 :
                py.draw.rect(window, BLANC, [CARRE*j,CARRE*i, CARRE,CARRE])



# jeu de la vie
def gen1(terre):
    nvterre=[[terre[i][j] for j in range(len(terre))] for i in range(len(terre))]

    for i in range(len(terre)):
        for j in range(len(terre)):
            if i==0 or j==0 or i==len(terre)-1 or j==len(terre)-1:
                nvterre[i][j]=0

            else:
                compt=0
                if terre[i-1][j-1] == 1 :
                    compt+=1

                if terre[i][j-1]   == 1 :
                    compt+=1

                if terre[i+1][j-1] == 1 :
                    compt+=1

                if terre[i+1][j]   == 1 :
                    compt+=1

                if terre[i+1][j+1] == 1 :
                    compt+=1

                if terre[i][j+1]   == 1 :
                    compt+=1

                if terre[i-1][j+1] ==1:
                    compt+=1

                if terre[i-1][j]   ==1:
                    compt+=1

                if compt==3:
                    nvterre[i][j]=1
                if compt!=2 and compt!=3:
                    nvterre[i][j]=0
    return(nvterre)

