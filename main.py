import turtle, time
from random import choice, randint

# Fullscreen the canvas
screen = turtle.Screen()
screen.setup(400, 500)
screen.bgcolor("black")

# Begin!
t = turtle.Turtle()
t.speed(0)
t.penup()
t.color("white")
t.hideturtle()

  
#NPCs
Cyan = turtle.Turtle()
Cyan.penup()
Red = turtle.Turtle()
Red.penup()
Magenta = turtle.Turtle()
Magenta.penup()
User = turtle.Turtle()
User.penup()
Red.hideturtle()
Cyan.hideturtle()
Magenta.hideturtle()
User.hideturtle()

#NPC FUNCTIONS
Cyan.color("cyan")
Cyan_char = {
  "name": "Cyan", 
  turtle: Cyan,
  "guilt": "not guilty",
  "guilt level": 0
}


Red.color("Red")
Red_char = {
  "name": "Red", 
  turtle: Red,
  "guilt": "not guilty",
  "guilt level": 0
}


Magenta.color("magenta")
Magenta_char = {
  "name": "Magenta", 
  turtle: Magenta,
  "guilt": "not guilty",
  "guilt level": 0
}

#User
User.color("purple")
user_name = ""

User_char = {
  "name": user_name, 
  "guilt": "not guilty",
  turtle: User,
  "guilt level": 0
}

crewmates = []
imposter = []

#Guilty Not Guilty
guilt_num = randint(0,3)
if guilt_num == 0:
  Cyan_char["guilt"] = "guilty"
  imposter.append(Cyan_char)
  crewmates.append(Magenta_char)
  crewmates.append(Red_char)
  crewmates.append(User_char)
elif guilt_num == 1:
  Red_char["guilt"] = "guilty"
  imposter.append(Red_char)
  crewmates.append(Magenta_char)
  crewmates.append(Cyan_char)
  crewmates.append(User_char)
else: #elif guilt_num == 2:
  Magenta_char["guilt"] = "guilty"
  imposter.append(Magenta_char)
  crewmates.append(Red_char)
  crewmates.append(Cyan_char)
  crewmates.append(User_char)

#crewmates, imposters, players and moving them

players = [Cyan_char, Red_char, Magenta_char, User_char]
NPCplayers = [Cyan_char, Red_char, Magenta_char]
NPCnames = ["Cyan", "Red", "Magenta"]

user_name = input("What is your name? ")
print ("Welcome " + user_name)

Red.showturtle()
Cyan.showturtle()
Magenta.showturtle()
User.showturtle()


Cyan.setheading(225)
Magenta.setheading(225)
User.setheading(315)
Red.setheading(315)

def box_offices():
  #Office rooms

  t.clear()
  t.setheading(0)
  t.goto(-25,190)
  t.pendown()
  t.forward(50)

  t.penup()
  t.goto(-50,125)
  t.pendown()
  t.forward(100)

  t.penup()
  t.goto(0,125)
  t.pendown()
  t.setheading(270)
  t.forward(200)
  t.left(90)
  t.forward(100)
  t.left(90)
  t.forward(50)
  t.penup()
  t.forward(50)
  t.left(90)
  t.pendown()
  t.forward(100)
  t.forward(-100)
  t.right(90)
  t.forward(50)
  t.penup()

  t.goto(0,-75)
  t.setheading(180)
  t.pendown()
  t.forward(100)
  t.right(90)
  t.forward(50)
  t.penup()
  t.forward(50)
  t.right(90)
  t.pendown()
  t.forward(100)
  t.forward(-100)
  t.left(90)
  t.forward(50)

  t.forward(-20)
  t.right(90)
  t.forward(50)
  t.left(45)
  t.forward(28.28)
  t.left(45)
  t.forward(50)
  t.penup()

  t.goto(-100,-45)
  t.setheading(0)
  t.pendown()
  t.forward(50)
  t.left(45)
  t.forward(28.28)
  t.left(45)
  t.forward(50)
  t.penup()

  t.goto(30,125)
  t.setheading(270)
  t.pendown()
  t.forward(50)
  t.left(45)
  t.forward(28.28)
  t.left(45)
  t.forward(50)
  t.penup()

  t.goto(30,25)
  t.setheading(270)
  t.pendown()
  t.forward(50)
  t.left(45)
  t.forward(28.28)
  t.left(45)
  t.forward(50)
  t.penup()

  Red.goto(-55,-25)
  User.goto(-55,75)
  Magenta.goto(55,-25)
  Cyan.goto(55,75)

  #t.hideturtle()

def meeting_room():
  t.clear()
  t.goto(-25,-190)
  t.setheading(0)
  t.pendown()
  t.forward(50)
  t.penup()

  t.goto(-50,-100)
  t.pendown()
  for i in range(4):
    t.forward(100)
    t.left(22.5)
    t.forward(25)
    t.left(22.5)
    t.forward(25)
    t.left(22.5)
    t.forward(25)
    t.left(22.5)

  Red.goto(110, 40)
  Red.setheading(180)
  Magenta.goto(110, -40)
  Magenta.setheading(180)

  User.goto(-110, 40)
  User.setheading(0)
  Cyan.goto(-110, -40)
  Cyan.setheading(0)
  

  t.penup()

ready = input('Please enter "Yes" when you are ready: ')
while ready != "Yes":
  ready = input('Please Enter "Yes" when you are ready (and capitalize): ')


# Telling user if they are a Loyal worker and their objective
print ("\nIn this game you're a loyal worker, and a great manager!")
print ("Try voting the imposter out from the information you're provided to win.")
print ("The goal is to get all the math correct so you can win!")

Time = 8
average_suspicion = 6
User_guilt_level = 0
User_char["guilt_level"] = User_guilt_level
while len(imposter) > 0:
  box_offices()
  if Time == 12:
    Time = 0
  Time += 1
  print("It is", Time, "O'clock")

  # NPC impostor (not the user)
  invalid_alibis = {
    "says: I was on lunch break so I got up from my desk.": 3,
    "says: I was working on a long task, so I didn’t pay attention to that part of the project.": 2,
    "says: I wasn’t near my desk at the time, I was getting coffee.": 2,
    "says: I wasn't assigned that task today.": 3
  }
  
  # NPC/crewmate alibis
  alibis = {
    "says: I was working on a long task, so I didn’t pay attention to that part of the project.": 2,
    "says: I wasn’t near my desk at the time, I was getting coffee.": 2,
    "says: I wasn't assigned that task today.": 3
  }
  
  
  # alibis for user when they are crewmate
  user_alibis = {
    "(A): I passed by (Player Name), but we didn’t interact much.": 2,
    "(B): I was in a completely different area focusing on my own work, so I didn’t see anything out of the ordinary.": 3,
    "(C): I wasn’t even near the issue.": 3,
    "(D): I was on my way to get some coffee when the accusation came up.": 5,
  }


  score = 0
  while score < 5:
    sign = choice(["+","-","x","/"])
    questionAns = 0
    num1 = 0
    num2 = 0
    if sign == "+":
      num1 = randint(1,100)
      num2 = randint(1,100)
      questionAns = num1 + num2
      question = str(num1) + sign + str(num2)
    elif sign == "-":
      num1 = randint(1,100)
      num2 = randint(1, num1)
      questionAns = num1 - num2
      question = str(num1) + sign + str(num2)
    elif sign == "x":
      num1 = randint(1,20)
      num2 = randint(1,20)
      questionAns = num1 * num2
      question = str(num1) + sign + str(num2)
    else: #if sign == "/":
      num1 = randint(1,100)
      num2 = randint(1,num1)
      questionAns= int(num1 / num2)
      question = str(num1) + sign + str(num2)

    print("\n!")
    time.sleep(1)
    user_answer = int(input("What is the answer to this question? \n(if a decimal or repeat, enter the answer without decimals). \n" + question + " = "))
    print("\nExpected Answer", questionAns)
    if (questionAns == user_answer):
      score += 1
      print("Correct!")
    else:
      print("Try again!")
  
  time.sleep(1.5)
  print ("\nAnnouncement: MEETING CALLED\n")
  time.sleep(1.5)
  meeting_room()

  User_alibi = ""
  # Allows user to pick an alibi
  print ("Pick an alibi from the list! ")
  for i in user_alibis:
    print ("\n", i)
  print ("\n")
  options = ["A", "B", "C", "D", "E"]
  while User_alibi.upper() not in options:
    print ("Please enter a letter from above.")
    User_alibi = input("Pick an alibi from the list! ")
    User_alibi = User_alibi.upper()
    if User_alibi in options: #may not need this if statement
      break
  #while User_alibi == "A" or User_alibi == "B" or User_alibi == "C" or User_alibi == "D" or User_alibi == "E":
  if User_alibi == 'A':
    User_person = input("Who, or which color, did you pass by? ")
    while User_person not in NPCnames:
      print("please enter a player")
      User_person = input("Who, or which color, did you pass by? (please capitalize) ")
    User_alibi = "I passed by", User_person, "but we didn’t interact much."
    User_guilt_level += 2
  elif User_alibi == 'B':
    User_alibi = "I was in a completely different area focusing on my own questions, so I didn’t see anything suspicious."
    User_guilt_level += 3
  elif User_alibi == 'C':
    User_guilt_level += 3
    User_alibi = "I wasn’t even near the issue."
  elif User_alibi == 'D':
    User_guilt_level += 5
    User_alibi = "I was on my way to get some coffee when the accusation came up."

  User_char["alabi"] = User_alibi


  suspicious_list = []
  
  print ("Here are the alibis for the NPCs: \n")
  for p in NPCplayers:
    if p["guilt"] == "guilty":
      p_alibi, p_guiltlevel = choice(list(invalid_alibis.items()))
      p["alibi"] = p["name"] + " " + p_alibi
      p["guilt level"] = p_guiltlevel + 2.5
    else:
      p_alibi, p_guiltlevel = choice(list(invalid_alibis.items()))
      p["alibi"] = p["name"] + " "+ p_alibi
      p["guilt level"] = p_guiltlevel
    print (p["alibi"])

  
  for p in players:
    if p["guilt level"] >= average_suspicion:
      p["supposed guilt"] = "guilty"
      suspicious_list.append(p)
    else:
      p["supposed guilt"] = "not guilty"

  user_choice = input("\nWhich player is guilty?! (Magenta, Cyan, or Red and please capitalize or enter space to skip this round.) ")

  User_char["vote"] = user_choice
  User_char["votes against"] = 0
  Cyan_char["votes against"] = 0
  Red_char["votes against"] = 0
  Magenta_char["votes against"] = 0

  if user_choice == "Magenta":
    Magenta_char["votes against"] += 1
  elif user_choice == "Red":
    Red_char["votes against"] += 1
  elif user_choice == "Cyan":
    Cyan_char["votes against"] += 1
    
  for i in players:
    if i["votes against"] > 0:
      print (i["name"] + " has been voted off")
      if i["guilt"] == "guilty":
        print("You won! \nGreat job, you've got brilliant detective skills!\nIf you'd like to play again, click stop then run again!")
        imposter.remove(i)
      else:
        print("You just got your good coworker fired!! Go back and work again.")
        players.remove(i)
        NPCplayers.remove(i)
        NPCnames.remove(i["name"])
        (i[turtle]).hideturtle()

  average_suspicion += 3

screen.mainloop()