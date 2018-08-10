# legendary-characters

So this is my design guide.

## Step 1:  Describe your character.

- [ ] Bare minimum:
  - [ ] User should be able to enter a name.
  - [ ] User should be able to enter a race.
  - [ ] User should be able to select a size for their character.
  - [ ] User should be able to select/enter two exceptional physical traits.
  - [ ] User should be able to select/enter two defining social traits.
  - [ ] User should be able to select/enter a secret.

- [ ] Optional:
  - [ ] Random name generator
  - [ ] Random physical/social trait buttons
  - [ ] Random secret generator
  
## Step 2. Choose Attributes
  
There are two methods of choosing attribute.  I should account for both of them.  
  
1. [ ] Quick build (profiles with pre-selected attributes)
2. [ ] Custom build
  1. [ ] User is given 40 attribute points to buy initial attributes.
  2. [ ] Cost to raise attributes is based on table below:
    
  | Attribute Level | Cost to Raise |
  | --- | --- |
  | 0 | 0 |
  | 1 | 1 |
  | 2 | 3 |
  | 3 | 6 |
  | 4 | 10 |
  | 5 | 15 |
  
  3. [ ] User should be able to raise the following attributes:

  | Physical |
  | --- |
  | Agility |
  | Fortitude |
  | Might |

  | Mental |
  | --- |
  | Learning |
  | Logic |
  | Perception |
  | Will |
  
  |Social|
  |---|
  |Deception|
  |Persuasion|
  |Presense|

  | Extraordinary |
  | --- |
  | Alteration |
  | Creation |
  | Engergy |
  | Entropy | 
  | Influence |
  | Prescience |
  | Protection |

## Step 3. Record Defenses, Hit Points, and Speed

- [ ] The application should calculate the following for the user.
  - [ ] Toughness = 10 + Fortitude + Will
  - [ ] Guard = 10 + Agility + Will
  - [ ] Resolve = 10 + Presence + Will
  - [ ] Hit Points = 2 * (Fortitude + Presence + Will) + 10
- [ ] The characters base speed should be set to 30 and made available or feat/abilities to alter later on.

## Step 4: Purchase Feats

Minimum:
- [ ] User should be given 6 feat points to spend.
- [ ] User should be able to browse a list and spend points to purchase chosen feats.

Optional:
- [ ] Search for feats
- [ ] Create-a-feat

## Step 5: Choose Start Equipment

- [ ] User should be able to set wealth level.
- [ ] User should be able to pick 3 items of the same wealth level.
- [ ] User should be able to pick any number of items of a wealth level lower than that.

## Step 6:  Choose Perks and Flaws

- [ ] User should optionally be able to select up to two perks.
- [ ] User should optionally be able to select up to two flaws.

## Levelling Up 

Notes:

| XP | Level | Max Attribute Score |
| --- | --- | --- |
| 0 | 1 | 5 |
| 3 | 2 | 5 |
| 6 | 3 | 6 |
| 9 | 4 | 6 |
| 12 | 5 | 7 |
| 15 | 6 | 7 |
| 18 | 7 | 8 |
| 21 | 8 | 8 |
| 24 | 9 | 9 |
| 27 | 10 | 9 |

For each point of XP earned the user is given 1 feat point and 3 attribute points.  The costs associated with spending those attributes point is different.  See table below.

| Score | Cost |
| --- | --- |
| 1 | 1 |
| 2 | 3 |
| 3 | 6 |
| 4 | 10 |
| 5 | 15 |
| 6 | 21 |
| 7 | 28 |
| 8 | 36 |
| 9 | 45 |
| 10 | - |
