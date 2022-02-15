import random
from collections import defaultdict
card_dict = defaultdict(list)

cards = ["A0","A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","B0","B1","B2","B3","B4","B5","B6","B7","B8","B9","B10","B11","C0","C1","C2","C3","C4","C5","C6","C7","C8","C9","C10","C11","D0","D1","D2","D3","D4","D5","D6","D7","D8","D9","D10","D11","E0","E1","E2","E3","E4","E5","E6","E7","E8","E9","E10","E11","F0","F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","F11","G0","G1","G2","G3","G4","G5","G6","G7","G8","G9","G10","G11","H0","H1","H2","H3","H4","H5","H6","H7","H8","H9","H10","H11","I0","I1","I2","I3","I4","I5","I6","I7","I8","I9","I10","I11"]
def draw_hands(users):
    card = cards
    j = 0
    for user in users:
        for i in range(5):
            anz = len(card)
            cardn = random.randint(0,anz-1)
            card_dict[user].append(card[cardn])
            del card[cardn]
    return card_dict, card
            
def get_card(user, hand, cards):
    anz = len(cards)
    cardn = random.randint(0,anz)
    hand[user].append(cards[cardn])
    del cards[cardn]
    print(hand)
    
def del_card(user,hands,cardx,cardy):
    str_card = ""
    str_card = cardx + str(cardy)
    print(str_card)
    print(str_card in hands.values())