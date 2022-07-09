## Codage graphique Conway jeu de la vie :
# coding: utf8

# taille fenetre :
import pygame as py
import module_jdlv as m
import numpy as np
from random import randint
# initialisation de pygame
py.init()

# Initialisation de la fenetre graphique avec son nom
# | py.RESIZABLE
fenetre = py.display.set_mode((m.LARGUEUR,m.LARGUEUR), py.DOUBLEBUF | py.HWSURFACE )
py.display.set_caption("JDLV P.A.")

# Vérif des paramètres d'affichage dans le terminal :
print(py.display.Info())

# Iniatilisation choix situation de départ :

fenetre.fill(m.BLANC)
terre = [[0]*m.NBCARRE for i in range(m.NBCARRE)]
py.time.delay(m.speed)
py.display.flip()


A = True
while A :
    for event in py.event.get() :
        # conditions d'arrets de l'initialisation
        if event.type == py.QUIT :
            A = False
        if event.type == py.KEYDOWN and event.key == py.K_SPACE:
            A = False

        elif event.type == py.MOUSEBUTTONDOWN :
            if event.button == 3 :
                terre=[[randint(0,1)for j in range(m.NBCARRE)]for i in range(m.NBCARRE)]
            elif event.button == 6:
                terre = [[0]*m.NBCARRE for i in range(m.NBCARRE)]
            else :
                #print(event.pos)
                b,a = event.pos
                a,b = int(a//m.CARRE) , int(b//m.CARRE)

                if terre[a][b] == 1 :
                    terre[a][b] = 0
                if terre[a][b] == 0 :
                    terre[a][b] = 1
                    terre[a+1][b] = 1
                    terre[a][b+1] = 1
                    terre[a+1][b+1] = 1
                    terre[a-1][b-1] = 1
                    terre[a-1][b] = 1
                    terre[a][b-1] = 1
                    terre[a+1][b-1] = 1
                    terre[a-1][b+1] = 1


            #for x in terre: print(x)
            m.affichage1(fenetre,terre)

    py.display.flip()


## Sauvegarde pour récupérer les données
sauv =[[terre[i][j] for j in range(len(terre))] for i in range(len(terre))]

A = True
compt=0
## Générations
while A :
    for event in py.event.get() :
        # conditions d'arrets de l'initialisation
        if event.type == py.QUIT :
            A = False
        if event.type == py.KEYDOWN and event.key == py.K_SPACE:
            A = False
        elif event.type == py.MOUSEBUTTONDOWN :
            if event.button == 3 :
                terre=[[randint(0,1)for j in range(m.NBCARRE)]for i in range(m.NBCARRE)]
            elif event.button == 6:
                terre = [[0]*m.NBCARRE for i in range(m.NBCARRE)]
            else :
                #print(event.pos)
                b,a = event.pos
                a,b = int(a//m.CARRE) , int(b//m.CARRE)

                if terre[a][b] == 1 :
                    terre[a][b] = 0
                if terre[a][b] == 0 :
                    terre[a][b] = 1
                    terre[a+1][b] = 1
                    terre[a][b+1] = 1
                    terre[a+1][b+1] = 1
                    terre[a-1][b-1] = 1
                    terre[a-1][b] = 1
                    terre[a][b-1] = 1
                    terre[a+1][b-1] = 1
                    terre[a-1][b+1] = 1
    ###partie qui change entre les simulations
    terre = m.gen1(terre)

    m.affichage1(fenetre,terre)
    py.display.flip()

    py.time.delay(m.speed)
    compt+=1
    print(compt)



gard = input("garder ? ( O / N ) ... ")

if gard == "O":
    comment=input("commentaire : ... ")
    fichier = open("sauv.txt", "w")

    fichier.write(comment+"\n")
    fichier.write("LARGUEUR = "+str(m.LARGUEUR)+"  "+"CARRE = "+str(m.CARRE)+"\n")
    for i in range(len(sauv)):
        for j in range(len(sauv)):
            if j==0 and i==0 : fichier.write("[\n")
            if j==0 : fichier.write("[")

            fichier.write(str(sauv[i][j]))
            if j!=len(sauv)-1 : fichier.write(",")

            if j==len(sauv)-1 : fichier.write("] , \n")

            if j==len(sauv)-1 and i==len(sauv)-1 : fichier.write("]")
    fichier.write("\n")
    fichier.write("\n")
    fichier.close()

py.quit()






