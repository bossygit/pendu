# -*-coding:Latin-1 -*

""" Le fichier pour les fonctions """

from random import choice
import pickle



def random_num(liste):
  return choice(liste)

def recup_lettre(lettre_saisie):
  return lettre_saisie

def recup_scores():
  with open("scores","rb") as scores:
    score_pickler = pickle.Unpickler(scores)
    mes_scores = score_pickler.load()

def inser_score(points):
  with open("scores","wb")   as scores:
    score_pickler = pickle.Pickler(scores)
    score_pickler.dump(points)

    