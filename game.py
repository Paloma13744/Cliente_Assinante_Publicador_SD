import turtle
import time

delay = 0.08

# Score
score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Move Game by @Garrocho")
wn.bgpic("jogo.gif") 
wn.setup(width=900, height=900)  
wn.tracer(0)  

# Lista para os jogadores
players = []

# Criando jogadores
colors = ["red", "blue", "green"]  # Cores distintas para os jogadores
start_positions = [(0, 0), (100, 0), (-100, 0)]  # Posições iniciais dos jogadores

for i in range(3):
    player = turtle.Turtle()
    player.speed(0)
    player.shape("circle")
    player.color(colors[i])
    player.penup()
    player.goto(start_positions[i])
    player.direction = "stop"
    player.shapesize(stretch_wid=1.5, stretch_len=1.5)  # Tamanho das bolinhas
    players.append(player)

# Funções para movimentar os jogadores
def go_up(player):
    player.direction = "up"

def go_down(player):
    player.direction = "down"

def go_left(player):
    player.direction = "left"

def go_right(player):
    player.direction = "right"

def stop(player):
    player.direction = "stop"  

def close():
    wn.bye()

def move(player):
    if player.direction == "up":
        y = player.ycor()
        if y < 420:  
            player.sety(y + 20)

    if player.direction == "down":
        y = player.ycor()
        if y > -420: 
            player.sety(y - 20)

    if player.direction == "left":
        x = player.xcor()
        if x > -420: 
            player.setx(x - 20)

    if player.direction == "right":
        x = player.xcor()
        if x < 420: 
            player.setx(x + 20)

# Bindings de teclado para cada jogador
def setup_controls(player_index):
    wn.listen()
    if player_index == 0:
        wn.onkeypress(lambda: go_up(players[player_index]), "w")
        wn.onkeypress(lambda: go_down(players[player_index]), "s")
        wn.onkeypress(lambda: go_left(players[player_index]), "a")
        wn.onkeypress(lambda: go_right(players[player_index]), "d")
        wn.onkeypress(lambda: stop(players[player_index]), "x")  # Parar com a tecla "x"
    elif player_index == 1:
        wn.onkeypress(lambda: go_up(players[player_index]), "i")
        wn.onkeypress(lambda: go_down(players[player_index]), "k")
        wn.onkeypress(lambda: go_left(players[player_index]), "j")
        wn.onkeypress(lambda: go_right(players[player_index]), "l")
        wn.onkeypress(lambda: stop(players[player_index]), "m")  # Parar com a tecla "m"
    elif player_index == 2:
        wn.onkeypress(lambda: go_up(players[player_index]), "Up")
        wn.onkeypress(lambda: go_down(players[player_index]), "Down")
        wn.onkeypress(lambda: go_left(players[player_index]), "Left")
        wn.onkeypress(lambda: go_right(players[player_index]), "Right")
        wn.onkeypress(lambda: stop(players[player_index]), "p")  # Parar com a tecla "p"

# Configurar os controles para cada jogador
for i in range(3):
    setup_controls(i)

# Loop principal do jogo
try:
    while True:
        wn.update()
        for player in players:
            move(player)
        time.sleep(delay)
except turtle.Terminator:
    print("A janela foi fechada." +"\n "+" ______O jogo terminou._______")
