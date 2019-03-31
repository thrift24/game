#!/usr/bin/python3
import copy
import yaml

characterXPMax = 150

gameDefinitionsFile = open("gamedefs.yaml", "r")
gameDefinitions = yaml.load(gameDefinitionsFile, Loader=yaml.FullLoader)
gameDefinitionsFile.close()

attributeDefaults = {}
for attributeName in gameDefinitions['game']['defaults']['attributes']:
       attributeDefaults[attributeName] = gameDefinitions['game']['defaults']['attributes'][attributeName]

skillDefaults = {}
for skillName in gameDefinitions['game']['defaults']['skills']:
    skillDefaults[skillName] = {}
    skillDefaults[skillName]['attribute'] = gameDefinitions['game']['defaults']['skills'][skillName]['attribute']
    skillDefaults[skillName]['default'] = gameDefinitions['game']['defaults']['skills'][skillName]['default']

    skillDefaults[skillName]['specializations'] = {}
    for specialization in gameDefinitions['game']['defaults']['skills'][skillName]['specializations']:
        skillDefaults[skillName]['specializations'][specialization] = gameDefinitions['game']['defaults']['skills'][skillName]['specializations'][specialization]

class Race:
    def __init__(self, raceName, raceAttributes, raceSkills, raceTalents, raceFlaws, raceSkillBonus, raceTalentBonus):
       self.name            = raceName
       self.attributes      = copy.deepcopy(attributeDefaults)
       self.skills          = copy.deepcopy(skillDefaults)
       self.talents         = raceTalents
       self.flaws           = raceFlaws
       self.raceSkillBonus  = raceSkillBonus
       self.raceTalentBonus = raceTalentBonus

       for raceAttribute, attributeValue in raceAttributes.items():
           self.attributes[raceAttribute] += attributeValue

       for raceSkill, skillDictionary in raceSkills.items():
           self.skills[raceSkill]['default'] = skillDictionary['default']

           if 'specializations' in skillDictionary:
              for skillSpeciality, skillValue in skillDictionary['specializations'].items():
                  self.skills[raceSkill]['specializations'][skillSpeciality] = skillValue

#class Character:
#   def __init__(self, characterName, characterStrength, characterAgility, characterIntelligence, characterWillpower):
#       self.name         = characterName
#       self.strength     = characterStrength
#       self.agility      = characterAgility
#       self.intelligence = characterIntelligence
#       self.willpower    = characterWillpower
#       self.power        = floor ( ( self.strength     + self.agility ) / 2 )
#       self.reflex       = floor ( ( self.agility      + self.intelligence ) / 2 )
#       self.awareness    = floor ( ( self.intelligence + self.willpower ) / 2 )
#       self.resistance   = floor ( ( self.will         + self.strength ) / 2 )
#

races = {}
generatedRaces ={}
for race in gameDefinitions['game']['race']:
   races[race] = {}
   races[race]['attributeDefaults'] = {}
   if "attributes" in gameDefinitions['game']['race'][race]:
      for attributeName in gameDefinitions['game']['race'][race]['attributes']:
         races[race]['attributeDefaults'][attributeName] = gameDefinitions['game']['race'][race]['attributes'][attributeName]

   races[race]['skillDefaults'] = {}
   if "skills" in gameDefinitions['game']['race'][race]:
      for skillName in gameDefinitions['game']['race'][race]['skills']:

         races[race]['skillDefaults'][skillName] = {}
         races[race]['skillDefaults'][skillName]['default'] = gameDefinitions['game']['race'][race]['skills'][skillName]['default']
   
         races[race]['skillDefaults'][skillName]['specializations'] = {}
         if "specializations" in gameDefinitions['game']['race'][race]['skills'][skillName]:
            for specialization in gameDefinitions['game']['race'][race]['skills'][skillName]['specializations']:
               races[race]['skillDefaults'][skillName]['specializations'][specialization] = gameDefinitions['game']['race'][race]['skills'][skillName]['specializations'][specialization]

   races[race]['talentDefaults'] = []
   if "talents" in gameDefinitions['game']['race'][race]:
       races[race]['talentDefaults'] = gameDefinitions['game']['race'][race]['talents']

   races[race]['flawDefaults'] = []
   if "flaws" in gameDefinitions['game']['race'][race]:
       races[race]['flawDefaults'] = gameDefinitions['game']['race'][race]['flaws']

   races[race]['skillBonus'] = 0
   if "skillBonus" in gameDefinitions['game']['race'][race]:
       races[race]['skillBonus'] = gameDefinitions['game']['race'][race]['skillBonus']

   races[race]['talentBonus'] = 0
   if "talentBonus" in gameDefinitions['game']['race'][race]:
       races[race]['talentBonus'] = gameDefinitions['game']['race'][race]['talentBonus']

   generatedRaces[race] = Race(race, 
                               races[race]['attributeDefaults'], 
                               races[race]['skillDefaults'], 
                               races[race]['talentDefaults'], 
                               races[race]['flawDefaults'], 
                               races[race]['skillBonus'], 
                               races[race]['talentBonus'])

#generatedRaces[racenamegoeshere]
#XP cost
#generate a character
