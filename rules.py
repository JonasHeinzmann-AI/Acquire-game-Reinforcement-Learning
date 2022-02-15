from worth import *


def chk_coop(coop, used):
    free = []
    if coop == used:
        print("Test")
        return False
    else:
        for item in coop:
            if item not in used:
                free.append(item)
            else:
                print("Vorhanden")
        return(free)
'''
def chk_neighbours():

def chk_cooperations():

def chk_num_hold():
'''
cop = ["Prestige","Continental","Luxor","Imperial","Oriental","Airport","Festival"]

