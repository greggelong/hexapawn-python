# hexapawn py

herBrain = []

boardStates = ["CCC---HHH"] # list of strings tht Identify board states

herBrain.append( {
  'board': "CCCH---HH",
  'gameMove':"2 left",
  'expl': "computer starts with list of three possible moves",
  "compMove":["C-CHC--HH",
                "CC-H-C-HH",
                "C-CC---HH"]})

herBrain.append({
  'board': "CCC--HHH-",
  'gameMove':"2 right",
  'expl': "computer starts with list of three possible moves",
  "compMove":["C-C-CHHH-",
           "-CCC-HHH-",
           "C-C--CHH-"]})

def printBoard(bstring):
    print("*"*12)
    print(bstring[0:3])
    print(bstring[3:6])
    print(bstring[6:9])




for i in herBrain:
    print(i["compMove"], i["gameMove"],boardStates)
    for j in i["compMove"]:
        printBoard(j)

