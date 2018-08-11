class CharacterSheet:
  def __init__(self, name, description, stats, banes, boons, feats):
    self.name = name
    self.description = description
    self.stats = stats
    self.banes = banes
    self.boons = boons
    self.feats = feats

cindy = CharacterSheet(name='cindy', description='pretty lady', 
stats={'physical':{'might':0, 'agility':0, 'fortitude':0}, \
      'mental':{'learning':0}}, banes='potatoes', boons='unicorn 
mastery', 
feats='unicorn potato attack')

print(cindy)
