#!/usr/bin/python3
import copy
import yaml

characterXPMax = 150

gameDefinitionsFile = open("gamedefs.yaml", "r")
gameDefinitions = yaml.load(gameDefinitionsFile, Loader=yaml.FullLoader)
gameDefinitionsFile.close()

attributeValues = {}
for attributeName in gameDefinitions['game']['values']['attributes']:
       attributeValues[attributeName] = gameDefinitions['game']['values']['attributes'][attributeName]

skillValues = {}
for skillName in gameDefinitions['game']['values']['skills']:
    skillValues[skillName] = {}
    skillValues[skillName]['attribute'] = gameDefinitions['game']['values']['skills'][skillName]['attribute']
    skillValues[skillName]['value'] = gameDefinitions['game']['values']['skills'][skillName]['value']

    skillValues[skillName]['specializations'] = {}
    for specialization in gameDefinitions['game']['values']['skills'][skillName]['specializations']:
        skillValues[skillName]['specializations'][specialization] = gameDefinitions['game']['values']['skills'][skillName]['specializations'][specialization]

class Race:
    def __init__(self, raceName, raceAttributes, raceSkills, raceTalents, raceFlaws, raceSkillBonus, raceTalentBonus):
       self.name            = raceName
       self.attributes      = copy.deepcopy(attributeValues)
       self.skills          = copy.deepcopy(skillValues)
       self.talents         = raceTalents
       self.flaws           = raceFlaws
       self.raceSkillBonus  = raceSkillBonus
       self.raceTalentBonus = raceTalentBonus

       for raceAttribute, attributeValue in raceAttributes.items():
           self.attributes[raceAttribute] += attributeValue

       for raceSkill, skillDictionary in raceSkills.items():
           self.skills[raceSkill]['value'] = skillDictionary['value']

           if 'specializations' in skillDictionary:
              for skillSpeciality, skillValue in skillDictionary['specializations'].items():
                  self.skills[raceSkill]['specializations'][skillSpeciality] = skillValue

class CharacterCustomizations:
   def __init__(self, customAttributes, customSkills, customTalents, customFlaws, skillBonus, talentBonus):
      self.attributes        = copy.deepcopy(attributeValues)
      self.skills            = copy.deepcopy(skillValues)
      self.talents           = customTalents
      self.flaws             = customFlaws
      self.skillBonus  = skillBonus
      self.talentBonus = talentBonus

      self.XPSpent = 0
      validCharacter = True

      for customAttribute, attributeValue in customAttributes.items():
          for nextRank in range(0,attributeValue+1):
              self.XPSpent += nextRank * 20

          self.attributes[customAttribute] += attributeValue
      
      for customSkill, skillDictionary in customSkills.items():
         for nextRank in range(0,skillDictionary['value']+1):
            cost = nextRank * 5

            if self.skillBonus < cost:
               cost -= self.skillBonus
               self.skillBonus = 0
            else :
               self.skillBonus -= cost
               cost = 0

            self.XPSpent += cost

         self.skills[customSkill]['value'] = skillDictionary['value']

         if 'specializations' in skillDictionary:
            for skillSpeciality, skillValue in skillDictionary['specializations'].items():
               for nextRank in range(0,skillValue+1):
                  cost = nextRank * 5

                  if self.skillBonus < cost:
                     cost -= self.skillBonus
                     self.skillBonus = 0
                  else :
                     self.skillBonus -= cost
                     cost = 0

                  self.XPSpent += cost

                  self.skills[customSkill]['specializations'][skillSpeciality] = skillValue

      print(self.XPSpent)


class Character:
   def __init__(self, characterName, race, customizations):
      self.name             = characterName

      for attributeName, raceValueValue in race.attributes.items():
          print(attributeName + " : " + str(raceValueValue))

      #self.attributes.bonus      = copy.deepcopy(race.attributeValues)
      #self.skills.bonus          = copy.deepcopy(race.skillValues)
      #self.talents         = copy.deepcopy(race.talents)
      #self.flaws           = copy.deepcopy(race.flaws)
      #self.skillBonus      = race.skillBonus
      #self.talentBonus     = race.talentBonus

      #self.power        = floor ( ( self.strength     + self.agility ) / 2 )
      #self.reflex       = floor ( ( self.agility      + self.intelligence ) / 2 )
      #self.awareness    = floor ( ( self.intelligence + self.willpower ) / 2 )
      #self.resistance   = floor ( ( self.will         + self.strength ) / 2 )


races = {}
generatedRaces ={}
for race in gameDefinitions['game']['race']:
   races[race] = {}
   races[race]['attributeValues'] = {}
   if "attributes" in gameDefinitions['game']['race'][race]:
      for attributeName in gameDefinitions['game']['race'][race]['attributes']:
         races[race]['attributeValues'][attributeName] = gameDefinitions['game']['race'][race]['attributes'][attributeName]

   races[race]['skillValues'] = {}
   if "skills" in gameDefinitions['game']['race'][race]:
      for skillName in gameDefinitions['game']['race'][race]['skills']:

         races[race]['skillValues'][skillName] = {}
         races[race]['skillValues'][skillName]['value'] = gameDefinitions['game']['race'][race]['skills'][skillName]['value']
   
         races[race]['skillValues'][skillName]['specializations'] = {}
         if "specializations" in gameDefinitions['game']['race'][race]['skills'][skillName]:
            for specialization in gameDefinitions['game']['race'][race]['skills'][skillName]['specializations']:
               races[race]['skillValues'][skillName]['specializations'][specialization] = gameDefinitions['game']['race'][race]['skills'][skillName]['specializations'][specialization]

   races[race]['talentValues'] = []
   if "talents" in gameDefinitions['game']['race'][race]:
       races[race]['talentValues'] = gameDefinitions['game']['race'][race]['talents']

   races[race]['flawValues'] = []
   if "flaws" in gameDefinitions['game']['race'][race]:
       races[race]['flawValues'] = gameDefinitions['game']['race'][race]['flaws']

   races[race]['skillBonus'] = 0
   if "skillBonus" in gameDefinitions['game']['race'][race]:
       races[race]['skillBonus'] = gameDefinitions['game']['race'][race]['skillBonus']

   races[race]['talentBonus'] = 0
   if "talentBonus" in gameDefinitions['game']['race'][race]:
       races[race]['talentBonus'] = gameDefinitions['game']['race'][race]['talentBonus']

   generatedRaces[race] = Race(race, 
                               races[race]['attributeValues'], 
                               races[race]['skillValues'], 
                               races[race]['talentValues'], 
                               races[race]['flawValues'], 
                               races[race]['skillBonus'], 
                               races[race]['talentBonus'])

#quitthat
mycustomizations = CharacterCustomizations( { 'agility': 2}, { 'melee': {'value': 2, 'specializations': { 'swords': 1 }}}, [], [], 0, 0)
#mycharacter = Character("hero", generatedRaces['ork'], {})
#generatedRaces[racenamegoeshere]
#XP cost
#generate a character
