Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print("Q1 Do you like Dawn or Dusk?")
print("1 Dawn")
print("2 Dusk")
q_1 = int(input())
if q_1 == 1:
  Gryffindor = Gryffindor + 1 
  Ravenclaw = Ravenclaw + 1
elif q_1 == 2:
  Hufflepuff = Hufflepuff + 1
  Slytherin = Slytherin + 1
else:
  print("Wrong input")
print("Q2 When I'm dead, I want people to remember me as:")
print("1 The Good")
print("2 The Great")
print("3 The Wise")
print("4 The Bold")

q_2 = int(input())
if q_2 == 1:
  Gryffindor = Gryffindor + 1
elif q_2 == 2:
  Ravenclaw = Ravenclaw + 1
elif q_2 == 3:
  Hufflepuff = Hufflepuff + 1
elif q_2 == 4:
  Slytherin = Slytherin + 1
else:
  print("Wrong input")

print("Q3  Which kind of instrument most pleases your ear?")
print("1 The violin")
print("2 The trumpet")
print("3 The piano")
print("4 The drum")
 
q_3 = int(input())
if q_3 == 1:
  Gryffindor = Gryffindor + 1
elif q_3 == 2:
  Ravenclaw = Ravenclaw + 1
elif q_3 == 3:
  Hufflepuff = Hufflepuff + 1
elif q_3 == 4:
  Slytherin =  Slytherin + 1
else:
  print("Wrong input")
print("Final score for your selection-")
print("Gryffindor:",Gryffindor)
print("Ravenclaw:",Ravenclaw)
print("Hufflepuff:",Hufflepuff)
print("Slytherin:",Slytherin)

score = {Gryffindor, Ravenclaw , Hufflepuff , Slytherin}
print("you are chosen in -")
if max(score) == Gryffindor:
  print("Gryffinfor")
elif max(score) == Ravenclaw:
  print("Ravenclaw")
elif max(score) == Hufflepuff:
  print("Hufflepuff")
elif max(score) == Slytherin:
  print("Slytherin")