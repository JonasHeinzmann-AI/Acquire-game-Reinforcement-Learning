from ast import Return
from worth import *
from company import create_corp#, attach_corp, merge_corp


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

def chk_pos(x,y, field):
    if field.iloc[y][x] == 0:
        return True
    else:
        return False
    

def chk_neighbours(x,y, field):
    ref_arr = {}
    xc = ord(x)
    xc=xc+1
    r = chr(xc)
    xc=xc-1
    l = chr(xc)
    d = y + 1
    u = y - 1
    pos_lista = [r, l]
    pos_listb = [u, d]
    pos_listav = ["r", "l"]
    pos_listbv = ["u", "d"]
    i = 0
    for pos in pos_lista:
        print(pos)
        a = field.iloc[y][pos]
        print(a)
        ref_arr[pos_listav[i]] = a
        if a > 0:
            print("Yes")
        i +=1
    i = 0
    for pos in pos_listb:
        print(pos)
        a = field.iloc[pos][x]
        print(field.iloc[pos][x])
        ref_arr[pos_listbv[i]] = a
        if a > 0:
            print("Yes")
        i +=1
    return ref_arr

coop= ["Prestige", "Continental", "Luxor", "Imperial", "Oriental", "Airport", "Festival"]

def chk_cooperations(field, ref_arr, used,x,y):
    sum = 0
    for item in ref_arr:
        sum = ref_arr[item] + sum
    if sum == 1:
        for item in ref_arr:
            if ref_arr[item] == 0:
                continue
            elif ref_arr[item] > 0:
                free = chk_coop(coop, used)
                #print(a)
                cop = create_corp(free,x,y, field)
            else:
                #cop = attach_corp()
                print("dead")
        return cop
    elif sum == 0:
        return False
    else:
        #merge_corp()
        print("dead")
    
'''
def chk_num_hold():
'''
cop = ["Prestige","Continental","Luxor","Imperial","Oriental","Airport","Festival"]

