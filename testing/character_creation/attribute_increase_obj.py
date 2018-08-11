pnt = 40
COST_TO_INCREASE = {0:0, 1:1, 2:3, 3:6, 4:10, 5:15}

stats = {"physical":{"agility":0, "fortitue":0, "might":0}, \
        "mental":{"learning":0, "logic":0, "perception":0, "will":0}, \
        "social":{"deception":0, "persausion":0, "presence":0}, \
        "extraordinary":{"alteration":0, "creation":0, "energy":0, \
            "entropy":0, "influence":0, "prescience":0, "protection":0}}

class CharacterSheet(object):
    def __init__(self, name, description, stats, banes, boons, feats):
        self.name = name
        self.description = description
        self.stats = stats
        self.banes = banes
        self.boons = boons
        self.feats = feats

    def increase_ability_score(self, category, ability, amount):
        global pnt
        for num in range(self.stats[category][ability], amount+1):
            pnt = pnt - COST_TO_INCREASE[num]
        self.stats[category].update({ability:amount})

cindy = CharacterSheet(name='cindy', description='pretty lady', 
stats={'physical':{'might':0, 'agility':0, 'fortitude':0}, \
      'mental':{'learning':0}}, banes='potatoes', boons='unicorn mastery',
feats='unicorn potato attack')

print(cindy.name, "is a", cindy.description + ".")
print(cindy.name, "is afraid of", cindy.banes + ".")
print(cindy.name + "'s agility is", str(cindy.stats['physical']['agility']) + ".")

do_the_thing = input('y/n >> ')

if do_the_thing == 'y':
    cindy.increase_ability_score("physical", "agility", 3)
    print(cindy.name + "'s agility is", str(cindy.stats['physical']['agility']) + ".")
