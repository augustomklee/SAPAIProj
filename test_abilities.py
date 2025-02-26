# Different pet abilities
# Shark, Hippo

# The shark seems to be buggy, could be the graph
from sapai import Pet,Food,Team,Battle
from sapai.graph import graph_battle

t0 = Team(["sheep", "deer", "shark"])

hippo = Pet("hippo")

teamHippo = Team([hippo])

pig = Pet("pig")
teamPig = Team([pig])

hippo._attack += 20
hippo._health += 20

pig._attack -= 3
pig._health += 20

# Battle between shark team
# Shark stops summons from going through,
# Also may upgrade on deaths from enemy team
# Seems like it might disable abilities?
b = Battle(t0,teamHippo)
winner = b.battle()
print("WINNER: {}".format(winner))

graph_battle(b, file_name="sharkBug1")

# Shark is increasing stats from enemy team kills
t0 = Team(["shark"])
t1 = Team(["cricket", "cricket", "spider"])

b = Battle(t0,t1)
winner = b.battle()
print("WINNER: {}".format(winner))

graph_battle(b, file_name="sharkBug2")

#Updating on ally kills

t0 = Team([hippo, "shark"])
t1 = Team(["cricket", "cricket", "spider"])

b = Battle(t0,t1)
winner = b.battle()
print("WINNER: {}".format(winner))

graph_battle(b, file_name="sharkBug3")

#Hippo is not capped

t0 = Team(["hippo"])
t1 = Team(["cricket", "cricket", "spider"])

b = Battle(t0,t1)
winner = b.battle()
print("WINNER: {}".format(winner))

graph_battle(b, file_name="hippoBug")


# Rat bug, one rat summons and instantly dies

t0 = Team(["rat"])
t1 = Team(["rat"])

b = Battle(t0,t1)
winner = b.battle()
print("WINNER: {}".format(winner))

graph_battle(b, file_name="testRat")


#TODO

#Ox, Skunk, Blowfish, Turtle, Parrot, Crocodile, rhino, armadillo, rooster, turkey, leopard, boar, tiger, wolverine, gorilla, mammoth, snake