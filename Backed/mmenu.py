from  GameMode import pvemode
from  Backed import korajz
def menu():
    modv = 0
    print("válaszon játék módot")
    print("1 játék a gép ellen")
    print("2 játék egy játékos ellen")
    modv = input("írja be a játék mód kódját: ")
    if modv == 1:
        pvemode.pve
    if modv == 2:
        pvemode.pvp