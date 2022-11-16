

def locate_cards(cards, query):
    position = 0
    
    while True:
        if cards == query:
            return position
        
        position += 1
        
        if position == len(cards):
            return "Card not found!"

