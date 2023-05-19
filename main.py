from turtle import Turtle, Screen
import time
import random


turtle = Turtle()
turtle.hideturtle()
screen1 = Screen()
screen1.bgpic("bg1.png")
screen1.title("Snake game")
screen1.setup(width=600, height=600)
screen1.tracer(False)

apple = Turtle("circle")
apple.color("red")
apple.penup()
apple.goto(100, 100) 

head = Turtle("square")
head.color("green")
head.penup()
head.speed(0)
head.goto(0, 0)
head.direction = "stop"

# Funkce
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def move_up():
    if head.direction != "down":
        head.direction = "up"

def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_left():
    if head.direction != "right":
        head.direction = "left"

def move_right():
    if head.direction != "left":
        head.direction = "right"

# WASD
screen1.listen()
screen1.onkeypress(move_up, "w")
screen1.onkeypress(move_down, "s")
screen1.onkeypress(move_left, "a")
screen1.onkeypress(move_right, "d")

body_parts = []
score = 0
highest_score = 0
score_sign = Turtle("square")
score_sign.speed(0)
score_sign.color("red")
score_sign.penup()
score_sign.hideturtle()
score_sign.goto(0, 265)
score_sign.write("Score: 0  Max.Score: 0", align="center", font=("Times New Roman", 20))
score_sign2 = Turtle("square")
score_sign2.speed(0)
score_sign2.color("red")
score_sign2.penup()
score_sign2.hideturtle()
score_sign2.goto(0, 195)



# Hlavní cyklus
while True:

    # Hlava mimo zonu
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < - 290:
        time.sleep(2)
        head.goto(0, -7)
        apple.goto(0, 900)
        head.direction = "stop"

        # Bodyparts == 0
        for one_body_part in body_parts:
            one_body_part.goto(1500, 1500)   
        body_parts.clear()
        # Reset score
        score = 0

        score_sign.clear()
        score_sign.write(f"Skóre: {score}  Nejvyšší skóre: {highest_score}", align="center", font=("Times New Roman", 20))
        score_sign2.clear()
        score_sign2.write("YOU LOSE", align="center", font=("Times New Roman", 20))
        import end

    # Hlava a jablko
    if head.distance(apple) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        apple.goto(x, y)

        # Přidání části těla
        new_body_part = Turtle("square")
        new_body_part.speed(0)
        new_body_part.color("dark green")
        new_body_part.penup()
        body_parts.append(new_body_part)

        # Zvýšení skóre
        score += 10

        if score > highest_score:
            highest_score = score
        
        score_sign.clear()
        score_sign.write(f"Skóre: {score}  Nejvyšší skóre: {highest_score}", align="center", font=("Times New Roman", 20))

    for index in range(len(body_parts) - 1, 0, -1):
        x = body_parts[index - 1].xcor()
        y = body_parts[index - 1].ycor()
        body_parts[index].goto(x, y)

    if len(body_parts) > 0:
        x = head.xcor()
        y = head.ycor()
        body_parts[0].goto(x,y)
    move()

    # Hlava a tělo
    for one_body_part in body_parts:
        if one_body_part.distance(head) < 20:
            time.sleep(2)
            head.goto(0, 0)
            head.direction = "stop"
            score_sign2.clear()
            score_sign2.write("YOU LOSE", align="center", font=("Times New Roman", 20))
            import end
            
            # Skryjeme části těla
            for one_body_part in body_parts:
                one_body_part.goto(1500, 1500)

            # Vyprázdníme list s částmi těla (šedé čtverečky)    
            body_parts.clear()

            # Reset score
            score = 0

            score_sign.clear()
            score_sign.write(f"Skóre: {score}  Nejvyšší skóre: {highest_score}", align="center", font=("Times New Roman", 20))
            
    screen1.update()
    time.sleep(0.1)
screen1.exitonclick()
    

 





    


