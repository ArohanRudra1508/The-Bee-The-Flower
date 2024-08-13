import pgzrun
from random import randint

TITLE = "The Bee & The Flower"
WIDTH = 600
HEIGHT = 500

score = 0
game_over = False

bee = Actor('bee2')
flower = Actor('flower1')

bee.pos = (50,60)
flower.pos = (60,50)

def draw():
    screen.fill(color = (173,216,230))
    bee.draw()
    flower.draw()
    screen.draw.text("Score: "+str(score),color = "black", topleft = (10,10),fontsize = 30)

    if game_over:
        screen.fill(color = "red")
        screen.draw.text("Your final score is "+str(score),color = "black", midbottom = (250,450),fontsize = 40)

def place_flower():
    flower.x = randint(50,WIDTH-50)
    flower.y = randint(50,HEIGHT-50)

def time_up():
    global game_over
    game_over = True

def update():
    global score
    if keyboard.left:
        bee.x = bee.x -2
    if keyboard.right:
        bee.x = bee.x +2
    if keyboard.up:
        bee.y = bee.y -2
    if keyboard.down:
        bee.y = bee.y +2

    flower_collected = bee.colliderect(flower)
    if flower_collected:
        score +=10
        place_flower()

clock.schedule(time_up,30.0)


pgzrun.go()
