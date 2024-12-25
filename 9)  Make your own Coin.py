# MAKING OWN COIN PROJECT
import random

class Coin:
    def __init__(self, rare = False, clean = True, heads = True,**kwargs):

        for key,value in kwargs.items():
            setattr(self,key,value)
        
        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value


        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour

    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour

    def __del__(self):
        print("Coin Spent!")

    def flip(self):
        heads_options = [True,False]
        choice = random.choice(heads_options)
        self.heads = choice

    def __str__(self):
        if self.original_value >= 1:
            return "₹{}coin".format(int(self.original_value))

class One_Rupees(Coin):
    def __init__(self):
        data = {
            "original_value":1.00,
            "clean_colour":"silver",
            "rusty_colour": None,
            "edges":0,
            "diameter": 20,
            "thickness":1.45,
            "mass":3.09,
            }
        super().__init__(**data)

        def rust(self):
            self.colour = self.clean_colour
        def clean(self):
            self.clean = self.clean_colour

class Two_Rupees(Coin):
    def __init__(self):
        data = {
            "original_value":2.00,
            "clean_colour":"silver",
            "rusty_colour":"redish",
            "edges":0,
            "diameter": 25,
            "thickness":15.62,
            "mass":4.07,
            }
        super().__init__(**data)

        def rust(self):
            self.colour = self.clean_colour
        def clean(self):
            self.clean = self.clean_colour


class Five_Rupees(Coin):
    def __init__(self):
        data = {
            "original_value":5.00,
            "clean_colour":"gold",
            "rusty_colour":"grey",
            "edges":0,
            "diameter": 23,
            "thickness":1.9,
            "mass":6.74,
            }
        super().__init__(**data)
            
class Ten_Rupees(Coin):
    def __init__(self):
        data = {
            "original_value":10.00,
            "clean_colour":"gold,silver",
            "rusty_colour":"redish",
            "edges":0,
            "diameter": 27,
            "thickness":1.7,
            "mass":7.74,
            }
        super().__init__(**data)
    
class Twenty_Rupees(Coin):
    def __init__(self):
        data = {
            "original_value":20.00,
            "clean_colour":"reddish brown",
            "rusty_colour":"greenish",
            "edges":12,
            "diameter": 27,
            "thickness":2,
            "mass":9.95,
            }
        super().__init__(**data)


coins = [One_Rupees(),Two_Rupees(),Five_Rupees(),Ten_Rupees(),Twenty_Rupees()]
    
for coin in coins:
    arguments = [coin,coin.colour,coin.value,coin.diameter,coin.thickness,coin.edges,coin.mass]

    strings = "{}-colour:{}, Value:{}, diameter(mm):{}, thickness(mm):{}, edges:{}, mass(g):{}".format(*arguments)

    print(strings)
    
   
