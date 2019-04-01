#!/usr/bin/python3
import copy
import yaml

class Defaults:
   def __init__(self, gameDefinitionsFilePath, characterXPMax):
      self.gameDefinitionsFilePath=gameDefinitionsFilePath
      self.characterXPMax = characterXPMax
       
      self.attributes       = {}
      self.skills           = {}
      self.talents          = {}
      self.flaws            = {}
      self.races            = []

      self.skillBonusXP     = 0
      self.talentBonusXP    = 0

      gameDefinitionsFile = open(self.gameDefinitionsFilePath, "r")
      gameDefinitions = yaml.load(gameDefinitionsFile, Loader=yaml.FullLoader)
      gameDefinitionsFile.close()

      for attributeName in gameDefinitions['game']['defaults']['attributes']:
         self.attributes[attributeName] = gameDefinitions['game']['defaults']['attributes'][attributeName]

      for skillName in gameDefinitions['game']['defaults']['skills']:
         self.skills[skillName] = {}
         self.skills[skillName]['attribute'] = gameDefinitions['game']['defaults']['skills'][skillName]['attribute']
         self.skills[skillName]['value'] = gameDefinitions['game']['defaults']['skills'][skillName]['value']

         self.skills[skillName]['specializations'] = {}
         for specialization in gameDefinitions['game']['defaults']['skills'][skillName]['specializations']:
            self.skills[skillName]['specializations'][specialization] = gameDefinitions['game']['defaults']['skills'][skillName]['specializations'][specialization]

      for talentName in gameDefinitions['game']['defaults']['talents']:
         self.talents[talentName] = {}
         self.talents[talentName]['value'] = gameDefinitions['game']['defaults']['talents'][talentName]['value']
         self.talents[talentName]['max'] = gameDefinitions['game']['defaults']['talents'][talentName]['max']

         if gameDefinitions['game']['defaults']['talents'][talentName]['type'] == "attribute modifier":
            self.talents[talentName]['type'] = "attribute modifier"
            self.talents[talentName]['attribute'] = gameDefinitions['game']['defaults']['talents'][talentName]['attribute']
            self.talents[talentName]['intensity'] = gameDefinitions['game']['defaults']['talents'][talentName]['intensity']
         else:
            self.talents[talentName]['type'] = "other"

      for flawName in gameDefinitions['game']['defaults']['flaws']:
         self.flaws[flawName] = {}
         self.flaws[flawName]['value'] = gameDefinitions['game']['defaults']['flaws'][flawName]['value']
         self.flaws[flawName]['max'] = gameDefinitions['game']['defaults']['flaws'][flawName]['max']

         if gameDefinitions['game']['defaults']['flaws'][flawName]['type'] == "attribute modifier":
            self.flaws[flawName]['type'] = "attribute modifier"
            self.flaws[flawName]['attribute'] = gameDefinitions['game']['defaults']['flaws'][flawName]['attribute']
            self.flaws[flawName]['intensity'] = gameDefinitions['game']['defaults']['flaws'][flawName]['intensity']
         elif gameDefinitions['game']['defaults']['flaws'][flawName]['type'] == "skill roll modifier":
            self.flaws[flawName]['type'] = "skill roll modifier"
            self.flaws[flawName]['skill'] = gameDefinitions['game']['defaults']['flaws'][flawName]['skill']
            self.flaws[flawName]['intensity'] = gameDefinitions['game']['defaults']['flaws'][flawName]['intensity']
         else:
            self.talents[talentName]['type'] = "other"

      for talentName in gameDefinitions['game']['defaults']['talents']:
         self.talents[talentName] = {}
         self.talents[talentName]['value'] = gameDefinitions['game']['defaults']['talents'][talentName]['value']
         self.talents[talentName]['max'] = gameDefinitions['game']['defaults']['talents'][talentName]['max']

         if gameDefinitions['game']['defaults']['talents'][talentName]['type'] == "attribute modifier":
            self.talents[talentName]['type'] = "attribute modifier"
            self.talents[talentName]['attribute'] = gameDefinitions['game']['defaults']['talents'][talentName]['attribute']
            self.talents[talentName]['intensity'] = gameDefinitions['game']['defaults']['talents'][talentName]['intensity']
         else:
            self.talents[talentName]['type'] = "other"

      for talentName in gameDefinitions['game']['defaults']['talents']:
         self.talents[talentName] = {}
         self.talents[talentName]['value'] = gameDefinitions['game']['defaults']['talents'][talentName]['value']
         self.talents[talentName]['max'] = gameDefinitions['game']['defaults']['talents'][talentName]['max']

         if gameDefinitions['game']['defaults']['talents'][talentName]['type'] == "attribute modifier":
            self.talents[talentName]['type'] = "attribute modifier"
            self.talents[talentName]['attribute'] = gameDefinitions['game']['defaults']['talents'][talentName]['attribute']
            self.talents[talentName]['intensity'] = gameDefinitions['game']['defaults']['talents'][talentName]['intensity']
         else:
            self.talents[talentName]['type'] = "other"



      for race in gameDefinitions['game']['races']:
         self.races.append(race)

      del gameDefinitions

class Race:
   def __init__(self, raceName, defaults):
      self.name            = raceName
      self.attributes      = copy.deepcopy(defaults.attributes)
      self.skills          = copy.deepcopy(defaults.skills)
      self.talents         = copy.deepcopy(defaults.talents)
      self.flaws           = copy.deepcopy(defaults.flaws)
      self.skillBonusXP    = defaults.skillBonusXP
      self.talentBonusXP   = defaults.talentBonusXP

      gameDefinitionsFile = open(defaults.gameDefinitionsFilePath, "r")
      gameDefinitions = yaml.load(gameDefinitionsFile, Loader=yaml.FullLoader)
      gameDefinitionsFile.close()

      for attributeName, attributeValue in self.attributes.items():
         if "attributes" in gameDefinitions['game']['races'][raceName] and \
            attributeName in gameDefinitions['game']['races'][raceName]['attributes']:
            self.attributes[attributeName] += gameDefinitions['game']['races'][raceName]['attributes'][attributeName]

      for skillName in self.skills:
         if "skills" in gameDefinitions['game']['races'][raceName] and \
            skillName in gameDefinitions['game']['races'][raceName]['skills']:
            self.skills[skillName]['value'] += gameDefinitions['game']['races'][raceName]['skills'][skillName]['value']

            for specializationName in self.skills[skillName]['specializations']:
               if 'specializations' in gameDefinitions['game']['races'][raceName]['skills'][skillName] and \
                 specializationName in gameDefinitions['game']['races'][raceName]['skills'][skillName]['specializations']:
                  self.skills[skillName]['specializations'][specilizationName]['value'] += gameDefinitions['game']['races'][raceName]['skills'][skillName]['specializations'][specilizationName]['value']

      for talentName in self.talents:
         if "talents" in gameDefinitions['game']['races'][raceName] and \
            talentName in gameDefinitions['game']['races'][raceName]['talents']:
            self.talents[talentName]['value'] += gameDefinitions['game']['races'][raceName]['talents'][talentName]['value']

      for flawName in self.flaws:
         if "flaws" in gameDefinitions['game']['races'][raceName] and \
            flawName in gameDefinitions['game']['races'][raceName]['flaws']:
            self.flaws[flawName]['value'] += gameDefinitions['game']['races'][raceName]['flaws'][flawName]['value']

      if "skillBonusXP" in gameDefinitions['game']['races'][raceName]:
          self.skillBonusXP += gameDefinitions['game']['races'][raceName]['skillBonusXP']

      if "talentBonusXP" in gameDefinitions['game']['races'][raceName]:
          self.talentBonusXP += gameDefinitions['game']['races'][raceName]['talentBonusXP']

class CharacterTemplate:
   def __init__(self, defaults):
      self.attributes      = copy.deepcopy(defaults.attributes)
      self.skills          = copy.deepcopy(defaults.skills)
      self.talents         = copy.deepcopy(defaults.talents)
      self.flaws           = copy.deepcopy(defaults.flaws)
      self.skillBonusXP    = defaults.skillBonusXP
      self.talentBonusXP   = defaults.talentBonusXP

   def modifyAttribute(attributeName, intensity):
      print("test")

   def modifySkill(skillName, intensity):
      print("test")

   def modifySpecialization(skillName, specialization, intensity):
      print("test")

   def modifyTalent(talentName, intensity):
      print("test")

   def modifyFlaw(flawName, intensity):
      print("test")

gameDefinitionFile="gamedefs.yaml"
MaxXP=150
defaults = Defaults(gameDefinitionFile, MaxXP)

races = {}
for race in defaults.races:
   races[race] = Race(race, defaults)

mytemplate = CharacterTemplate
#mytemplate.increaseAttribute("strength", amount)  #only allow primary attributes
#mytemplate.decreaseAttribute("agility", amount)

#sanity checks should check xp, min/max attrib/skill/talent/flaw values of template itself
#just run up tab of xp isolated to attributes, skills, and talents then add together reducing bonusxp at the end

#characer is then combination of template and race

#print(races['ork'].skills)

      #self.power        = floor ( ( self.strength     + self.agility ) / 2 )
      #self.reflex       = floor ( ( self.agility      + self.intelligence ) / 2 )
      #self.awareness    = floor ( ( self.intelligence + self.willpower ) / 2 )
      #self.resistance   = floor ( ( self.will         + self.strength ) / 2 )
