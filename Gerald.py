import turtle
import random

Gerald = turtle.Turtle()
Gerald.shape("turtle")
Gerald.color("SteelBlue")
Gerald.pencolor("SkyBlue")
Gerald.pensize(10)


Action = random.randint(1, 3)

def GetAction():
    global Action
    Action = random.randint(1, 4)
    DoAction()

def Start():
    print("Howdy! I'm Gastronomical Existentialist Recording Artisanal Legalistic Dude, or G.E.R.A.L.D. for short!")
    print("")
    print("Type GetAction() to start me up, or use a shape command to start me going.")
    
def MoveElsewhere():
    global Gerald
    global takeAction
    takeAction = 1
    Gerald.penup()
    Gerald.goto(random.randint(0,900), random.randint(0,900))
    Gerald.pendown()
    Check()
    
    
def Shape1():
    global Gerald
    global RandomTurn
    global RandomLeft
    global ForwardRandom2
    global takeAction
    takeAction = 2
    Gerald.pencolor("Violet")
    Gerald.penup()
    Gerald.forward(ForwardRandom2)
    for i in range(9):
        Gerald.pendown()
        for i in range(4):
            Gerald.forward(ForwardRandom1)
            Gerald.right(RandomTurn)

        Gerald.left(RandomLeft)

    Check()
ForwardRandom1 = random.randint(1, 100)
ForwardRandom2 = random.randint(1, 100)
RandomTurn = random.randint(1, 90)
RandomLeft = random.randint(1, 400)
def Shape2():
    global RandomTurn
    global Gerald
    global ForwardRandom1
    global takeAction
    takeAction = 3
    Gerald.pencolor("LightBlue")
    for i in range(50):
        
        for i in range(4):
            
            Gerald.forward(ForwardRandom1)
            Gerald.right(RandomTurn)

        Gerald.left(RandomLeft)

    Check()
    
takeAction = 0

def Shape3():
    global Gerald
    global takeAction
    takeAction = 4
    Gerald.pendown()
    Gerald.pencolor("LightGreen")
    for i in range(2):
        for i in range(4):
            Gerald.forward(400)
            Gerald.left(200)

        Gerald.left(100)

    Check()

def DoAction():
    if(Action) == 1:
        Shape1()

    if(Action) == 2:
        Shape2()

    if(Action) == 3:
        Shape3()

    if(Action) == 4:
        MoveElsewhere()

Start()

def Check():
    print("So, did you like that shape?")
    print(" Y / N ")
    praise = input(" ")
    if((praise) == "Y" or (praise) == "y"):
        print("Thanks!")
        if(takeAction) == 4:
            Shape3()
        if(takeAction) == 3:
            Shape2()
        if(takeAction) == 2:
            Shape1()
        if(takeAction) == 1:
            MoveElsewhere()
    else:
        print("Awwwww.....")
        print(" :( ")
        print("")
        GetAction()
        
        
    
    

    
