def Fruits(type, season):
    if type == "fruits" and season == "hiver": 
        print("orange, mandarine et kiwi")
    if type == "fruits" and season == "été":
        print("poire, fraise et cassis")
    if type == "legume" and season == "hiver":
        print("carott, topinambour et endive")
    if type == "legume" and season == "été":
        print("artichaud, aubergine et navet")

Fruits("legume", "été")