pnt = 40
COST_TO_INCREASE = {0:0, 1:1, 2:3, 3:6, 4:10, 5:15}

stats = {"physical":{"agility":0, "fortitue":0, "might":0}, \
        "mental":{"learning":0, "logic":0, "perception":0, "will":0}, \
        "social":{"deception":0, "persausion":0, "presence":0}, \
        "extraordinary":{"alteration":0, "creation":0, "energy":0, \
            "entropy":0, "influence":0, "prescience":0, "protection":0}}

print(pnt)
print(stats)

def increase_ability_score(category, ability, amount):
    global pnt
    for num in range(stats[category][ability], amount+1):
        pnt = pnt - COST_TO_INCREASE[num]
    stats[category].update({ability:amount})

increase_ability_score("physical", "agility", 3)
increase_ability_score("mental", "learning", 3)
increase_ability_score("mental", "will", 3)
increase_ability_score("social", "presence", 4)
increase_ability_score("social", "persausion", 3)
increase_ability_score("extraordinary", "influence", 2)

print("\nIncreasing abilities...\n")

print(pnt)
print(stats)
