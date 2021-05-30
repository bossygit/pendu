# -*-coding:Latin-1 -*

import os

from fonctions import random_num
from donnees import data
from donnees import nb_essai

mot_a_trouver = random_num(data)

print("""Le mot à trouver est {}""".format(mot_a_trouver))


placeholder = ""
placeholder.index()

while nb_essai != 0:
    lettre = input("Tapes une lettre : ")
    try:
        if len(lettre) != 1:
            raise ValueError("Saissis une seule lettre")
    except ValueError:
        print("Saissis une lettre")
    for i in range(len(mot_a_trouver)):
        if mot_a_trouver[i] == lettre:
            placeholder[i] = mot_a_trouver[i]
        else:
            placeholder[i] = "-"

print("""Vous avez trouvé""".format(placeholder))
  

os.system('pause')