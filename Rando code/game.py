import random 
 
class Item(object): 
    def __init__(self, name, weight): 
        self.name = name 
        self.weight = weight 
 
 
class Axe(Item): 
    def __init__(self, name, weight, blade, damage): 
        super(Axe, self).__init__(name, weight) 
        self.handle = True 
        self.blade = blade 
        self.damage = damage 
 
    def Axe(self, long): 
        self.blade = long 
 
    def damage(self): 
        self.damage = 10 
 
 
class LongAxe(Axe): 
    def __init__(self, name, weight): 
          super(LongAxe, self).__init__(name, weight, "long", 10) 
my_axe = LongAxe 
 
class Sword(Item): 
    def __init__(self, name, weight, blade, damage): 
        super(Sword, self).__init__(name, weight) 
        self.handle = True 
        self.blade = blade 
        self.damage = damage 
 
    def blade(self, short): 
        self.blade = short 
 
    def damage(self): 
        self.damage = 10 
 
 
class ShortSword(Sword): 
    def __init__(self): 
        super(ShortSword, self).__init__("short sword", 15, "short", 15) 
 
    def attack(self): 
        random.randint(12, 15) 
 
 
my_shortsword = ShortSword 
 
class Bow(Item): 
     def __init__(self, name, weight, range, shoot, damage, arrows = 10): 
         super(Bow, self).__init__(name, weight) 
         self.range = range 
         self.shoot = shoot 
         self.damage = damage 
         self.arrows = arrows 
 
     def Crossbow(self): 
         self.Crossbow = shoot 
        if 
            self.shoot = True 
            self.arrows =-1 
     def damage = 50 
     def range = 20 
shoot = True 
 
class CrossBow(Bow): 
 
     def __init__(self, name, weight,"Normal",15 

 
def forItem(orders, item):
    max = 0
    count = 0
    for order in orders:
        neworder= order.split(":")
        if neworder[0] == item:
            if int(neworder[1]) >= max:
                max=int(neworder[1])
                count+=1
    return [max, count]
    


if __name__ == '__main__':
    orders = ['banana:14', 'banana:1', 'banana:25', 'banana:14', 'banana:13']
    item = 'banana'
    print(forItem(orders, item))


def forItem(orders, item):
        max = 0
	    count = 0
	    for order in orders:
	        neworder= order.split(":")
	        if neworder[0] == item:
	            if int(neworder[1]) > max:
	                max=int(neworder[1])
	                count = 1
	            elif int(neworder[1]) == max:
	                count += 1
	    return [max, count]
	    
	
	
	if __name__ == '__main__':
	    orders = ['banana:14', 'banana:1', 'banana:25', 'banana:14', 'banana:13']
	    item = 'banana'
	    print(forItem(orders, item))
