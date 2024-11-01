import paho.mqtt.client as paho
import time
import random
import json

# Configurações do broker
broker = "localhost"
port = 1883

# Função chamada ao publicar uma mensagem
def on_publish(client, userdata, result):
    print("Dados Publicados.")

# Criação do cliente MQTT
client = paho.Client("admin")
client.on_publish = on_publish
client.connect(broker, port)

# Lista para armazenar informações dos jogadores
players = [
    {"name": "Jogador1", "position": {"x": 0, "y": 0}},
    {"name": "Jogador2", "position": {"x": 0, "y": 0}},
    {"name": "Jogador3", "position": {"x": 0, "y": 0}},
]

# Limites do campo
FIELD_LIMIT = 10

# Loop para simular a movimentação dos jogadores
for i in range(20):
    for player in players:
        # Gera um movimento aleatório
        move_x = random.choice([-1, 0, 1])  # Movimento na direção X
        move_y = random.choice([-1, 0, 1])  # Movimento na direção Y
        
        # Atualiza a posição do jogador
        player["position"]["x"] += move_x
        player["position"]["y"] += move_y

        # Limita a posição para que o jogador não ultrapasse as bordas
        player["position"]["x"] = max(-FIELD_LIMIT, min(player["position"]["x"], FIELD_LIMIT))
        player["position"]["y"] = max(-FIELD_LIMIT, min(player["position"]["y"], FIELD_LIMIT))

        # Criando mensagem em formato JSON
        message = json.dumps({"name": player["name"], "position": player["position"]})
        
        # Publicando mensagem
        ret = client.publish("/data", message)
        
        # Espera aleatória entre publicações para simular movimento
        d = random.randint(1, 5)
        time.sleep(d)

print("Parou...")
