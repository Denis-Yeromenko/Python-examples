class Basket:
    def __init__(self, volume):
        self.volume = volume


    def is_volume_size(self, thing):
        self.thing = thing
        if self.volume < thing.volume:
            print('Your thing is too large for this basket!')
        else:
            print('Your thing in the basket!')

class Bag(Basket):
    def is_volume_size(self, thing):
        self.thing = thing
        if self.volume < thing.volume:
            print('Your thing is too large for this bag!')
        else:
            print('Your thing in the bag!')

class Meal:
    def __init__(self, volume):
        self.volume = volume


apple15 = Meal(15)
pear35 = Meal(35)
Bas20 = Basket(20)
bag30 = Bag(30)
Bas20.is_volume_size(apple15)
bag30.is_volume_size(pear35)

