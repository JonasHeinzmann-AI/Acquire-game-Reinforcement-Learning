coop_num = {"Prestige":8, "Continental":7, "Luxor":6, "Imperial":5, "Oriental":4, "Airport":3, "Festival":2}
def create_corp(free):
    print(free)
    sel = input("Hotelkette auswählen: ")
    val = coop_num.get(sel)
    print(val)
    num = val
    return num
    
    
    
'''def attach_corp():
    

def merge_corp():
    '''