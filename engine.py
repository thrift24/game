#!/usr/bin/python3
import copy
import yaml

class Defaults:
   def __init__(self, gameDefinitionsFilePath):
      self.gameDefinitionsFilePath=gameDefinitionsFilePath
       
      self.XP                = {}
      self.spentXP           = {}
      self.attributes        = {}
      self.skills            = {}
      self.talents           = {}
      self.flaws             = {}
      self.races             = []

      gameDefinitionsFile = open(self.gameDefinitionsFilePath, "r")
      gameDefinitions = yaml.load(gameDefinitionsFile, Loader=yaml.FullLoader)
      gameDefinitionsFile.close()

      for XPType in gameDefinitions['game']['defaults']['xp']:
         self.XP[XPType] = gameDefinitions['game']['defaults']['xp'][XPType]

      for XPType in gameDefinitions['game']['defaults']['spentxp']:
         self.spentXP[XPType] = gameDefinitions['game']['defaults']['spentxp'][XPType]

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

#class Race:
#   def __init__(self, raceName, defaults):
#      self.name            = raceName
#      self.attributes      = copy.deepcopy(defaults.attributes)
#      self.skills          = copy.deepcopy(defaults.skills)
#      self.talents         = copy.deepcopy(defaults.talents)
#      self.flaws           = copy.deepcopy(defaults.flaws)
#      self.skillBonusXP    = defaults.skillBonusXP
#      self.talentBonusXP   = defaults.talentBonusXP
#
#      gameDefinitionsFile = open(defaults.gameDefinitionsFilePath, "r")
#      gameDefinitions = yaml.load(gameDefinitionsFile, Loader=yaml.FullLoader)
#      gameDefinitionsFile.close()
#
#      for attributeName, attributeValue in self.attributes.items():
#         if "attributes" in gameDefinitions['game']['races'][raceName] and \
#            attributeName in gameDefinitions['game']['races'][raceName]['attributes']:
#            self.attributes[attributeName] += gameDefinitions['game']['races'][raceName]['attributes'][attributeName]
#
#      for skillName in self.skills:
#         if "skills" in gameDefinitions['game']['races'][raceName] and \
#            skillName in gameDefinitions['game']['races'][raceName]['skills']:
#            self.skills[skillName]['value'] += gameDefinitions['game']['races'][raceName]['skills'][skillName]['value']
#
#            for specializationName in self.skills[skillName]['specializations']:
#               if 'specializations' in gameDefinitions['game']['races'][raceName]['skills'][skillName] and \
#                 specializationName in gameDefinitions['game']['races'][raceName]['skills'][skillName]['specializations']:
#                  self.skills[skillName]['specializations'][specilizationName]['value'] += gameDefinitions['game']['races'][raceName]['skills'][skillName]['specializations'][specilizationName]['value']
#
#      for talentName in self.talents:
#         if "talents" in gameDefinitions['game']['races'][raceName] and \
#            talentName in gameDefinitions['game']['races'][raceName]['talents']:
#            self.talents[talentName]['value'] += gameDefinitions['game']['races'][raceName]['talents'][talentName]['value']
#
#      for flawName in self.flaws:
#         if "flaws" in gameDefinitions['game']['races'][raceName] and \
#            flawName in gameDefinitions['game']['races'][raceName]['flaws']:
#            self.flaws[flawName]['value'] += gameDefinitions['game']['races'][raceName]['flaws'][flawName]['value']
#
#      if "skillBonusXP" in gameDefinitions['game']['races'][raceName]:
#          self.skillBonusXP += gameDefinitions['game']['races'][raceName]['skillBonusXP']
#
#      if "talentBonusXP" in gameDefinitions['game']['races'][raceName]:
#          self.talentBonusXP += gameDefinitions['game']['races'][raceName]['talentBonusXP']

class CharacterTemplate:
   def __init__(self, defaults, trackXP=True, checkCaps=True):
      self.XP               = copy.deepcopy(defaults.XP)
      self.spentXP          = copy.deepcopy(defaults.spentXP)
      self.attributes       = copy.deepcopy(defaults.attributes)
      self.skills           = copy.deepcopy(defaults.skills)
      self.talents          = copy.deepcopy(defaults.talents)
      self.flaws            = copy.deepcopy(defaults.flaws)

      self.trackXP=trackXP

      self.log = [ "Initial Character Creation" ]

   def modifyXP(self, XPType, intensity):
      self.XP[XPType] += intensity
      self.log.append("Modified XP: XPType=" + XPType + " Intensity=" + str(intensity))

   def printXP(self):
      print("XP:")
      for XPType, XPValue in self.XP.items():
         print("\t" + XPType + ": " + str(XPValue))
      print("Spent XP:")
      for XPType, XPValue in self.spentXP.items():
         print("\t" + XPType + ": " + str(XPValue))

   def modifyAttributes(self, attributeName, intensity):
      if self.trackXP:
         for rank in range(self.attributes[attributeName],self.attributes[attributeName]+intensity):
            print("intensity: " + str(intensity) + "base: " + str(self.attributes[attributeName]))
            if intensity < 0: #issue here
               if self.attribute[attributeName] != 0:
                  print("Bad Human!")
                  sys.exit(1)
               else:
                  self.spentXP['attributes'] += (rank+1)*self.XP['attributesRankCostFactor'] * -1
            else:
               self.spentXP['attributes'] += (rank+1)*self.XP['attributesRankCostFactor']

      self.attributes[attributeName] += intensity
      self.log.append("Modified Atribute: attributeName=\"" + attributeName + "\" Intensity=" + str(intensity))

   def printAttributes(self):
      print("Attributes:")
      for attributeName, attributeValue in self.attributes.items():
         print("\t" + attributeName + ": " + str(attributeValue))

   def modifySkills(self, skillName, intensity):
      if self.trackXP:
         for rank in range(self.skills[skillName]['value'],self.skills[skillName]['value']+intensity):
            self.spentXP['skills'] += (rank+1)*self.XP['skillsRankCostFactor']

      self.skills[skillName]['value'] += intensity
      self.log.append("Modified Skill: skillName=\"" + skillName + "\" Intensity=" + str(intensity))

   def printSkillTree(self):
      print("Skills:")
      for skillName, skillDetails in self.skills.items():
         print("\t" + skillName + ": " + str(skillDetails['value']))

         for specializationName, specializationValue in skillDetails['specializations'].items():
            print("\t\t" + specializationName + ": " + str(specializationValue))

   def modifySpecializations(self, skillName, specializationName, intensity):
      if self.trackXP:
         for rank in range(self.skills[skillName]['specializations'][specializationName],self.skills[skillName]['specializations'][specializationName]+intensity):
            self.spentXP['skills'] += (rank+1)*self.XP['skillsRankCostFactor']

      self.skills[skillName]['specializations'][specializationName] += intensity
      self.log.append("Modified Specialization: skillName=\"" + skillName + "\" specializationName=" + specializationName + " Intensity=" + str(intensity))

   def modifyTalents(self, talentName, intensity):
      if self.trackXP:
         talentsTaken=0
         for takenTalentName,takenTalentDetails in self.talents.items():
            if takenTalentDetails['value'] > 0:
               talentsTaken += 1
         for rank in range(self.talents[talentName]['value'],self.talents[talentName]['value']+intensity):
            self.spentXP['talents'] += (talentsTaken + 1) * ( rank + 1 ) * self.XP['talentRankCostFactor']

      self.talents[talentName]['value'] += intensity
      self.log.append("Modified Talent: talentName=\"" + talentName + "\" Intensity=" + str(intensity))

   def printTalents(self):
      print("Talents:")
      for talentName, talentDetails in self.talents.items():
         print("\t" + talentName + ": " + str(talentDetails['value']))

   def modifyFlaws(self, flawName, enabled):
      if enabled:
         self.flaws[flawName]['value'] = 1
         self.log.append("Modified Flaw: flawName=\"" + talentName + "\" Enabled")
      else: 
         self.flaws[flawName]['value'] = 0
         self.log.append("Modified Flaw: flawName=\"" + talentName + "\" Disabled")

   def printFlaws(self):
      print("Flaws:")
      for flawName, flawDetails in self.flaws.items():
         print("\t" + flawName + ": " + str(flawDetails['value']))

gameDefinitionFile="gamedefs.yaml"
defaults = Defaults(gameDefinitionFile)

myTemplate = CharacterTemplate(defaults, True, False)
myTemplate.printXP()
myTemplate.modifyAttributes("willpower", 1)
myTemplate.printXP()
myTemplate.modifyAttributes("willpower", 1)
myTemplate.printXP()
myTemplate.modifyAttributes("willpower", -1)
myTemplate.printXP()
print(myTemplate.log)

#races = {}
#for race in defaults.races:
#   races[race] = Race(race, defaults)

#mytemplate.increaseAttribute("strength", amount)  #only allow primary attributes
#mytemplate.decreaseAttribute("agility", amount)

#sanity checks should check XP, min/max attrib/skill/talent/flaw values of template itself
#just run up tab of XP isolated to attributes, skills, and talents then add together reducing bonusXP at the end

#characer is then combination of template and race

#print(races['ork'].skills)

      #self.power        = floor ( ( self.strength     + self.agility ) / 2 )
      #self.reflex       = floor ( ( self.agility      + self.intelligence ) / 2 )
      #self.awareness    = floor ( ( self.intelligence + self.willpower ) / 2 )
      #self.resistance   = floor ( ( self.will         + self.strength ) / 2 )
