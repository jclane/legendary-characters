alterationval = 1

class Feat:
    
    def __init__(self, name, cost, prereqs, desc, effect):
        self.name = name
        self.cost = cost
        self.prereqs = prereqs
        self.desc = desc
        self.effect = effect
        
f1 = Feat("Ageless", 5,  alterationval == 9, "life forever young", "see desc")
