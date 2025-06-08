#importing packages
import math
import random
import turtle
turtle.colormode(255)
p1score = 0
#Setting up hangtree
p2score = 0
print("Welcome to the 2 player arcade with 2 fun games!")
nickp1 = input("Player 1, type a nickname you would like to use! ")
nickp2 = input("Player 2, type a nickname you would like to use! ")
print('Keep switching between the result and console to play the games.')
print("Welcome to Hangtree, try to guess as many letters as you can of an unknown word.")
print('Please go to the result until the stand is finished.')
screen = turtle.Screen()
screen.bgcolor(0, 255, 0)
screen.tracer(0)
treeParts = turtle.Turtle()
treeParts.penup()
treeParts.hideturtle()
treeParts.speed(1000)
stand = turtle.Turtle()
stand.speed(1000)
stand.penup()
stand.goto(-400, -400)
stand.setheading(0)
stand.color(51, 153, 255)
stand.begin_fill()
for i in range(4):
  if i % 2 == 0:
    stand.forward(400)
    stand.left(90)
  else:
    stand.forward(50)
    stand.left(90)
stand.end_fill()
stand.goto(-175, -350)
stand.setheading(90)
stand.color(0, 128, 255)
stand.begin_fill()
for i in range(4):
  if i % 2 == 0:
    stand.forward(700)
    stand.left(90)
  else:
    stand.forward(50)
    stand.left(90)
stand.end_fill()
stand.goto(-225, 350)
stand.setheading(0)
stand.color(51, 153, 255)
stand.begin_fill()
for i in range(4):
  if i % 2 == 0:
    stand.forward(425)
    stand.left(90)
  else:
    stand.forward(50)
    stand.left(90)
stand.end_fill()
stand.hideturtle()
screen.update()
#Playing hangtree
def currentWordState(gw, cw):
  out = ""
  for i in range(len(cw)):
    if cw[i] not in gw:
      out += " _"
    else:
      out += " " + str(cw[i])
  return out
for d in range(2):
  cd = 6
  if d % 2 == 0:
    print(nickp1 + ', it is your turn to guess!')
    correctword = input(nickp2 + ', please type a word for ' + nickp1 + ' to guess(please make it a word and not random letters): ')
  else:
    print(nickp2 + ', it is your turn to guess!')
    correctword = input(nickp1 + ', please type a word for ' + nickp2 + ' to guess(please make it a word and not random letters): ')
  for i in range(0, 100):
    print('')
  correctword = correctword.lower()
  correctwordset = set()
  guessedword = set()
  for i in range(0, len(correctword)):
    correctwordset.add(correctword[i])
  while cd > 0:
    print(currentWordState(guessedword, correctword))
    print("You have " + str(cd) + " guess(es) remaining.")
    guessedletter = input("Guess a letter: ")
    guessedletter = guessedletter.lower()
    for i in range(0, 100):
      print('')
    if guessedletter in correctwordset:
      guessedword.add(guessedletter)
    elif guessedletter not in correctwordset:
      cd -= 1
      if cd == 5:
        treeParts.goto(200, 350)
        treeParts.setheading(270)
        treeParts.color(48, 38, 33)
        treeParts.begin_fill()
        for i in range(4):
          if i % 2 == 0:
            treeParts.forward(350)
            treeParts.right(90)
          else:
            treeParts.forward(50)
            treeParts.right(90)
        treeParts.end_fill()
      elif cd == 4:
        treeParts.goto(200, 0)
        treeParts.setheading(270)
        treeParts.color(48, 38, 33)
        treeParts.begin_fill()
        for i in range(4):
          if i % 2 == 0:
            treeParts.forward(350)
            treeParts.right(90)
          else:
            treeParts.forward(50)
            treeParts.right(90)
        treeParts.end_fill()
        treeParts.forward(175)
        treeParts.right(90)
        treeParts.forward(225)
      elif cd < 4 and cd > 0:
        treeParts.color(3, 125, 80)
        treeParts.right(120)
        treeParts.begin_fill()
        for i in range(3):
          treeParts.forward(400)
          treeParts.right(120)
        treeParts.end_fill()
        treeParts.left(30)
        treeParts.forward(115)
        treeParts.left(90)
        treeParts.end_fill()
    if len(guessedword.intersection(correctwordset)) == len(correctwordset):
      if d % 2 == 0:
        print("Nice job " + nickp1 + " you won, the correct word is: " + correctword + ".")
        p1score += 1
      else:
        print("Nice job " + nickp2 + " you won, the correct word is: " + correctword + ".")
        p2score += 1
      break
    screen.update()
  if cd == 0:
    treeParts.pensize(4)
    treeParts.color(48, 38, 33)
    treePartTempAngle = 315
    treePartTempXPosition = 200
    for i in range(5):
      treeParts.goto(treePartTempXPosition, -350)
      treePartTempXPosition -= 12.5
      treeParts.setheading(treePartTempAngle)
      treePartTempAngle -= 22.5
      treeParts.pendown()
      treeParts.forward(50)
      treeParts.setheading(random.randint(180, 360))
      treeParts.forward(random.randint(50, 100))
      treeParts.penup()
      screen.update()
    input("Sorry you hung the tree, the correct word is: " + correctword + ". Press enter to continue.")
    if d % 2 == 0:
      p2score += 1
    else:
      p1score += 1
  treeParts.clear()
  screen.update()
  print(nickp1 + ", you have " + str(p1score) + " points.")
  print(nickp2 + ", you have " + str(p2score) + " points.")
#Setting up polluted water and logs ultimate
print("Let's play Polluted Water and Logs Ultimate!")
hmb = input("Type in how many blocks you want(Type a perfect square from 25 to 400 or press enter too set as default). ")
if hmb == '':
  hmb = 100
else:
  hmb = int(hmb)
  while not (math.sqrt(hmb) * math.sqrt(hmb) == hmb) or hmb > 400 or hmb < 25:
    hmb = input("Seems like you made a mistake, Type in how many blocks you want(Type a perfect square from 25 to 400 or press enter too set as default). ")
    if hmb == '':
      hmb = 100
      break
    hmb = int(hmb)
r = set()
t = set()
p1 = 0
p2 = 0
f = True
while f:
  r = set()
  t = set()
  s1 = [random.randint((hmb // 2) + 1, hmb - 1), random.randint(5, (hmb // 2) - 1)]
  s2 = [random.randint((hmb // 2) + 1, hmb - 1), random.randint(5, (hmb // 2) - 1)]
  s3 = [random.randint((hmb // 2) + 1, hmb - 1), random.randint(5, (hmb // 2) - 1)]
  s4 = [random.randint((hmb // 2) + 1, hmb - 1), random.randint(5, (hmb // 2) - 1)]
  s5 = [random.randint((hmb // 2) + 1, hmb - 1), random.randint(5, (hmb // 2) - 1)]
  s6 = [random.randint((hmb // 2) + 1, hmb - 1), random.randint(5, (hmb // 2) - 1)]
  s7 = [random.randint((hmb // 2) + 1, hmb - 1), random.randint(5, (hmb // 2) - 1)]
  s8 = [random.randint((hmb // 2) + 1, hmb - 1), random.randint(5, (hmb // 2) - 1)]
  s9 = [random.randint((hmb // 2) + 1, hmb - 1), random.randint(5, (hmb // 2) - 1)]
  s10 = [random.randint((hmb // 2) + 1, hmb - 1), random.randint(5, (hmb // 2) - 1)]
  l1 = [random.randint(5, (hmb // 2) - 1), random.randint((hmb // 2) + 1, hmb - 1)]
  l2 = [random.randint(5, (hmb // 2) - 1), random.randint((hmb // 2) + 1, hmb - 1)]
  l3 = [random.randint(5, (hmb // 2) - 1), random.randint((hmb // 2) + 1, hmb - 1)]
  l4 = [random.randint(5, hmb //2), random.randint((hmb // 2) + 1, hmb - 1)]
  l5 = [random.randint(5, (hmb // 2) - 1), random.randint((hmb // 2) + 1, hmb - 1)]
  l6 = [random.randint(5, (hmb // 2) - 1), random.randint((hmb // 2) + 1, hmb - 1)]
  l7 = [random.randint(5, (hmb // 2) - 1), random.randint((hmb // 2) + 1, hmb - 1)]
  l8 = [random.randint(5, (hmb // 2) - 1), random.randint((hmb // 2) + 1, hmb - 1)]
  l9 = [random.randint(5, (hmb // 2) - 1), random.randint((hmb // 2) + 1, hmb - 1)]
  l10 = [random.randint(5, (hmb // 2) - 1), random.randint((hmb // 2) + 1, hmb - 1)]
  if hmb > 24 and hmb < 99:
    r.add(s1[0])
    t.add(s1[1])
    r.add(s2[0])
    t.add(s2[1])
    r.add(l1[1])
    t.add(l1[0])
    r.add(l2[1])
    t.add(l2[0])
    if len(r) == 4 and len(t) == 4:
      f = False
  elif hmb > 98 and hmb < 174:
    r.add(s1[0])
    t.add(s1[1])
    r.add(s2[0])
    t.add(s2[1])
    r.add(s3[0])
    t.add(s3[1])
    r.add(s4[0])
    t.add(s4[1])
    r.add(l1[1])
    t.add(l1[0])
    r.add(l2[1])
    t.add(l2[0])
    r.add(l3[1])
    t.add(l3[0])
    r.add(l4[1])
    t.add(l4[0])
    if len(r) == 8 and len(t) == 8:
      f = False
  elif hmb > 173 and hmb < 249:
    r.add(s1[0])
    t.add(s1[1])
    r.add(s2[0])
    t.add(s2[1])
    r.add(s3[0])
    t.add(s3[1])
    r.add(s4[0])
    t.add(s4[1])
    r.add(s5[0])
    t.add(s5[1])
    r.add(s6[0])
    t.add(s6[1])
    r.add(l1[1])
    t.add(l1[0])
    r.add(l2[1])
    t.add(l2[0])
    r.add(l3[1])
    t.add(l3[0])
    r.add(l4[1])
    t.add(l4[0])
    r.add(l5[1])
    t.add(l5[0])
    r.add(l6[1])
    t.add(l6[0])
    if len(r) == 12 and len(t) == 12:
      f = False
  elif hmb > 248 and hmb < 324:
    r.add(s1[0])
    t.add(s1[1])
    r.add(s2[0])
    t.add(s2[1])
    r.add(s3[0])
    t.add(s3[1])
    r.add(s4[0])
    t.add(s4[1])
    r.add(s5[0])
    t.add(s5[1])
    r.add(s6[0])
    t.add(s6[1])
    r.add(s7[0])
    t.add(s7[1])
    r.add(s8[0])
    t.add(s8[1])
    r.add(l1[1])
    t.add(l1[0])
    r.add(l2[1])
    t.add(l2[0])
    r.add(l3[1])
    t.add(l3[0])
    r.add(l4[1])
    t.add(l4[0])
    r.add(l5[1])
    t.add(l5[0])
    r.add(l6[1])
    t.add(l6[0])
    r.add(l7[1])
    t.add(l7[0])
    r.add(l8[1])
    t.add(l8[0])
    if len(r) == 16 and len(t) == 16:
      f = False
  elif hmb > 323 and hmb < 401:
    r.add(s1[0])
    t.add(s1[1])
    r.add(s2[0])
    t.add(s2[1])
    r.add(s3[0])
    t.add(s3[1])
    r.add(s4[0])
    t.add(s4[1])
    r.add(s5[0])
    t.add(s5[1])
    r.add(s6[0])
    t.add(s6[1])
    r.add(s7[0])
    t.add(s7[1])
    r.add(s8[0])
    t.add(s8[1])
    r.add(s9[0])
    t.add(s9[1])
    r.add(s10[0])
    t.add(s10[1])
    r.add(l1[1])
    t.add(l1[0])
    r.add(l2[1])
    t.add(l2[0])
    r.add(l3[1])
    t.add(l3[0])
    r.add(l4[1])
    t.add(l4[0])
    r.add(l5[1])
    t.add(l5[0])
    r.add(l6[1])
    t.add(l6[0])
    r.add(l7[1])
    t.add(l7[0])
    r.add(l8[1])
    t.add(l8[0])
    r.add(l9[1])
    t.add(l9[0])
    r.add(l10[1])
    t.add(l10[0])
    if len(r) == 20 and len(t) == 20:
      f = False
print("To play:")
if hmb > 24 and hmb < 99:
  print(nickp1 + " and " + nickp2 + " will take turns rolling 1 or 2 dice.")
elif hmb > 98 and hmb < 174:
  print(nickp1 + " and " + nickp2 + " will take turns rolling 1, 2, 3 or 4 dice.")
elif hmb > 173 and hmb < 249:
  print(nickp1 + " and " + nickp2 + " will take turns rolling 1, 2, 3, 4, 5 or 6 dice.")
elif hmb > 248 and hmb < 324:
  print(nickp1 + " and " + nickp2 + " will take turns rolling 1, 2, 3, 4, 5, 6, 7 or 8 dice.")
elif hmb > 323 and hmb < 401:
  print(nickp1 + " and " + nickp2 + " will take turns rolling 1, 2, 3, 4, 5, 6, 7, 8, 9 or 10 dice.")
print("Whatever the dice lands on, " + nickp1 + " or " + nickp2 + " will move forward.")
print(nickp1 + " is red and " + nickp2 + " is orange.")
print("If you land on a polluted waterfall, you go back some blocks.")
print("If you land on a log, you go up some blocks.")
print("If you get to a block equal to " + str(hmb) + ", you win!")
print("Please go to the result until the game board is built.")
stand.clear()
sq1 = turtle.Turtle()
sq1.penup()
sq1.speed(-15)
sq1.goto(-400, -400)
numbers = []
numTurtDict = {}
for i in range(0, hmb):
  numbers.append(str(i))
for number in numbers:
  numTurtDict[number] = turtle.Turtle()
  numTurtDict[number].speed(1000)
  numTurtDict[number].hideturtle()
  numTurtDict[number].penup()
  numTurtDict[number].goto(-400 + (800 / int(math.sqrt(hmb))) / 2, -400 + (800 / int(math.sqrt(hmb))) / 2)
def square(t, l):
  for i in range(4):
    t.forward(l)
    t.left(90)
temp = -400
for j in range(0, int(math.sqrt(hmb))):
  for i in range(1, int(math.sqrt(hmb)) + 1):
    if j % 2 == 0:
      if i % 2 == 0:
        sq1.color(0, 128, 255)
      else:
        sq1.color(51, 153, 255)
    else:
      if i % 2 == 0:
        sq1.color(51, 153, 255)
      else:
        sq1.color(0, 128, 255)
    sq1.begin_fill()
    square(sq1, 800 / int(math.sqrt(hmb)))
    sq1.end_fill()
    sq1.forward(800 / int(math.sqrt(hmb)))
  temp += 800 / int(math.sqrt(hmb))
  sq1.goto(-400, temp)
sq1.hideturtle()
temp2 = -400 + (800 / int(math.sqrt(hmb))) / 2
temp2y = -400 + (800 / int(math.sqrt(hmb))) / 2
t = 0
for j in range(0, int(math.sqrt(hmb))):
  for i in range(t, t + int(math.sqrt(hmb))):
    numTurtDict[str(i)].goto(temp2, temp2y)
    temp2 += 800 / int(math.sqrt(hmb))
  temp2 = -400 + (800 / int(math.sqrt(hmb))) / 2
  temp2y += 800 / int(math.sqrt(hmb))
  t += int(math.sqrt(hmb))
tree = turtle.Turtle()
tree.penup()
def Distance(x1,y1,x2,y2):  
  distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)  
  return distance
def logsOrWater(distance, l, r, g, b):
  tree.speed(1000)
  tree.setheading(tree.towards(l))
  tree.right(90)
  tree.forward(25)
  tree.left(180)
  tree.color(r, g, b)
  tree.begin_fill()
  for i in range(4):
    if i % 2 == 0:
      tree.forward(50)
    else:
      tree.forward(distance)
    tree.right(90)
  tree.end_fill()
colorR = 48
colorG = 38
colorB = 33
if hmb > 24 and hmb < 99:
  tree.goto(numTurtDict[str(l1[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(l1[1] - 1)].xcor(), numTurtDict[str(l1[1] - 1)].ycor()), numTurtDict[str(l1[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(l2[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(l2[1] - 1)].xcor(), numTurtDict[str(l2[1] - 1)].ycor()), numTurtDict[str(l2[1] - 1)], colorR, colorG, colorB)
  colorR = 22
  colorG = 216
  colorB = 145
  tree.goto(numTurtDict[str(s1[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(s1[1] - 1)].xcor(), numTurtDict[str(s1[1] - 1)].ycor()), numTurtDict[str(s1[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(s2[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(s2[1] - 1)].xcor(), numTurtDict[str(s2[1] - 1)].ycor()), numTurtDict[str(s2[1] - 1)], colorR, colorG, colorB)
elif hmb > 98 and hmb < 174:
  tree.goto(numTurtDict[str(l1[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(l1[1] - 1)].xcor(), numTurtDict[str(l1[1] - 1)].ycor()), numTurtDict[str(l1[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(l2[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(l2[1] - 1)].xcor(), numTurtDict[str(l2[1] - 1)].ycor()), numTurtDict[str(l2[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(l3[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(l3[1] - 1)].xcor(), numTurtDict[str(l3[1] - 1)].ycor()), numTurtDict[str(l3[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(l4[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(l4[1] - 1)].xcor(), numTurtDict[str(l4[1] - 1)].ycor()), numTurtDict[str(l4[1] - 1)], colorR, colorG, colorB)
  colorR = 22
  colorG = 216
  colorB = 145
  tree.goto(numTurtDict[str(s1[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(s1[1] - 1)].xcor(), numTurtDict[str(s1[1] - 1)].ycor()), numTurtDict[str(s1[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(s2[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(s2[1] - 1)].xcor(), numTurtDict[str(s2[1] - 1)].ycor()), numTurtDict[str(s2[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(s3[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(s3[1] - 1)].xcor(), numTurtDict[str(s3[1] - 1)].ycor()), numTurtDict[str(s3[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(s4[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(s4[1] - 1)].xcor(), numTurtDict[str(s4[1] - 1)].ycor()), numTurtDict[str(s4[1] - 1)], colorR, colorG, colorB)
elif hmb > 173 and hmb < 249:
  tree.goto(numTurtDict[str(l1[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(l1[1] - 1)].xcor(), numTurtDict[str(l1[1] - 1)].ycor()), numTurtDict[str(l1[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(l2[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(l2[1] - 1)].xcor(), numTurtDict[str(l2[1] - 1)].ycor()), numTurtDict[str(l2[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(l3[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(l3[1] - 1)].xcor(), numTurtDict[str(l3[1] - 1)].ycor()), numTurtDict[str(l3[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(l4[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(l4[1] - 1)].xcor(), numTurtDict[str(l4[1] - 1)].ycor()), numTurtDict[str(l4[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(l5[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(l5[1] - 1)].xcor(), numTurtDict[str(l5[1] - 1)].ycor()), numTurtDict[str(l5[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(l6[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(l6[1] - 1)].xcor(), numTurtDict[str(l6[1] - 1)].ycor()), numTurtDict[str(l6[1] - 1)], colorR, colorG, colorB)
  colorR = 22
  colorG = 216
  colorB = 145
  tree.goto(numTurtDict[str(s1[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(s1[1] - 1)].xcor(), numTurtDict[str(s1[1] - 1)].ycor()), numTurtDict[str(s1[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(s2[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(s2[1] - 1)].xcor(), numTurtDict[str(s2[1] - 1)].ycor()), numTurtDict[str(s2[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(s3[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(s3[1] - 1)].xcor(), numTurtDict[str(s3[1] - 1)].ycor()), numTurtDict[str(s3[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(s4[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(s4[1] - 1)].xcor(), numTurtDict[str(s4[1] - 1)].ycor()), numTurtDict[str(s4[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(s5[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(s5[1] - 1)].xcor(), numTurtDict[str(s5[1] - 1)].ycor()), numTurtDict[str(s5[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(s6[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(s6[1] - 1)].xcor(), numTurtDict[str(s6[1] - 1)].ycor()), numTurtDict[str(s6[1] - 1)], colorR, colorG, colorB)
elif hmb > 248 and hmb < 324:
  tree.goto(numTurtDict[str(l1[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(l1[1] - 1)].xcor(), numTurtDict[str(l1[1] - 1)].ycor()), numTurtDict[str(l1[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(l2[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(l2[1] - 1)].xcor(), numTurtDict[str(l2[1] - 1)].ycor()), numTurtDict[str(l2[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(l3[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(l3[1] - 1)].xcor(), numTurtDict[str(l3[1] - 1)].ycor()), numTurtDict[str(l3[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(l4[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(l4[1] - 1)].xcor(), numTurtDict[str(l4[1] - 1)].ycor()), numTurtDict[str(l4[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(l5[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(l5[1] - 1)].xcor(), numTurtDict[str(l5[1] - 1)].ycor()), numTurtDict[str(l5[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(l6[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(l6[1] - 1)].xcor(), numTurtDict[str(l6[1] - 1)].ycor()), numTurtDict[str(l6[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(l7[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(l7[1] - 1)].xcor(), numTurtDict[str(l7[1] - 1)].ycor()), numTurtDict[str(l7[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(l8[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(l8[1] - 1)].xcor(), numTurtDict[str(l8[1] - 1)].ycor()), numTurtDict[str(l8[1] - 1)], colorR, colorG, colorB)
  colorR = 22
  colorG = 216
  colorB = 145
  tree.goto(numTurtDict[str(s1[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(s1[1] - 1)].xcor(), numTurtDict[str(s1[1] - 1)].ycor()), numTurtDict[str(s1[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(s2[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(s2[1] - 1)].xcor(), numTurtDict[str(s2[1] - 1)].ycor()), numTurtDict[str(s2[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(s3[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(s3[1] - 1)].xcor(), numTurtDict[str(s3[1] - 1)].ycor()), numTurtDict[str(s3[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(s4[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(s4[1] - 1)].xcor(), numTurtDict[str(s4[1] - 1)].ycor()), numTurtDict[str(s4[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(s5[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(s5[1] - 1)].xcor(), numTurtDict[str(s5[1] - 1)].ycor()), numTurtDict[str(s5[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(s6[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(s6[1] - 1)].xcor(), numTurtDict[str(s6[1] - 1)].ycor()), numTurtDict[str(s6[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(s7[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(s7[1] - 1)].xcor(), numTurtDict[str(s7[1] - 1)].ycor()), numTurtDict[str(s7[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(s8[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(s8[1] - 1)].xcor(), numTurtDict[str(s8[1] - 1)].ycor()), numTurtDict[str(s8[1] - 1)], colorR, colorG, colorB)
elif hmb > 323 and hmb < 401:
  tree.goto(numTurtDict[str(l1[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(l1[1] - 1)].xcor(), numTurtDict[str(l1[1] - 1)].ycor()), numTurtDict[str(l1[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(l2[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(l2[1] - 1)].xcor(), numTurtDict[str(l2[1] - 1)].ycor()), numTurtDict[str(l2[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(l3[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(l3[1] - 1)].xcor(), numTurtDict[str(l3[1] - 1)].ycor()), numTurtDict[str(l3[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(l4[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(l4[1] - 1)].xcor(), numTurtDict[str(l4[1] - 1)].ycor()), numTurtDict[str(l4[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(l5[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(l5[1] - 1)].xcor(), numTurtDict[str(l5[1] - 1)].ycor()), numTurtDict[str(l5[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(l6[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(l6[1] - 1)].xcor(), numTurtDict[str(l6[1] - 1)].ycor()), numTurtDict[str(l6[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(l7[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(l7[1] - 1)].xcor(), numTurtDict[str(l7[1] - 1)].ycor()), numTurtDict[str(l7[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(l8[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(l8[1] - 1)].xcor(), numTurtDict[str(l8[1] - 1)].ycor()), numTurtDict[str(l8[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(l9[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(l9[1] - 1)].xcor(), numTurtDict[str(l9[1] - 1)].ycor()), numTurtDict[str(l9[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(l10[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(l10[1] - 1)].xcor(), numTurtDict[str(l10[1] - 1)].ycor()), numTurtDict[str(l10[1] - 1)], colorR, colorG, colorB)
  colorR = 22
  colorG = 216
  colorB = 145
  tree.goto(numTurtDict[str(s1[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(s1[1] - 1)].xcor(), numTurtDict[str(s1[1] - 1)].ycor()), numTurtDict[str(s1[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(s2[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(s2[1] - 1)].xcor(), numTurtDict[str(s2[1] - 1)].ycor()), numTurtDict[str(s2[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(s3[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(s3[1] - 1)].xcor(), numTurtDict[str(s3[1] - 1)].ycor()), numTurtDict[str(s3[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(s4[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(s4[1] - 1)].xcor(), numTurtDict[str(s4[1] - 1)].ycor()), numTurtDict[str(s4[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(s5[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(s5[1] - 1)].xcor(), numTurtDict[str(s5[1] - 1)].ycor()), numTurtDict[str(s5[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(s6[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(s6[1] - 1)].xcor(), numTurtDict[str(s6[1] - 1)].ycor()), numTurtDict[str(s6[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(s7[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(s7[1] - 1)].xcor(), numTurtDict[str(s7[1] - 1)].ycor()), numTurtDict[str(s7[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(s8[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(s8[1] - 1)].xcor(), numTurtDict[str(s8[1] - 1)].ycor()), numTurtDict[str(s8[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(s9[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(s9[1] - 1)].xcor(), numTurtDict[str(s9[1] - 1)].ycor()), numTurtDict[str(s9[1] - 1)], colorR, colorG, colorB)
  tree.goto(numTurtDict[str(s10[0] - 1)].pos())
  logsOrWater(Distance(tree.xcor(), tree.ycor(), numTurtDict[str(s10[1] - 1)].xcor(), numTurtDict[str(s10[1] - 1)].ycor()), numTurtDict[str(s10[1] - 1)], colorR, colorG, colorB)
tree.hideturtle()
p1turt = turtle.Turtle()
p1turt.shape('turtle')
p1turt.color(255, 0, 0)
p1turt.penup()
p2turt = turtle.Turtle()
p2turt.color(255, 216, 0)
p2turt.penup()
p2turt.shape('turtle')
p1turt.goto(numTurtDict[str(0)].pos())
p2turt.goto(numTurtDict[str(0)].pos())
screen.update()
screen.tracer(1)
#Playing polluted water and logs ultimate
def snakesandladders(dice):
  dicesum = 0
  for i in range(dice):
    dicesum += random.randint(1, 6)
  return dicesum
print("Lets Start!")
while p1 < hmb and p2 < hmb:
  p1temp = p1
  if hmb > 24 and hmb < 99:
    dicep1 = input(nickp1 + " write down if you want to roll 1 or 2 dice.")
    while not (dicep1 == "1" or dicep1 =="2"):
      dicep1 = input(nickp1 + ", seems like you made a mistake, try typing the number again.")
    dicep1 = int(dicep1)
  elif hmb > 98 and hmb < 174:
    dicep1 = input(nickp1 + " write down if you want to roll 1, 2, 3 or 4 dice.")
    while not (dicep1 == "1" or dicep1 =="2" or dicep1 =="3" or dicep1 =="4"):
      dicep1 = input(nickp1 + ", seems like you made a mistake, try typing the number again.")
    dicep1 = int(dicep1)
  elif hmb > 173 and hmb < 249:
    dicep1 = input(nickp1 + " write down if you want to roll 1, 2, 3, 4, 5 or 6 dice.")
    while not(dicep1 == "1" or dicep1 =="2" or dicep1 =="3" or dicep1 =="4" or dicep1 =="5" or dicep1 =="6"):
      dicep1 = input(nickp1 + ", seems like you made a mistake, try typing the number again.")
    dicep1 = int(dicep1)
  elif hmb > 248 and hmb < 324:
    dicep1 = input(nickp1 + " write down if you want to roll 1, 2, 3, 4, 5, 6, 7 or 8 dice.")
    while not (dicep1 == "1" or dicep1 =="2" or dicep1 =="3" or dicep1 =="4" or dicep1 == "5" or dicep1 =="6" or dicep1 =="7" or dicep1 == "8"):
      dicep1 = input(nickp1 + ", seems like you made a mistake, try typing the number again.")
    dicep1 = int(dicep1)
  elif hmb > 323 and hmb < 401:
    dicep1 = input(nickp1 + " write down if you want to roll 1, 2, 3, 4, 5, 6, 7, 8, 9, or 10 dice.")
    while not (dicep1 == "1" or dicep1 =="2" or dicep1 =="3" or dicep1 =="4" or dicep1 == "5" or dicep1 =="6" or dicep1 =="7" or dicep1 == "8" or dicep1 == "9" or dicep1 == "10"):
      dicep1 = input(nickp1 + ", seems like you made a mistake, try typing the number again.")
    dicep1 = int(dicep1)
  p1 += snakesandladders(dicep1)
  if p1 > hmb:
    p1 = p1temp
    print(nickp1 + ', your dice roll went over ' + str(hmb) + '. You have been put back to the place you were on before you rolled.')
  print(nickp1 + " is on block " + str(p1) + ".")
  p1turt.goto(numTurtDict[str(p1 - 1)].pos())
  if p1 == hmb:
    break
  if hmb > 24 and hmb < 99 and (p1 == s1[0] or p1 == s2[0]):
    if p1 == s1[0]:
      p1 = s1[1]
    elif p1 == s2[0]:
      p1 = s2[1]
    print("Sorry " + nickp1 + ", you fell down a polluted waterfall. Seems like you are on block " + str(p1) + ".")
  elif hmb > 98 and hmb < 174 and (p1 == s1[0] or p1 == s2[0] or p1 == s3[0] or p1 == s4[0]):
    if p1 == s1[0]:
      p1 = s1[1]
    elif p1 == s2[0]:
      p1 = s2[1]
    elif p1 == s3[0]:
      p1 = s3[1]
    elif p1 == s4[0]:
      p1 = s4[1]
    print("Sorry " + nickp1 + ", you fell down a polluted waterfall. Seems like you are on block " + str(p1) + ".")
  elif hmb > 173 and hmb < 249 and (p1 == s1[0] or p1 == s2[0] or p1 == s3[0] or p1 == s4[0] or p1 == s5[0] or p1 == s6[0]):
    if p1 == s1[0]:
      p1 = s1[1]
    elif p1 == s2[0]:
      p1 = s2[1]
    elif p1 == s3[0]:
      p1 = s3[1]
    elif p1 == s4[0]:
      p1 = s4[1]
    elif p1 == s5[0]:
      p1 = s5[1]
    elif p1 == s6[0]:
      p1 = s6[1]
    print("Sorry " + nickp1 + ", you fell down a polluted waterfall. Seems like you are on block " + str(p1) + ".")
  elif hmb > 248 and hmb < 324 and (p1 == s1[0] or p1 == s2[0] or p1 == s3[0] or p1 == s4[0] or p1 == s5[0] or p1 == s6[0] or p1 == s7[0] or p1 == s8[0]):
    if p1 == s1[0]:
      p1 = s1[1]
    elif p1 == s2[0]:
      p1 = s2[1]
    elif p1 == s3[0]:
      p1 = s3[1]
    elif p1 == s4[0]:
      p1 = s4[1]
    elif p1 == s5[0]:
      p1 = s5[1]
    elif p1 == s6[0]:
      p1 = s6[1]
    elif p1 == s7[0]:
      p1 = s7[1]
    elif p1 == s8[0]:
      p1 = s8[1]
    print("Sorry " + nickp1 + ", you fell down a polluted waterfall. Seems like you are on block " + str(p1) + ".")
  elif hmb > 323 and hmb < 401 and (p1 == s1[0] or p1 == s2[0] or p1 == s3[0] or p1 == s4[0] or p1 == s5[0] or p1 == s6[0] or p1 == s7[0] or p1 == s8[0] or p1 == s9[0] or p1 == s10[0]):
    if p1 == s1[0]:
      p1 = s1[1]
    elif p1 == s2[0]:
      p1 = s2[1]
    elif p1 == s3[0]:
      p1 = s3[1]
    elif p1 == s4[0]:
      p1 = s4[1]
    elif p1 == s5[0]:
      p1 = s5[1]
    elif p1 == s6[0]:
      p1 = s6[1]
    elif p1 == s7[0]:
      p1 = s7[1]
    elif p1 == s8[0]:
      p1 = s8[1]
    elif p1 == s9[0]:
      p1 = s9[1]
    elif p1 == s10[0]:
      p1 = s10[1]
    print("Sorry " + nickp1 + ", you fell down a polluted waterfall. Seems like you are on block " + str(p1) + ".")
  elif hmb > 24 and hmb < 99 and (p1 == l1[0] or p1 == l2[0]):
    if p1 == l1[0]:
      p1 = l1[1]
    elif p1 == l2[0]:
      p1 = l2[1]
    print("Great job " + nickp1 + ", you climbed up a log. Seems like you are on block " + str(p1) + ".")
  elif hmb > 98 and hmb < 174 and (p1 == l1[0] or p1 == l2[0] or p1 == l3[0] or p1 == l4[0]):
    if p1 == l1[0]:
      p1 = l1[1]
    elif p1 == l2[0]:
      p1 = l2[1]
    elif p1 == l3[0]:
      p1 = l3[1]
    elif p1 == l4[0]:
      p1 = l4[1]
    print("Great job " + nickp1 + ", you climbed up a log. Seems like you are on block " + str(p1) + ".")
  elif hmb > 173 and hmb < 249 and (p1 == l1[0] or p1 == l2[0] or p1 == l3[0] or p1 == l4[0] or p1 == l5[0] or p1 == l6[0]):
    if p1 == l1[0]:
      p1 = l1[1]
    elif l1 == s2[0]:
      p1 = l2[1]
    elif p1 == l3[0]:
      p1 = l3[1]
    elif p1 == l4[0]:
      p1 = l4[1]
    elif p1 == l5[0]:
      p1 = l5[1]
    elif p1 == l6[0]:
      p1 = l6[1]
    print("Great job " + nickp1 + ", you climbed up a log. Seems like you are on block " + str(p1) + ".")
  elif hmb > 248 and hmb < 324 and (p1 == l1[0] or p1 == l2[0] or p1 == l3[0] or p1 == l4[0] or p1 == l5[0] or p1 == l6[0] or p1 == l7[0] or p1 == l8[0]):
    if p1 == l1[0]:
      p1 = l1[1]
    elif p1 == l2[0]:
      p1 = l2[1]
    elif p1 == l3[0]:
      p1 = l3[1]
    elif p1 == l4[0]:
      p1 = l4[1]
    elif p1 == l5[0]:
      p1 = l5[1]
    elif p1 == l6[0]:
      p1 = l6[1]
    elif p1 == l7[0]:
      p1 = l7[1]
    elif p1 == l8[0]:
      p1 = l8[1]
    print("Great job " + nickp1 + ", you climbed up a log. Seems like you are on block " + str(p1) + ".")
  elif hmb > 323 and hmb < 401 and (p1 == l1[0] or p1 == l2[0] or p1 == l3[0] or p1 == l4[0] or p1 == l5[0] or p1 == l6[0] or p1 == l7[0] or p1 == l8[0] or p1 == l9[0] or p1 == l10[0]):
    if p1 == l1[0]:
      p1 = l1[1]
    elif p1 == l2[0]:
      p1 = l2[1]
    elif p1 == l3[0]:
      p1 = l3[1]
    elif p1 == l4[0]:
      p1 = l4[1]
    elif p1 == l5[0]:
      p1 = l3[1]
    elif p1 == l4[0]:
      p1 = l4[1]
    elif p1 == l5[0]:
      p1 = l5[1]
    elif p1 == l6[0]:
      p1 = l6[1]
    elif p1 == l7[0]:
      p1 = l7[1]
    elif p1 == l8[0]:
      p1 = l8[1]
    elif p1 == l9[0]:
      p1 = l9[1]
    elif p1 == l10[0]:
      p1 = l10[1]
    print("Great job " + nickp1 + ", you climbed up a log. Seems like you are on block " + str(p1) + ".")
  p1turt.goto(numTurtDict[str(p1 - 1)].pos())
  p2temp = p2
  if hmb > 24 and hmb < 99:
    dicep2 = input(nickp2 + " write down if you want to roll 1 or 2 dice.")
    while not (dicep2 == "1" or dicep2 =="2"):
      dicep2 = input(nickp2 + ", seems like you made a mistake, try typing the number again.")
    dicep2 = int(dicep2)
  elif hmb > 98 and hmb < 174:
    dicep2 = input(nickp2 + " write down if you want to roll 1, 2, 3 or 4 dice.")
    while not (dicep2 == "1" or dicep2 =="2" or dicep2 =="3" or dicep2 =="4"):
      dicep2 = input(nickp2 + ", seems like you made a mistake, try typing the number again.")
    dicep2 = int(dicep2)
  elif hmb > 173 and hmb < 249:
    dicep2 = input(nickp2 + " write down if you want to roll 1, 2, 3, 4, 5, or 6 dice.")
    while not (dicep2 == "1" or dicep2 =="2" or dicep2 =="3" or dicep2 =="4" or dicep2 =="5" or dicep2 =="6"):
      dicep2 = input(nickp2 + ", seems like you made a mistake, try typing the number again.")
    dicep2 = int(dicep2)
  elif hmb > 248 and hmb < 324:
    dicep2 = input(nickp2 + " write down if you want to roll 1, 2, 3, 4, 5, 6, 7 or 8 dice.")
    while not (dicep2 == "1" or dicep2 =="2" or dicep2 =="3" or dicep2 =="4" or dicep2 == "5" or dicep2 =="6" or dicep2 =="7" or dicep2 == "8"):
      dicep2 = input(nickp2 + ", seems like you made a mistake, try typing the number again.")
    dicep2 = int(dicep2)
  elif hmb > 323 and hmb < 401:
    dicep2 = input(nickp2 + " write down if you want to roll 1, 2, 3, 4, 5, 6, 7, 8, 9, or 10 dice.")
    while not (dicep2 == "1" or dicep2 =="2" or dicep2 =="3" or dicep2 =="4" or dicep2 == "5" or dicep2 =="6" or dicep2 =="7" or dicep2 == "8" or dicep2 == "9" or dicep2 == "10"):
      dicep2 = input(nickp2 + ", seems like you made a mistake, try typing the number again.")
    dicep2 = int(dicep2)
  p2 += snakesandladders(dicep2)
  if p2 > hmb:
    p2 = p2temp
    print(nickp2 + ', your dice roll went over ' + str(hmb) + '. You have been put back to the place you were on before you rolled.')
  print(nickp2 + " is on block " + str(p2) + ".")
  p2turt.goto(numTurtDict[str(p2 - 1)].pos())
  if p2 == hmb:
    break
  if hmb > 24 and hmb < 99 and (p2 == s1[0] or p2 == s2[0]):
    if p2 == s1[0]:
      p2 = s1[1]
    elif p2 == s2[0]:
      p2 = s2[1]
    print("Sorry " + nickp2 + ", you fell down a polluted waterfall. Seems like you are on block " + str(p2) + ".")
  elif hmb > 98 and hmb < 174 and (p2 == s1[0] or p2 == s2[0] or p2 == s3[0] or p2 == s4[0]):
    if p2 == s1[0]:
      p2 = s1[1]
    elif p2 == s2[0]:
      p2 = s2[1]
    elif p2 == s3[0]:
      p2 = s3[1]
    elif p2 == s4[0]:
      p2 = s4[1]
    print("Sorry " + nickp2 + ", you fell down a polluted waterfall. Seems like you are on block " + str(p2) + ".")
  elif hmb > 173 and hmb < 249 and (p2 == s1[0] or p2 == s2[0] or p2 == s3[0] or p2 == s4[0] or p2 == s5[0] or p2 == s6[0]):
    if p2 == s1[0]:
      p2 = s1[1]
    elif p2 == s2[0]:
      p2 = s2[1]
    elif p2 == s3[0]:
      p2 = s3[1]
    elif p2 == s4[0]:
      p2 = s4[1]
    elif p2 == s5[0]:
      p2 = s5[1]
    elif p2 == s6[0]:
      p2 = s6[1]
    print("Sorry " + nickp2 + ", you fell down a polluted waterfall. Seems like you are on block " + str(p2) + ".")
  elif hmb > 248 and hmb < 324 and (p2 == s1[0] or p2 == s2[0] or p2 == s3[0] or p2 == s4[0] or p2 == s5[0] or p2 == s6[0] or p2 == s7[0] or p2 == s8[0]):
    if p2 == s1[0]:
      p2 = s1[1]
    elif p2 == s2[0]:
      p2 = s2[1]
    elif p2 == s3[0]:
      p2 = s3[1]
    elif p2 == s4[0]:
      p2 = s4[1]
    elif p2 == s5[0]:
      p2 = s5[1]
    elif p2 == s6[0]:
      p2 = s6[1]
    elif p2 == s7[0]:
      p2 = s7[1]
    elif p2 == s8[0]:
      p2 = s8[1]
    print("Sorry " + nickp2 + ", you fell down a polluted waterfall. Seems like you are on block " + str(p2) + ".")
  elif hmb > 323 and hmb < 401 and (p2 == s1[0] or p2 == s2[0] or p2 == s3[0] or p2 == s4[0] or p2 == s5[0] or p2 == s6[0] or p2 == s7[0] or p2 == s8[0] or p2 == s9[0] or p2 == s10[0]):
    if p2 == s1[0]:
      p2 = s1[1]
    elif p2 == s2[0]:
      p2 = s2[1]
    elif p2 == s3[0]:
      p2 = s3[1]
    elif p2 == s4[0]:
      p2 = s4[1]
    elif p2 == s5[0]:
      p2 = s5[1]
    elif p2 == s6[0]:
      p2 = s6[1]
    elif p2 == s7[0]:
      p2 = s7[1]
    elif p2 == s8[0]:
      p2 = s8[1]
    elif p2 == s9[0]:
      p2 = s9[1]
    elif p2 == s10[0]:
      p2 = s10[1]
    print("Sorry " + nickp2 + ", you fell down a polluted waterfall. Seems like you are on block " + str(p2) + ".")
  elif hmb > 24 and hmb < 99 and (p2 == l1[0] or p2 == l2[0]):
    if p2 == l1[0]:
      p2 = l1[1]
    elif p2 == l2[0]:
      p2 = l2[1]
    print("Great job " + nickp2 + ", you climbed up a log. Seems like you are on block " + str(p2) + ".")
  elif hmb > 98 and hmb < 174 and (p2 == l1[0] or p2 == l2[0] or p2 == l3[0] or p2 == l4[0]):
    if p2 == l1[0]:
      p2 = l1[1]
    elif p2 == l2[0]:
      p2 = l2[1]
    elif p2 == l3[0]:
      p2 = l3[1]
    elif p2 == l4[0]:
      p2 = l4[1]
    print("Great job " + nickp2 + ", you climbed up a log. Seems like you are on block " + str(p2) + ".")
  elif hmb > 173 and hmb < 249 and (p2 == l1[0] or p2 == l2[0] or p2 == l3[0] or p2 == l4[0] or p2 == l5[0] or p2 == l6[0]):
    if p2 == l1[0]:
      p2 = l1[1]
    elif l1 == s2[0]:
      p2 = l2[1]
    elif p2 == l3[0]:
      p2 = l3[1]
    elif p2 == l4[0]:
      p2 = l4[1]
    elif p2 == l5[0]:
      p2 = l5[1]
    elif p2 == l6[0]:
      p2 = l6[1]
    print("Great job " + nickp2 + ", you climbed up a log. Seems like you are on block " + str(p2) + ".")
  elif hmb > 248 and hmb < 324 and (p2 == l1[0] or p2 == l2[0] or p2 == l3[0] or p2 == l4[0] or p2 == l5[0] or p2 == l6[0] or p2 == l7[0] or p2 == l8[0]):
    if p2 == l1[0]:
      p2 = l1[1]
    elif p2 == l2[0]:
      p2 = l2[1]
    elif p2 == l3[0]:
      p2 = l3[1]
    elif p2 == l4[0]:
      p2 = l4[1]
    elif p2 == l5[0]:
      p2 = l5[1]
    elif p2 == l6[0]:
      p2 = l6[1]
    elif p2 == l7[0]:
      p2 = l7[1]
    elif p2 == l8[0]:
      p2 = l8[1]
    print("Great job " + nickp2 + ", you climbed up a log. Seems like you are on block " + str(p2) + ".")
  elif hmb > 323 and hmb < 401 and (p2 == l1[0] or p2 == l2[0] or p2 == l3[0] or p2 == l4[0] or p2 == l5[0] or p2 == l6[0] or p2 == l7[0] or p2 == l8[0] or p2 == l9[0] or p2 == l10[0]):
    if p2 == l1[0]:
      p2 = l1[1]
    elif p2 == l2[0]:
      p2 = l2[1]
    elif p2 == l3[0]:
      p2 = l3[1]
    elif p2 == l4[0]:
      p2 = l4[1]
    elif p2 == l5[0]:
      p2 = l3[1]
    elif p2 == l4[0]:
      p2 = l4[1]
    elif p2 == l5[0]:
      p2 = l5[1]
    elif p2 == l6[0]:
      p2 = l6[1]
    elif p2 == l7[0]:
      p2 = l7[1]
    elif p2 == l8[0]:
      p2 = l8[1]
    elif p2 == l9[0]:
      p2 = l9[1]
    elif p2 == l10[0]:
      p2 = l10[1]
    print("Great job " + nickp2 + ", you climbed up a log. Seems like you are on block " + str(p2) + ".")
  p2turt.goto(numTurtDict[str(p2 - 1)].pos())
sq1.clear()
tree.clear()
p1turt.hideturtle()
p2turt.hideturtle()
screen.update()
#Determining who wins at polluted water and logs ultimate
if p1 == hmb:
  print(nickp1 + " wins at polluted water and logs ultimate! Sorry " + nickp2 + ", better luck next time!")
  p1score += 1
elif p2 == hmb:
  print(nickp2 + " wins at polluted water and logs ultimate! Sorry " + nickp1 + ", better luck next time!")
  p2score += 1
#Determining who wins the 2 player arcade
input('Press enter to see who wins the whole 2 player arcade!: ')
if p1score > p2score:
  print(nickp1 + " wins! Sorry " + nickp2 + ", better luck next time!")
elif p2score > p1score:
  print(nickp2 + " wins! Sorry " + nickp1 + ", better luck next time!")
print('Two game projects are on this URL also go to https://repl.it/@AlightDesert892/Earth-Day-Hackathon-2nd-Part for co2 analysis and prediction.')
#Two game projects are on this URL also go to https://repl.it/@AlightDesert892/Earth-Day-Hackathon-2nd-Part for co2 analysis and prediction.