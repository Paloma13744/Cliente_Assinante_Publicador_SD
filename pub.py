import paho.mqtt.client as mqtt
import time
import random
import json

# Configurações do broker
broker = "localhost"
port = 1883

# Função chamada ao publicar uma mensagem
def on_publish(client, userdata, result):
    print("Dados publicados com sucesso.")

# Criação do cliente MQTT
client = mqtt.Client("admin")
client.on_publish = on_publish
client.connect(broker, port)

# Lista para armazenar informações dos jogadores
players = [
    {"name": "Jogador1", "position": {"x": 0, "y": 0}},
    {"name": "Jogador2", "position": {"x": 100, "y": 0}},
    {"name": "Jogador3", "position": {"x": -100, "y": 0}},
]

# Limites do campo
FIELD_LIMIT = 420  # Limite do campo de jogo, adaptado para os jogadores

# Função para atualizar a posição dos jogadores
def update_positions():
    for player in players:
        # Gera movimento aleatório dentro dos limites
        move_x = random.choice([-20, 0, 20])  # Movimento na direção X
        move_y = random.choice([-20, 0, 20])  # Movimento na direção Y
        
        # Atualiza a posição do jogador
        player["position"]["x"] += move_x
        player["position"]["y"] += move_y

        # Limita a posição para que o jogador não ultrapasse as bordas
        player["position"]["x"] = max(-FIELD_LIMIT, min(player["position"]["x"], FIELD_LIMIT))
        player["position"]["y"] = max(-FIELD_LIMIT, min(player["position"]["y"], FIELD_LIMIT))

        # Cria a mensagem em formato JSON
        message = json.dumps({"name": player["name"], "position": player["position"]})
        
        # Publica a mensagem no tópico MQTT
        client.publish("/data", message)
        print(f"Publicado: {player['name']} -> posição {player['position']}")

# Loop principal para publicar as posições dos jogadores
try:
    while True:
        update_positions()
        time.sleep(2)  # Aguarda 2 segundos antes da próxima atualização
except KeyboardInterrupt:
    print("Publicador encerrado.")
    client.disconnect()
