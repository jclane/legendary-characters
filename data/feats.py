import csv


class NewCharacter:

    def __init__(self, stats):
        self.stats = stats
        
char = NewCharacter(stats={'might':9, 'alterationval':10, 'creationval':2, 'entropyval':9, 'protectionval':1})

class Feat:
    
    def __init__(self, title, cost, prereqs, prereq_min, desc, effect):
        self.title = title
        self.cost = cost
        self.prereqs = prereqs
        self.prereq_min = prereq_min
        self.desc = desc
        self.effect = effect
        
file = r'C:\Users\<BLAH>\Desktop\data.csv'

feats = {}
        
with open(file, "r", encoding="latin1") as csvfile:
    reader = csv.reader(csvfile, quotechar='"', skipinitialspace=True)
    for row in reader:
        title = row[0]
        cost = int(row[1])
        prereqs = row[2].split(' ')
        prereq_min = int(row[3])
        desc = row[4]
        effect = row[5]
        
        feats[title.lower()] = Feat(title, cost, prereqs, prereq_min, desc, effect)

def meets_prereqs(character, feat): 
    for prereq in feat.prereqs:
        if character.stats[prereq] and character.stats[prereq] >= feat.prereq_min: 
            return True
        else:
            return False
                
print(meets_prereqs(char, feats['ageless']))
