import paho.mqtt.client as mqtt
import threading
import time
import json

# Configurações do broker
broker = "localhost"
port = 1883
timelive = 60

# Dicionário para armazenar as posições dos jogadores
players = {}

# Função chamada ao conectar ao broker
def on_connect(client, userdata, flags, rc):
    print("Conectado com código de resultado " + str(rc))
    client.subscribe("/data")

# Função chamada ao receber uma mensagem
def on_message(client, userdata, msg):
    # Decodifica a mensagem e atualiza a posição do jogador
    data = json.loads(msg.payload.decode())
    player_name = data['name']
    position = data['position']
    players[player_name] = position
    print(f"Atualização: {player_name} está na posição {position}")

# Função para executar o loop MQTT em uma thread separada
def mqtt_loop():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, port, timelive)
    client.loop_forever()  # Mantém o loop rodando

# Inicia a thread do loop MQTT
threading.Thread(target=mqtt_loop, daemon=True).start()

# Função principal para manter o programa ativo
def main():
    try:
        while True:
            # Imprime as posições dos jogadores a cada 5 segundos
            time.sleep(5)
            print("Estado atual dos jogadores:", players)
    except KeyboardInterrupt:
        print("Encerrando o assinante...")

if __name__ == "__main__":
    main()
