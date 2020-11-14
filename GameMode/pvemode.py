from GameMode import pve, pvp

def pvegame():
    for _ in range(10):
        pve.gepellen()
        pve.biro()
    pve.vegeredmeny()

def pvpgame():
    for _ in range(10):
        pvp.ketjatekos()
        pvp.biro()
    pvp.vegetedmeny()