from random import shuffle, seed

class Card:
    def __init__(self, number, color, shading, shape): 
        self.number = number
        self.color = color
        self.shading = shading
        self.shape = shape

    def __str__(self): 
        return (f"Card({self.number}, {self.color}, {self.shading}, {self.shape})")

    # repr() is called instead of str() by some of pytho's built-ins. We'll always
    # want the same value returned in this course, so we can piggyback off of str
    def __repr__(self): return str(self)

    def __eq__(self, other): 
        if (self.number == other.number) and \
        (self.color == other.color) and \
        (self.shading == other.shading) and \
        (self.shape == other.shape):
            return True
        else:
            return False



class Deck:
    def __init__(self, numbers = [1, 2, 3], colors = ["green", "blue", "purple"], shadings = ["empty", "striped", "solid"], shapes = ["diamond", "squiggle", "oval"]):
        self.numbers = numbers
        self.colors = colors
        self.shadings = shadings
        self.shapes = shapes
        self.deck = []  
        for n in self.numbers:
            for c in self.colors:
                for shad in self.shadings:                                            
                    for shap in self.shapes:
                        self.deck.append(Card(n, c, shad, shap))   
                        
    def draw_top(self): 
        if len(self.deck) == 0:
            raise AttributeError       
        else:
            return self.deck.pop()     

    
    def shuffle(self): 
        shuffle(self.deck)


    def __len__(self): 
        return len(self.deck)


# True if, for all attributes, each card has the same or different values;
# e.g. {1, 1, 1} or {1, 2, 3}, but not {1, 1, 3}
def is_group(card1, card2, card3):

    if (card1.number == card2.number and card2.number == card3.number):
        return True
    elif (card1.color == card2.color and card2.color == card3.color):
        return True
    elif (card1.shading == card2.shading and card2.shading == card3.shading):
        return True
    elif (card1.shape == card2.shape and card2.shape == card3.shape):
        return True
    else:
        list1= [card1.number, card1.color, card1.shading, card1.shape] 
        list2= [card2.number, card2.color, card2.shading, card2.shape] 
        list3= [card3.number, card3.color, card3.shading, card3.shape]
        count = 0
    for i in range(len(list1)):
        if (list1[i] != list2[i] and list2[i] != list3[i] and list1[i]!= list3[i]):
            count += 1
    if (count != 4): 
        return False
    else:
        return True
