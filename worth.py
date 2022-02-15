#from rules import *

worth = {"Prestige":3, "Continental":3, "Luxor":2, "Imperial":2, "Oriental":2, "Airport":1, "Festival":1}
price_tab = {1:{2:200,3:300,4:400,5:500,6:600,7:700,8:800,9:900,10:1000},
            2:{2:300,3:400,4:500,5:600,6:700,7:800,8:900,9:1000,10:1100},
            3:{2:400,3:500,4:600,5:700,6:800,7:900,8:1000,9:1100,10:1200}
}

#print(price_tab.get(2).get(3))

def get_price(coop, m):
    coop_num  = worth.get(coop)
    if m > 5:
        if m <= 10:
            a = 6
        elif m <= 20:
            a = 7
        elif m <= 30:
            a = 8
        elif m <= 40:
            a = 9
        else:
            a = 10
    else:
        a = m
    return price_tab.get(coop_num).get(a)

#print(price("Prestige",16))