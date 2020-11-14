import random
import os

jatekosnyer = []
gepnyer = []

def gepellen():
  gepkez = ""
  emb = 0
  gep = random.randint(1,3)
  if gep == 1:
    gepkez += "kő"
  if gep == 2:
    gepkez += "papír"
  if gep == 3:
    gepkez += "olló"

  embkez = input("Válassz: kő, papír, olló?: ")
  print("A gép keze: ", gepkez)
  print("A te kezed: ", embkez)

  if "k" in embkez:
    emb += 1
  if "p" in embkez:
    emb += 2
  if "l" in embkez:
    emb += 3
  if gep == 1 and emb == 2 or gep == 2 and emb == 3 or emb == 1 and gep == 3:
    jatekosnyer.append("x")
    print("Nyertél!")
  if gep == emb:
    print("Döntetlen!")
  if gep == 2 and emb == 1 or gep == 3 and emb == 2 or emb == 3 and gep == 1:
    gepnyer.append("x")
    print("Vesztettél")

def biro():
    print("játékos győzelmei: ", len(jatekosnyer))
    print("gép nyőzelmei: ", len(gepnyer))

def vegeredmeny():
  if len(jatekosnyer) > len(gepnyer):
    print("játékos nyer")
  else:
    print("a gép nyer")
