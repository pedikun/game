import turtle

wn=turtle.Screen()
wn.title("painful prototype")
wn.bgcolor("black")
wn.setup(width=1280,height=720)
wn.tracer(0)

#balls
tutcube=turtle.Turtle()
tutcube.speed(0)
tutcube.shape("square") 
tutcube.color("white")
tutcube.penup()
tutcube.goto(100,0)

numbah=-1
numbah2=0
numbah3=0

random_y=[250,200,100,-50,0]
random_p=[250,330,0,100,0]

tea=["hi there","i am tutcube","first thing first"
     ,"dont shoot at that hansome white cube",
     "(its me)","yeah sad i know",
     "anyway","this is the end of this demo",
     "idk what to put yet just byee","oh well why not keep typing",
     "help i forgot what to type"]

sure=["aww are you trying to kill me?","are you sure about that?","yes you are trying to kill me","uff hard mode has not developed yet"]
hardmode=["aww","please just fire at yellow button","its hurt kid","youre lucky hard mode is not developed yet",""]

arrow=turtle.Turtle()
arrow.speed(0)
arrow.shape("arrow")
arrow.color("red")
arrow.penup()
arrow.goto(900,900)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, -260)
pen.write("hi (hit the yellow box to continyou>", align="center", font=("Courier", 24, "normal"))

nekt=turtle.Turtle()
nekt.speed(0)
nekt.shape("square")
nekt.color("yellow")
nekt.penup()
nekt.goto(350,-240)

arrow.dx=1
arrow.dy=1

def shot():
    arrow.goto(100,100)

def klik(x,y):
    arrow.goto(-620,y)
    
#notused
def boolet():
    arrow=turtle.Turtle()
    arrow.speed(0)
    arrow.shape("arrow")
    arrow.color("red")
    arrow.penup()
    arrow.goto(100,100)
    arrow.dx=0.5
    arrow.dy=1
#keybind
wn.listen()
wn.onkeypress(shot,"p")
#\/only work on wn/screen value
wn.onclick(klik)
while True:
    wn.update()
    #movement
    arrow.setx(arrow.xcor() + arrow.dx)
    
    if arrow.distance(nekt)<20:
        numbah+=1
        arrow.goto(900,900)
        pen.clear()
        pen.write(tea[numbah], align="center", font=("Comic Sans MS", 24, "normal"))
    #del
    elif arrow.distance(tutcube)<20:
        tutcube.goto(random_y[numbah2],random_p[numbah2])
        pen.clear()
        pen.write(hardmode[numbah2], align="center", font=("Comic Sans MS", 24, "normal"))
        numbah2+=1
        if numbah > 3:
            pen.clear()
            pen.write(sure[numbah2], align="center", font=("Comic Sans MS", 24, "normal"))
            
            
        #if: try: numbah2 ==5:exec
    #del