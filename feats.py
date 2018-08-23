from csv import reader as csvreader


class Feat:

    def __init__(self, title, cost, prereqs, prereq_min, desc, effect):
        self.title = title
        self.cost = cost
        self.prereqs = prereqs
        self.prereq_min = prereq_min
        self.desc = desc
        self.effect = effect


file = r'./data/feat_list.csv'

feat_list = {}

with open(file, "r", encoding="latin1") as csvfile:
    reader = csvreader(csvfile, quotechar='"', skipinitialspace=True)
    for row in reader:
        title = row[0]
        cost = int(row[1])
        prereqs = row[2].split(' ')
        prereq_min = int(row[3])
        desc = row[4]
        effect = row[5]

        feat_list[title.lower()] = Feat(title, cost, prereqs, prereq_min, desc, effect)


def meets_prereqs(character, feat):
    for prereq in feat_list[feat].prereqs:
        if character.stats[prereq] and character.stats[prereq].get() >= feat_list[feat].prereq_min:
            return True
            
            
