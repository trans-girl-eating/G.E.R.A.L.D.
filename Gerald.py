




    

    
import turtle
import random

Gerald = turtle.Turtle()
Gerald.shape("turtle")
Gerald.color("SteelBlue")
Gerald.pencolor("SkyBlue")
Gerald.pensize(10)
NameQuestions = ["what is this?", "what is this called?", "name?", "what is this piece named?" "what is the name of your art?", "what is the name?"]
NamePart1 = ["Void", "Beam", "Sky", "Trilogy", "Oddysey", "Perfection", "Pornography", "Poem", "Song", "Meeting"]
NamePart2 = ["of", "and", "Lady", "Gentleman", "World"]
NamePart3 = ["God", "Asgaard", "Holy Light", "Temple", "Feline", "Arson", "Cows", "Aliens"]
goodVibes = ["y", "Y", "Yes", "Good", "Awesome", "Nice", "!", "Love", "Happy", "Content"]
badVibes = ["B", "b", "Bad", "Worst", "Terrible", "No", "n", "N", "no", "Anger", "Sad", "Depressed"]
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
    for i in range(50):
        Gerald.pendown()
        for i in range(4):
            Gerald.forward(ForwardRandom1)
            Gerald.right(RandomTurn)

        Gerald.left(RandomLeft)

    Check()
ForwardRandom1 = random.randint(1, 500)
ForwardRandom2 = random.randint(1, 500)
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
    if(praise) in goodVibes:
        print("Thanks!")
        if(takeAction) == 4:
            Shape3()
        if(takeAction) == 3:
            Shape2()
        if(takeAction) == 2:
            Shape1()
        if(takeAction) == 1:
            MoveElsewhere()
    if(praise) in badVibes:
        print("Awwwww.....")
        print(" :( ")
        print("")
        GetAction()

    if(praise) in NameQuestions:
        NameArt()

    if((praise) == "exit" or (praise) == "Exit"):
        Start()

def NameArt():
    print(random.choice(NamePart1) + " " + random.choice(NamePart2) + " " + random.choice(NamePart3))
    Check()
###############Conversational_Matrix####################

def Convo():
    for i in range(70):
        print("")

    print("Let's just talk! How are you?")
    answer = input("")
    if(answer) in goodVibes:
        print("That's great! I'm happy for ya! ")
        
     

    if(answer) in badVibes:
        print("I'm sorry! Wanna talk about it?")
        
        
    
    

    
        
        
    
    

    



