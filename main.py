from queue import Empty
import pandas as pd
import numpy as np
from rules import chk_neighbours, chk_pos, chk_cooperations, get_d_field, get_l_field,get_r_field,get_u_field, chk_neighbour_corp
from cards import draw_hands, get_card, del_card

users = ["Max", "Jonas"]
field = pd.DataFrame(0, index=np.arange(14), columns =["A","B","C","D","E","F","G","H","I","J","K"])
print(field.head(16))
hands,cards = draw_hands(users)
used = []
while True:
    for user in users:
        print("{} ist dran".format(user))
        print(hands.get(user))
        #cardx,cardy = input("Karte Angeben: ").split()
        card_num = int(input("Karte Eingeben: "))
        hand = hands.get(user)
        card = hand[card_num]
        #str1 = slice(0,1)
        #str2 = slice(1,len(card))
        #cardx = card[str1]
        #cardy = card[str2]
        cardx, cardy = card[:1], card[1:]
        cardy = int(cardy)
        if chk_pos(cardx,cardy, field):
            a = chk_neighbours(cardx, cardy, field)
            print(a)
            cop, nei = chk_cooperations(a, used, cardx, cardy)
            print(nei)

            #card2 = int(input("Zahl Angeben"))
            #field.at[card2, card] = 10
            field.loc[cardy,cardx]=1
            field.loc[cardy,cardx]=cop
            if nei:
                for item in nei:
                    if item == "u":
                        y = get_u_field(cardy)
                        field.loc[y,cardx]=cop

                    elif item == "l":
                        x = get_l_field(cardx)
                        field.loc[cardx,x]=cop
                    
                    elif item == "d":
                        y = get_d_field(cardy)
                        field.loc[y,cardx]=cop

                    elif item == "r":
                        x = get_r_field(cardx)
                        field.loc[cardy,x]=cop
            val, valch = chk_neighbour_corp(a,used,cardx,cardy)
            if val == "x":
                field.loc[cardy,valch]=cop
            elif val == "y":
                field.loc[valch,cardx]=cop
            print(field.head(16))
            get_card(user,hands,cards)
            del_card(user,hands,cardx,cardy)
        else:
            print("Hä")
