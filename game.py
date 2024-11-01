import turtle
import time
import json
import threading
import paho.mqtt.client as mqtt

# Configurações do broker
broker = "localhost"
port = 1883
timelive = 60

# Variáveis de jogo
delay = 0.08
players_data = {}

# Configuração da tela do Turtle
wn = turtle.Screen()
wn.title("Move Game by @Garrocho")
wn.bgpic("jogo.gif") 
wn.setup(width=900, height=900)  
wn.tracer(0)  

# Lista para os jogadores
players = {}

# Cores e posições iniciais para os jogadores
colors = ["red", "blue", "green"]
start_positions = [(0, 0), (100, 0), (-100, 0)]

# Função para inicializar os jogadores na tela
def init_players():
    for i, color in enumerate(colors):
        player = turtle.Turtle()
        player.speed(0)
        player.shape("circle")
        player.color(color)
        player.penup()
        player.goto(start_positions[i])
        player.direction = "stop"
        player.shapesize(stretch_wid=1.5, stretch_len=1.5)  # Tamanho dos jogadores
        players[f"Jogador{i+1}"] = player

# Função chamada ao conectar ao broker
def on_connect(client, userdata, flags, rc):
    print("Conectado com código de resultado " + str(rc))
    client.subscribe("/data")  # Assina o tópico /data

# Função chamada ao receber uma mensagem
def on_message(client, userdata, msg):
    # Atualiza as posições dos jogadores a partir das mensagens MQTT
    data = json.loads(msg.payload.decode())
    player_name = data["name"]
    position = data["position"]
    players_data[player_name] = position

# Função para executar o loop MQTT em uma thread separada
def mqtt_loop():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, port, timelive)
    client.loop_forever()  # Mantém o loop rodando para receber mensagens

# Função para atualizar as posições dos jogadores na tela
def update_players():
    for player_name, position in players_data.items():
        if player_name in players:
            player = players[player_name]
            player.goto(position["x"], position["y"])

# Inicia o loop MQTT em uma thread separada
threading.Thread(target=mqtt_loop, daemon=True).start()

# Inicializa os jogadores na tela
init_players()

# Loop principal do jogo
try:
    while True:
        wn.update()
        update_players()  # Atualiza a posição dos jogadores com base nas mensagens MQTT
        time.sleep(delay)
except turtle.Terminator:
    print("A janela foi fechada.\n ______O jogo terminou._______")
