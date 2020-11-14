
p1nyer = []
p2nyer = []
jatekosok = []

def jatekosmegadas():

    p1 = input("Az 1. játékos neve: ")
    p2 = input("Az 2. játékos neve: ")
    jatekosok.append(p1n)
    jatekosok.append(p2n)

    print(jatekosok)


def ketjatekos():

    p1sz = 0
    p1kez = input("válasz1: kő papír olló: ")
    if p1kez == "kő":
      p1sz += 1
    if p1kez == "papír":
      p1sz += 2
    if p1kez == "olló":
      p1sz += 3

    p2sz = 0
    p2kez = input("válasz2: kő papír olló: ")
    if p2kez == "kő":
      p2sz += 1
    if p2kez == "papír":
      p2sz += 2
    if p2kez == "olló":
      p2sz += 3

    if p1sz == 2 and p2sz == 1 or p1sz == 3 and p2sz == 2 or p1sz == 1 and p2sz == 3:
      p1nyer.append("X")
      print("1. játékos nyert")

    if p2sz == 2 and p1sz == 1 or p2sz == 3 and p1sz == 2 or p2sz == 1 and p1sz == 3:
      p2nyer.append("X")
      print("2.játékos nyert")

def biro():
    print("1. játékos győzelmei: ", len(p1nyer))
    print("2. játékos győzelmei: ", len(p2nyer))

def vegetedmeny():
    if len(p1nyer) > len(p2nyer):
      print("A győztes: ", jatekosok[0])
    if len(p2nyer) > len(p1nyer):
      print("A győztes: ", jatekosok[1])