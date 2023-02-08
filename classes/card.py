class Card:

    def __init__( self , suit , point_val , string_val ):
        
        self.suit = suit
        self.point_val = point_val
        self.string_val = string_val

        self.blackjack_points()

    def card_info(self):
        print(f"{self.string_val} of {self.suit} : {self.point_val} points")

    def blackjack_points(self):
        if self.string_val == "Ace":
            self.point_val = 11
        elif self.string_val =="Jack" or self.string_val =="Queen" or self.string_val =="King":
            self.point_val = 10